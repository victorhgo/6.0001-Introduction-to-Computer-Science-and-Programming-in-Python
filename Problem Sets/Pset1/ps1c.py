# Part 1 - Inputs
annual_salary = float(input("Enter the starting salary: "))

# Part 2 - Variables
portion_down_payment = 250000 # 0.25 * total_cost ($1m)
current_savings = 0
steps = 0
epsilon = 100 # 100$
low = 0.0
high = max(0.000,0.9999)
answer = (high + low) / 2.0

# Part 3 - Processing

# Calculate the annual return based on rate
def calcRate(annual_salary, rate):
    """
    Input: Annual salary and savings rate as floats
    Returns total amount based on the entered rate as float
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

# If the income is too low, it won't be possible to pay in 36 months:
if calcRate(annual_salary, 1.0) < portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
    exit()

# Bisection search for the best saving rate
while abs(current_savings - portion_down_payment) > epsilon: 

    current_savings = round((calcRate(annual_salary, answer)), 2)

    if current_savings > portion_down_payment:
        high = answer
    else:
        low = answer

    steps += 1
    answer = round(((high + low) / 2.0), 4)
                         
print("Best saving rate:", answer)
print("Steps in bisection search:", steps)