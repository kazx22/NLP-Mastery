# Mini Projects — Command Prompt + Python (Beginner → Practical)

---

## 🔹 Mini Project 1 — Create NLP Project Structure (CMD only)

**🎯 Goal:** Manually create a clean NLP project using CMD

<details>
<summary>🧾 Show Steps</summary>

```cmd
cd C:\University\Projects
mkdir nlp_project
cd nlp_project
mkdir data src models notebooks
mkdir data\raw data\processed
dir
```

✅ **Result**

```
nlp_project/
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── models/
└── notebooks/
```

💡 **What you learn:** `mkdir` · nested folders · project structure

</details>

---

## 🔹 Mini Project 2 — Create & Run a Python Script

**🎯 Goal:** Create a script and run it via CMD

<details>
<summary>🧾 Show Steps</summary>

```cmd
cd src
echo print("NLP Project Running") > main.py
cd ..
python src\main.py
```

✅ **Result**

```
NLP Project Running
```

💡 **What you learn:** file creation · running Python · correct path usage

</details>

---

## 🔹 Mini Project 3 — Use `-m` Properly

**🎯 Goal:** Run your script the correct project way

<details>
<summary>🧾 Show Steps</summary>

```cmd
python -m src.main
```

✅ **Result**

```
NLP Project Running
```

💡 **What you learn:** proper execution · project-style running

</details>

---

## 🔹 Mini Project 4 — Virtual Environment Setup

**🎯 Goal:** Set up isolated environment

<details>
<summary>🧾 Show Steps</summary>

```cmd
python -m venv .venv
.venv\Scripts\activate
python --version
deactivate
```

✅ **Result**

```
(.venv) C:\University\Projects\nlp_project>
```

💡 **What you learn:** environment isolation · correct Python usage

</details>

---

## 🔹 Mini Project 5 — Install NLP Package

**🎯 Goal:** Install and verify a package

<details>
<summary>🧾 Show Steps</summary>

```cmd
.venv\Scripts\activate
python -m pip install pandas
pip list
```

✅ **Result**

```
pandas listed in pip list output
```

💡 **What you learn:** pip usage · environment-specific installs

</details>

---

## 🔹 Mini Project 6 — File Handling Workflow

**🎯 Goal:** Simulate dataset workflow

<details>
<summary>🧾 Show Steps</summary>

```cmd
cd data\raw
echo sample text > sample.txt
cd ..
mkdir backup
copy raw\sample.txt backup\
move raw\sample.txt processed\
dir processed
```

✅ **Result**

```
sample.txt now in data\processed\
```

💡 **What you learn:** dataset movement · copy vs move · project organisation

</details>

---

## 🔹 Mini Project 7 — Rename Outputs

**🎯 Goal:** Rename experiment outputs

<details>
<summary>🧾 Show Steps</summary>

```cmd
cd data\processed
ren sample.txt cleaned_sample.txt
dir
```

✅ **Result**

```
cleaned_sample.txt shown in dir
```

💡 **What you learn:** `ren` usage · naming conventions

</details>

---

## 🔹 Mini Project 8 — Requirements Workflow

**🎯 Goal:** Save environment

<details>
<summary>🧾 Show Steps</summary>

```cmd
pip freeze > requirements.txt
type requirements.txt
```

✅ **Result**

```
List of installed packages printed
```

💡 **What you learn:** reproducibility · pip freeze · requirements.txt

</details>

---

## 🔹 Mini Project 9 — Run with Arguments

**🎯 Goal:** Pass arguments to script

<details>
<summary>🧾 Modify src\main.py</summary>

```python
import sys
print("Model:", sys.argv[1])
```

</details>

<details>
<summary>🧾 Show Run Command</summary>

```cmd
python -m src.main biobert
```

✅ **Result**

```
Model: biobert
```

💡 **What you learn:** sys.argv · arguments · flexible scripts

</details>

---

## 🔹 Mini Project 10 — Full Workflow

**🎯 Goal:** Run like a real NLP project

<details>
<summary>🧾 Show Steps</summary>

```cmd
cd C:\University\Projects\nlp_project
.venv\Scripts\activate
python -m src.main
deactivate
```

✅ **Result**

```
NLP Project Running
```

💡 **What you learn:** full pipeline · professional workflow

</details>
