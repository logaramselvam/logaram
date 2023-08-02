
month_number = int(input("Enter a month number (1-12): "))
days_in_month = {
    1: 31,  # January
    2: 28,  # February (assuming not a leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

if 1 <= month_number <= 12:
    
    num_days = days_in_month[month_number]
    print(f"The number of days in month {month_number} is: {num_days}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
