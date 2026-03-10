#!/usr/bin/env python3
"""Git-Notes based knowledge graph for Elite Longterm Memory"""

import subprocess
import json
import sys
from datetime import datetime

def run_git_notes(args):
    """Run git notes command"""
    cmd = ['git', 'notes'] + args
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/home/admin/.openclaw/workspace')
        return result.stdout.decode('utf-8').strip(), result.returncode
    except Exception as e:
        return str(e), 1

def remember(content, tags="", importance="m"):
    """Store a decision/fact in git notes"""
    timestamp = datetime.now().isoformat()
    note = {
        "type": "memory",
        "content": content,
        "tags": tags.split(",") if tags else [],
        "importance": importance,  # l=low, m=medium, h=high
        "created": timestamp
    }
    
    # Store as git note on latest commit
    note_json = json.dumps(note, ensure_ascii=False)
    stdout, rc = run_git_notes(['add', '-m', note_json])
    if rc != 0:
        # If note exists, append
        stdout, rc = run_git_notes(['append', '-m', note_json])
    
    return f"Stored: {content[:50]}..." if rc == 0 else f"Error: {stdout}"

def get(query):
    """Retrieve memories from git notes"""
    stdout, rc = run_git_notes(['show'])
    if rc != 0:
        return "No memories found"
    
    memories = []
    for line in stdout.split('\n'):
        line = line.strip()
        if not line:
            continue
        try:
            note = json.loads(line)
            if query.lower() in note.get('content', '').lower():
                memories.append(note)
        except:
            continue
    
    return memories[:10]

def list_all():
    """List all memories"""
    stdout, rc = run_git_notes(['show'])
    if rc != 0:
        return []
    
    memories = []
    for line in stdout.split('\n'):
        line = line.strip()
        if not line:
            continue
        try:
            note = json.loads(line)
            memories.append(note)
        except:
            continue
    
    return memories

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 memory.py <command> [args]")
        print("Commands: remember <content> [tags] [importance], get <query>, list")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "remember":
        content = sys.argv[2] if len(sys.argv) > 2 else ""
        tags = sys.argv[3] if len(sys.argv) > 3 else ""
        importance = sys.argv[4] if len(sys.argv) > 4 else "m"
        print(remember(content, tags, importance))
    elif cmd == "get":
        query = sys.argv[2] if len(sys.argv) > 2 else ""
        results = get(query)
        for r in results:
            print(f"- {r.get('content', '')}")
    elif cmd == "list":
        results = list_all()
        for r in results:
            print(f"[{r.get('importance', 'm')}] {r.get('content', '')[:60]}...")
    else:
        print(f"Unknown command: {cmd}")
