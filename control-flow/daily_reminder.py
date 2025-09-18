# daily_reminder.py
# A simple program to remind the user about a single priority task

# Prompt for task details
task = input("Enter your task: ")

# Loop until user enters a valid priority
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Please enter a valid priority: high, medium, or low.")

# Loop until user enters val
