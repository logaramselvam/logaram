month_number = int(input("Enter a month number (1-12): "))
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

if 1 <= month_number <= 12:

    month_name = months[month_number]
    print(f"month number {month_number} is {month_name}.")
else:
    print(".Please enter a number between 1 and 12.")
