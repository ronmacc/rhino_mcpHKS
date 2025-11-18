# Check Claude Desktop MCP Support

## Important: Does Your Claude Desktop Support MCP?

Not all versions of Claude Desktop support MCP servers. Let's check:

### Step 1: Check Claude Desktop Version

1. Open Claude Desktop
2. Go to **Settings** (gear icon, usually bottom left)
3. Look for **About** or **Version** information
4. You need a recent version (from late 2024 or 2025)

### Step 2: Check for MCP Settings

1. In Claude Desktop Settings
2. Look for:
   - **Developer** section
   - **MCP** or **Model Context Protocol** section
   - **Servers** section
3. If you see "rhino" listed there, it's reading the config
4. If you see an error next to "rhino", that's the problem

### Step 3: Alternative - Check Cursor IDE Instead

If Claude Desktop doesn't support MCP, you can use Cursor IDE:

1. Install Cursor IDE (if you don't have it)
2. Create/edit: `%USERPROFILE%\.cursor\mcp.json`
3. Add the same config:
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
4. Restart Cursor
5. It should work there

### Step 4: Verify Claude Desktop is Actually Using the Config

The config file location might be wrong. Claude Desktop might be looking elsewhere.

Try creating the config in multiple locations:

1. `%APPDATA%\Claude\claude_desktop_config.json` (current)
2. `%LOCALAPPDATA%\Claude\claude_desktop_config.json`
3. `%USERPROFILE%\.claude\claude_desktop_config.json`

### Step 5: Check if MCP is Enabled

Some Claude Desktop versions require MCP to be explicitly enabled:

1. Check Settings → Developer
2. Look for "Enable MCP" or "MCP Servers" toggle
3. Make sure it's ON

## If Nothing Works:

The issue might be that your Claude Desktop version doesn't support MCP yet. In that case:

1. **Update Claude Desktop** to the latest version
2. Or **use Cursor IDE** instead (it definitely supports MCP)
3. Or **use Claude in a browser** with MCP extensions (if available)

