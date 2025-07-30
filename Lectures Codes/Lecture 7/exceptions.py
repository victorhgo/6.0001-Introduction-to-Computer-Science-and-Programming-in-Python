# try:
#     a = int(input("Type a number: "))
#     b = int(input("Type another number: "))
#     print(a/b)
# except:
#     print("Error! Invalid user input!")

try:
    a = int(input("Type a number: "))
    b = int(input("Type another number: "))
    print("a / b =", a/b)
    print("a + b =", a + b)
except ValueError:
    print("Could not convert to an integer")
except ZeroDivisionError:
    print("Division by zero can't be handled")
except:
    print("Error!") 