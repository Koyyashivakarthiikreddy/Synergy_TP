import csv
# this function reads the csv file and returns the list of students
def read_submissions(file_path: str) -> list:
    students = []
    try:
        # this opens the csv file and read each row as a dictionary
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
    #if the file is not found, prints an error message
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    return students
# this function filters and returns only students who submitted
def get_submitted_students(students: list) -> list:
    return [s for s in students if s['submitted'] == 'yes']


# this function calculates the average of scores of all the students
def calculate_average_score(students: list) -> float:
    if not students:
        return 0.0
    scores = [float(s['score']) for s in students]
    return sum(scores) / len(scores)


# this function groups the students by domain and calc the average score of each domain
def get_domain_wise_average(students: list) -> dict:
    domains = {}
    for s in students:
        domain = s['domain']
        score = float(s['score'])
        if domain not in domains:
            domains[domain] = []
        domains[domain].append(score)
    return {domain: sum(scores) / len(scores) for domain, scores in domains.items()} 


#  this function helps to return all the names of students who didnt submit
def get_missing_submissions(students: list) -> list:
    return [s['name'] for s in students if s['submitted'] == 'no'] 


# this function writes the final summary dictionary to ajson file
def write_summary(summary: dict, output_path: str) -> None:
    import os
    import json
    # creates an output folder if it doesnt exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(summary, f, indent=4)