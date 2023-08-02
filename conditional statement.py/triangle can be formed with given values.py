# Read angles from the user
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))
if angle1 > 0 and angle2 > 0 and angle3 > 0:
    
    if angle1 + angle2 + angle3 == 180:
        print("The given angles can form a triangle.")
    else:
        print("The given angles cannot form a triangle.")
else:
    print("Invalid input. Please enter valid positive angle values.")
