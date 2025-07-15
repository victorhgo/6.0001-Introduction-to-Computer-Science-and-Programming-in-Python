# Part 1 - Inputs
annual_salary = float(input("Enter the starting salary: "))

# Part 2 - Processing
portion_down_payment = 250000 # 0.25 * total_cost ($1m)
epsilon = 100 # 100$

low = 0.0
high = max(0.000,0.999)

answer = (high + low) / 2.0

current_savings = 0
steps = 0

# Functions
def testRate(annual_salary, rate):
    """
    Input: Annual salary and the savings rate
    Returns total amount based on the entered rate
    """
    current_savings = 0
    i = 0
    for i in range(36):
        i += 1
        #print("Month = ", i, "Current Savings:", current_savings, "Rate:", answer)
        annual_return = current_savings * 0.04 / 12
        current_savings += ((annual_salary / 12) * rate) + annual_return

        if(i % 6 == 0):
            annual_salary += (annual_salary * 0.07)
    
    return current_savings

# 3 - Implement Bisection Method

while abs(round(current_savings,1) / portion_down_payment) <= epsilon:

    current_savings = testRate(annual_salary, answer)

    if current_savings > portion_down_payment:
        high = answer
    else:
        low = answer
    steps += 1
    answer = (high + low) / 2.0

    print("Current savings: ", current_savings, "Answer: ", answer, "Steps: ", steps)

    
print("answer = ", answer, "current savings = ", current_savings)
