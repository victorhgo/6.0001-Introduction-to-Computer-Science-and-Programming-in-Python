x = -25
epsilon = 0.01
step = epsilon**3
numGuesses = 0
low = 0.0
high = max(1.0, x)
answer = (high + low)/ 2.0
# answer = 0.0

# Finding square root of a number x by exhaustion:
# while abs(answer**2 - x) >= epsilon and answer <= x:
# while abs(answer ** 2 - x) >= epsilon and answer*answer <=x:
#   answer += step
#    numGuesses += 1
#print("NumGuesses:", numGuesses)
#if abs(answer**2 - x) >= epsilon:
#    print("Failed on square root of", x)
#else:
#    print(answer, "is close to the square root of", x)

# Finding the square root of a number x by bisection search
while abs(answer**2 - x) >= epsilon:
    print("Low =", low, "High =", high, "Answer =", answer)
    numGuesses += 1
    if answer**2 < x:
        low = answer
    else:
        high = answer
    answer = (high + low)/2.0

print("numGuesses =", numGuesses)
print(answer, "is close to the square root of", x)