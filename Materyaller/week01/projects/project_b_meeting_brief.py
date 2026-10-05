"""Week 1 project B: turn meeting input into a consistent text brief."""

print("MIS Team Meeting Brief")
print("This program gathers text and presents it clearly.")
print()

team_name = input("Team name: ").strip()
meeting_title = input("Meeting title: ").strip()
date = input("Date (YYYY-MM-DD): ").strip()
time = input("Time: ").strip()
room = input("Room or video link: ").strip()
host = input("Meeting host: ").strip()
participant_one = input("First participant: ").strip()
participant_two = input("Second participant: ").strip()
agenda_one = input("First agenda item: ").strip()
agenda_two = input("Second agenda item: ").strip()
expected_result = input("Expected result: ").strip()

title = f"{team_name}: {meeting_title}"
participants = f"{participant_one}, {participant_two}"
schedule = f"{date} at {time}"

print()
print("=" * 60)
print(title)
print("=" * 60)
print(f"When         : {schedule}")
print(f"Where        : {room}")
print(f"Host         : {host}")
print(f"Participants : {participants}")
print()
print("AGENDA")
print(f"1. {agenda_one}")
print(f"2. {agenda_two}")
print()
print(f"Expected result: {expected_result}")
print("=" * 60)
print("Save this output in your project notes if useful.")
