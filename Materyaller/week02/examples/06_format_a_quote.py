customer = input("Customer: ")
item = input("Item: ")
quantity = int(input("Quantity: "))
price = float(input("Unit price: "))
total = quantity * price
print(f"Quote for {customer}")
print(f"{quantity} x {item} at {price:.2f} TRY")
print(f"Total: {total:.2f} TRY")
