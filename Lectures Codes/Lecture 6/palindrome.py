def isPalindrome(string):
    """
    Receives an string, converts everything to chars and lower case using
    toChars(string) function, which will return a list to isPal(string) that
    verifies if string is a palindrome.

    Return True if string is a palindrome, and False otherwise.
    """
    def toChars(string):
        string = string.lower()
        ans = ''
        for ch in string:
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + ch
        return ans
    
    def isPal(string):
        if len(string) <= 1:
            return True
        else:
            return string[0] == string[-1] and isPal(string[1:-1])
    
    return isPal(toChars(string))

napoleon = "Able was I, ere I saw Elba"
print("Is,'", napoleon, "' a palindrome?", isPalindrome(napoleon))

string = "Ate Cubanos"
print("Is,'", string, "' a palindrome?", isPalindrome(string))
