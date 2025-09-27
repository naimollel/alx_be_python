# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format it as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    try:
        # Ask user for number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer for the number of days.")
        return
    
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format it as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

# Main execution
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
