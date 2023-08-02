import roman no
i = roman.fromRoman("MCMIV")
j = roman.fromRoman("LV")
k = roman.fromRoman("XXIV")
print(i,j,k)

num1 = int(input("Enter a number = "))  
num2 = int(input("Enter a number = "))
print(f"{num1} in Roman numerals is: {roman.toRoman(num1)}") 
print(f"{num2} in Roman numerals is: {roman.toRoman(num2)}") 