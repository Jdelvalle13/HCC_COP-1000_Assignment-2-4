# input statements
salary = float(input("Enter the salary: "))
numDependents = float(input("Enter the number of dependents: "))

# calculate taxes here
stateTax = salary * .065
federalTax = salary *.28
dependentDeduction = salary * numDependents * .025
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
