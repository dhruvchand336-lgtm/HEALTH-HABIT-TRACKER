from datetime import datetime, timedelta

print("\n--- Daily Health Habit Tracker ---\n")

water = int(input("Water (glasses): "))
sleep = int(input("Sleep (hours): "))
steps = int(input("Steps walked: "))
exercise = int(input("Exercise minutes: "))

today = datetime.now().strftime("%Y-%m-%d")

data[today] = {
    "water": water,
    "sleep": sleep,
    "steps": steps,
    "exercise": exercise
}

print("\n✔ Entry saved!\n")

print("--- Weekly Summary (Last 7 Days) ---\n")

total = {"water": 0, "sleep": 0, "steps": 0, "exercise": 0}
days_count = 0

for i in range(7):
    date_check = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")

    if date_check in data:
        total["water"] += data[date_check]["water"]
        total["sleep"] += data[date_check]["sleep"]
        total["steps"] += data[date_check]["steps"]
        total["exercise"] += data[date_check]["exercise"]
        days_count += 1

if days_count > 0:
    print("Average Water     :", total["water"] // days_count)
    print("Average Sleep     :", total["sleep"] // days_count)
    print("Average Steps     :", total["steps"] // days_count)
    print("Average Exercise  :", total["exercise"] // days_count)
else:
    print("No enough data for summary.")
