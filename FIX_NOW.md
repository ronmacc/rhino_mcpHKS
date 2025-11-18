# Fix: Claude Desktop Not Connecting

## The Problem

Claude Desktop is running but saying "I don't have the ability to access information about a Rhino scene" - this means the MCP server isn't connecting.

## Quick Fix - Try This:

### Option 1: Check Claude Desktop Settings

1. Open Claude Desktop
2. Go to **Settings** (gear icon)
3. Look for **Developer** or **MCP** settings
4. Check if "rhino" server is listed
5. If there's an error, it will show here

### Option 2: Verify Config File Location

Claude Desktop might be looking in a different location. Check:

1. Press `Win + R`
2. Type: `%APPDATA%\Claude`
3. Make sure `claude_desktop_config.json` is there
4. Open it and verify it has the rhino config

### Option 3: Try a Different Config Format

Sometimes Claude Desktop is picky. Try this exact format:

```json
{
  "mcpServers": {
    "rhino": {
      "command": "C:/Users/aroncal/.conda/envs/rhino_mcp/python.exe",
      "args": [
        "-m",
        "rhino_mcp.server"
      ]
    }
  }
}
```

Make sure:
- No trailing commas
- Proper indentation
- Forward slashes in paths
- python.exe (not just python)

### Option 4: Check Claude Desktop Version

Make sure you have a recent version of Claude Desktop that supports MCP. Older versions might not work.

### Option 5: Manual Test

1. Open terminal
2. Run: `conda activate rhino_mcp`
3. Run: `python -m rhino_mcp.server`
4. If this works (no errors), the server is fine
5. Press Ctrl+C to stop it

If the server starts manually but Claude Desktop doesn't connect, the issue is with Claude Desktop reading the config.

## Most Likely Issue:

**Claude Desktop isn't reading the config file.**

Try:
1. Close Claude Desktop completely
2. Delete the config file
3. Recreate it with the exact content above
4. Save it
5. Open Claude Desktop
6. Wait 30 seconds
7. Check if it connects

