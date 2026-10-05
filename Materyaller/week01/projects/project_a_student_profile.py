"""Week 1 project A: collect a student profile and print a readable summary."""

print("MIS203 Student Profile Builder")
print("Please enter the details below.")
print()

first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()
student_id = input("Student ID: ").strip()
department = input("Department: ").strip()
year = input("Year of study: ").strip()
email = input("University email: ").strip()
favorite_subject = input("Favorite subject: ").strip()
programming_goal = input("What would you like to build in Python? ").strip()
github_username = input("GitHub username: ").strip()

full_name = f"{first_name} {last_name}"
repository_name = f"basic-programming-{student_id}"
profile_heading = f"PROFILE: {full_name}"

print()
print("=" * 52)
print(profile_heading)
print("=" * 52)
print(f"Student ID       : {student_id}")
print(f"Department       : {department}")
print(f"Year             : {year}")
print(f"Email            : {email}")
print(f"Favorite subject : {favorite_subject}")
print(f"Python goal      : {programming_goal}")
print(f"GitHub username  : {github_username}")
print(f"Suggested repo   : {repository_name}")
print("=" * 52)
print("Next step: copy one sentence about your goal into README.md.")
