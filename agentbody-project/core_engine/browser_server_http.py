#!/usr/bin/env python3
"""
AgentBody Browser Server - HTTP API Server
FastAPI based HTTP service for browser automation
"""

import asyncio
import uuid
import time
from urllib.parse import urlparse
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nodriver as nd

app = FastAPI(title="AgentBody Browser Server")

# Global state
browser: Optional[nd.Browser] = None
current_page: Optional[nd.Tab] = None

# Task management
tasks: Dict[str, Dict] = {}
current_task_id: Optional[str] = None

# ==================== Data Classes ====================

@dataclass
class TabInfo:
    id: str
    url: str
    title: str = ""
    created_at: float = 0

# ==================== Models ====================

class StartRequest(BaseModel):
    headless: bool = True
    port: int = 9222

class SmartOpenRequest(BaseModel):
    url: str

class OpenRequest(BaseModel):
    url: str

class ClickRequest(BaseModel):
    selector: str

class FillRequest(BaseModel):
    selector: str
    text: str

class FocusTabRequest(BaseModel):
    tab_id: str

class StartTaskRequest(BaseModel):
    task_id: Optional[str] = None

class EndTaskRequest(BaseModel):
    cleanup: bool = True

# ==================== Helpers ====================

def extract_main_domain(url: str) -> str:
    if not url:
        return ""
    try:
        parsed = urlparse(url)
        parts = parsed.netloc.split('.')
        if len(parts) >= 2:
            return '.'.join(parts[-2:])
        return parsed.netloc
    except:
        return ""

def should_start_new_task(url: str) -> bool:
    global current_task_id, tasks
    if not current_task_id or current_task_id not in tasks:
        return True
    
    task = tasks.get(current_task_id, {})
    domain_history = task.get("domain_history", [])
    
    new_domain = extract_main_domain(url)
    current_domain = domain_history[-1] if domain_history else ""
    
    # Different domain
    if current_domain and new_domain != current_domain:
        return True
    
    # OAuth keywords
    oauth_keywords = {"oauth", "authorize", "callback", "sso", "federated"}
    if any(k in url.lower() for k in oauth_keywords):
        return True
    
    return False

# ==================== API Endpoints ====================

@app.get("/")
async def root():
    return {"status": "ok", "service": "AgentBody Browser Server"}

@app.get("/health")
async def health():
    return {"status": "healthy", "browser": browser is not None}

# ==================== Browser Control ====================

@app.post("/start")
async def start(req: StartRequest):
    global browser, current_page, current_task_id, tasks
    
    cookie_path = "/tmp/agentbody_cookies.json"
    
    print(f"[start] Called with headless={req.headless}, browser={browser}")
    
    if browser is None:
        print("[start] Starting browser...")
        browser = await nd.start(headless=req.headless, port=req.port)
        print(f"[start] Browser started: {browser}")
        current_page = await browser.get('about:blank')
        print(f"[start] Current page: {current_page}")
        
        # 自动加载之前保存的 Cookie
        try:
            import json
            with open(cookie_path, 'r') as f:
                cookies = json.load(f)
            if cookies:
                for cookie in cookies:
                    try:
                        await current_page.evaluate(f"document.cookie = '{cookie['name']}={cookie['value']}'")
                    except:
                        pass
                print(f"[start] Loaded {len(cookies)} cookies")
        except FileNotFoundError:
            print("[start] No saved cookies found")
        except Exception as e:
            print(f"[start] Cookie load error: {e}")
    
    # Create default task
    task_id = "default"
    current_task_id = task_id
    tasks[task_id] = {
        "tabs": [],
        "domain_history": [],
        "created_at": time.time()
    }
    
    return {"status": "ready", "task_id": task_id}

@app.post("/smart_open")
async def smart_open(req: SmartOpenRequest):
    global browser, current_page, current_task_id, tasks
    
    if browser is None:
        raise HTTPException(status_code=400, detail="Browser not started")
    
    url = req.url
    task_id = current_task_id or "default"
    task = tasks.setdefault(task_id, {"tabs": [], "domain_history": [], "created_at": time.time()})
    
    # Auto task switch
    if should_start_new_task(url):
        task_id = str(uuid.uuid4())[:8]
        current_task_id = task_id
        task = tasks[task_id] = {"tabs": [], "domain_history": [], "created_at": time.time()}
    
    new_domain = extract_main_domain(url)
    
    # Check for reuse in same task
    for tab_info in task.get("tabs", []):
        if tab_info["url"] == url:
            # Focus existing
            for tab in browser.targets:
                if str(tab.target_id) == tab_info["id"]:
                    current_page = tab
                    try:
                        await tab.bring_to_front()
                    except:
                        pass
                    return {"action": "focus", "tab_id": tab_info["id"], "task_id": task_id}
    
    # Same domain navigation
    for tab_info in task.get("tabs", []):
        tab_domain = extract_main_domain(tab_info["url"])
        if tab_domain == new_domain and new_domain:
            for tab in browser.targets:
                if str(tab.target_id) == tab_info["id"]:
                    await tab.get(url)
                    current_page = tab
                    tab_info["url"] = url
                    return {"action": "navigate", "tab_id": tab_info["id"], "task_id": task_id}
    
    # New tab
    new_page = await browser.get(url, new_tab=True)
    new_id = str(new_page.target_id)
    
    try:
        await new_page.bring_to_front()
    except:
        pass
    
    current_page = new_page
    
    # Track
    task.setdefault("tabs", []).append({
        "id": new_id,
        "url": url,
        "title": new_page.title or "",
        "created_at": time.time()
    })
    
    domain_history = task.get("domain_history", [])
    if new_domain and domain_history and new_domain != domain_history[-1]:
        task.setdefault("domain_history", []).append(url)
    
    return {"action": "new_tab", "tab_id": new_id, "url": url, "task_id": task_id}

@app.post("/open")
async def open_url(req: OpenRequest):
    """Force new tab"""
    global browser, current_page, current_task_id, tasks
    
    if browser is None:
        raise HTTPException(status_code=400, detail="Browser not started")
    
    url = req.url
    task_id = str(uuid.uuid4())[:8]
    current_task_id = task_id
    task = tasks[task_id] = {"tabs": [], "domain_history": [], "created_at": time.time()}
    
    new_page = await browser.get(url, new_tab=True)
    new_id = str(new_page.target_id)
    
    try:
        await new_page.bring_to_front()
    except:
        pass
    
    current_page = new_page
    
    task["tabs"].append({
        "id": new_id,
        "url": url,
        "title": new_page.title or "",
        "created_at": time.time()
    })
    
    return {"action": "new_tab", "tab_id": new_id, "url": url, "task_id": task_id}

@app.post("/click")
async def click(req: ClickRequest):
    global browser, current_page, current_task_id, tasks
    
    if browser is None:
        raise HTTPException(status_code=400, detail="Browser not started")
    
    if not current_page:
        raise HTTPException(status_code=400, detail="No active page")
    
    # Get tabs before
    tabs_before = set(t.target_id for t in browser.targets if t.type_ == "page")
    
    # Click
    element = await current_page.query_selector(req.selector)
    if element:
        await element.click()
    
    await asyncio.sleep(1)
    
    # Check for new tabs
    tabs_after = set(t.target_id for t in browser.targets if t.type_ == "page")
    new_tab_ids = tabs_after - tabs_before
    
    result = {"success": True, "clicked": req.selector}
    
    if new_tab_ids:
        new_tabs = []
        new_tab_obj = None
        for tab in browser.targets:
            if tab.target_id in new_tab_ids:
                tab_id = str(tab.target_id)
                new_tabs.append({
                    "id": tab_id,
                    "url": tab.url or "",
                    "title": tab.title or ""
                })
                # Auto-switch to new tab
                current_page = tab
                new_tab_obj = tab
                # Track in current task
                if current_task_id and current_task_id in tasks:
                    task = tasks[current_task_id]
                    task.setdefault("tabs", []).append({
                        "id": tab_id,
                        "url": tab.url or "",
                        "title": tab.title or "",
                        "created_at": time.time()
                    })
        
        result["new_tabs"] = new_tabs
        result["switched_to"] = new_tabs[0]["id"] if new_tabs else None
    
    return result

@app.post("/focus")
async def focus(req: FocusTabRequest):
    """切换到指定标签页"""
    global browser, current_page, current_task_id, tasks
    
    if browser is None:
        raise HTTPException(status_code=400, detail="Browser not started")
    
    tab_id = req.tab_id
    
    # Find and switch to tab
    for tab in browser.targets:
        if str(tab.target_id) == tab_id:
            current_page = tab
            try:
                await tab.bring_to_front()
            except:
                pass
            
            # Track in current task
            if current_task_id and current_task_id in tasks:
                task = tasks[current_task_id]
                task.setdefault("tabs", []).append({
                    "id": tab_id,
                    "url": tab.url or "",
                    "title": tab.title or "",
                    "created_at": time.time()
                })
            
            return {
                "success": True, 
                "tab_id": tab_id, 
                "url": tab.url,
                "title": tab.title
            }
    
    raise HTTPException(status_code=404, detail="Tab not found")

@app.post("/fill")
async def fill(req: FillRequest):
    global current_page
    
    if not current_page:
        raise HTTPException(status_code=400, detail="No active page")
    
    element = await current_page.query_selector(req.selector)
    if element:
        await element.send_keys(req.text)
        return {"success": True, "filled": req.selector}
    
    raise HTTPException(status_code=404, detail=f"Element not found: {req.selector}")

@app.get("/tabs")
async def get_tabs():
    if browser is None:
        return {"tabs": []}
    
    tabs = []
    for tab in browser.targets:
        if tab.type_ == "page":
            tabs.append({
                "id": str(tab.target_id),
                "url": tab.url or "",
                "title": tab.title or ""
            })
    
    return {"tabs": tabs}

@app.get("/tabs/tree")
async def get_tab_tree():
    result = {"tasks": []}
    
    for task_id, task in tasks.items():
        result["tasks"].append({
            "task_id": task_id,
            "tab_count": len(task.get("tabs", [])),
            "tabs": task.get("tabs", [])
        })
    
    return result

@app.get("/task/info")
async def get_task_info():
    return {
        "current_task_id": current_task_id,
        "task_count": len(tasks),
        "tasks": [
            {"task_id": t, "tabs": len(info.get("tabs", []))}
            for t, info in tasks.items()
        ]
    }

@app.post("/task/start")
async def start_task(req: StartTaskRequest):
    global current_task_id, tasks
    
    task_id = req.task_id or str(uuid.uuid4())[:8]
    current_task_id = task_id
    tasks[task_id] = {"tabs": [], "domain_history": [], "created_at": time.time()}
    
    return {"task_id": task_id, "status": "started"}

@app.post("/task/end")
async def end_task(req: EndTaskRequest):
    global current_task_id, browser, tasks
    
    if not current_task_id or current_task_id not in tasks:
        raise HTTPException(status_code=400, detail="No active task")
    
    task = tasks[current_task_id]
    closed_count = 0
    
    if req.cleanup and browser:
        for tab_info in task.get("tabs", []):
            try:
                for tab in browser.targets:
                    if str(tab.target_id) == tab_info["id"]:
                        await tab.close()
                        closed_count += 1
                        break
            except:
                pass
    
    task["is_active"] = False
    old_task_id = current_task_id
    current_task_id = None
    
    return {"task_id": old_task_id, "closed_tabs": closed_count}

@app.post("/screenshot")
async def screenshot(path: str = "/tmp/screenshot.png"):
    global current_page
    
    if not current_page:
        raise HTTPException(status_code=400, detail="No active page")
    
    await current_page.save_screenshot(path)
    return {"success": True, "path": path}

@app.post("/snapshot")
async def snapshot():
    global current_page
    
    if not current_page:
        raise HTTPException(status_code=400, detail="No active page")
    
    try:
        html = await current_page.evaluate("document.body.innerHTML")
        return {"snapshot": str(html)[:5000]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/stop")
async def stop():
    global browser, current_page, tasks, current_task_id
    
    cookie_path = "/tmp/agentbody_cookies.json"
    
    if browser:
        # 自动保存 Cookie
        try:
            import json
            jar = browser.cookies
            cookies_list = await jar.get_all()
            cookies = []
            for c in cookies_list:
                cookies.append({
                    "name": c.name,
                    "value": c.value,
                    "domain": c.domain,
                    "path": c.path
                })
            with open(cookie_path, 'w') as f:
                json.dump(cookies, f)
            print(f"[stop] Auto-saved {len(cookies)} cookies to {cookie_path}")
        except Exception as e:
            print(f"[stop] Cookie save error: {e}")
        
        try:
            await browser.stop()
        except Exception as e:
            print(f"[stop] Browser stop error: {e}")
    
    # 强制清理残留的 Chrome 进程
    import subprocess
    try:
        # 查找 nodriver 启动的 Chrome 进程
        result = subprocess.run(
            ["pgrep", "-f", "Chrome.*--user-data-dir.*tmp"],
            capture_output=True, text=True
        )
        if result.stdout.strip():
            pids = result.stdout.strip().split()
            for pid in pids:
                try:
                    subprocess.run(["kill", "-9", pid], capture_output=True)
                    print(f"[stop] Killed process {pid}")
                except:
                    pass
    except:
        pass
    
    browser = None
    current_page = None
    tasks.clear()
    current_task_id = None
    
    return {"status": "stopped"}


@app.post("/cleanup")
async def cleanup():
    """清理残留的 Chrome 进程"""
    import subprocess
    
    count = 0
    try:
        # 查找 nodriver 启动的 Chrome 进程
        result = subprocess.run(
            ["pgrep", "-f", "Chrome.*uc_"],
            capture_output=True, text=True
        )
        if result.stdout.strip():
            pids = result.stdout.strip().split()
            for pid in pids:
                try:
                    subprocess.run(["kill", "-9", pid], capture_output=True)
                    count += 1
                except:
                    pass
    except:
        pass
    
    return {"killed": count}



# ==================== Visual Click ====================

class ClickAtRequest(BaseModel):
    x: int
    y: int

class GetPositionRequest(BaseModel):
    selector: str

@app.post("/click_at")
async def click_at(req: ClickAtRequest):
    """通过坐标点击"""
    global current_page
    
    if not current_page:
        raise HTTPException(status_code=400, detail="No active page")
    
    js_code = f"""
    (function() {{
        var element = document.elementFromPoint({req.x}, {req.y});
        if (element) {{
            element.click();
            return element.tagName;
        }}
        return null;
    }})()
    """
    
    try:
        result = await current_page.evaluate(js_code)
        return {"success": True, "clicked_tag": result, "x": req.x, "y": req.y}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.post("/get_element_position")
async def get_element_position(req: GetPositionRequest):
    """获取元素坐标"""
    global current_page
    
    if not current_page:
        raise HTTPException(status_code=400, detail="No active page")
    
    js_code = f"""
    (function() {{
        var el = document.querySelector('{req.selector}');
        if (!el) return null;
        var rect = el.getBoundingClientRect();
        return {{
            x: Math.round(rect.x + rect.width / 2),
            y: Math.round(rect.y + rect.height / 2),
            width: rect.width,
            height: rect.height
        }};
    }})()
    """
    
    try:
        result = await current_page.evaluate(js_code)
        if result:
            return {"success": True, "position": result}
        return {"success": False, "error": "Element not found"}
    except Exception as e:
        return {"success": False, "error": str(e)}

# ==================== Main ====================

# ==================== Cookie Persistence ====================

class SaveCookieRequest(BaseModel):
    name: Optional[str] = None
    path: str = "/tmp/cookies.json"

class LoadCookieRequest(BaseModel):
    path: str = "/tmp/cookies.json"

@app.post("/cookie/save")
async def save_cookies(req: SaveCookieRequest):
    """保存 Cookie 到文件"""
    import json
    
    print(f"[cookie/save] browser: {browser}")
    
    if not browser:
        raise HTTPException(status_code=400, detail="Browser not started")
    
    try:
        jar = browser.cookies
        print(f"[cookie/save] jar: {jar}")
        
        cookies_list = await jar.get_all()
        print(f"[cookie/save] cookies_list count: {len(cookies_list)}")
        
        cookies = []
        for c in cookies_list:
            cookies.append({
                "name": c.name,
                "value": c.value,
                "domain": c.domain,
                "path": c.path
            })
        
        print(f"[cookie/save] saving {len(cookies)} cookies")
        
        with open(req.path, 'w') as f:
            json.dump(cookies, f, indent=2)
        
        return {"success": True, "count": len(cookies), "path": req.path}
    except Exception as e:
        import traceback
        print(f"[cookie/save] error: {e}")
        traceback.print_exc()
        return {"success": False, "error": str(e)}

@app.post("/cookie/load")
async def load_cookies(req: LoadCookieRequest):
    """从文件加载 Cookie"""
    import json
    
    if not browser:
        raise HTTPException(status_code=400, detail="Browser not started")
    
    try:
        with open(req.path, 'r') as f:
            cookies = json.load(f)
    except FileNotFoundError:
        return {"success": False, "error": "Cookie file not found"}
    
    if current_page:
        for cookie in cookies:
            try:
                await current_page.set_cookies(cookie["name"], cookie["value"])
            except:
                pass
    
    return {"success": True, "loaded": len(cookies)}

@app.post("/cookie/clear")
async def clear_cookies():
    """清除所有 Cookie"""
    if not browser:
        raise HTTPException(status_code=400, detail="Browser not started")
    
    count = 0
    for tab in browser.targets:
        if tab.type_ == "page":
            try:
                await tab.clear_cookies()
                count += 1
            except:
                pass
    
    return {"success": True, "cleared_pages": count}




# ==================== Selector Library ====================

class SelectorRequest(BaseModel):
    site: str
    element: str

@app.get("/selectors")
async def list_selectors():
    """列出所有可用的选择器"""
    from selector_lib import SELECTORS
    return {"sites": list(SELECTORS.keys())}

@app.get("/selectors/{site}")
async def get_site_selectors(site: str):
    """获取网站的选择器"""
    from selector_lib import get_site_selectors
    return {"site": site, "selectors": get_site_selectors(site)}

@app.get("/selector/{site}/{element}")
async def get_selector(site: str, element: str):
    """获取特定选择器"""
    from selector_lib import get_selector
    selector = get_selector(site, element)
    if selector:
        return {"site": site, "element": element, "selector": selector}
    return {"error": "Selector not found"}, 404



# ==================== Memory Management ====================

class RestartRequest(BaseModel):
    force: bool = False

@app.post("/memory/stats")
async def memory_stats():
    """获取内存使用统计"""
    import os
    
    open_tabs = 0
    if browser:
        try:
            open_tabs = len([t for t in browser.targets if t.type_ == "page"])
        except:
            pass
    
    return {
        "open_tabs": open_tabs,
        "browser_running": browser is not None
    }

@app.post("/memory/restart")
async def memory_restart(req: RestartRequest):
    """重启浏览器释放内存"""
    global browser, current_page, tasks
    
    if not browser:
        return {"status": "not_running"}
    
    # 保存当前标签页 URL
    tab_urls = []
    for tab in browser.targets:
        if tab.type_ == "page" and tab.url != "about:blank":
            tab_urls.append(tab.url)
    
    # 停止旧浏览器
    try:
        await browser.stop()
    except:
        pass
    
    # 重新启动
    browser = await nd.start(headless=False)
    current_page = await browser.get('about:blank')
    
    # 恢复标签页
    for url in tab_urls[:5]:  # 最多恢复5个
        try:
            await browser.get(url)
        except:
            pass
    
    # 重置任务
    tasks = {
        "default": {
            "tabs": [],
            "domain_history": [],
            "created_at": time.time()
        }
    }
    
    return {"status": "restarted", "tabs_restored": len(tab_urls)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9229)
