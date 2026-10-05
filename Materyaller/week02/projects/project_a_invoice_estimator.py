"""Week 2 project A: calculate a two-line invoice estimate."""

print("Two-Line Invoice Estimator")
customer = input("Customer name: ").strip()
item_one = input("First item: ").strip()
quantity_one = int(input("First quantity: "))
price_one = float(input("First unit price: "))
item_two = input("Second item: ").strip()
quantity_two = int(input("Second quantity: "))
price_two = float(input("Second unit price: "))
shipping = float(input("Shipping charge: "))
discount_percent = float(input("Discount percentage (0-100): "))
tax_percent = float(input("Tax percentage (0-100): "))

line_one = quantity_one * price_one
line_two = quantity_two * price_two
subtotal = line_one + line_two
discount = subtotal * discount_percent / 100
discounted = subtotal - discount
tax = discounted * tax_percent / 100
grand_total = discounted + tax + shipping

print()
print("=" * 58)
print(f"ESTIMATED INVOICE FOR {customer}")
print("=" * 58)
print(f"{item_one:25} {quantity_one:3d} x {price_one:8.2f} = {line_one:9.2f}")
print(f"{item_two:25} {quantity_two:3d} x {price_two:8.2f} = {line_two:9.2f}")
print("-" * 58)
print(f"Subtotal:                {subtotal:10.2f} TRY")
print(f"Discount ({discount_percent:.1f}%):       -{discount:10.2f} TRY")
print(f"Tax ({tax_percent:.1f}%):                 {tax:10.2f} TRY")
print(f"Shipping:                {shipping:10.2f} TRY")
print(f"TOTAL:                   {grand_total:10.2f} TRY")
print("=" * 58)
print("Discuss: which inputs should be checked in a later version?")
