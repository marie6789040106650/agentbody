#!/usr/bin/env python3
"""
从 OpenClaw Managed Browser 提取 Cookies，用于 Selenium 自动化
"""
import json
import sqlite3
import os
import sys

# 配置
CHROME_COOKIES_PATH = "/Users/bypasser/.openclaw/browser/openclaw/user-data/Default/Cookies"
OUTPUT_FILE = "/Users/bypasser/.openclaw/workspace/browser_cookies.json"

def extract_cookies():
    """提取 Chrome cookies"""
    if not os.path.exists(CHROME_COOKIES_PATH):
        print(f"❌ Cookies 文件不存在: {CHROME_COOKIES_PATH}")
        return {}

    cookies = {}

    try:
        conn = sqlite3.connect(CHROME_COOKIES_PATH)
        cursor = conn.cursor()

        # 查询所有 cookies
        cursor.execute("""
            SELECT name, host_key, path, encrypted_value, expires_utc, is_secure, is_httponly
            FROM cookies
        """)

        for row in cursor.fetchall():
            name, host_key, path, encrypted_value, expires_utc, is_secure, is_httponly = row

            # 跳过特殊主机
            if host_key.startswith('.') or 'chrome' in host_key.lower():
                continue

            # 解密 cookie（macOS Keychain）
            try:
                import subprocess
                result = subprocess.run(
                    ['security', 'find-generic-password', '-w', '-s', 'Chrome Safe Storage'],
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    decrypted = subprocess.run(
                        ['openssl', 'enc', '-aes-256-cbc', '-d', '-A', '-base64'],
                        input=encrypted_value,
                        capture_output=True
                    )
                    value = decrypted.stdout.decode('utf-8', errors='ignore') if decrypted.stdout else ""
                else:
                    value = ""
            except Exception:
                value = ""

            domain = host_key.lstrip('.')
            if domain not in cookies:
                cookies[domain] = []

            cookies[domain].append({
                'name': name,
                'value': value,
                'domain': domain,
                'path': path or '/',
                'secure': bool(is_secure),
                'httpOnly': bool(is_httponly)
            })

        conn.close()

        # 保存到文件
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(cookies, f, indent=2, ensure_ascii=False)

        print(f"✅ 提取完成！")
        print(f"📁 输出文件: {OUTPUT_FILE}")
        print(f"📊 发现 {len(cookies)} 个域名的 cookies:")
        for domain in cookies.keys():
            print(f"   - {domain}")

        return cookies

    except Exception as e:
        print(f"❌ 提取失败: {e}")
        return {}

def generate_selenium_code(cookies):
    """生成 Selenium 代码"""
    if not cookies:
        return

    print("\n📝 Selenium 使用示例:")
    print("=" * 50)

    code = '''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json

# 加载 cookies
with open('/Users/bypasser/.openclaw/workspace/browser_cookies.json', 'r') as f:
    COOKIES = json.load(f)

options = Options()
options.add_argument(r"--user-data-dir=/Users/bypasser/.openclaw/browser/openclaw/user-data")
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=options)

# 访问网站（自动带上 cookies）
driver.get("https://wx.zsxq.com/")

# 或者手动添加 cookies：
# driver.get("https://example.com")
# for cookie in COOKIES.get('example.com', []):
#     driver.add_cookie(cookie)
'''

    print(code)

if __name__ == '__main__':
    cookies = extract_cookies()
    if cookies:
        generate_selenium_code(cookies)
