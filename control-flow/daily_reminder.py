task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

while priority not in ["high", "medium", "low"]:
    priority = input("Please enter a valid priority (high/medium/low): ").strip().lower()

while time_bound not in ["yes", "no"]:
    time_bound = input("Please answer time-bound with 'yes' or 'no': ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Try to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task. Work on it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
