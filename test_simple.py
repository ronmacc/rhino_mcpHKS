"""Super simple test - just tells you if it will work"""
import sys
import os

print("Testing if everything is ready...")
print()

# Test 1: Can we import?
try:
    import rhino_mcp.server
    print("[OK] Package is installed")
except:
    print("[FAIL] Package not installed - run: cd rhino_mcp && pip install -e .")
    sys.exit(1)

# Test 2: Check config
config_path = os.path.expandvars(r'%APPDATA%\Claude\claude_desktop_config.json')
if os.path.exists(config_path):
    print("[OK] Config file exists")
    try:
        import json
        with open(config_path) as f:
            config = json.load(f)
        if 'rhino' in config.get('mcpServers', {}):
            cmd = config['mcpServers']['rhino']['command']
            if '/' in cmd or '\\' in cmd:
                print(f"[OK] Config looks good: {cmd[:50]}...")
            else:
                print("[WARN] Config command might be wrong")
        else:
            print("[FAIL] Config missing 'rhino' server")
    except Exception as e:
        print(f"[FAIL] Config file error: {e}")
else:
    print("[FAIL] Config file not found!")

print()
print("If both say [OK], then:")
print("1. Start Rhino and run rhino_mcp_client.py")
print("2. Restart Claude Desktop")
print("3. Wait 20 seconds")
print("4. It should work!")

