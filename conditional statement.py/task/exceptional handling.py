try:
    a = 10
    print(a/0)
except NameError:
    print("Check")
except ZeroDivisionError:
    print("Can't divide by 0")



try:
    a = int(input("Enter a value ="))
    b = int(input("Enter a value ="))
    print(a+b)
except ValueError:
    print("string cant added")
    raise ValueError("string cant added")
except:
    print("Something went wrong")

else:
    print("code error")
finally:
    print("Program ended")