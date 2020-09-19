purchase = float(input("Enter the amount of purchases: "))

stateTax = purchase * 5 / 100
countyTax = purchase * 2.5 / 100
totalTax = stateTax + countyTax
totalSale = purchase + totalTax

print("The amount of purchase: ", purchase)
print("The state sales tax: ", stateTax)
print("The county sales tax: ", countyTax)
print("The total of tax: ", totalTax)
print("The total of sale: ", totalSale)
