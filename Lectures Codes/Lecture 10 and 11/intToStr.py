def intToStr(i):
    """ Assumes I is nonnegative integer
    Returns a decimal string representation of i"""
    digits = '0123456789'

    if i == 0:
        return '0'

    result = ''

    while i > 0:
        result = digits[i%10] + result
        i = i // 10

    return result

def addDigits(n):
    """ Assumes n is a nonnegative integer
    Returns the sum of the digits in n"""
    stringRep = intToStr(n)

    val = 0

    for c in stringRep:
        val += int(c)
    
    return val

print(intToStr(4))

print(addDigits(411)) # 4 + 1 + 1

print(addDigits(123456789)) # 1 + 2 + 3 + ... + 9 = 45