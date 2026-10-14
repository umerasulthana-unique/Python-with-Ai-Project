"""Optional charts for the Student Performance Analytics System."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from functions import SUBJECTS, process_students, validate_dataset

def main():
    root = Path(__file__).resolve().parent
    output_dir = root / "outputs"
    output_dir.mkdir(exist_ok=True)
    data = validate_dataset(pd.read_csv(root / "students.csv"))
    processed = process_students(data)

    averages = data[SUBJECTS].mean().sort_values(ascending=False)
    averages.index = [name.replace("_", " ") for name in averages.index]
    averages.plot(kind="bar", title="Average Marks by Subject", xlabel="Subject", ylabel="Average Marks")
    plt.tight_layout()
    plt.savefig(output_dir / "subject_averages.png", dpi=160)
    plt.close()

    result_counts = processed["Result"].value_counts().reindex(["Pass", "Fail"], fill_value=0)
    result_counts.plot(kind="bar", title="Student Pass/Fail Summary", xlabel="Result", ylabel="Number of Students")
    plt.tight_layout()
    plt.savefig(output_dir / "pass_fail_summary.png", dpi=160)
    plt.close()

    attendance = processed.sort_values("Attendance")
    plt.figure()
    plt.bar(attendance["Student_ID"], attendance["Attendance"])
    plt.title("Student Attendance")
    plt.xlabel("Student ID")
    plt.ylabel("Attendance (%)")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(output_dir / "attendance.png", dpi=160)
    plt.close()
    print(f"Charts saved in {output_dir}")

if __name__ == "__main__":
    main()
