import csv
from datetime import date

def get_duration():
    while True:
        try:
            duration = int(input("Enter study duration (minutes): "))
            if duration <= 0:
                print("Duration must be greater than 0.")
                continue
            return duration
            break
        except ValueError:
            print("Please enter a valid number.")

def get_focus():
    while True:
        try:
            focus = int(input("Focus level (1-5): "))
            if focus < 1 or focus > 5:
                print("Focus must be between 1 and 5.")
                continue
            return focus
            break
        except ValueError:
            print("Please enter a valid number")

def save_to_csv(row):
    with open("data/study_log.csv", mode='a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

def read_study_data():
    rows = []
    with open("data/study_log.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                rows.append(row)
    return rows

def show_summary(data):
    total_sessions = len(data)
    total_minutes = sum(int(row[2]) for row in data)

    print("\nStudy Summary")
    print("----------------------")
    print(f"Total Sessions: {total_sessions}")
    print(f"Total Study Time: {total_minutes} minutes")

def study_time_by_subject(data):
    subject_totals = {}

    for row in data:
        subject = row[1]
        duration = int(row[2])

        if subject in subject_totals:
            subject_totals[subject] += duration
        else:
            subject_totals[subject] =  duration
    
    return subject_totals

def show_subject_analysis(subject_totals):
    print("\nStudy Time by Subject")
    print("-----------------------------")

    for subject, minutes in subject_totals.items():
        print(f"{subject}: {minutes} minutes")

def most_studied_subject(subject_totals):
    if not subject_totals:
        return None, 0
    
    subject = max(subject_totals, key=subject_totals.get)
    return subject, subject_totals[subject]

def show_insights(subject_totals):
    subject, minutes = most_studied_subject(subject_totals)

    if subject:
        print("\nInsight")
        print("-------------")
        print(f"Most studied subject: {subject} ({minutes} minutes)")

def focus_by_time_of_day(data):
    focus_data = {}

    for row in data:
        time_of_day = row[3]
        focus = int(row[4])

        if time_of_day not in focus_data:
            focus_data[time_of_day] = {"total_focus": 0, "count": 0}

        focus_data[time_of_day]["total_focus"] += focus
        focus_data[time_of_day]["count"] += 1

    return focus_data

def average_focus(focus_data):
    averages = {}

    for time, values in focus_data.items():
        averages[time] = values["total_focus"] / values["count"]

    return averages

def show_focus_insights(averages):
    print("\n Focus by Time of Day")
    print("---------------------------")

    for time, avg in averages.items():
        print(f"{time}: Average focus = {avg:.2f}")

    best_time = max(averages, key=averages.get)
    print(f"\n You focus best during: {best_time}")

def main():
    print("Smart Study and Productivity Analyzer")

    study_date = date.today().isoformat()
    subject = input("Enter subject: ")
    duration = get_duration()
    time_of_day = input("Enter Time of Day (Morning/Afternoon/Night): ")
    focus = get_focus()
    
    save_to_csv([study_date, subject, duration, time_of_day, focus])

    data = read_study_data()
    show_summary(data)

    subject_totals = study_time_by_subject(data)
    show_subject_analysis(subject_totals)
    show_insights(subject_totals)

    focus_data = focus_by_time_of_day(data)
    averages = average_focus(focus_data)
    show_focus_insights(averages)
    print("\nStudy Session recorded sucessfully")

if __name__ == "__main__":
    main()