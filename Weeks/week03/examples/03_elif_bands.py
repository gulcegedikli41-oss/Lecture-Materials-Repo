score = int(input("Score (0-100): "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 85:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Needs improvement")
