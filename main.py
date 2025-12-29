import csv

print("Smart Study and Productivity Analyzer")

date = input("Enter date (YYYY-MM-DD): ")
subject = input("Enter subject: ")
while True:
    try:
        duration = int(input("Enter study duration (minutes): "))
        if duration <= 0:
            print("Duration must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

time_of_day = input("Enter Time of Day (Morning/Afternoon/Night): ")

while True:
    try:
        focus = int(input("Focus level (1-5): "))
        if focus < 1 or focus > 5:
            print("Focus must be between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number") 

with open("data/study_log.csv", mode='a', newline="") as file:
    writer = csv.writer(file)
    writer.writerow([date, subject, duration, time_of_day, focus])

print("\nStudy Session recorded")