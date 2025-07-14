# Part 1 - Inputs
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))


# Part 2 - Processing
portion_down_payment = 0.25 * total_cost

r = 0.04 # annual rate: 4%
i = 0 # Number of months
current_savings = 0

while(current_savings < portion_down_payment):
    i += 1

    annual_return = current_savings * r / 12
    current_savings += ((annual_salary / 12) * portion_saved) + annual_return

    if(i % 6 == 0):
        annual_salary += (annual_salary * semi_annual_raise)

# Part 3 - Outputs
print("Number of Months: ", i)