import csv
from datetime import date
import pandas as pd
import os
import matplotlib.pyplot as plt

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
    file_exists = os.path.isfile("data/study_log.csv")

    with open("data/study_log.csv", mode='a', newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date", "subject", "durations", "time_of_day", "focus"])
        writer.writerow(row)

def read_study_data():
    rows = []
    with open("data/study_log.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader, None)
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
    print(f"\nYou focus best during: {best_time}")

def load_data_pandas():
    columns = ["date", "subject", "duration", "time_of_day", "focus"]
    return pd.read_csv("data/study_log.csv")

def pandas_summary(df):
    print("\n Pandas Summary")
    print("-------------------")
    print(df.groupby("subject")["duration"].sum())

def plot_study_time(df):
    df.groupby("subject")["duration"].sum().plot(kind="bar")
    plt.title("Study Time by Subject")
    plt.ylabel("Minutes")
    plt.xlabel("Subject")
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\nSmart Study and Productivity Analyzer")
        print("1. Add study session")
        print("2. Show basic summary")
        print("3. Study time per subject")
        print("4. Most studied subject")
        print("5. Focus Analysis")
        print("6. Pandas Analysis")
        print("7. Visual Representation")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            study_date = date.today().isoformat()
            subject = input("Enter subject: ")
            duration = get_duration()
            time_of_day = input("Enter Time of Day (Morning/Afternoon/Night): ")
            focus = get_focus()
            save_to_csv([study_date, subject, duration, time_of_day, focus])
            print("\nStudy Session recorded sucessfully")
        elif choice == "2":
            data = read_study_data()
            show_summary(data)
        elif choice == "3":
            subject_totals = study_time_by_subject(data)
            show_subject_analysis(subject_totals)
        elif choice == "4":
            subject_totals = study_time_by_subject(data)
            show_subject_analysis(subject_totals)
            show_insights(subject_totals)
        elif choice == "5":
            focus_data = focus_by_time_of_day(data)
            averages = average_focus(focus_data)
            show_focus_insights(averages)
        elif choice == "6":
            df = load_data_pandas()
            pandas_summary(df)
        elif choice == "7":
            plot_study_time(df)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice. Please enter 1-8.")

if __name__ == "__main__":
    main()