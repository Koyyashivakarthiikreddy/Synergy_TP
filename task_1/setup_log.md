# Setup Log

This file documents the exact commands I used to set up Task 1 from scratch.

---
## 1.Initializing Git

I did not run `git init` separately because I had already cloned the repository from GitHub. Cloning automatically sets up Git and connects the local folder to the remote repository.

```bash
git clone https://github.com/KoyyashivakarthiikReddy/Synergy_TP.git
cd Synergy_TP
```

---

## 2.Creating the Folder Structure

I created the required folders inside the repository using the following commands:

```bash
mkdir -p task_1/src
mkdir -p task_1/data
```

The `-p` flag creates the parent folder and the subfolder together in a single command. Without `-p`, I would have had to create `task_1` first and then `src` and `data` separately.

I then navigated into `task_1` and created the required files:

```bash
cd task_1
touch README.md
touch requirements.txt
touch setup_log.md
touch linux_commands.md
touch src/hello.py
touch data/sample.txt
```
---

## 3. Creating and Activating the Virtual Environment

I created a virtual environment named `venv` inside the `task_1` folder:

```bash
python -m venv venv
```

I then activated it using the following command on Windows (Git Bash):

```bash
source venv/Scripts/activate
```

Once activated, `(venv)` appeared at the beginning of my terminal prompt, confirming the virtual environment was active.

---

## 4.Installing Packages

I installed the `requests` package using pip:

```bash
pip install requests
```

---

## 5.Generating requirements.txt

After installing the package, I generated the `requirements.txt` file using:

```bash
pip freeze > requirements.txt
```

The `pip freeze` command lists all installed packages with their exact version numbers. The `>` symbol writes that output directly into `requirements.txt`.

I verified the contents of `requirements.txt` using:

```bash
cat requirements.txt
```

The output was:

```
certifi==2026.6.17
charset-normalizer==3.4.7
idna==3.18
requests==2.34.2
urllib3==2.7.0
```

---

## 6.Writing and Running the Python Script

I navigated into the `src` folder and opened VS Code to write the `hello.py` script:

```bash
cd src
code .
```

After writing the script, I navigated back to the `Synergy_TP` root and ran it:

```bash
cd ..
cd ..
python task_1/src/hello.py
```

The output was:

```
hello
synergy
```

This confirmed that the script was working correctly.

---

## 7.Creating the .gitignore File

I created the `.gitignore` file at the root of the repository:

```bash
touch .gitignore
code .
```

I added the following entries to exclude the virtual environment, Python cache files, OS files, and IDE files from being pushed to GitHub:

```
# Virtual environment
venv/
env/
.env/
.venv/

# Python cache
__pycache__/
*.py[cod]
*.pyo
*.pyc

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
```

---

## 8.Verifying Git Status and .gitignore

I ran `git status` to check which files were being tracked:

```bash
git status
```

The output showed `.gitignore` and `task_1/` as untracked files, which was expected.

I then verified that the `venv` folder was being correctly ignored by Git:

```bash
git check-ignore -v task_1/venv/
```

The output confirmed that `venv/` was matched by the `.gitignore` rule, meaning it would not be pushed to GitHub.

---

## 9.Committing Changes

After completing all the files, I staged and committed the changes:

```bash
git add .
git commit -m "Add task_1 with venv setup, hello.py, and documentation"
```

The `git add .` command stages all new and modified files. The `git commit` command saves a snapshot of the project with a message describing what was done.

---

## 10.Pushing to GitHub

Finally, I pushed the committed changes to the remote GitHub repository:

```bash
git push origin main
```

This uploaded all my local changes to the `main` branch on GitHub.
