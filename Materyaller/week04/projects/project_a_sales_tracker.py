"""Week 4 project A: collect daily sales and report a simple summary."""

print("Daily Sales Tracker")
days = int(input("Number of days (1-31): "))
if days < 1 or days > 31:
    print("Please choose a number from 1 to 31.")
else:
    total = 0.0
    highest = None
    lowest = None
    best_day = 0
    days_above_target = 0
    target = float(input("Daily sales target: "))

    for day in range(1, days + 1):
        sale = float(input(f"Sales for day {day}: "))
        while sale < 0:
            print("Sales cannot be negative.")
            sale = float(input(f"Sales for day {day}: "))
        total += sale
        if highest is None or sale > highest:
            highest = sale
            best_day = day
        if lowest is None or sale < lowest:
            lowest = sale
        if sale >= target:
            days_above_target += 1

    average = total / days
    print()
    print("=" * 50)
    print("SALES SUMMARY")
    print("=" * 50)
    print(f"Days recorded:       {days}")
    print(f"Total sales:         {total:.2f} TRY")
    print(f"Daily average:       {average:.2f} TRY")
    print(f"Highest daily sales: {highest:.2f} TRY (day {best_day})")
    print(f"Lowest daily sales:  {lowest:.2f} TRY")
    print(f"Days meeting target: {days_above_target}")
    print("=" * 50)
