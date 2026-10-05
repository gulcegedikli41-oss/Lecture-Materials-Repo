price = float(input("Unit price: "))
for quantity in range(1, 6):
    print(f"{quantity:2d} units: {quantity * price:8.2f} TRY")
