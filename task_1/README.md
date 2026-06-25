# Task 1: GitHub, Virtual Environment, and Linux Basics

## Description

This folder contains the work for Task 1 of the Synergy Task Phase. The goal of this task was to set up a clean Python project, learn how to use a virtual environment, manage dependencies, and get comfortable with basic Linux command-line usage.This was my first time working with Git and GitHub, so this task helped me understand how to clone a repository, structure a project, and push changes to GitHub.

---

## Setup Instructions

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Koyyashivakarthiikreddy/Synergy_TP.git
cd Synergy_TP
```

### 2. Create a Virtual Environment

Navigate into the task_1 folder and create a virtual environment named venv:

```bash
cd task_1
python -m venv venv
```

### 3. Activate the Virtual Environment

**On Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

Once activated, you will see `(venv)` appear at the beginning of your terminal prompt.

### 4. Install Dependencies

Install all required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Running the Python Script

Go back to the root of the repository and run the script using the following command:

```bash
cd ..
python task_1/src/hello.py
```
Expected output:
```
hello
synergy
```
