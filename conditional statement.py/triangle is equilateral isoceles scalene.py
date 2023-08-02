
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 > 0 and side2 > 0 and side3 > 0:
    
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        
        if side1 == side2 == side3:
            print("The triangle is an Equilateral triangle.")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("The triangle is an Isosceles triangle.")
        else:
            print("The triangle is a Scalene triangle.")
    else:
        print("The given side lengths cannot form a valid triangle.")
else:
    print("Please enter valid positive side lengths.")
