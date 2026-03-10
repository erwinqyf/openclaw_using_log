#!/bin/bash
# Elite Longterm Memory - Auto Extraction Script
# Usage: ./.elite-memory/extract.sh "user message"

MESSAGE="${1:-}"

if [ -z "$MESSAGE" ]; then
    echo "Usage: ./.elite-memory/extract.sh \"user message\""
    exit 1
fi

echo "🧠 Extracting facts from: '${MESSAGE:0:50}...'"

# Extract patterns using simple heuristics
# In production, this would use LLM API for extraction

# Pattern 1: Preferences ("I prefer...", "I like...", "I want...")
if echo "$MESSAGE" | grep -qiE "(prefer|like|want|need|use|choose)"; then
    echo "📌 Detected: Preference"
    echo "   Content: $MESSAGE"
    echo "   Action: Store in SESSION-STATE.md and Git-Notes"
fi

# Pattern 2: Decisions ("Let's use...", "We decided...", "Use...")
if echo "$MESSAGE" | grep -qiE "(let's|we decided|decided to|use|choose|going with)"; then
    echo "📌 Detected: Decision"
    echo "   Content: $MESSAGE"
    echo "   Action: Store in Git-Notes with high importance"
fi

# Pattern 3: Facts ("The server is...", "API endpoint is...")
if echo "$MESSAGE" | grep -qiE "(is|are|has|endpoint|url|path|config)"; then
    echo "📌 Detected: Potential Fact"
    echo "   Content: $MESSAGE"
    echo "   Action: Verify before storing"
fi

echo ""
echo "💡 To store manually:"
echo "   python3 .elite-memory/git-notes/memory.py remember \"content\" \"tags\" \"importance(l/m/h)\""
