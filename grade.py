# Read the grade from the user
grade = input("Enter the grade: ")
grade = grade.upper()
if grade == 'E':
    print("Excellent")
elif grade == 'V':
    print("Very Good")
elif grade == 'G':
    print("Good")
elif grade == 'A':
    print("Average")
elif grade == 'F':
    print("Fail")
else:
    print("Invalid grade. Please enter a valid grade (E, V, G, A, or F).")
