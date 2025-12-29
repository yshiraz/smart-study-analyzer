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

    print("\nStudy Session recorded sucessfully")

if __name__ == "__main__":
    main()