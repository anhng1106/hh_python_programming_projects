interest_rate = float(input("Enter interest rate: "))
tax_rate = float(input("Enter capital income tax rate: "))
initial_deposit = float(input("Enter initial deposit: "))
num_of_years = int(input("Enter number of years: "))

print()

balance = initial_deposit

for i in range (1, num_of_years+1):
    interest = balance * interest_rate / 100
    tax_amount = interest - (interest * tax_rate / 100)

    balance = balance + tax_amount

    print(f"Year {i}: {balance:.2f}")
