import csv

print("Smart Study and Productivity Analyzer")

date = input("Enter date (YYYY-MM-DD): ")
subject = input("Enter subject: ")
duration = input("Enter study duration (minutes): ")
time_of_day = input("Enter Time of Day (Morning/Afternoon/Night): ")
focus = input("Focus level (1-5): ")

with open("data/study_log.csv", mode='a', newline="") as file:
    writer = csv.writer(file)
    writer.writerow([date, subject, duration, time_of_day, focus])

print("\nStudy Session recorded")