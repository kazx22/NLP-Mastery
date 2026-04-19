# Command Prompt Mastery for NLP Projects (Windows CMD)

This note follows the same beginner-friendly style as the lesson chat.

---

# Section 1 — What is Command Prompt (CMD)

## What is CMD?

Command Prompt (CMD) is a tool where you type commands to control your computer.

Instead of clicking folders, you type instructions.

Example:

```cmd
echo Hello
```

Output:

```text
Hello
```

---

## Why CMD is important for NLP

You will use CMD to:

- run Python scripts
- install packages
- activate environments
- execute NLP pipelines

Example:

```cmd
python -m src.benchmark
```

---

## Opening CMD

### Method 1

- Start Menu
- Type `cmd`
- Open **Command Prompt**

### Method 2

- Press `Windows + R`
- Type `cmd`
- Press Enter

---

## Prompt meaning

Example:

```cmd
C:\Users\Kazi>
```

This shows your current folder.

---

# Section 2 — Navigation

## 2.1 View files (`dir`)

Command:

```cmd
dir
```

Shows all files and folders in current location.

Think of it like:

- you are inside a room
- `dir` means “look around”

---

## 2.2 Move into folder (`cd`)

Command:

```cmd
cd Documents
```

Moves into the `Documents` folder.

If the prompt changes from:

```cmd
C:\Users\Kazi>
```

to

```cmd
C:\Users\Kazi\Documents>
```

that means you moved into the folder.

---

## Go back

```cmd
cd ..
```

Moves one level up.

---

## 2.3 Absolute vs Relative Path

### Absolute path

```cmd
cd C:\Users\Kazi\Documents
```

This works from anywhere.

### Relative path

```cmd
cd Documents
```

This only works if `Documents` exists in your current location.

### Important

Use backslash in Windows:

```cmd
cd data\raw
```

Not Linux-style slash.

---

# Section 3 — File & Folder Management

## 3.1 Create folder (`mkdir`)

```cmd
mkdir folder_name
```

Example:

```cmd
mkdir data
```

Create multiple folders:

```cmd
mkdir data src models
```

---

## 3.2 Delete file (`del`)

```cmd
del file.txt
```

This deletes a file.

Important:

- no recycle bin
- no undo

---

## Delete empty folder (`rmdir`)

```cmd
rmdir folder_name
```

---

## Delete folder with contents

```cmd
rmdir /s folder_name
```

This deletes the folder and everything inside it.

Be careful.

---

## 3.3 Copy file (`copy`)

```cmd
copy file.txt backup\
```

This creates a duplicate.

---

## Move file (`move`)

```cmd
move file.txt backup\
```

This removes it from the old place and puts it in the new place.

---

## Rename file

```cmd
move old.txt new.txt
```

# Rename Files and Folders (`ren`)

## What `ren` means

`ren` means:

> rename a file or folder

---

## Basic command# Command Prompt Mastery for NLP Projects (Windows CMD)

This note follows the same beginner-friendly style as the lesson chat.

---

# Section 1 — What is Command Prompt (CMD)

## What is CMD?

Command Prompt (CMD) is a tool where you type commands to control your computer.

Instead of clicking folders, you type instructions.

Example:

```cmd
echo Hello
```

Output:

```text
Hello
```

---

## Why CMD is important for NLP

You will use CMD to:

- run Python scripts
- install packages
- activate environments
- execute NLP pipelines

Example:

```cmd
python -m src.benchmark
```

---

## Opening CMD

### Method 1

- Start Menu
- Type `cmd`
- Open **Command Prompt**

### Method 2

- Press `Windows + R`
- Type `cmd`
- Press Enter

---

## Prompt meaning

Example:

```cmd
C:\Users\Kazi>
```

This shows your current folder.

---

# Section 2 — Navigation

## 2.1 View files (`dir`)

Command:

```cmd
dir
```

Shows all files and folders in current location.

Think of it like:

- you are inside a room
- `dir` means "look around"

---

## 2.2 Move into folder (`cd`)

Command:

```cmd
cd Documents
```

Moves into the `Documents` folder.

If the prompt changes from:

```cmd
C:\Users\Kazi>
```

to

```cmd
C:\Users\Kazi\Documents>
```

that means you moved into the folder.

---

## Go back

```cmd
cd ..
```

Moves one level up.

---

## 2.3 Absolute vs Relative Path

### Absolute path

```cmd
cd C:\Users\Kazi\Documents
```

This works from anywhere.

### Relative path

```cmd
cd Documents
```

This only works if `Documents` exists in your current location.

### Important

Use backslash in Windows:

```cmd
cd data\raw
```

Not Linux-style slash.

---

# Section 3 — File & Folder Management

## 3.1 Create folder (`mkdir`)

```cmd
mkdir folder_name
```

Example:

```cmd
mkdir data
```

Create multiple folders:

```cmd
mkdir data src models
```

---

## 3.2 Delete file (`del`)

```cmd
del file.txt
```

This deletes a file.

Important:

- no recycle bin
- no undo

---

## Delete empty folder (`rmdir`)

```cmd
rmdir folder_name
```

---

## Delete folder with contents

```cmd
rmdir /s folder_name
```

This deletes the folder and everything inside it.

Be careful.

---

## 3.3 Copy file (`copy`)

```cmd
copy file.txt backup\
```

This creates a duplicate.

---

## Move file (`move`)

```cmd
move file.txt backup\
```

This removes it from the old place and puts it in the new place.

---

## 3.4 Rename Files and Folders (`ren`)

### What `ren` means

`ren` means:

> rename a file or folder

---

### Basic command

```cmd
ren old_name new_name
```

---

### Rename a file

```cmd
ren report.txt final_report.txt
```

This renames `report.txt` to `final_report.txt`.

The file stays in the same folder.

---

### Rename a folder

```cmd
ren old_folder new_folder
```

Example:

```cmd
ren data raw_data
```

---

### Important rules

- you cannot move a file with `ren` — only rename it
- the new name must not already exist in the same folder
- do not include a path in the new name

Wrong:

```cmd
ren file.txt backup\file.txt
```

Right (just rename):

```cmd
ren file.txt file_v2.txt
```

---

### Alternative

You can also use `move` to rename a file:

```cmd
move old.txt new.txt
```

Both work. `ren` is cleaner when you only want to rename.

---

# Section 4 — Python in CMD

## Check Python

```cmd
python --version
```

This checks whether Python is installed and working.

---

## Run file

```cmd
python test.py
```

This runs a Python file.

Important:
you must be in the correct folder first.

Example:

```cmd
cd C:\University\Projects\my-nlp-project
python test.py
```

---

# Section 5 — Virtual Environment (`venv`)

## Why `venv`?

Different projects need different versions of packages.

Without `venv`, packages can conflict.

That is why we use one environment per project.

---

## Create venv

```cmd
python -m venv .venv
```

This creates a virtual environment folder called `.venv`.

---

## Activate venv

```cmd
.venv\Scripts\activate
```

After activation, your prompt should look like:

```cmd
(.venv) C:\University\Projects\my-nlp-project>
```

---

## Deactivate

```cmd
deactivate
```

This turns the environment off.

---

## Check Python path

```cmd
where python
```

It should point to:

```text
.venv\Scripts\python.exe
```

That tells you the virtual environment is active.

---

# Section 6 — pip (Package Management)

## Install package

```cmd
pip install pandas
```

Safer version:

```cmd
python -m pip install pandas
```

This makes sure pip belongs to the Python you are using.

---

## List packages

```cmd
pip list
```

Shows installed packages.

---

## Uninstall package

```cmd
pip uninstall pandas
```

Removes a package.

---

## Save dependencies

```cmd
pip freeze > requirements.txt
```

Writes installed packages to a file.

This is important for GitHub and reproducibility.

---

## Install from file

```cmd
pip install -r requirements.txt
```

This installs all packages listed in the file.

---

# Section 7 — Running Projects Properly

## Example project structure

```text
src/
  main.py
  benchmark.py
```

---

## Correct execution

```cmd
python -m src.main
```

---

## Why use `-m`?

Because it treats the code as part of a project, not just a random file.

That helps:

- imports work properly
- structure stays clean
- execution is more professional

---

## Rule to remember

### Single file

```cmd
python file.py
```

### Project file inside `src/`

```cmd
python -m src.file
```

---

## Passing arguments

Example:

```cmd
python -m src.benchmark --model biobert
```

Meaning:

- `--model` = argument name
- `biobert` = value

This lets you control the script without editing the code.

---

# Section 8 — Debugging

## 8.1 Command not recognized

Example:

```text
'python' is not recognized
```

This means CMD cannot find Python.

### Fix

- install Python properly
- make sure Python is in PATH
- activate `.venv`

Check with:

```cmd
where python
```

---

## 8.2 Path errors

Example:

```text
The system cannot find the path specified.
```

This means the folder or file does not exist from your current location.

### Fix

- check current prompt
- run `dir`
- fix typo
- use correct path

If folder name contains spaces:

```cmd
cd "My Folder"
```

---

## 8.3 Environment issues

Example:
you installed a package but Python says:

```text
ModuleNotFoundError
```

This often means:

- `pip` installed into one Python
- but you ran another Python

### Fix

Activate `.venv`, then check:

```cmd
where python
where pip
```

Safer install command:

```cmd
python -m pip install package
```

---

## 8.4 Final Workflow

A clean routine to follow every time:

```cmd
cd C:\University\Projects\my-nlp-project
.venv\Scripts\activate
python -m src.main
deactivate
```

For your NLP workflow, this can become:

```cmd
cd C:\University\Projects\spatial-human-anatomy
.venv\Scripts\activate
python -m src.benchmark
deactivate
```

---

# Golden Rules

- always activate `.venv`
- always run from project root
- use `python -m` for project files
- use `python -m pip` if unsure
- use backslashes in Windows CMD paths

---

# End

````cmd
ren old_name new_name

---

# Section 4 — Python in CMD

## Check Python

```cmd
python --version
````

This checks whether Python is installed and working.

---

## Run file

```cmd
python test.py
```

This runs a Python file.

Important:
you must be in the correct folder first.

Example:

```cmd
cd C:\University\Projects\my-nlp-project
python test.py
```

---

# Section 5 — Virtual Environment (`venv`)

## Why `venv`?

Different projects need different versions of packages.

Without `venv`, packages can conflict.

That is why we use one environment per project.

---

## Create venv

```cmd
python -m venv .venv
```

This creates a virtual environment folder called `.venv`.

---

## Activate venv

```cmd
.venv\Scripts\activate
```

After activation, your prompt should look like:

```cmd
(.venv) C:\University\Projects\my-nlp-project>
```

---

## Deactivate

```cmd
deactivate
```

This turns the environment off.

---

## Check Python path

```cmd
where python
```

It should point to:

```text
.venv\Scripts\python.exe
```

That tells you the virtual environment is active.

---

# Section 6 — pip (Package Management)

## Install package

```cmd
pip install pandas
```

Safer version:

```cmd
python -m pip install pandas
```

This makes sure pip belongs to the Python you are using.

---

## List packages

```cmd
pip list
```

Shows installed packages.

---

## Uninstall package

```cmd
pip uninstall pandas
```

Removes a package.

---

## Save dependencies

```cmd
pip freeze > requirements.txt
```

Writes installed packages to a file.

This is important for GitHub and reproducibility.

---

## Install from file

```cmd
pip install -r requirements.txt
```

This installs all packages listed in the file.

---

# Section 7 — Running Projects Properly

## Example project structure

```text
src/
  main.py
  benchmark.py
```

---

## Correct execution

```cmd
python -m src.main
```

---

## Why use `-m`?

Because it treats the code as part of a project, not just a random file.

That helps:

- imports work properly
- structure stays clean
- execution is more professional

---

## Rule to remember

### Single file

```cmd
python file.py
```

### Project file inside `src/`

```cmd
python -m src.file
```

---

## Passing arguments

Example:

```cmd
python -m src.benchmark --model biobert
```

Meaning:

- `--model` = argument name
- `biobert` = value

This lets you control the script without editing the code.

---

# Section 8 — Debugging

## 8.1 Command not recognized

Example:

```text
'python' is not recognized
```

This means CMD cannot find Python.

### Fix

- install Python properly
- make sure Python is in PATH
- activate `.venv`

Check with:

```cmd
where python
```

---

## 8.2 Path errors

Example:

```text
The system cannot find the path specified.
```

This means the folder or file does not exist from your current location.

### Fix

- check current prompt
- run `dir`
- fix typo
- use correct path

If folder name contains spaces:

```cmd
cd "My Folder"
```

---

## 8.3 Environment issues

Example:
you installed a package but Python says:

```text
ModuleNotFoundError
```

This often means:

- `pip` installed into one Python
- but you ran another Python

### Fix

Activate `.venv`, then check:

```cmd
where python
where pip
```

Safer install command:

```cmd
python -m pip install package
```

---

# Section 8.4 — Final Workflow

A clean routine to follow every time:

```cmd
cd C:\University\Projects\my-nlp-project
.venv\Scripts\activate
python -m src.main
deactivate
```

For your NLP workflow, this can become:

```cmd
cd C:\University\Projects\spatial-human-anatomy
.venv\Scripts\activate
python -m src.benchmark
deactivate
```

---

# Golden Rules

- always activate `.venv`
- always run from project root
- use `python -m` for project files
- use `python -m pip` if unsure
- use backslashes in Windows CMD paths

---

# End
