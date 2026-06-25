import sys
# importing all the functions from analyzer.py
from analyzer import read_submissions, get_submitted_students, calculate_average_score, get_domain_wise_average, get_missing_submissions, write_summary

def main():
    # check if the user provided both input and output file paths
    if len(sys.argv) != 3:
        print("Please provide input and output file paths.")
        print("Example: python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json")
        sys.exit(1)
    
    # get the input and output file paths from terminal
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    # reads the student data from csv file
    students = read_submissions(input_file)
    if not students:
        print("No student data found.")
        sys.exit(1) 

        
    # get submitted students and missing students
    submitted = get_submitted_students(students)
    missing = get_missing_submissions(students) 

    # calculate average score and domain wise average
    avg_score = calculate_average_score(students)
    domain_avg = get_domain_wise_average(students) 

    # finds highest and lowest scorer among submitted students
    highest = max(submitted, key=lambda s: float(s['score']))
    lowest = min(submitted, key=lambda s: float(s['score']))

    # find students who scored below 5
    below_five = [s['name'] for s in students if float(s['score']) < 5]

    # the final summary
    summary = {
        "total_students": len(students),
        "submitted_count": len(submitted),
        "missing_count": len(missing),
        "average_score": round(avg_score, 2),
        "highest_scorer": {"name": highest['name'], "score": float(highest['score'])},
        "lowest_scorer": {"name": lowest['name'], "score": float(lowest['score'])},
        "domain_wise_average": domain_avg,
        "missing_submissions": missing,
        "students_below_5": below_five
    }

    # prints the summary in the terminal
    print(f"Total Students: {len(students)}")
    print(f"Submitted: {len(submitted)}")
    print(f"Missing: {len(missing)}")
    print(f"Average Score: {round(avg_score, 2)}")
    print(f"Highest Scorer: {highest['name']} ({highest['score']})")
    print(f"Missing Submissions: {missing}")
    write_summary(summary, output_file)
    print(f"Summary written to {output_file}")

if __name__ == "__main__":
    main()