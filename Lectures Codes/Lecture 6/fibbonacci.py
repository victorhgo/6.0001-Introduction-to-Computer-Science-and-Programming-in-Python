def fib(x):
    """
    Assumes x an integer >= 0
    Returns Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib (x - 2)
    

print("Number of female rabbits after 12 months:", fib(12))

# Fibonacci with a dictionary: (Comparing using memoization)
# It will do a lookup first in case it already calculated the value and
# modify dictionary as progress through function calls:

print("Let's run the efficient one:")
def fibEfficient(number, dictionary):
    if number in dictionary:
        return dictionary[number]
    else:
        answer = fibEfficient(number - 1, dictionary) + fibEfficient(number - 2, dictionary)
        dictionary = answer
        return answer

dictionary = {1:1, 2:2}
print(fibEfficient(6, dictionary))

