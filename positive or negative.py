def check_number(number):
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Example usage
num = float(input("Enter a number: "))
check_number(num)

