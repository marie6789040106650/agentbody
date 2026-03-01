#!/usr/bin/env python3
"""
子代理监控脚本
每5分钟检查子代理状态，连续2次无响应自动重启
"""
import subprocess
import json
import time
from datetime import datetime, timedelta
from pathlib import Path

CONFIG = {
    'check_interval': 300,  # 5分钟
    'max_failures': 2,      # 最大失败次数
    'sessions_dir': Path.home() / '.openclaw' / 'sessions',
}

class SubAgentWatcher:
    def __init__(self):
        self.failures = {}  # {session_key: failure_count}
        self.last_check = {}
    
    def list_sessions(self) -> list:
        """列出活跃会话"""
        try:
            result = subprocess.run(
                ['openclaw', 'sessions', 'list', '--json'],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                return json.loads(result.stdout)
        except Exception:
            pass
        return []
    
    def check_session(self, session_key: str) -> bool:
        """检查会话响应状态"""
        try:
            result = subprocess.run(
                ['openclaw', 'sessions', 'history', session_key, '--limit=1'],
                capture_output=True, text=True, timeout=10
            )
            return result.returncode == 0
        except Exception:
            return False
    
    def get_session_status(self, session_key: str) -> dict:
        """获取会话详细状态"""
        try:
            result = subprocess.run(
                ['openclaw', 'sessions', 'list', '--filter', session_key],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                sessions = json.loads(result.stdout)
                for s in sessions:
                    if s.get('key') == session_key:
                        return s
        except Exception:
            pass
        return {}
    
    def restart_session(self, session_key: str) -> bool:
        """重启会话"""
        try:
            # 发送唤醒事件
            subprocess.run(
                ['openclaw', 'cron', 'wake', '--session', session_key],
                capture_output=True, text=True, timeout=10
            )
            return True
        except Exception:
            return False
    
    def watch(self):
        """主监控循环"""
        print(f"[{datetime.now().isoformat()}] SubAgentWatcher started")
        
        while True:
            sessions = self.list_sessions()
            print(f"Found {len(sessions)} active sessions")
            
            for session in sessions:
                session_key = session.get('key', '')
                if not session_key:
                    continue
                
                is_responsive = self.check_session(session_key)
                now = datetime.now()
                
                if not is_responsive:
                    failure_count = self.failures.get(session_key, 0) + 1
                    self.failures[session_key] = failure_count
                    
                    last_response = self.last_check.get(session_key)
                    time_since = (now - last_response).seconds if last_response else 0
                    
                    print(f"⚠️ {session_key}: failure #{failure_count}, last response: {time_since}s ago")
                    
                    if failure_count >= CONFIG['max_failures']:
                        print(f"🔄 Restarting {session_key}...")
                        if self.restart_session(session_key):
                            self.failures[session_key] = 0
                            print(f"✅ Restarted {session_key}")
                        else:
                            print(f"❌ Failed to restart {session_key}")
                else:
                    self.failures[session_key] = 0
                    self.last_check[session_key] = now
                    print(f"✅ {session_key}: responsive")
            
            time.sleep(CONFIG['check_interval'])

if __name__ == '__main__':
    watcher = SubAgentWatcher()
    watcher.watch()
