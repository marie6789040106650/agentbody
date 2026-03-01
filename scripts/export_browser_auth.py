#!/usr/bin/env python3
"""
从 OpenClaw Managed Browser 提取认证信息，用于 Selenium 自动化
"""
import json
import os

COOKIES_DB = "/Users/bypasser/.openclaw/browser/openclaw/user-data/Default/Cookies"
OUTPUT_FILE = "/Users/bypasser/.openclaw/workspace/selenium_auth.json"

def extract_cookies_sqlite():
    """直接读取 Chrome Cookies SQLite 数据库"""
    import sqlite3

    if not os.path.exists(COOKIES_DB):
        print(f"❌ Cookies 数据库不存在")
        return {}

    try:
        conn = sqlite3.connect(COOKIES_DB)
        cursor = conn.cursor()

        # 查询所有 cookies
        cursor.execute("""
            SELECT host_key, name, path, is_secure, is_httponly, expires_utc
            FROM cookies
        """)

        domains = {}
        for row in cursor.fetchall():
            host_key, name, path, is_secure, is_httponly, expires_utc = row
            domain = host_key.lstrip('.')

            # 只记录重要域名
            if any(d in domain for d in ['zsxq.com', 'scys.com', 'feishu.cn']):
                if domain not in domains:
                    domains[domain] = []
                domains[domain].append({
                    'name': name,
                    'domain': domain,
                    'path': path or '/',
                    'secure': bool(is_secure),
                    'httpOnly': bool(is_httponly)
                })

        conn.close()
        return domains

    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return {}

def generate_auth_files(domains):
    """生成认证配置文件"""

    auth_config = {
        'description': 'OpenClaw Browser Auth Cookies',
        'source': '/Users/bypasser/.openclaw/browser/openclaw/user-data/Default/Cookies',
        'usage': 'Load cookies in Selenium or requests',
        'domains': domains
    }

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(auth_config, f, indent=2, ensure_ascii=False)

    print(f"✅ 已保存: {OUTPUT_FILE}")

    # 生成 Selenium 示例
    selenium_code = f'''from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

def get_driver():
    """获取带有登录状态的 Chrome driver"""
    options = Options()
    options.add_argument(r"--user-data-dir=/Users/bypasser/.openclaw/browser/openclaw/user-data")
    options.add_argument("--profile-directory=Default")
    return webdriver.Chrome(options=options)

def add_cookies(driver, domain):
    """为指定域名添加 cookies"""
    with open('/Users/bypasser/.openclaw/workspace/selenium_auth.json', 'r') as f:
        auth = json.load(f)

    driver.get(f"https://{{domain}}")
    for cookie in auth.get('domains', {{}}).get(domain, []):
        driver.add_cookie(cookie)

# 使用示例
driver = get_driver()

# 访问知识星球（自动登录）
driver.get("https://wx.zsxq.com/")

# 访问生财有术
driver.get("https://scys.com/")
'''

    code_file = OUTPUT_FILE.replace('.json', '_selenium.py')
    with open(code_file, 'w', encoding='utf-8') as f:
        f.write(selenium_code)

    print(f"✅ Selenium 示例: {code_file}")

    return auth_config

if __name__ == '__main__':
    domains = extract_cookies_sqlite()
    if domains:
        generate_auth_files(domains)
        print(f"\\n📊 发现 {len(domains)} 个已登录域名:")
        for d in domains:
            print(f"   - {d} ({len(domains[d])} cookies)")
