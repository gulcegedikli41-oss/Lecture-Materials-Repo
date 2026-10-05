total = 0.0
for day in range(1, 4):
    sale = float(input(f"Sales for day {day}: "))
    total += sale
print(f"Three-day total: {total:.2f} TRY")
print(f"Daily average: {total / 3:.2f} TRY")
