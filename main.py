import json
import os
from datetime import datetime, timedelta

file_path = "data/habits.json"

if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    with open(file_path, "w") as f:
        json.dump({}, f)

with open(file_path, "r") as f:
    data = json.load(f)

today = datetime.now().strftime("%Y-%m-%d")

print("\n--- Daily Health Habit Tracker ---\n")

water = int(input("Water (glasses): "))
sleep = int(input("Sleep (hours): "))
steps = int(input("Steps walked: "))
exercise = int(input("Exercise minutes: "))

data[today] = {
    "water": water,
    "sleep": sleep,
    "steps": steps,
    "exercise": exercise
}

with open(file_path, "w") as f:
    json.dump(data, f, indent=4)

print("\n✔ Entry saved!\n")

print("--- Weekly Summary (Last 7 Days) ---\n")

total = {"water": 0, "sleep": 0, "steps": 0, "exercise": 0}
days_count = 0

for i in range(7):
    date_chk = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
    
    if date_chk in data:
        total["water"] += data[date_chk]["water"]
        total["sleep"] += data[date_chk]["sleep"]
        total["steps"] += data[date_chk]["steps"]
        total["exercise"] += data[date_chk]["exercise"]
        days_count += 1
        
if days_count > 0:
    print("Average Water     :", total["water"] // days_count)
    print("Average Sleep     :", total["sleep"] // days_count)
    print("Average Steps     :", total["steps"] // days_count)
    print("Average Exercise  :", total["exercise"] // days_count)
else:
    print("No enough data for summary.")
