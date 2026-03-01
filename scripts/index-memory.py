#!/usr/bin/env python3
"""
Memory Indexer - 建立 memory 文件索引
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path

WORKSPACE = "/Users/bypasser/.openclaw/workspace"
CACHE_DIR = f"{WORKSPACE}/memory/cache"
MEMORY_DIR = f"{WORKSPACE}/memory"

def get_file_hash(filepath):
    """获取文件内容的hash"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return hashlib.md5(content.encode('utf-8')).hexdigest()[:8]

def get_file_mtime(filepath):
    """获取文件修改时间"""
    timestamp = os.path.getmtime(filepath)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def scan_memory_files():
    """扫描所有 memory 文件"""
    files = []
    
    # 扫描 memory 目录（不包括 cache）
    for root, dirs, filenames in os.walk(MEMORY_DIR):
        # 跳过 cache 目录
        if 'cache' in root:
            continue
        
        for filename in filenames:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, WORKSPACE)
                files.append({
                    'path': rel_path,
                    'mtime': get_file_mtime(filepath),
                    'hash': get_file_hash(filepath),
                    'size': os.path.getsize(filepath)
                })
    
    # 也扫描 MEMORY.md
    memory_main = f"{WORKSPACE}/MEMORY.md"
    if os.path.exists(memory_main):
        files.append({
            'path': 'MEMORY.md',
            'mtime': get_file_mtime(memory_main),
            'hash': get_file_hash(memory_main),
            'size': os.path.getsize(memory_main)
        })
    
    return files

def create_index():
    """创建索引"""
    print("🔍 扫描 memory 文件...")
    
    files = scan_memory_files()
    
    # 创建索引数据
    index = {
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_files': len(files),
        'files': files,
        'by_date': {},
        'by_directory': {}
    }
    
    # 按日期分类
    for f in files:
        date = f['mtime']
        if date not in index['by_date']:
            index['by_date'][date] = []
        index['by_date'][date].append(f['path'])
    
    # 按目录分类
    for f in files:
        dir_name = os.path.dirname(f['path']).split('/')[0] if '/' in f['path'] else 'root'
        if dir_name not in index['by_directory']:
            index['by_directory'][dir_name] = []
        index['by_directory'][dir_name].append(f['path'])
    
    # 保存索引
    index_file = f"{CACHE_DIR}/index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 索引已创建: {index_file}")
    print(f"📊 共索引 {len(files)} 个文件")
    print(f"\n按日期分类:")
    for date, count in sorted(index['by_date'].items(), reverse=True):
        print(f"  {date}: {len(count)} 个文件")
    print(f"\n按目录分类:")
    for dir_name, file_list in sorted(index['by_directory'].items()):
        print(f"  {dir_name}/: {len(file_list)} 个文件")
    
    return index

if __name__ == '__main__':
    # 确保 cache 目录存在
    os.makedirs(CACHE_DIR, exist_ok=True)
    
    # 创建索引
    create_index()
