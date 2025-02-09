import json

def save_results(data, filename="results.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_results(filename="results.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)