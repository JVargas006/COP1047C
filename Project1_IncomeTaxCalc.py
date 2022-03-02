#All taxpayers are charged a flat tax rate of 20%
#All taxpayers are allowed a $10,000 standard deduction
#For each dependent, a taxpayer is allowed an additional $3,000 deduction
TaxRate = 0.20
StandardDed = 10000.0
DependentDed = 3000.0

#inputs 
GrossIncome = float(input("Enter the gross income: "))
NumDependents = int (input("Enter the number of dependents: "))

#equation
TaxInc = GrossIncome - StandardDed - \
        DependentDed * NumDependents
IncTax = TaxInc * TaxRate

print("The income tax is $" + str(IncTax))