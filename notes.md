# Python Learning Notes - Phase 1

<!--TOC-->
# Table of Contents
- [Day 1 - Initial commit and environment setup](#day-1---initial-commit-and-environment-setup)
- [Day 2 - Added Python basic calculator script](#day-2---added-python-basic-calculator-script)
- [Day 3 - Conditional logic and loops](#day-3---conditional-logic-and-loops)
- [Day 4 - Functions and basic modularization](#day-4---functions--basic-modularization)
---

## Day 1 - Initial commit and environment setup
**Date:** 2025-11-17

**What I did:**
- Installed Python, VS Code, Git
- Created GitHub repo
- Wrote first Python program `day1_hello.py`
- Pushed initial commit to GitHub
- Started freeCodeCamp Python Certification

**File(s):**
`day1_hello.py`

**Key Lessons / Notes:**
- Python basics: `print()` and `input()`
- How to run a script in VS Code
- Version control: commit, push

**Issues / Fixes:**
- None on Day 1

---

## Day 2 - Added Python basic calculator script
**Date:** 2025-11-19

**What I did:**
- Practiced converting input to numbers with `float`
- Built small calculator to add two numbers
- Increased variables and calculations to include subtraction, multiplication and division
- Pushed updated script to GitHub
- Completed 5 freeCodeCamp lessons in Introduction to Python

**File(s):**
`day2_basics.py`

**Key Lessons / Notes:**
- Always type valid numbers into `input()`
- Debugged `ValueError` from invalid float conversion
- Reminder to double check sequence for typing errors
- GitHub workflow: `add`, `commit`, `push`

**Issues / Fixes:**
- `ValueError` occurred when trying to substitute the number directly into the `input()` prompt
- Entered numbers in the code line itself instead of creating the prompt
- Fixed by keeping the prompt text static and typing numbers in terminal

---

## Day 3 - Conditional logic and loops
**Date:** 2025-11-19

**What I did:**
- Learned `for` loops and `range()`
- Built a script to count by 1, 2, or 5
- Experimented counting by various multiples, 2s or 5s, both positive and negative directions
- Experimented with `range(start, stop, step)`
- Pushed updated script to GitHub using VS Code Source Control
- Created automated script that appends a new day entry to notes.md
- Amended code to atuomatically detect the last day and incrememnt the day number
- Amended code to append a formatted Markdown heading and template to notes.md
- Amended code to automatically add a Table of Contents (TOC) entry at the top

**File(s):**
`day3_loops.py`

**Key Lessons / Notes:**
- `range(start, stop, step)` controls counting
- Step can be negative to count down
- Learned how to make counting flexible with step values

**Issues / Fixes:**
- None on Day 3
## Day 4 - Functions & Basic Modularization
**Date:** 2025-11-25

**What I did:**
- Learned to define functions using def
- Practiced writing Python functions with inputs and return values.
- Learned to separate code into multiple files.
- Created multiple small functions to handle greetings, aritmetic and logic checks.
- Created a separate module of functions (greet, add_numbers, is_even, etc.)
- Imported functions using 'from helpers import'.
- Tested several functions and verified that imports worked correctly.
- Other functions included conversions (c to f, f to c, km to m, etc.), asking user for choice.
- Created a tip calculator factoring total bill, percentage required, and split with however many people. 
- Created prompt to identify how many words in a sentence.
- Built a Caesar cypher in freecodecamp Python certification course.

**File(s):**
- `day4_functions.py`
- `day4_helpers.py`

**Key Lessons / Notes:**
- Functions allow me to reuse code rather than repeating logic.
- Parameters let me pass in different values to customize behaviour/result.
- Return values allow functions to send back results to the main script.
- Modularization - learning how real prokects are structed/multiple Python files.
- Using import helps keep the main script clean and organized - I need to remember to keep it cleaner.
- Learned the difference between running a file and importing it. 
- A little more comfortable with Python syntax. 

**Issues / Fixes:**
- Typos in function names (addnumber vs add_number) caused errors.
- Pay attention to input values coming in as strings (convert with int() or float())