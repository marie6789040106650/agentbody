#!/usr/bin/env python3
"""提取小红书登录状态"""
import json
import sqlite3
import os

COOKIES_DB = "/Users/bypasser/.openclaw/browser/openclaw/user-data/Default/Cookies"
OUTPUT_FILE = "/Users/bypasser/.openclaw/workspace/xiaohongshu_auth.json"

def extract_xiaohongshu_cookies():
    """提取小红书所有 cookies"""
    if not os.path.exists(COOKIES_DB):
        return {}

    conn = sqlite3.connect(COOKIES_DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT host_key, name, path, is_secure, is_httponly
        FROM cookies
        WHERE host_key LIKE '%.xiaohongshu.com' OR host_key LIKE 'xiaohongshu.com'
    """)

    cookies = []
    for row in cursor.fetchall():
        host_key, name, path, is_secure, is_httponly = row
        cookies.append({
            'name': name,
            'domain': host_key.lstrip('.'),
            'path': path or '/',
            'secure': bool(is_secure),
            'httpOnly': bool(is_httponly)
        })

    conn.close()
    return cookies

def main():
    cookies = extract_xiaohongshu_cookies()

    config = {
        'platform': 'xiaohongshu',
        'domain': 'xiaohongshu.com',
        'count': len(cookies),
        'cookies': cookies,
        'critical': ['web_session', 'xsecappid', 'sec_poison_id', 'websectiga']
    }

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"✅ 已保存: {OUTPUT_FILE}")
    print(f"📊 共 {len(cookies)} 个 cookies")

    critical = [c['name'] for c in cookies if c['name'] in config['critical']]
    print(f"🔑 关键 cookies: {', '.join(critical)}")

    return config

if __name__ == '__main__':
    main()
