# Write a function isln that accepts two strings as arguments and returns True if either string
# occurs anywhere in the other, and false otherwise. Uses built in str operation in

string1 = "Hello Victor, how are you?"
string2 = "Hello Victor"

def isln(string1, string2):
    """
    Input two strings
    Return True if either string occur anywhere in the other, and False otherwise
    """
    if string1 in string2:
        return True
    elif string2 in string1:
        return True
    else:
        return False

print(isln(string1,string2))
