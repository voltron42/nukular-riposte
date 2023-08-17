"""_summary_
"""
import json
out = json.dumps({ "name": "steve"})
with open("output.json","w") as f:
    f.write(out)
