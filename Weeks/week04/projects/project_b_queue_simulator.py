"""Week 4 project B: process a simple service queue until the operator stops."""

print("Service Queue Simulator")
waiting = int(input("Customers initially waiting: "))
if waiting < 0:
    print("Initial queue cannot be negative.")
else:
    served = 0
    arrived = 0
    rounds = 0
    print("Commands: serve, arrive, status, stop")

    while True:
        command = input("Command: ").strip().lower()
        if command == "stop":
            break
        elif command == "serve":
            if waiting == 0:
                print("Nobody is waiting.")
            else:
                waiting -= 1
                served += 1
                print("One customer served.")
        elif command == "arrive":
            count = int(input("How many arrived? "))
            if count < 0:
                print("Arrival count cannot be negative.")
                continue
            waiting += count
            arrived += count
            print(f"{count} customer(s) added.")
        elif command == "status":
            print(f"Waiting: {waiting}; served: {served}")
        else:
            print("Unknown command.")
            continue
        rounds += 1

    print()
    print("=" * 48)
    print("QUEUE SESSION")
    print(f"Commands processed: {rounds}")
    print(f"Customers arrived: {arrived}")
    print(f"Customers served:  {served}")
    print(f"Still waiting:     {waiting}")
    print("=" * 48)
