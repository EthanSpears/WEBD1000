# Week 1 Lab – IDE Setup, Git Repo, Pseudocode & Flowcharts

**Course:** PROG1700 – Logic & Programming
**Time:** \~3 hours

---

## 🎯 Goals

By the end of this lab, you will:

* Set up your **IDE (VS Code)** for Python programming.
* Create and use a **GitHub repository** to save your code.
* Practice writing **pseudocode** for simple problems.
* Draw **flowcharts** using a free online tool.

---

## Part 1 – Set Up Your IDE (VS Code)

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com) → download **VS Code** for your OS.
2. Open VS Code → go to **Extensions (Ctrl+Shift+X)** → install:

   * **Python** (by Microsoft).
   * **Pylance** (for IntelliSense).
3. Install **Python 3.x** from [https://www.python.org/downloads/](https://www.python.org/downloads/).
4. In VS Code:

   * Open the **Command Palette (Ctrl+Shift+P)** → search **Python: Select Interpreter** → pick Python 3.x.
5. Create a new file `hello.py`:

   ```python
   print("Hello, PROG1700!")
   ```
6. Run the program:

   * Right-click in the editor → **Run Python File in Terminal**.
   * You should see:

     ```
     Hello, PROG1700!
     ```

---

## Part 2 – Create Your Git Repository

1. Create a GitHub account at [https://github.com](https://github.com) (if you don’t already have one).
2. On GitHub → click **New Repository** → name it:

   ```
   prog1700-labs
   ```

   * Choose **Public** or **Private**.
   * Add a README (optional).
3. Open **VS Code terminal** (\`Ctrl+\`\`). Run:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
4. In VS Code terminal, clone your repo:

   ```bash
   git clone https://github.com/your-username/prog1700-labs.git
   ```
5. Move `hello.py` into the new repo folder.
6. Commit & push:

   ```bash
   git add hello.py
   git commit -m "Lab 1: hello world"
   git push origin main
   ```

---

## Part 3 – Write Pseudocode

Use **plain text** to describe steps for solving problems.

**Example Problem 1: Temperature Converter**

```
START
PROMPT user for Celsius temperature
CALCULATE Fahrenheit = (Celsius × 9/5) + 32
DISPLAY Fahrenheit
END
```

**Problem 2: Simple Grading Rule**

```
START
PROMPT user for grade
IF grade >= 50 THEN
   DISPLAY "Pass"
ELSE
   DISPLAY "Fail"
ENDIF
END
```

Write both pseudocode snippets in a file `week1_pseudocode.txt`.

---

## Part 4 – Draw Flowcharts (Free Tool)

1. Go to [https://app.diagrams.net/](https://app.diagrams.net/) (free online tool).
2. Choose **“Decide later”** when asked about storage.
3. Use shapes:

   * **Oval** → Start/End
   * **Parallelogram** → Input/Output
   * **Rectangle** → Process/Calculation
   * **Diamond** → Decision (Yes/No)
4. Create flowcharts for the **Temperature Converter** and **Grading Rule** problems.
5. Export each as **PNG image** (`File → Export As → PNG`). Save as `temp_converter.png` and `grading_rule.png`.

---

## Part 5 – Reflection

Write a short paragraph (\~100–150 words):

* What was easy or difficult about setting up your tools?
* How do pseudocode and flowcharts help before coding?
* One new thing you learned today.

Save this in a file called `week1_reflection.txt`.

---

## ✅ Deliverables (Submit to LMS or Repo)

* `hello.py` (first program).
* `week1_pseudocode.txt` (two problems).
* Flowchart images (`temp_converter.png`, `grading_rule.png`).
* `week1_reflection.txt`.
