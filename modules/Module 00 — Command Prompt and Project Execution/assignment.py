# assignment.py
# Command Prompt Practice — Python Simulation Tasks
# Beginner Friendly

import os
from pathlib import Path
import shutil

print("=== Assignment Started ===\n")

# -------------------------
# Task 1 — Create folders using Python
# -------------------------
print("Task 1: Creating folders")

base = Path("assignment_project")
(base / "data").mkdir(parents=True, exist_ok=True)
(base / "src").mkdir(parents=True, exist_ok=True)

print("Created folders: data, src\n")


# -------------------------
# Task 2 — Create and write a file
# -------------------------
print("Task 2: Creating a file")

file_path = base / "data" / "sample.txt"
file_path.write_text("This is a sample NLP file.", encoding="utf-8")

print("File created:", file_path, "\n")


# -------------------------
# Task 3 — Copy file
# -------------------------
print("Task 3: Copy file")

backup_dir = base / "backup"
backup_dir.mkdir(exist_ok=True)

shutil.copy(file_path, backup_dir / "sample_copy.txt")

print("File copied to backup\n")


# -------------------------
# Task 4 — Rename file
# -------------------------
print("Task 4: Rename file")

old_file = backup_dir / "sample_copy.txt"
new_file = backup_dir / "renamed_sample.txt"

old_file.rename(new_file)

print("File renamed to:", new_file.name, "\n")


# -------------------------
# Task 5 — List installed packages
# -------------------------
print("Task 5: Check installed packages")

print("Run this in CMD:")
print("python -m pip list\n")


print("=== Assignment Complete ===")
