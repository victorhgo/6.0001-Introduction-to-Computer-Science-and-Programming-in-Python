def isPal(x):
    """ 
    Assumes x is a list
    Returns True if the list is a palindrome; False otherwise
    """
    temp = x
    temp.reverse

    if temp == x:
        return True
    else:
        return False
    
def silly(n):
    """
    Assumes n is an int > 0
    Gets n inputs from user
    Print 'yes' if the sequence of inputs forms a palindrome:
          'No' otherwise.
    """
    for i in range(n):
        result = []
        elem = input("Enter element: ")
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')

silly(2) # Test if is a palindrome or not, returns yes