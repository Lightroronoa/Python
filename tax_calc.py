

units=int(input("Enter the number of units used :"))

price_per_unit=float(input("Enter the price per unit: "))
discount_percentage=float(input("Enter the discount percentage: "))

tax_percentage     =float(input("Enter the tax percentage: "))
subtotal           = units * price_per_unit

discount_amount    =(discount_percentage / 100) * subtotal
subtotal -= discount_amount

tax_amount=(tax_percentage / 100) * subtotal
total_bill= subtotal + tax_amount

print(f"Total bill to be paid: {total_bill:.2f}")
