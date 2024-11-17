# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as f:
      data = json.load(f)
    total_sum = 0.0
    for item in data:
        score = item["score"]
        weight = item["weight"]
        total_sum += score * weight
    return round(total_sum, 3)

print(task())