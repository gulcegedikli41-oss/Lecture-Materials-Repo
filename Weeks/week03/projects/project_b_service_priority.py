"""Week 3 project B: classify a service request with explicit rules."""

print("Service Desk Priority Classifier")
ticket_id = input("Ticket ID: ").strip()
customer = input("Customer: ").strip()
service_down = input("Service completely down (yes/no): ").strip().lower()
users_affected = int(input("Users affected: "))
deadline_hours = float(input("Hours until business deadline: "))
vip = input("Priority customer (yes/no): ").strip().lower()

if users_affected < 0 or deadline_hours < 0:
    print("Invalid numerical input.")
elif service_down not in ("yes", "no") or vip not in ("yes", "no"):
    print("Please answer yes or no.")
else:
    down = service_down == "yes"
    priority_customer = vip == "yes"

    if down and users_affected >= 20:
        priority = "Critical"
        target_hours = 1
    elif down or (users_affected >= 20 and deadline_hours <= 4):
        priority = "High"
        target_hours = 4
    elif priority_customer or users_affected >= 5 or deadline_hours <= 8:
        priority = "Medium"
        target_hours = 8
    else:
        priority = "Normal"
        target_hours = 24

    print()
    print("=" * 52)
    print(f"TICKET {ticket_id}: {customer}")
    print("=" * 52)
    print(f"Priority: {priority}")
    print(f"Suggested response target: {target_hours} hour(s)")
    print(f"Users affected: {users_affected}")
    print(f"Service down: {down}")
    print("Review the rule with the service team before real use.")
    print("=" * 52)
