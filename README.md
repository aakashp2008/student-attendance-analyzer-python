# 🎓 Student Attendance Analyzer

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue.svg">
<img src="https://img.shields.io/badge/JSON-Data%20Storage-orange.svg">
<img src="https://img.shields.io/badge/CSV-Reports-green.svg">
<img src="https://img.shields.io/badge/Attendance-Analytics-purple.svg">
<img src="https://img.shields.io/badge/CLI-Application-black.svg">
<img src="https://img.shields.io/badge/Status-Completed-success.svg">
<img src="https://img.shields.io/badge/License-Educational-yellow.svg">

</p>

<p align="center">
  <b>📊 A Python-based system for managing student attendance, calculating attendance percentages, analyzing performance, and generating reports.</b>
</p>

---

## 📖 Overview

The **Student Attendance Analyzer** is a professional Python-based application designed to manage, track, and analyze student attendance records.

The system allows users to add students, view student records, search students, update attendance, calculate attendance percentages, identify students with low attendance, analyze overall attendance performance, and export detailed CSV reports.

This project demonstrates practical implementation of **Python programming, data management, JSON storage, CSV reporting, CRUD operations, input validation, attendance analytics, and command-line application development**.

---

## ✨ Features

- 👨‍🎓 Student Management
- ➕ Add Students
- 📋 View All Students
- 🔍 Search Students
- 📄 View Student Details
- ✏️ Update Student Information
- 📊 Update Attendance
- 🗑️ Delete Students
- 🧮 Attendance Percentage Calculation
- 🏆 Attendance Status Evaluation
- ⚠️ Low Attendance Detection
- 📈 Attendance Performance Analysis
- 📊 Attendance Dashboard
- 📄 CSV Report Generation
- 💾 JSON Data Storage
- 🖥️ Command-Line Interface
- ✅ Input Validation
- 🔄 Automatic Data Saving

---

## 🏆 Attendance Evaluation

The system automatically evaluates student attendance based on the attendance percentage.

### Attendance Levels

| Attendance | Status |
|-----------:|--------|
| 90–100% | 🌟 Excellent |
| 75–89% | 🟢 Good |
| 65–74% | 🟡 Warning |
| Below 65% | 🔴 Low |

The attendance percentage is calculated using:

```text
Attendance Percentage = (Classes Attended / Total Classes) × 100
```

---

## 📊 Attendance Analytics

The application provides useful attendance analytics including:

- Total Students
- Total Classes Conducted
- Total Classes Attended
- Total Classes Absent
- Average Attendance
- Highest Attendance
- Lowest Attendance
- Excellent Students
- Good Students
- Warning Students
- Low Attendance Students

Example:

```text
======================================================================
ATTENDANCE ANALYSIS
======================================================================

Total Students       : 10
Average Attendance   : 82.40%

Highest Attendance   : Student Name (95.00%)
Lowest Attendance    : Student Name (58.00%)

Attendance Categories
----------------------------------------
Excellent (90%+)     : 3
Good (75%-89%)       : 4
Warning (65%-74%)    : 2
Low (Below 65%)      : 1
```

---

## 💡 Smart Attendance Monitoring

The system can identify students whose attendance falls below a selected threshold.

Example:

```text
======================================================================
LOW ATTENDANCE REPORT
======================================================================

Enter attendance threshold (%): 75

ID: STU003 | Name: Student Name | Attendance: 68.00%
ID: STU007 | Name: Student Name | Attendance: 72.50%
```

This helps identify students who may need to improve their attendance.

---

## 🛠️ Technologies Used

- Python 3
- JSON
- CSV
- Datetime
- OS
- File Handling
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling
- Input Validation
- Data Processing
- Command-Line Interface

---

## 📂 Project Structure

```text
student-attendance-analyzer-python/
│
├── student_attendance_analyzer.py
├── attendance_data.json
├── attendance_report.csv
└── README.md
```

The `attendance_data.json` and `attendance_report.csv` files are generated automatically when the corresponding features are used.

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/aakashp2008/student-attendance-analyzer-python.git
```

### Navigate to the Project

```bash
cd student-attendance-analyzer-python
```

### Run the Program

```bash
python student_attendance_analyzer.py
```

No external Python packages are required.

### Programiz

The project uses only Python's standard library, so it can also be executed using the **Programiz Python Online Compiler** without installing external packages.

---

## 🖥️ Main Menu

```text
======================================================================
        STUDENT ATTENDANCE ANALYZER
======================================================================

1.  Add Student
2.  View All Students
3.  View Student Details
4.  Search Student
5.  Update Attendance
6.  Update Student Information
7.  Delete Student
8.  Analyze Attendance
9.  Low Attendance Report
10. Dashboard
11. Export CSV Report
12. Exit
======================================================================
```

---

## 📋 Example

### Add Student

```text
======================================================================
ADD STUDENT
======================================================================

Enter Student ID: STU001
Enter Student Name: Aakash
Enter Department: Information Technology
Enter Year: 2
Enter Total Classes Conducted: 100
Enter Classes Attended: 88

Student added successfully!
Attendance Percentage: 88.00%
Status: Good
```

### View Student Details

```text
======================================================================
STUDENT DETAILS
======================================================================

Enter Student ID: STU001

Student ID          : STU001
Student Name        : Aakash
Department          : Information Technology
Year                : 2
Total Classes       : 100
Classes Attended    : 88
Classes Absent      : 12
Attendance          : 88.00%
Status              : Good
```

### Update Attendance

```text
======================================================================
UPDATE ATTENDANCE
======================================================================

Enter Student ID: STU001

Student: Aakash
Current Total Classes: 100
Current Classes Attended: 88

Enter Updated Total Classes: 110
Enter Updated Classes Attended: 97

Attendance updated successfully!
New Attendance: 88.18%
Status: Good
```

### Dashboard

```text
======================================================================
STUDENT ATTENDANCE DASHBOARD
======================================================================

Total Students       : 10
Total Classes        : 1000
Total Present        : 824
Total Absent         : 176
Average Attendance   : 82.40%

Status Distribution
----------------------------------------
Excellent      : 3
Good           : 4
Warning        : 2
Low            : 1
```

---

## 📄 Reports

The application can generate a detailed CSV attendance report containing:

- Student ID
- Student Name
- Department
- Year
- Total Classes
- Present Classes
- Absent Classes
- Attendance Percentage
- Attendance Status

Generated file:

```text
attendance_report.csv
```

The report can be opened using spreadsheet applications such as **Microsoft Excel** or other compatible software.

---

## 💾 Data Storage

Student attendance information is stored locally using JSON.

Generated file:

```text
attendance_data.json
```

The JSON data contains information such as:

- Student ID
- Student Name
- Department
- Year
- Total Classes
- Present Classes
- Absent Classes
- Attendance Percentage
- Attendance Status
- Record Date
- Updated Date

Example:

```json
{
    "STU001": {
        "name": "Aakash",
        "department": "Information Technology",
        "year": 2,
        "total_classes": 100,
        "present_classes": 88,
        "absent_classes": 12,
        "attendance_percentage": 88.0,
        "status": "Good"
    }
}
```

This makes the application lightweight and easy to run without requiring a database server.

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Python Programming
- Student Management
- Attendance Management
- Data Processing
- JSON Data Storage
- CSV Report Generation
- Data Structures
- CRUD Operations
- Input Validation
- Functions
- Lists and Dictionaries
- Conditional Statements
- Exception Handling
- Attendance Calculations
- Performance Analysis
- File Handling
- Command-Line Application Development
- Problem-Solving Skills

---

## 🚀 Future Enhancements

- 🌐 Web-Based Attendance Management System
- 🖥️ Graphical User Interface using Tkinter
- 📱 Mobile Attendance Application
- 🗄️ MySQL / SQLite Database
- 👤 User Authentication
- 👨‍🏫 Faculty Login
- 🎓 Student Login
- 📚 Subject-Wise Attendance
- 📅 Monthly Attendance Reports
- 📈 Interactive Attendance Charts
- 🔔 Automatic Low Attendance Notifications
- 📄 PDF Report Generation
- 📧 Email Notifications
- ☁️ Cloud Data Storage
- 📊 Advanced Attendance Analytics
- 🏫 College-Level Attendance Management System

---

## 🌟 Project Purpose

Student attendance is an important part of academic management.

The **Student Attendance Analyzer** provides a simple solution for maintaining student attendance records, calculating attendance percentages, analyzing attendance performance, identifying students with low attendance, and generating reports.

The project can be extended into a complete **college attendance management platform** with database integration, authentication, graphical dashboards, subject-wise tracking, and automated notifications.

---

## 👨‍💻 About

The **Student Attendance Analyzer** was developed as a Python project to demonstrate practical application development, student data management, attendance analysis, file handling, and report generation.

The application combines **student management, attendance calculations, analytics, JSON storage, and CSV reporting** into one professional command-line system.

---

## ⭐ Support

If you find this project useful, please consider giving the repository a **⭐ Star** on GitHub.

---

## 📄 License

This project is developed for educational and learning purposes.

```text
© 2026 Aakash P
```
