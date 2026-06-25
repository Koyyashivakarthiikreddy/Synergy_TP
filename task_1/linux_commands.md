# Linux Commands
This file documents the Linux commands used during the setup and exploration of this project.
---

## 1.pwd

**Command used:**
```bash
pwd
```
**What it does:**
Prints the current working directory. It shows the full path of the folder you are currently in.

**Output observed:**
```
/c/Users/koyya/Desktop/Synergy_TP
```
---

## 2.ls

**Command used:**
```bash
ls
```
**What it does:**
Lists all the files and folders in the current directory.

**Output observed:**
```
README.md  task_1/
```
---

## 3.ls -la

**Command used:**
```bash
ls -la
```
**What it does:**
Lists all files and folders in the current directory in detailed format. The `-l` flag shows permissions, owner, size, and date. The `-a` flag also shows hidden files like `.git` and `.gitignore`.

**Output observed:**
```
total 18
drwxr-xr-x 1 koyya 197609   0 Jun 24 18:51 ./
drwxr-xr-x 1 koyya 197609   0 Jun 24 17:50 ../
drwxr-xr-x 1 koyya 197609   0 Jun 24 20:00 .git/
-rw-r--r-- 1 koyya 197609 175 Jun 24 19:59 .gitignore
-rw-r--r-- 1 koyya 197609  12 Jun 24 17:50 README.md
drwxr-xr-x 1 koyya 197609   0 Jun 24 18:31 task_1/
```
---

## 4.cd

**Command used:**
```bash
cd task_1
```
**What it does:**
Changes the current directory to the specified folder. In this case, it moved into the `task_1` folder.

**Output observed:**
No output is shown. The terminal prompt changes to reflect the new directory.
---

## 5.mkdir

**Command used:**
```bash
mkdir -p task_1/src
mkdir -p task_1/data
```

**What it does:**
Creates a new directory. The `-p` flag creates the parent directory and the subdirectory together in a single command.

**Output observed:**
No output is shown. The folders are created silently.

---

## 6.touch

**Command used:**
```bash
touch README.md
touch requirements.txt
touch setup_log.md
touch linux_commands.md
touch src/hello.py
touch data/sample.txt
```

**What it does:**
Creates a new empty file. If the file already exists, it updates the timestamp of the file.

**Output observed:**
No output is shown. The files are created silently.

---

## 7. cat

**Command used:**
```bash
cat requirements.txt
```
**What it does:**
Displays the full contents of a file directly in the terminal.
**Output observed:**
```
certifi==2026.6.17
charset-normalizer==3.4.7
idna==3.18
requests==2.34.2
urllib3==2.7.0
```
---

## 8. echo

**Command used:**
```bash
echo "hello synergy"
```
**What it does:**
Prints the given text to the terminal. It is commonly used to display messages or to write text into files.

**Output observed:**
```
hello synergy
```
---

## 9. cp

**Command used:**
```bash
cp task_1/data/sample.txt task_1/data/sample_copy.txt
```

**What it does:**
Copies a file from one location to another. Here it created a copy of `sample.txt` named `sample_copy.txt` in the same folder.

**Output observed:**
No output is shown. The file is copied silently.

---

## 10.mv

**Command used:**
```bash
mv task_1/data/sample_copy.txt task_1/data/sample_renamed.txt
```

**What it does:**
Moves or renames a file. Here it renamed `sample_copy.txt` to `sample_renamed.txt`.

**Output observed:**
No output is shown. The file is renamed silently.

---

## 11.rm

**Command used:**
```bash
rm task_1/data/sample_renamed.txt
```

**What it does:**
Deletes a file permanently. The file cannot be recovered after deletion.

**Output observed:**
No output is shown. The file is deleted silently.

---

## 12. grep

**Command used:**
```bash
grep "venv" .gitignore
```
**What it does:**
Searches for a specific word or pattern inside a file and prints the matching lines. Here it searched for the word `venv` inside the `.gitignore` file.

**Output observed:**
```
venv/
env/
.env/
.venv/
```
---

## 13. find

**Command used:**
```bash
find . -name "*.py" -not -path "./task_1/venv/*"
```

**What it does:**
Searches for files matching a pattern inside the current directory and all its subfolders. The `-not -path` part excludes the virtual environment folder from the results.
**Output observed:**
```
./task_1/src/hello.py
```
---

## 14. head

**Command used:**
```bash
head task_1/README.md
```

**What it does:**
Displays the first 10 lines of a file. It is useful for quickly previewing the beginning of a file.

**Output observed:**
```
# Task 1: GitHub, Virtual Environment, and Linux Basics

## Description

This folder contains the work for Task 1 of the Synergy Task Phase. The goal of this task was to set up a clean Python project, learn how to use a virtual environment, manage dependencies, and get comfortable with basic Linux command-line usage. This was my first time working with Git and GitHub, so this task helped me understand how to clone a repository, structure a project, and push changes to GitHub.
```

---

## 15.tail

**Command used:**
```bash
tail task_1/README.md
```

**What it does:**
Displays the last 10 lines of a file. It is useful for quickly previewing the end of a file.

**Output observed:**
following command:

```bash
cd ..
python task_1/src/hello.py
```
Expected output:
```
hello
synergy
```

---

## 16.wc

**Command used:**
```bash
wc task_1/README.md
```

**What it does:**
Counts the number of lines, words, and characters in a file. The output shows lines first, then words, then characters.

**Output observed:**
```
59  215  1454  task_1/README.md
```
---

## 17.chmod

**Command used:**
```bash
chmod 755 task_1/src/hello.py
```
**What it does:**
Changes the permissions of a file. `755` means the owner can read, write, and execute the file, while others can only read and execute it.

**Output observed:**
No output is shown. The permissions are changed silently.
