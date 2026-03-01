#!/usr/bin/env python3
"""
Memory Search - 快速关键词搜索
"""

import os
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = "/Users/bypasser/.openclaw/workspace"
CACHE_DIR = f"{WORKSPACE}/memory/cache"
INDEX_FILE = f"{CACHE_DIR}/index.json"

def load_index():
    """加载索引"""
    if not os.path.exists(INDEX_FILE):
        print("❌ 索引不存在，请先运行 index-memory.py")
        return None
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_file_content(filepath):
    """读取文件内容"""
    full_path = os.path.join(WORKSPACE, filepath)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[读取失败: {e}]"

def calculate_relevance(content, query, mtime, filepath):
    """计算相关性分数"""
    score = 0
    query_lower = query.lower()
    content_lower = content.lower()
    
    # 关键词匹配
    if query_lower in content_lower:
        # 精确匹配
        score += 100
        # 开头匹配权重更高
        if content_lower.startswith(query_lower):
            score += 50
    
    # 标题匹配（如果文件名包含关键词）
    if query_lower in filepath.lower():
        score += 30
    
    # 时间衰减（新文件权重更高）
    try:
        file_date = datetime.strptime(mtime, '%Y-%m-%d')
        days_ago = (datetime.now() - file_date).days
        if days_ago < 30:
            score += (30 - days_ago) * 0.5
        elif days_ago < 90:
            score += (90 - days_ago) * 0.2
    except:
        pass
    
    return score

def search(query, top=5):
    """搜索"""
    index = load_index()
    if not index:
        return []
    
    results = []
    query_lower = query.lower()
    
    for file_info in index['files']:
        filepath = file_info['path']
        content = read_file_content(filepath)
        content_lower = content.lower()
        
        # 检查是否包含查询词
        if query_lower in content_lower:
            score = calculate_relevance(content, query, file_info['mtime'], filepath)
            results.append({
                'path': filepath,
                'title': filepath.split('/')[-1].replace('.md', ''),
                'score': score,
                'mtime': file_info['mtime'],
                'snippet': get_snippet(content, query_lower)
            })
    
    # 按分数排序
    results.sort(key=lambda x: x['score'], reverse=True)
    
    return results[:top]

def get_snippet(content, query, max_len=200):
    """获取包含关键词的片段"""
    idx = content.lower().find(query)
    if idx == -1:
        return content[:max_len] + '...'
    
    start = max(0, idx - 50)
    end = min(len(content), idx + len(query) + 150)
    
    snippet = content[start:end]
    if start > 0:
        snippet = '...' + snippet
    if end < len(content):
        snippet = snippet + '...'
    
    return snippet

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("用法: python3 search-memory.py \"查询词\" [--top N]")
        sys.exit(1)
    
    query = sys.argv[1]
    top = 5
    
    if len(sys.argv) > 2 and sys.argv[2] == '--top':
        try:
            top = int(sys.argv[3])
        except:
            pass
    
    print(f"🔍 搜索: \"{query}\"\n")
    
    results = search(query, top)
    
    if not results:
        print("❌ 未找到相关结果")
        return
    
    print(f"找到 {len(results)} 个相关文件:\n")
    
    for i, r in enumerate(results, 1):
        print(f"{i}. {r['title']}")
        print(f"   路径: {r['path']}")
        print(f"   日期: {r['mtime']} | 相关度: {r['score']:.1f}")
        print(f"   片段: {r['snippet']}")
        print()

if __name__ == '__main__':
    main()
