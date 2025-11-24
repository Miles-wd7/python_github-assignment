# app.py
# Simple Study Time Tracker Program
# This program asks the user for daily gaming hours, performs a calculation,
# and includes basic error handling.

print("Welcome to my Python program!")

# Ask for user input
hours = input("How many hours did you game today? ")

try:
    # Convert input to a number
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Perform a calculation
weekly_hours = hours * 7

# Display the result
print(f"You are on track to game {weekly_hours} hours this week.")

