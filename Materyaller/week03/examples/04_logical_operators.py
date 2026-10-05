amount = float(input("Basket amount: "))
member = input("Member (yes/no): ").strip().lower() == "yes"
if amount >= 1000 and member:
    print("15% discount")
elif amount >= 1000 or member:
    print("5% discount")
else:
    print("No discount")
