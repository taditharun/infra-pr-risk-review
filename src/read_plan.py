import argparse
import json
from pathlib import Path

# Find the sample file and read its JSON.
parser = argparse.ArgumentParser()
parser.add_argument("plan_file", type=Path)
plan_path = parser.parse_args().plan_file
plan = json.loads(plan_path.read_text(encoding="utf-8"))

# Show the name and planned action for each resource.
for resource in plan["resource_changes"]:
    address = resource["address"]
    actions = " -> ".join(resource["change"]["actions"])
    print(f"{address}: {actions}")