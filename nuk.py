"""_summary_
"""
import json
out = json.dumps({ "name": "steve"})
with open("output.json", "w", encoding="utf-8") as f:
    f.write(out)
