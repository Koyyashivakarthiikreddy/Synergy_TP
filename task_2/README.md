# Task 2 - Python Recap Assignment

## Description
This folder contains my solution for Task 2 of the Synergy_TP project.
The program reads student submission data from a CSV file and generates a summary report in JSON format.It uses Python functions, lists, dictionaries, file I/O, exception handling and type hints.

## Folder Structure
task_2/
    README.md
    requirements.txt
    data/
        submissions.csv
    output/
        summary.json
    src/
        analyzer.py
        main.py

## Setup Instructions

### 1.Clone the repository
git clone https://github.com/Koyyashivakarthiikreddy/Synergy_TP.git
cd Synergy_TP

### 2.No packages to install
All modules used are built-in Python modules. No pip install needed.

## How to Run
From the Synergy_TP root folder run:

python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json

## What the program does
- Reads student data from task_2/data/submissions.csv
- Calculates total students,submitted count and missing count
- Finds average score,highest scorer and lowest scorer
- Groups scores domain wise
- Saves the final summary to task_2/output/summary.json

## Error Handling
- If the input CSV file is not found, the program prints an error and stops
- If the CSV file is empty, the program prints a message and stops
- If the output folder does not exist, the program creates it automatically
- If score values are invalid, they are converted safely using float()