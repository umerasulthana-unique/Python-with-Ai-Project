# Student Performance Analytics System

## 1. Project objective
This Python data-analysis project reads student records from a CSV file and uses Pandas, NumPy, functions, loops, and conditions to analyse academic performance. It calculates totals, averages, grades, pass/fail status, subject averages, rankings, top performers, and attendance indicators.

## 2. Technologies used
- Python 3.10 or newer
- Pandas
- NumPy
- Matplotlib (used by the optional chart-generation script)

No machine-learning model is used; the assignment does not require advanced machine learning.

## 3. Dataset description
`students.csv` contains 25 sample student records with these fields:
- `Student_ID`
- `Name`
- `Department`
- `Python`
- `Mathematics`
- `Data_Analytics`
- `Computer_Networks`
- `Database_Management`
- `Attendance`

Marks and attendance are represented as percentages from 0 to 100. The names and records are illustrative sample data, not official student records.

## 4. Grading and pass/fail rules
The assignment asks students to define a clear grading rule; it does not prescribe exact thresholds. This project uses:
- A+: average >= 90
- A: average >= 80 and < 90
- B: average >= 70 and < 80
- C: average >= 60 and < 70
- D: average >= 50 and < 60
- F: average < 50

Pass rule: a student must score at least 35 in every subject and have an overall average of at least 40. Otherwise the result is Fail.

Attendance indicator: attendance below 75% is labelled `Low Attendance`. This is an informational indicator and does not affect the pass/fail result.

## 5. Features
- Reads and validates the CSV dataset using Pandas.
- Uses NumPy for row totals, averages, maximum/minimum and attendance labels.
- Uses reusable functions for validation, grading, processing, summary creation, searching, and reporting.
- Uses loops and conditions.
- Calculates each student's total and average.
- Assigns grades and pass/fail status.
- Finds highest/lowest performance and class average.
- Produces subject-wise averages and subject toppers.
- Ranks students and lists the top five.
- Compares department averages (when more than one department is present).
- Supports student search by ID.
- Exports processed results and summary CSV files.

## 6. Project files
- `main.py`: program entry point.
- `functions.py`: reusable calculation and reporting functions.
- `students.csv`: sample dataset (25 records).
- `generate_charts.py`: optional charts for subject averages and pass/fail counts.
- `requirements.txt`: Python dependencies.
- `Project_Documentation.md`: full project report.
- `outputs/`: generated CSV reports and charts after running the scripts.

## 7. Installation and execution
1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run the analysis:
   ```bash
   python main.py
   ```
5. Optionally generate charts:
   ```bash
   python generate_charts.py
   ```

On some systems, use `python3` instead of `python`.

## 8. Expected outputs
Running `main.py` displays a dataset preview, dataset dimensions, class summary, student results, subject-wise averages, subject toppers, and the top five students. It saves:
- `outputs/student_results.csv`
- `outputs/class_summary.csv`
- `outputs/subject_analysis.csv`

The optional chart script saves PNG charts to `outputs/`.

## 9. Assessment alignment
This project demonstrates variables, data types, loops, functions, conditions, NumPy, Pandas, data loading, data validation, and analysis as requested by the assignment. Advanced machine learning is not included.

## 10. GitHub submission checklist
1. Create a repository named `student-performance-analytics`.
2. Upload the project files and dataset.
3. Include this `README.md` and `Project_Documentation.md`.
4. Run the program and verify generated files.
5. Copy the repository URL.
6. Submit the URL through the Google Form provided by EWB Courses.
7. Check that the repository is accessible as instructed by your trainer.

The assignment PDF does not provide the actual Google Form URL, so obtain it from EWB Courses or your trainer.
