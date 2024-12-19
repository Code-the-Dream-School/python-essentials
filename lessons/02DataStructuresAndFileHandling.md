# Lesson 2 — Data Structures and File Handling

## Reminder: How to Follow This Content

* Start by reading the lesson's **learning objective** in the `Learning Overview` section. Each weekly assignment will measure your skill related to the learning objective.
* Lessons are split into **subsections**, labeled like this: `1.1`, `1,2`, etc.
* Each subsection has a short **supplemental video** that will help you understand the content in that subsection.
* At the end of each subsection, you'll find a multiple-choice **"Check for Understanding"** question. Complete the question and review the material if your answer is not correct!
* After reading through the lesson content and correctly answering the "Check for Understanding" questions, complete the **Weekly Assignment**.

If you have questions at any point, ask a question in the `discussion` Slack channel or reach out to your mentor!

## Lesson Overview

Congrats, you've made it to Lesson 2! This week, we'll deepen our knowledge of core Python concepts, including dictionaries and lists. We'll also learn how to import **modules**, powerful tools that help your Python projects reach their full potential.

**Learning objective**: Students will explore various data structures, such as lists, tuples, dictionaries, and sets. They will learn how to read and write data to files and use external modules.

Topics:

* Lists, Tuples, Dictionaries, and Sets: Creating, accessing, and modifying data structures.
* File Handling: Reading from and writing to text and CSV files.
* Introduction to Modules: Importing and using Python libraries.
* Keyboard Input

## 2.1 Lists, Tuples, Dictionaries, and Sets

Before we talk about lists and tuples, we need to define two new words: "mutable" and "immutable."

Something that is **mutable** can be modified or changed after it is created. Something that is **immutable** cannot be modified or changed after it is created.

Imagine a piece of clay (mutable) versus a ceramic statue (immutable):

* Clay can be reshaped, squished, or molded into different forms after it's first created. You can add or remove parts easily.
* A ceramic statue, once it's fired in a kiln, cannot be changed without breaking it completely.

In Python programming, here's a concrete example using *mutable* lists and *immutable* tuples:

``` python
# Mutable example (list)
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')  # We can add a new item
fruits[0] = 'orange'  # We can change an existing item
print(fruits)  # Now ['orange', 'banana', 'cherry', 'date']

# Immutable example (tuple)
colors = ('red', 'green', 'blue')
# colors[0] = 'yellow'  # This would cause an error
# You cannot change the tuple after creation
```

### Lists

A **list** is a *mutable*, ordered collection of items. Lists allow duplicates and can hold items of different types, although typically you’ll find lists containing items of the same type. You can add, remove, or modify elements in a list, making them versatile for storing data that may change.

```python
fruits = ['apple', 'banana', 'cherry']  # Define a list
fruits.append('orange')  # Add an item
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

#### Key List Methods

* `append(item)`: Adds `item` to the end of the list.
* `remove(item)`: Removes the first occurrence of `item`.
* `sort()`: Sorts the list in place.

### Tuples

A **tuple** is an *immutable*, ordered collection of items. Once defined, the elements in a tuple cannot be modified, added, or removed. Tuples are useful for data that shouldn’t change, like fixed configuration values or coordinates.

```python
dimensions = (1920, 1080)  # Define a tuple
print(dimensions[0])  # Access the first element: Output: 1920
```

#### Why use tuples?

* Tuples are memory-efficient compared to lists.
* Useful when you want a constant, fixed-size collection of data.

### Dictionaries

A **dictionary** is an unordered collection of key-value pairs. Each key is unique and used to store and retrieve data efficiently. Dictionaries are ideal for mapping relationships, such as a user’s name to their profile data or an item to its price.

```python
person = {'name': 'Jazmine', 'age': 30}  # Define a dictionary
print(person['name'])  # Output: Jazmine
person['email'] = 'jazmine@example.com'  # Add a new key-value pair
```

#### Key Dictionary Methods

* `keys()`: Returns a list of keys in the dictionary.
* `values()`: Returns a list of values.
* `get(key)`: Returns the value associated with `key`, or `None` if `key` is not found.

### Sets

A **set** is an unordered collection of unique elements. Sets are useful for removing duplicates from a list or performing mathematical set operations like union, intersection, and difference.

```python
unique_numbers = {1, 2, 3, 3, 4}  # Define a set (duplicates are ignored)
unique_numbers.add(5)  # Add a new item
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
```

#### Common Set Operations

* `union()`: Returns a set containing all unique elements from both sets.
* `intersection()`: Returns elements common to both sets.
* `difference()`: Returns elements present in one set but not the other.

### Review Table: Lists, Tuples, Dictionaries, and Sets

Ok, let's review! Here's a table demonstrating the key differences between the four new terms we just learned:

| Data Structure | Ordered | Changeable (Mutable) | Allows Duplicates | Key-Value Pairs |
|----------------|---------|----------------------|-------------------|-----------------|
| **List**       | Yes     | Yes                 | Yes               | No              |
| **Tuple**      | Yes     | No                  | Yes               | No              |
| **Dictionary** | No      | Yes (Keys: No)      | Keys: No, Values: Yes | Yes           |
| **Set**        | No      | Yes                 | No                | No              |

### 2.1 Video: Lists, Tuples, Dictonaries, and Sets

[Video Description TBD]

**View the video here:** [LINK TBD]

### 2.1 Check for Understanding

**Question**: Which of the following statements about Python data structures is correct?

* A) Lists are immutable, and tuples are mutable.
* B) Sets allow duplicate elements.
* C) Dictionaries store data in key-value pairs and do not allow duplicate keys.
* D) Tuples are ordered and changeable.

<details>

<summary>Answer</summary>

**Answer**: C) Dictionaries store data in key-value pairs and do not allow duplicate keys.

</details>

## 2.2 File Handling

In Python, reading from and writing to text files is handled with the `open()` function. Text files are simple, containing plain text data, making them ideal for storing simple logs, configuration data, or notes.

#### Reading a Text File

To read a file, use `open()` with the `"r"` (read) mode and call `.read()`, `.readline()`, or .`readlines()` to get the content.

```python
with open('example.txt', 'r') as file:
    content = file.read()  # Read entire file
    print(content)
```

#### Writing to a Text File

To write to a file, open it in `"w"` (write) or `"a"` (append) mode. Writing mode will overwrite the file if it exists, while append mode will add to the file.

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!")  # Write to the file
```

#### Additional Modes

* `"r+"`: Read and write
* `"a"`: Append to the file (keeps existing content).

### Reading and Writing CSV Files

CSV (Comma-Separated Values) files are commonly used to store tabular data, where each row is a new line, and each value is separated by a comma. Python’s built-in `csv` module makes it easy to work with these files.

#### Reading a CSV File

To read a CSV file, use `csv.reader()` and iterate through the rows.

```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

#### Writing to a CSV File

To write to a CSV file, use `csv.writer()`. Each row should be a list or tuple representing a row in the CSV.

```python
import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Write header row
    writer.writerow(['Jazmine', 30, 'New York'])  # Write a data row
```

#### Additional Options

* `csv.DictReader()` and `csv.DictWriter()`: Use dictionaries to work with row data, which can make reading and writing more convenient when you have headers.

### 2.2 Video: Reading and Writing a CSV File

In this video, we'll demonstrate reading and writing to a real CSV file. After the video, practice reading and writing to a CSV file using the W3 Resource tutorial [here](https://www.w3resource.com/python-exercises/csv/index.php).

**View the video here:** [LINK TBD]

### 2.2 Check for Understanding

**Question**: What does the `"w"` mode do when opening a file in Python?

* A) Reads the file without making changes.
* B) Appends new data to the end of the file.
* C) Overwrites the file with new data, creating it if it doesn’t exist.
* D) Opens the file for reading and writing without overwriting.

<details>

<summary>Answer</summary>

**Answer**: C) Overwrites the file with new data, creating it if it doesn’t exist.

</details>

## 2.3 Introduction to Modules

In Python, a **module** is a file containing Python code, which can define functions, classes, and variables. Modules allow you to organize code logically, keeping related code together, and help avoid redundancy by making it reusable across different parts of a project.

For example, if you’re working on a project involving math calculations, you could create a module `math_utils.py` to hold custom math functions, making your main program file cleaner and easier to maintain.

### Why Use Modules?

Modules help in several ways:

  1. **Code Organization**: Breaks up large codebases into smaller, more manageable files.
  2. **Reusability**: Commonly used code can be stored in a module and imported wherever needed.
  3. **Namespace Management**: Modules allow you to separate code into different namespaces, avoiding conflicts between variables and functions with the same name.
  4. **Built-in Functionality**: Python’s standard library includes many modules that provide pre-built functionality (like math operations, file handling, and more), so you don’t have to reinvent the wheel.

### Importing Modules

You can import modules using the `import` statement, either as a whole or by importing specific functions or classes.

#### Importing an Entire Module

You can import a module and use its functions by prefixing them with the module name:

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

#### Importing Specific Functions or Classes

To import specific parts of a module, use `from <module> import <name>`:

```python
from math import sqrt
print(sqrt(16))  # Output: 4.0
```

#### Using Aliases

If a module has a long name, you can give it an alias with the `as` keyword:

```python
import pandas as pd
df = pd.DataFrame({'Name': ['Jazmine', 'Luis'], 'Age': [30, 35]})
```

### Python Standard Library and External Libraries

Python’s **standard library** is packed with built-in modules for handling everything from file I/O and math operations to data serialization and date/time management. For example:

* `datetime` for working with dates and times.
* `json` for handling JSON data.
* `os` for interacting with the operating system.

You can install and use **external libraries** with the `pip` package manager. External libraries are modules that add more functionality not included in the standard library, such as `requests` for HTTP requests or `numpy` for numerical operations.

#### Installing and Importing Extrenal Libraries

To install a library, use:

```bash
pip install requests
```

Then, import and use it like any other module:

```python
import requests
response = requests.get('https://api.example.com/data')
print(response.json())
```

#### Example: Creating and Importing a Custom Module

Suppose you create a file called `greetings.py` with a function:

```python
# greetings.py
def say_hello(name):
    return f"Hello, {name}!"
```

Then, in another file, you can import and use it:

```python
from greetings import say_hello
print(say_hello("Luis"))  # Output: Hello, Luis!
```

Modules and libraries in Python offer flexibility and organization, making your code easier to manage, expand, and share across projects.

### 2.3 Video: Python Modules and Libraries

[Video Description TBD]

**View the video here:** [LINK TBD]

### 2.3 Check for Understanding

**Question**: Which of the following commands correctly imports only the sqrt function from the `math` module?

* A) `import sqrt from math`
* B) `from math import sqrt`
* C) `import math.sqrt`
* D) `import math as sqrt`

<details>

<summary>Answer</summary>

**Answer**: B) `from math import sqrt`

</details>

## 2.4 Keyboard Input

In Python, handling keyboard input is straightforward, making it easy to interact with users. The input() function is the main way to capture user input from the keyboard, which you can then use directly or store in a variable for further processing.

#### Using `input()`

The `input()` function displays a prompt (optional) and waits for the user to type something and press Enter. By default, `input()` captures the input as a string, so if you need it in another format (like an integer), you’ll have to convert it.

```python
name = input("Enter your name: ")  # Displays a prompt and waits for input
print(f"Hello, {name}!")  # Greets the user with their input
```

#### Converting Input Types

Since `input()` returns data as a string, you’ll often want to convert it for calculations or comparisons.

```python
age = input("Enter your age: ")  # Gets input as a string
age = int(age)  # Converts input to an integer
print(f"Next year, you will be {age + 1} years old.")
```

If the user types something that can’t be converted (e.g., entering "twenty" instead of "20"), this will raise an error. To handle this gracefully, you can use `try-except`:

```python
try:
    age = int(input("Enter your age: "))
    print(f"Next year, you will be {age + 1} years old.")
except ValueError:
    print("Please enter a valid number.")
```

### Example: Simple Calculator Using Keyboard Input

Here’s a basic example that combines multiple `input()` calls to create a calculator. Pay attention to this code, because you'll be creating a calculator in this week's assignment!

```python
# Simple calculator
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### 2.4 Video

[Video Description TBD]

**View the video here:** [LINK TBD]

### 2.4 Check for Understanding

**Question**: Which of the following statements about `input()` in Python is correct?

* A) `input()` captures user input and automatically converts it to an integer.
* B) `input()` displays a prompt and captures user input as a string by default.
* C) `input()` captures user input but only works with numbers.
* D) `input()` is used to output text to the console.

<details>

<summary>Answer</summary>

**Answer**: B) input() displays a prompt and captures user input as a string by default.

</details>

---
This content was created by Janet Zulu, Reid Russom, and CTD volunteers. To submit feedback, please fill out the [CTD Curriculum Feedback Form](https://airtable.com/apphJi94mO4Uc7a3k/pagD3WQmswgXJvgx3/form).
