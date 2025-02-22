# README: Introduction to Python Syntax and Basic Operations

Welcome to the **Introduction to Python Syntax and Basic Operations** course! This course is designed for beginners who are new to Python and want to get a solid foundation in the language’s basic syntax and core operations. By the end of this course, you should feel comfortable writing simple Python scripts and performing basic data manipulations.

---

## Table of Contents
1. [Prerequisites](#prerequisites)  
2. [Course Overview](#course-overview)  
3. [Python Syntax](#python-syntax)  
   - [Case Sensitivity](#case-sensitivity)  
   - [Comments](#comments)  
4. [Data Types](#data-types)  
   - [Numbers (int, float)](#numbers-int-float)  
   - [Strings](#strings)  
5. [Arithmetic Operations](#arithmetic-operations)  
6. [Printing and Formatting](#printing-and-formatting)  
   - [The `print()` Function](#the-print-function)  
   - [f-Strings](#f-strings)  
7. [How to Run Python Code](#how-to-run-python-code)  
8. [Further Reading and Resources](#further-reading-and-resources)  

---

# Prerequisites

- A basic understanding of how to use a computer and navigate the command line (optional but helpful).
- Python installed on your system (version 3.7+ recommended).  
  - Download and install from [python.org](https://www.python.org/downloads/) if you haven’t already.

---

# Course Overview

In this course, we’ll cover:
- The fundamental rules of Python syntax.
- How to include comments in your code for better readability.
- Core data types (integers, floats, strings).
- Basic arithmetic operations (+, -, `*`, `/`, `%`).
- Printing output using built-in Python functions and formatting outputs with f-strings.

By understanding these topics, you will have the groundwork to explore more advanced features of Python.

---

# Python Syntax

## Case Sensitivity
Python is a **case-sensitive** language, meaning it treats uppercase and lowercase letters as distinct characters. As a result:
- Variable names such as `myVar` and `myvar` would be considered two completely different variables.
- Function names also must match exactly when called. For example, if you define a function def `greet(): ...`, calling it as `Greet()` (with an uppercase "G") will result in an error because Python does not recognize it as the same function.
- Keywords in Python are always lowercase `(e.g., if, for, while)`, so you must not alter their case when using them.

This is different from languages that are not case-sensitive, where Var, vAr, and var might all refer to the same name. In Python, remember to use the exact letter cases for variables, functions, and keywords, or you might encounter unexpected `NameErrors` and other issues.

**Example**:
```python
my_var = 5
My_Var = 10
print(my_var)   # Outputs 5
print(My_Var)   # Outputs 10
```
## Comments
Comments in Python are created by placing the **`#`** symbol at the beginning of a line or after code. Comments are ignored by the Python interpreter, making them ideal for clarifying your code.

**Example**:
```python
# This is a single-line comment
x = 10  # Assign 10 to x
```

# Data Types

## Numbers (int, float)

- **Integers (int)** are whole numbers (e.g., `1`, `2`, `10`, `-3`).
- **Floats (float)** are numbers with a decimal point (e.g., `3.14`, `-7.25`).

**Example:**

```python
my_int = 10
my_float = 3.14
```

## Strings

Strings in Python are sequences of characters, created by enclosing text in quotes.

**Example:**

```python
my_string = "Hello, World!"
another_string = 'Python is fun'
```

# Arithmetic Operations
Python supports various arithmetic operations:

```python
Addition +
Subtraction -
Multiplication *
Division /
Modulo % (returns the remainder of a division)
```

**Example:**

```python
a = 10
b = 3

sum_result = a + b       # 13
diff_result = a - b      # 7
prod_result = a * b      # 30
quot_result = a / b      # 3.3333...
mod_result = a % b       # 1
```

# Printing and Formatting
## The print() Function
The print() function is used to display output to the terminal or console.

Example:

```python
print("Hello, World!")  # Outputs: Hello, World!
```

## f-Strings

f-Strings (formatted strings) allow you to embed variables directly in a string.
Prefix the string with f and place the variable inside curly braces {}.

Example:

```python
age = 25
print(f"My age is {age}")  # Outputs: My age is 25
```

# How to Run Python Code

Interactive Mode:

Open a terminal and type python or python3 (depending on your setup).
This will open the Python interpreter where you can type code line by line.
Script Mode:

Create a file with the .py extension (e.g., script.py).
Add your Python code in that file.
Run it in the terminal with python script.py or python3 script.py.

# Further Reading and Resources

Official Python Documentation — The official and most comprehensive guide.

W3Schools Python Tutorial — Beginner-friendly tutorials with examples.

Real Python — Tutorials, articles, and resources for all levels.


# Home work
1) Create a file naming `pratice.py` to calculate the sum, extraction of 2 numbers
      - 3.2121 + 5.24424
      - 8 + 9
   Print excitly in terminal the message example : "Sum of 2 number 3.2121 and  5.24424 is ... "

2) Consider/practice https://www.w3schools.com/python/python_datatypes.asp 
(Python Home -> Python Operators)
