
digit = input("Enter a single digit (0 to 9): ")

if len(digit) == 1 and digit.isdigit():
    digit_word = {
        '0': "Zero",
        '1': "One",
        '2': "Two",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine"
    }

    print(f"The digit {digit} in word format is: {digit_word[digit]}")
else:
    print("Invalid input. Please enter a single digit (0 to 9).")
