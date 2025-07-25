# daily_reminder.py
# This script collects a single task, its priority, and time sensitivity,
# then provides a custom reminder based on that input.

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate reminder using match case and conditionals
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Plan to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to get it done this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but needs to be done today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
