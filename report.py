import json

def to_json(results, filename="eval_report.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved report to {filename}")
