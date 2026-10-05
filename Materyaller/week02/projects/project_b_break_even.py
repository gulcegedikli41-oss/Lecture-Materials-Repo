"""Week 2 project B: estimate contribution margin and break-even point."""

print("Small Business Break-Even Explorer")
business = input("Business name: ").strip()
product = input("Product or service: ").strip()
selling_price = float(input("Selling price per unit: "))
variable_cost = float(input("Variable cost per unit: "))
monthly_fixed_cost = float(input("Monthly fixed cost: "))
planned_units = int(input("Planned monthly sales (units): "))

unit_margin = selling_price - variable_cost
planned_revenue = planned_units * selling_price
planned_variable_cost = planned_units * variable_cost
planned_contribution = planned_revenue - planned_variable_cost
planned_profit = planned_contribution - monthly_fixed_cost

# This first look at a decision previews Week 3 conditionals.
if unit_margin > 0:
    break_even_units = monthly_fixed_cost / unit_margin
    break_even_whole_units = int(break_even_units) + (break_even_units % 1 > 0)
else:
    break_even_units = None
    break_even_whole_units = None

print()
print("=" * 54)
print(f"BREAK-EVEN ESTIMATE: {business}")
print(f"Product: {product}")
print("=" * 54)
print(f"Selling price/unit       {selling_price:10.2f} TRY")
print(f"Variable cost/unit       {variable_cost:10.2f} TRY")
print(f"Contribution/unit        {unit_margin:10.2f} TRY")
print(f"Fixed cost/month         {monthly_fixed_cost:10.2f} TRY")
if break_even_units is None:
    print("Break-even: unavailable because unit margin is not positive")
else:
    print(f"Break-even (exact)       {break_even_units:10.2f} units")
    print(f"Break-even (whole units) {break_even_whole_units:10d} units")
print("-" * 54)
print(f"Planned revenue          {planned_revenue:10.2f} TRY")
print(f"Planned variable cost    {planned_variable_cost:10.2f} TRY")
print(f"Planned profit           {planned_profit:10.2f} TRY")
print("=" * 54)
