
character = input("Enter a character: ")
if len(character) == 1:
    
    if character.isalpha():
        print(f"{character} is an alphabet.")
    
    elif character.isdigit():
        print(f"{character} is a digit.")
    
    else:
        print(f"{character} is a special character.")
else:
    print("Please enter a single character.")
