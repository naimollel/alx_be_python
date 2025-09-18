# pattern_drawing.py
# A program that draws a square pattern of asterisks using nested loops

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print each asterisk in the row
    for col in range(size):
        print("*", end="")  # keep printing on the same line
    print()  # move to the next line after finishing a row
    row += 1
