"""Reusable calculations for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = [
    "Python",
    "Mathematics",
    "Data_Analytics",
    "Computer_Networks",
    "Database_Management",
]


def validate_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """Validate required columns and clean missing/invalid values."""
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
    missing_columns = [column for column in required if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    data = data.copy()
    if data["Student_ID"].duplicated().any():
        raise ValueError("Student_ID values must be unique.")
    if data[required].isnull().any().any():
        raise ValueError("Dataset contains missing values. Please correct students.csv.")

    for subject in SUBJECTS:
        data[subject] = pd.to_numeric(data[subject], errors="raise")
        if not data[subject].between(0, 100).all():
            raise ValueError(f"{subject} marks must be between 0 and 100.")

    data["Attendance"] = pd.to_numeric(data["Attendance"], errors="raise")
    if not data["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")

    return data


def assign_grade(average: float) -> str:
    """Assign a grade using the rules documented in README.md."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def process_students(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate totals, averages, grades, results, and rank."""
    result = data.copy()
    marks = result[SUBJECTS].to_numpy(dtype=float)
    result["Total_Marks"] = np.sum(marks, axis=1)
    result["Average_Marks"] = np.mean(marks, axis=1).round(2)

    grades = []
    pass_status = []
    # A loop is used intentionally to demonstrate the Python concepts in the assignment.
    for _, row in result.iterrows():
        average = float(row["Average_Marks"])
        grades.append(assign_grade(average))
        all_subjects_passed = all(row[subject] >= 35 for subject in SUBJECTS)
        pass_status.append("Pass" if all_subjects_passed and average >= 40 else "Fail")

    result["Grade"] = grades
    result["Result"] = pass_status
    result["Rank"] = result["Average_Marks"].rank(method="min", ascending=False).astype(int)
    result["Attendance_Status"] = np.where(result["Attendance"] >= 75, "Satisfactory", "Low Attendance")
    return result.sort_values(["Average_Marks", "Name"], ascending=[False, True]).reset_index(drop=True)


def create_summary(processed: pd.DataFrame) -> dict:
    """Create overall class statistics."""
    averages = processed["Average_Marks"].to_numpy(dtype=float)
    subject_averages = processed[SUBJECTS].mean().round(2)
    top_row = processed.loc[processed["Average_Marks"].idxmax()]
    low_row = processed.loc[processed["Average_Marks"].idxmin()]
    return {
        "total_students": int(len(processed)),
        "passed": int((processed["Result"] == "Pass").sum()),
        "failed": int((processed["Result"] == "Fail").sum()),
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": round(float(np.max(averages)), 2),
        "lowest_average": round(float(np.min(averages)), 2),
        "top_student": str(top_row["Name"]),
        "lowest_student": str(low_row["Name"]),
        "subject_averages": subject_averages,
        "subject_toppers": {
            subject: str(processed.loc[processed[subject].idxmax(), "Name"])
            for subject in SUBJECTS
        },
        "department_averages": processed.groupby("Department")["Average_Marks"].mean().round(2),
        "low_attendance_count": int((processed["Attendance"] < 75).sum()),
    }


def find_student(processed: pd.DataFrame, student_id: str) -> pd.DataFrame:
    """Find student records by ID (case-insensitive)."""
    return processed[processed["Student_ID"].astype(str).str.upper() == student_id.strip().upper()]


def print_report(processed: pd.DataFrame, summary: dict) -> None:
    """Print a readable student and class report."""
    display_columns = [
        "Student_ID", "Name", "Department", "Total_Marks", "Average_Marks",
        "Grade", "Result", "Attendance", "Attendance_Status", "Rank"
    ]
    print("\n" + "=" * 88)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 88)
    print(f"Students: {summary['total_students']} | Passed: {summary['passed']} | Failed: {summary['failed']}")
    print(f"Class average: {summary['class_average']:.2f}/100")
    print(f"Highest average: {summary['highest_average']:.2f} ({summary['top_student']})")
    print(f"Lowest average: {summary['lowest_average']:.2f} ({summary['lowest_student']})")
    print(f"Students with attendance below 75%: {summary['low_attendance_count']}")
    print("\nSTUDENT RESULTS (sorted by average, highest first)")
    print(processed[display_columns].to_string(index=False))
    print("\nSUBJECT-WISE AVERAGES")
    for subject, average in summary["subject_averages"].items():
        print(f"{subject.replace('_', ' '):25s}: {average:.2f}")
    best_subject = summary["subject_averages"].idxmax()
    lowest_subject = summary["subject_averages"].idxmin()
    print(f"Best-performing subject: {best_subject.replace('_', ' ')}")
    print(f"Lowest-performing subject: {lowest_subject.replace('_', ' ')}")
    print("\nSUBJECT TOPPERS")
    for subject, name in summary["subject_toppers"].items():
        print(f"{subject.replace('_', ' '):25s}: {name}")
    print("\nTOP 5 STUDENTS")
    print(processed[["Rank", "Student_ID", "Name", "Average_Marks", "Grade"]].head(5).to_string(index=False))
