"""Main entry point for Student Performance Analytics System."""

from pathlib import Path
import pandas as pd

from functions import (
    SUBJECTS,
    create_summary,
    find_student,
    print_report,
    process_students,
    validate_dataset,
)


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    dataset_path = project_dir / "students.csv"
    output_dir = project_dir / "outputs"
    output_dir.mkdir(exist_ok=True)

    try:
        raw_data = pd.read_csv(dataset_path)
        print("DATASET PREVIEW")
        print(raw_data.head(10).to_string(index=False))
        print(f"\nDataset shape: {raw_data.shape[0]} rows x {raw_data.shape[1]} columns")
        print("\nDATASET INFORMATION")
        print(raw_data.info())

        data = validate_dataset(raw_data)
        processed = process_students(data)
        summary = create_summary(processed)
        print_report(processed, summary)

        # Save detailed student calculations for future reference.
        processed.to_csv(output_dir / "student_results.csv", index=False)
        summary_rows = [
            ("Total students", summary["total_students"]),
            ("Passed", summary["passed"]),
            ("Failed", summary["failed"]),
            ("Class average", summary["class_average"]),
            ("Highest average", summary["highest_average"]),
            ("Top student", summary["top_student"]),
            ("Lowest average", summary["lowest_average"]),
            ("Lowest-performing student", summary["lowest_student"]),
            ("Low attendance count", summary["low_attendance_count"]),
        ]
        pd.DataFrame(summary_rows, columns=["Metric", "Value"]).to_csv(
            output_dir / "class_summary.csv", index=False
        )
        summary["subject_averages"].rename_axis("Subject").reset_index(
            name="Average_Marks"
        ).to_csv(output_dir / "subject_analysis.csv", index=False)

        print(f"\nSaved results to: {output_dir}")
        search_id = input("\nEnter a Student ID to search (or press Enter to finish): ").strip()
        if search_id:
            found = find_student(processed, search_id)
            if found.empty:
                print(f"No student found with ID {search_id}.")
            else:
                print("\nSTUDENT SEARCH RESULT")
                print(found.to_string(index=False))

    except FileNotFoundError:
        print(f"Dataset not found: {dataset_path}")
        print("Make sure students.csv is in the same folder as main.py.")
    except (ValueError, KeyError) as error:
        print(f"Unable to process dataset: {error}")


if __name__ == "__main__":
    main()
