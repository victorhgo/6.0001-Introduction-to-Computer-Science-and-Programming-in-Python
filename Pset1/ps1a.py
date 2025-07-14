# Part 1 - Inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Part 2 - Processing
portion_down_payment = 0.25 * total_cost
monthly_savings = ((annual_salary / 12) * portion_saved) # Salary monthly savings
r = 0.04 # annual rate: 4%
i = 0 # Number of months
current_savings = 0

while(current_savings < portion_down_payment):
    annual_return = current_savings * r / 12
    current_savings += monthly_savings + annual_return
    i += 1

# Part 3 - Outputs
print("Number of Months: ", i)

# Notes:

# My difficult was using while in the correct way to return the correct result