# Read an alphabet from the user
alphabet = input("Enter an alphabet: ")

# Convert the alphabet to lowercase (to handle uppercase input)
alphabet = alphabet.lower()

# Check if the input is a single alphabet
if len(alphabet) == 1 and 'a' <= alphabet <= 'z':
    # Check if it is a vowel or consonant
    if alphabet in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet.")
