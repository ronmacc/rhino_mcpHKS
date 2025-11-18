# Get RhinoMCP Working - Simple 3 Steps

I know this is frustrating. Let's get it working with just 3 steps.

## Step 1: Check Your Config File

1. Press `Win + R`
2. Type: `%APPDATA%\Claude\claude_desktop_config.json`
3. Press Enter

Make sure it looks EXACTLY like this:

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

**IMPORTANT:** Use forward slashes (`/`) not backslashes (`\`)

Save it and close.

---

## Step 2: Start Rhino

1. Open **Rhino 7**
2. Click **Tools** → **Python Script** → **Run...**
3. Go to: `C:\Users\aroncal\Repos\rhino_mcpHKS\rhino_mcp\`
4. Click on `rhino_mcp_client.py`
5. Click **Open**

You should see in the Python Editor: "RhinoMCP script loaded. Server started automatically."

**Keep Rhino open!**

---

## Step 3: Start Claude Desktop

1. **Close Claude Desktop completely** (if it's open)
2. **Wait 5 seconds**
3. **Open Claude Desktop**
4. **Wait 20 seconds** (seriously, wait - it needs time)
5. Click **New Chat**
6. Type: "Get information about the current Rhino scene"

---

## That's It!

If you see more than 3 buttons, it's working!

If not, check the logs:
- Press `Win + R`
- Type: `%APPDATA%\Claude\logs`
- Open the newest file
- Look for errors about "rhino" or "mcp"

---

## Common Problem:

**Claude Desktop wasn't restarted after fixing the config.**

It only reads the config when it starts. You MUST close it completely and reopen it.

