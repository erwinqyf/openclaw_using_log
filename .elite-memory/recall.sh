#!/bin/bash
# Elite Longterm Memory - Recall Script
# Usage: ./.elite-memory/recall.sh "query" [limit]

QUERY="${1:-}"
LIMIT="${2:-5}"

if [ -z "$QUERY" ]; then
    echo "Usage: ./.elite-memory/recall.sh \"query\" [limit]"
    echo "Example: ./.elite-memory/recall.sh \"project status\" 10"
    exit 1
fi

echo "🧠 Elite Memory Recall: '$QUERY'"
echo "================================"

# 1. Search SESSION-STATE.md (Hot RAM)
echo ""
echo "📌 HOT RAM (SESSION-STATE.md):"
if [ -f "SESSION-STATE.md" ]; then
    grep -i "$QUERY" SESSION-STATE.md 2>/dev/null | head -3 || echo "  (no direct match)"
else
    echo "  (SESSION-STATE.md not found)"
fi

# 2. Search memory files (Curated Archive)
echo ""
echo "📚 CURATED ARCHIVE (memory/):"
if [ -d "memory" ]; then
    grep -ri "$QUERY" memory/ 2>/dev/null | head -$LIMIT || echo "  (no matches)"
else
    echo "  (memory/ folder not found)"
fi

# 3. Search Git-Notes (Cold Store)
echo ""
echo "🧊 COLD STORE (Git-Notes):"
python3 .elite-memory/git-notes/memory.py get "$QUERY" 2>/dev/null | head -$LIMIT || echo "  (no git-notes memories)"

# 4. Search recent sessions
echo ""
echo "💬 RECENT SESSIONS:"
LATEST_SESSION=$(ls -t /home/admin/.openclaw/agents/main/sessions/*.jsonl 2>/dev/null | grep -v ".deleted." | head -1)
if [ -n "$LATEST_SESSION" ]; then
    echo "  Latest: $(basename $LATEST_SESSION)"
    echo "  Size: $(du -h $LATEST_SESSION | cut -f1)"
else
    echo "  (no recent sessions)"
fi

echo ""
echo "================================"
echo "Recall complete. Apply relevant context to response."
