#welcome message
print("Welcome to my Python program!")
#ask user for input
hours = input("How many hours did you study today? ")
#convert input and calculate result
#convert input to number then calculate estimated weekly time
try:
    hours = float(hours)
    weekly_hours = hours * 7
#display response
    print(f"You are on track to study {weekly_hours} hours this week.")

#run if the user entered invalid number
except ValueError:
    print("Please enter a valid number.")
    