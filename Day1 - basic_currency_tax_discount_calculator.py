er = int(input("Enter the amount in Euro: "))
print("Choose the product: 1. Gold  2. Books  3. Med")
pr = int(input("Enter your choice (1/2/3): "))

price_list = [100, 150, 200, 350, 99]
print("Available prices:", ", ".join(map(str, price_list)))

pro_price = int(input("Enter product price: "))
ir = er * 97.50

tax_rates = {1: 18, 2: 12, 3: 10}
if pr in tax_rates:
    ir -= ir * tax_rates[pr] / 100
else:
    print("Invalid product choice")

bal = ir
print("Balance in INR:", bal)
er = bal / 97.50
print("Balance in Euro:", er)

no_pr = int(input("Enter number of products: "))
total_price = no_pr * pro_price
bal -= total_price

if pr in tax_rates:
    bal -= bal * tax_rates[pr] / 100
else:
    print("Invalid product choice")

print("Remaining Balance in INR:", bal)
er = bal / 97.50
print("Remaining Balance in Euro:", er)

if er > 5000:
    er -= er * 10 / 100
    print("With discount:", er)
else:
    print("Without discount:", er)
