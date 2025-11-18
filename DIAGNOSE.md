# Diagnose Why Claude Desktop Isn't Connecting

## The Real Issue

Your config is perfect. The server can start. But Claude Desktop isn't connecting to it.

## Most Likely Causes:

### 1. Claude Desktop Version Doesn't Support MCP

**Check this first:**
- Open Claude Desktop
- Settings → About
- You need version from late 2024 or 2025
- If it's older, **update Claude Desktop**

### 2. MCP Not Enabled in Claude Desktop

Some versions require you to enable MCP:
- Settings → Developer
- Look for "MCP Servers" or "Enable MCP"
- Make sure it's ON

### 3. Claude Desktop Not Reading the Config

The config file is correct, but Claude Desktop might not be reading it:
- Close Claude Desktop completely
- Delete `claude_desktop_config.json`
- Recreate it with the exact content
- Open Claude Desktop
- Wait 30 seconds

### 4. Server Starting But Not Connecting

The server might start but fail to connect:
- Check Claude Desktop logs: `%APPDATA%\Claude\logs`
- Look for errors about "rhino" or "mcp"
- If you see "Cannot find module" → package not installed
- If you see "Permission denied" → Python path wrong

## Quick Test:

Run this to see if the server actually works:

```powershell
conda activate rhino_mcp
python -m rhino_mcp.server
```

If this starts (no errors), press Ctrl+C. The server works.

If Claude Desktop still doesn't connect, the problem is Claude Desktop, not the server.

## Solution: Use Cursor IDE Instead

If Claude Desktop doesn't support MCP or isn't working:

1. Install Cursor IDE
2. Create: `%USERPROFILE%\.cursor\mcp.json`
3. Add the same config
4. Restart Cursor
5. It should work there

Cursor IDE definitely supports MCP and is more reliable.

