# daily_reminder.py
# A simple program that reminds the user of a single, priority task

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Adjust message if the task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = "Note: " + reminder + ". Consider completing it when you have free time."

# Print final reminder
print("\nReminder:", reminder)
