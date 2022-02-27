gross_income = float(input("Enter the gross income: "))

num_dependents = int(input("Enter the number of dependents: "))

total = gross_income - 10000 - (num_dependents * 3000)

income_tax = (total * 20) / 100

print("The income tax is $" + str(income_tax))