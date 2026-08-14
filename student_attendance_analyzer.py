import json
import csv
import os
from datetime import datetime

DATA_FILE = "attendance_data.json"
REPORT_FILE = "attendance_report.csv"

students = {}


# ============================================================
# DATA MANAGEMENT
# ============================================================

def load_data():
    global students

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                students = json.load(file)
        except (json.JSONDecodeError, OSError):
            students = {}
    else:
        students = {}


def save_data():
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("\nUnable to save attendance data.")


# ============================================================
# INPUT VALIDATION
# ============================================================

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


# ============================================================
# ATTENDANCE CALCULATION
# ============================================================

def calculate_percentage(present, total):
    if total == 0:
        return 0.0

    return (present / total) * 100


def get_attendance_status(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Good"
    elif percentage >= 65:
        return "Warning"
    else:
        return "Low"


# ============================================================
# ADD STUDENT
# ============================================================

def add_student():
    print("\n" + "=" * 60)
    print("ADD STUDENT")
    print("=" * 60)

    student_id = get_non_empty_input("Enter Student ID: ")

    if student_id in students:
        print("\nStudent ID already exists.")
        return

    name = get_non_empty_input("Enter Student Name: ")
    department = get_non_empty_input("Enter Department: ")
    year = get_integer("Enter Year: ", 1, 6)

    total_classes = get_integer(
        "Enter Total Classes Conducted: ", 0
    )

    present_classes = get_integer(
        "Enter Classes Attended: ", 0, total_classes
    )

    absent_classes = total_classes - present_classes
    percentage = calculate_percentage(
        present_classes, total_classes
    )

    students[student_id] = {
        "name": name,
        "department": department,
        "year": year,
        "total_classes": total_classes,
        "present_classes": present_classes,
        "absent_classes": absent_classes,
        "attendance_percentage": round(percentage, 2),
        "status": get_attendance_status(percentage),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_data()

    print("\nStudent added successfully!")
    print(f"Attendance Percentage: {percentage:.2f}%")
    print(f"Status: {get_attendance_status(percentage)}")


# ============================================================
# VIEW ALL STUDENTS
# ============================================================

def view_all_students():
    print("\n" + "=" * 100)
    print("ALL STUDENT ATTENDANCE RECORDS")
    print("=" * 100)

    if not students:
        print("No student records found.")
        return

    print(
        f"{'ID':<12}"
        f"{'Name':<22}"
        f"{'Department':<15}"
        f"{'Year':<7}"
        f"{'Present':<10}"
        f"{'Total':<8}"
        f"{'Attendance':<12}"
        f"{'Status':<12}"
    )

    print("-" * 100)

    for student_id, data in students.items():
        print(
            f"{student_id:<12}"
            f"{data['name'][:20]:<22}"
            f"{data['department'][:13]:<15}"
            f"{data['year']:<7}"
            f"{data['present_classes']:<10}"
            f"{data['total_classes']:<8}"
            f"{data['attendance_percentage']:.2f}%"
            f"{'':<6}"
            f"{data['status']:<12}"
        )


# ============================================================
# VIEW STUDENT DETAILS
# ============================================================

def view_student_details():
    print("\n" + "=" * 60)
    print("STUDENT DETAILS")
    print("=" * 60)

    student_id = get_non_empty_input("Enter Student ID: ")

    if student_id not in students:
        print("\nStudent not found.")
        return

    data = students[student_id]

    print(f"\nStudent ID          : {student_id}")
    print(f"Student Name        : {data['name']}")
    print(f"Department          : {data['department']}")
    print(f"Year                : {data['year']}")
    print(f"Total Classes       : {data['total_classes']}")
    print(f"Classes Attended    : {data['present_classes']}")
    print(f"Classes Absent      : {data['absent_classes']}")
    print(f"Attendance          : {data['attendance_percentage']:.2f}%")
    print(f"Status              : {data['status']}")
    print(f"Created At          : {data['created_at']}")


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():
    print("\n" + "=" * 60)
    print("SEARCH STUDENT")
    print("=" * 60)

    keyword = get_non_empty_input(
        "Enter Student ID or Name: "
    ).lower()

    results = []

    for student_id, data in students.items():
        if (
            keyword in student_id.lower()
            or keyword in data["name"].lower()
        ):
            results.append((student_id, data))

    if not results:
        print("\nNo matching student found.")
        return

    print("\nMatching Students")
    print("-" * 70)

    for student_id, data in results:
        print(
            f"ID: {student_id} | "
            f"Name: {data['name']} | "
            f"Attendance: {data['attendance_percentage']:.2f}%"
        )


# ============================================================
# UPDATE ATTENDANCE
# ============================================================

def update_attendance():
    print("\n" + "=" * 60)
    print("UPDATE ATTENDANCE")
    print("=" * 60)

    student_id = get_non_empty_input("Enter Student ID: ")

    if student_id not in students:
        print("\nStudent not found.")
        return

    data = students[student_id]

    print(f"\nStudent: {data['name']}")
    print(f"Current Total Classes: {data['total_classes']}")
    print(f"Current Classes Attended: {data['present_classes']}")

    total_classes = get_integer(
        "Enter Updated Total Classes: ", 0
    )

    present_classes = get_integer(
        "Enter Updated Classes Attended: ",
        0,
        total_classes
    )

    absent_classes = total_classes - present_classes
    percentage = calculate_percentage(
        present_classes,
        total_classes
    )

    data["total_classes"] = total_classes
    data["present_classes"] = present_classes
    data["absent_classes"] = absent_classes
    data["attendance_percentage"] = round(
        percentage, 2
    )
    data["status"] = get_attendance_status(percentage)
    data["updated_at"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    save_data()

    print("\nAttendance updated successfully!")
    print(f"New Attendance: {percentage:.2f}%")
    print(f"Status: {get_attendance_status(percentage)}")


# ============================================================
# UPDATE STUDENT INFORMATION
# ============================================================

def update_student():
    print("\n" + "=" * 60)
    print("UPDATE STUDENT INFORMATION")
    print("=" * 60)

    student_id = get_non_empty_input("Enter Student ID: ")

    if student_id not in students:
        print("\nStudent not found.")
        return

    data = students[student_id]

    print("\nLeave a field empty to keep the current value.")

    name = input(
        f"Name [{data['name']}]: "
    ).strip()

    department = input(
        f"Department [{data['department']}]: "
    ).strip()

    year_input = input(
        f"Year [{data['year']}]: "
    ).strip()

    if name:
        data["name"] = name

    if department:
        data["department"] = department

    if year_input:
        try:
            year = int(year_input)

            if 1 <= year <= 6:
                data["year"] = year
            else:
                print("Invalid year. Previous year retained.")

        except ValueError:
            print("Invalid year. Previous year retained.")

    data["updated_at"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    save_data()

    print("\nStudent information updated successfully!")


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():
    print("\n" + "=" * 60)
    print("DELETE STUDENT")
    print("=" * 60)

    student_id = get_non_empty_input("Enter Student ID: ")

    if student_id not in students:
        print("\nStudent not found.")
        return

    print(f"\nStudent: {students[student_id]['name']}")

    confirmation = input(
        "Are you sure you want to delete this student? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        del students[student_id]
        save_data()
        print("\nStudent deleted successfully!")
    else:
        print("\nDelete operation cancelled.")


# ============================================================
# ATTENDANCE ANALYSIS
# ============================================================

def analyze_attendance():
    print("\n" + "=" * 70)
    print("ATTENDANCE ANALYSIS")
    print("=" * 70)

    if not students:
        print("No student records available.")
        return

    total_students = len(students)

    percentages = [
        data["attendance_percentage"]
        for data in students.values()
    ]

    average = sum(percentages) / total_students

    excellent = sum(
        1 for p in percentages if p >= 90
    )

    good = sum(
        1 for p in percentages if 75 <= p < 90
    )

    warning = sum(
        1 for p in percentages if 65 <= p < 75
    )

    low = sum(
        1 for p in percentages if p < 65
    )

    highest_id = max(
        students,
        key=lambda sid: students[sid]["attendance_percentage"]
    )

    lowest_id = min(
        students,
        key=lambda sid: students[sid]["attendance_percentage"]
    )

    print(f"\nTotal Students       : {total_students}")
    print(f"Average Attendance   : {average:.2f}%")
    print(
        f"Highest Attendance   : "
        f"{students[highest_id]['name']} "
        f"({students[highest_id]['attendance_percentage']:.2f}%)"
    )
    print(
        f"Lowest Attendance    : "
        f"{students[lowest_id]['name']} "
        f"({students[lowest_id]['attendance_percentage']:.2f}%)"
    )

    print("\nAttendance Categories")
    print("-" * 40)
    print(f"Excellent (90%+)     : {excellent}")
    print(f"Good (75%-89%)       : {good}")
    print(f"Warning (65%-74%)    : {warning}")
    print(f"Low (Below 65%)      : {low}")


# ============================================================
# LOW ATTENDANCE REPORT
# ============================================================

def low_attendance_report():
    print("\n" + "=" * 70)
    print("LOW ATTENDANCE REPORT")
    print("=" * 70)

    threshold = get_integer(
        "Enter attendance threshold (%): ",
        0,
        100
    )

    found = False

    print()

    for student_id, data in students.items():
        if data["attendance_percentage"] < threshold:
            found = True

            print(
                f"ID: {student_id} | "
                f"Name: {data['name']} | "
                f"Attendance: "
                f"{data['attendance_percentage']:.2f}%"
            )

    if not found:
        print(
            f"No students have attendance below {threshold}%."
        )


# ============================================================
# DASHBOARD
# ============================================================

def dashboard():
    print("\n" + "=" * 70)
    print("STUDENT ATTENDANCE DASHBOARD")
    print("=" * 70)

    if not students:
        print("No student data available.")
        return

    total_students = len(students)

    total_classes = sum(
        data["total_classes"]
        for data in students.values()
    )

    total_present = sum(
        data["present_classes"]
        for data in students.values()
    )

    total_absent = sum(
        data["absent_classes"]
        for data in students.values()
    )

    average = (
        sum(
            data["attendance_percentage"]
            for data in students.values()
        ) / total_students
    )

    print(f"\nTotal Students       : {total_students}")
    print(f"Total Classes        : {total_classes}")
    print(f"Total Present        : {total_present}")
    print(f"Total Absent         : {total_absent}")
    print(f"Average Attendance   : {average:.2f}%")

    print("\nStatus Distribution")
    print("-" * 40)

    status_count = {
        "Excellent": 0,
        "Good": 0,
        "Warning": 0,
        "Low": 0
    }

    for data in students.values():
        status = data["status"]

        if status in status_count:
            status_count[status] += 1

    for status, count in status_count.items():
        print(f"{status:<15}: {count}")


# ============================================================
# CSV REPORT
# ============================================================

def export_csv_report():
    if not students:
        print("\nNo student data available for export.")
        return

    try:
        with open(
            REPORT_FILE,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Student ID",
                "Name",
                "Department",
                "Year",
                "Total Classes",
                "Present Classes",
                "Absent Classes",
                "Attendance Percentage",
                "Status"
            ])

            for student_id, data in students.items():
                writer.writerow([
                    student_id,
                    data["name"],
                    data["department"],
                    data["year"],
                    data["total_classes"],
                    data["present_classes"],
                    data["absent_classes"],
                    data["attendance_percentage"],
                    data["status"]
                ])

        print(
            f"\nCSV report generated successfully: "
            f"{REPORT_FILE}"
        )

    except OSError:
        print("\nUnable to create CSV report.")


# ============================================================
# MENU
# ============================================================

def display_menu():
    print("\n")
    print("=" * 70)
    print("        STUDENT ATTENDANCE ANALYZER")
    print("=" * 70)
    print("1.  Add Student")
    print("2.  View All Students")
    print("3.  View Student Details")
    print("4.  Search Student")
    print("5.  Update Attendance")
    print("6.  Update Student Information")
    print("7.  Delete Student")
    print("8.  Analyze Attendance")
    print("9.  Low Attendance Report")
    print("10. Dashboard")
    print("11. Export CSV Report")
    print("12. Exit")
    print("=" * 70)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    load_data()

    print("=" * 70)
    print("        WELCOME TO STUDENT ATTENDANCE ANALYZER")
    print("=" * 70)

    while True:
        display_menu()

        choice = input(
            "Enter your choice (1-12): "
        ).strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_all_students()

        elif choice == "3":
            view_student_details()

        elif choice == "4":
            search_student()

        elif choice == "5":
            update_attendance()

        elif choice == "6":
            update_student()

        elif choice == "7":
            delete_student()

        elif choice == "8":
            analyze_attendance()

        elif choice == "9":
            low_attendance_report()

        elif choice == "10":
            dashboard()

        elif choice == "11":
            export_csv_report()

        elif choice == "12":
            save_data()

            print("\n" + "=" * 70)
            print("Thank you for using Student Attendance Analyzer!")
            print("Goodbye! 👋")
            print("=" * 70)

            break

        else:
            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 12."
            )


if __name__ == "__main__":
    main()
