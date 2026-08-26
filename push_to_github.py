import base64, json, urllib.request

TOKEN = "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"
REPO = "iconrealestate77/navigation"
FILES = [
"Navigation.ipynb", "Report.md", "README.md",
"dqn_agent.py", "model.py", "navigation.py",
"checkpoint.pth", "training_scores.png", "scores.pkl"
]

for fname in FILES:
with open(fname, "rb") as f:
content = base64.b64encode(f.read()).decode()

url = f"https://api.github.com/repos/{REPO}/contents/{fname}"
data = json.dumps({
"message": f"Add {fname}",
"content": content
}).encode()

req = urllib.request.Request(url, data=data, method="PUT")
req.add_header("Authorization", f"token {TOKEN}")
req.add_header("Accept", "application/vnd.github+json")

try:
resp = urllib.request.urlopen(req)
print(f"{fname}: {resp.status} OK")
except urllib.error.HTTPError as e:
print(f"{fname}: FAILED - {e.code} {e.read().decode()}")