# Lesson 1 — Introduction to Python

Welcome to **Python Essentials** with Code the Dream!

## How to Follow This Content

* Start by reading the lesson's **learning objective** in the `Learning Overview` section. Each weekly assignment will measure your skill related to the learning objective.
* Lessons are split into **subsections**, labeled like this: `1.1`, `1,2`, etc.
* Each subsection has a short **supplemental video** that will help you understand the content in that subsection.
* At the end of each subsection, you'll find a multiple-choice **"Check for Understanding"** question. Complete the question and review the material if your answer is not correct!
* After reading through the lesson content and correctly answering the "Check for Understanding" questions, complete the **Weekly Assignment**.

If you have questions at any point, ask a question in the `discussion` Slack channel or reach out to your mentor!

## Lesson Overview

**Learning objective:** Students will learn the basics of Python programming, including variables, data types, operators, control flow statements, and functions. They will also practice debugging their code.

Topics:

* Python Basics: Variables, data types, data conversion, operators.
* Control Flow: Conditional statements (if, elif, else), loops (for, while).
* Functions: Defining and calling functions, parameters, and return values.
* Error Handling: Introduction to try, except for basic debugging.
* Basic Debugging: Using print statements or logging for debugging.

## 1.1 Python Basics

### Variables in Python

A **variable** is like a labeled box where you store data. In Python, variables don’t need explicit declaration before assignment, and the type of data they hold can change dynamically.

In the example below,

* `name` is assigned a **string** `"Jazmine"`
* `age` is assigned an **integer** `28`
* `height` is assigned a **float** `5.8`

```python
name = "Jazmine"   # A variable storing a string
age = 28           # A variable storing an integer
height = 5.8       # A variable storing a float (decimal)
```

### Data Types in Python

**Data types** tell Python what kind of data is stored in a variable. Common data types include:

* Integer (`int`): Whole numbers (e.g., 42, -3)
* Float (`float`): Decimal numbers (e.g., 3.14, -0.5)
* String (`str`): Text (e.g., "hello", "world")
* Boolean (`bool`): Represents True or False values

```python
is_student = True       # Boolean
balance = 1000.75       # Float
first_name = "Charlie"  # String
number_of_days = 7      # Integer
```

You can check the type of a variable using the `type()` function:

```python
print(type(balance))  # Output: <class 'float'>
```

### Data Conversion

Data conversion, or **type casting**, is the process of converting one data type to another. Python provides several built-in functions to make this easy. Common conversion functions include `int()`, `float()`, `str()`, and `bool()`. Notice that these conversion functions line up with the data types demonstrated in the previous section.

```python
# Convert a string to an integer
num_str = "42"
num_int = int(num_str)  # 42 (integer)

# Convert an integer to a float
num_float = float(num_int)  # 42.0 (float)

# Convert a number to a string
num_str_again = str(num_int)  # "42" (string)

# Convert to a Boolean
is_empty = bool("")  # False (an empty string is considered False)
is_non_zero = bool(5)  # True (non-zero numbers are considered True)
```

#### Why Convert Data Types?

Data conversion is helpful when you need to perform operations between incompatible types or display values in specific formats. For instance, combining a number with text requires converting the number to a string.

```python
# Without type conversion
age = 30
message = "I am " + age + " years old."  # "TypeError: can only concatenate str (not "int") to str"
```

```python
# With type conversion
age = 30
message = "I am " + str(age) + " years old."  # "I am 30 years old."
```

#### Implicit vs. Explicit Conversion

Python sometimes performs **implicit conversion** (automatic type conversion), such as when adding an integer and a float, the result is automatically a float. However, for more control, it’s usually better to use **explicit conversion** with the functions above.

```python
# Implicit conversion
result = 3 + 2.5  # 5.5 (float, because Python converts the integer to float)

# Explicit conversion
result = int(2.8) + 3  # 5 (integer, because we explicitly converted the float to int)
```

### Video 1.1: Data Types and Conversion

Learn how to work with data types in Python in our first video, which covers essential type conversions with `int()`, `float()`, `str()`, and `bool()`, practical examples of when to use them, and tips to avoid common pitfalls.

**Watch the video here.** [LINK TBD]

### Operators in Python

**Operators** are special symbols that perform operations on variables and values. Some of the most commonly used operators are:

1. **Arithmetic Operators**: For mathematical calculations

* `+` (addition): `3 + 2` → `5`
* `-` (subtraction): `5 - 3` → `2`
* `*` (multiplication): `4 * 2` → `8`
* `/` (division): `9 / 3` → `3.0`
* `//` (integer division): `9 // 3` → `3`
* `%` (modulus, remainder): `7 % 3` → `1`
* `**` (exponentiation): `2 ** 3` → 8

2. **Comparison Operators**: Compare two values and return a Boolean (`True` or `False`)

* `==` (equal to): `5 == 5` → `True`
* `!=` (not equal to): `5 != 4` → `True`
* `<` (less than): `3 < 4` → `True`
* `>` (greater than): `10 > 5` → `True`
* `<=` (less than or equal to): `5 <= 5` → `True`
* `>=` (greater than or equal to): `7 >= 3` → `True`

3. **Logical Operators**: Used to combine conditional statements

* `and`: `True and False` → `False`
* `or`: `True or False` → `True`
* `not`: `not True` → `False`

Operators Examples:

```python
# Arithmetic
result = 10 + 5  # 15
remainder = 9 % 4  # 1

# Comparison
print(5 > 3)  # True

# Logical
print(True and False)  # False
```

### 1.1 Check for Understanding

**Question:** What type of data is stored in the variable `age` in the following code?

```python
age = 28
```

* A) String
* B) Integer
* C) Float
* D) Boolean
  
<details>

<summary>Answer</summary>

**Answer**: B) Integer

</details>

**Question:** Which of the following data types would you use to store the value `"Hello, World!"`?

* A) Integer
* B) Float
* C) String
* D) Boolean

<details>

<summary>Answer</summary>

**Answer**: C) String

</details>

**Question**: What will be the output of the following code?

```python
num_str = "42"
num_int = int(num_str)
print(num_int)
```

* A) `"42"`
* B) `42`
* C) `<class 'str'>`
* D) An error message

<details>

<summary>Answer</summary>

**Answer**: B) `42`

</details>

**Question**: What will the following code output?

``python
print(10 % 3)
``

* A) `3`
* B) `1`
* C) `10`
* D) `0`

<details>

<summary>Answer</summary>

**Answer:** B) `1`

</details>

## 1.2 Control Flow

Control flow structures allow us to direct the execution of code based on conditions or repeat code until a condition is met. The two main control flow structures in Python are **conditional statements** and **loops**.

### Conditional Statements

Conditional statements enable code to execute only when specific conditions are met. Python uses `if`, `elif`, and `else` statements to handle different conditions.

* `if`: Checks the initial condition. If `True`, it runs the code block.
* `else`: Runs if none of the previous conditions were `True`.
* `elif`: Stands for 'else if'; checks additional conditions if the previous ones were `False`.

```python
age = 20

if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")
```

#### Nested Conditionals

You can also nest conditionals inside each other for more complex decision-making.

```python
score = 85

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        print("C")
```

### Loops

**Loops** allow us to repeat code multiple times, either for a specific range or while a condition is `True`

#### `For` Loop

The `for` loop is commonly used to iterate over a sequence (like a list or range of numbers).

```python
# Looping through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Using range to loop a specific number of times
for i in range(3):
    print("Loop iteration:", i)
```

#### `While` Loop

A `while` loop runs as long as a condition remains `True`. Be careful to ensure the condition will eventually be `False` to avoid infinite loops.

```python
count = 0

while count < 3:
    print("Count is:", count)
    count += 1
```

#### Breaking Out of Loops

The `break` statement can be used to exit a loop early.

```python
for num in range(10):
    if num == 5:
        break
    print(num)
# Output: 0, 1, 2, 3, 4
```

#### Skipping Iterations

The `continue` statement allows you to skip the rest of the code in the current iteration and move to the next iteration.

```python
for num in range(5):
    if num == 2:
        continue
    print(num)
# Output: 0, 1, 3, 4
```

### Video 1.2: Loops and Conditionals

Our video on loops and conditionals breaks down some common situations in which you might use loops, how to control loop behavior with `break` and `continue`, and **loop nesting**.

**View the video here:** [LINK TBD]

### 1.2 Check for Understanding

**Question:** What will the following code output if `age = 16`?

```python
if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")
```

* A) "You're an adult!"
* B) "You're a teenager."
* C) "You're a child."
* D) No output

<details>

<summary>Answer</summary>

**Answer**: B) "You're a teenager."

</details>

**Question**: What will the following code output?

```python
for i in range(3):
    print(i)
```

* A) `1 2 3`
* B) `0 1 2`
* C) `0 1 2 3`
* D) `3`

<details>

<summary>Answer</summary>

**Answer**: B) `0 1 2`

</details>

## 1.3 Functions

**Functions** are reusable blocks of code that perform specific tasks. They help keep your code organized, modular, and easy to understand.

### Defining and Calling Functions

A function is defined using the `def` keyword, followed by a function name, parentheses `()`, and a colon. The code inside the function is indented.

```python
def greet():
    print("Hello, world!")
```

To call a function, simply use its name followed by parentheses.

```python
greet()  # Output: Hello, world!
```

### Parameters and Arguments

Functions can take **parameters** (variables defined within the parentheses in the function definition) to make them more versatile. When calling the function, you pass **arguments** (the actual values).

```python
def greet(name):
    print("Hello, " + name + "!")
    
greet("Jazmine")  # Output: Hello, Jazmine!
```

You can also define multiple parameters.

```python
def add(a, b):
    print(a + b)

add(3, 5)  # Output: 8
```

### Return Values

A function can return a value to the caller using the `return` keyword. This makes the function's output available for use outside the function.

```python
def square(number):
    return number * number

result = square(4)  # result is 16
```

If a function doesn’t explicitly return a value, it implicitly returns `None`

### Default Parameters

You can set **default values** for parameters, making them optional when the function is called.

```python
def greet(name="stranger"):
    print("Hello, " + name + "!")

greet()            # Output: Hello, stranger!
greet("Luis")   # Output: Hello, Luis!
```

### Video 1.3: Functions

[Video Description TBD]

**View the video here:** [LINK TBD]

### 1.3 Check for Understanding

**Question**: What is the purpose of the `return` statement in a function?

* A) To stop the function
* B) To send a value back to the caller
* C) To print a message
* D) To define a variable

<details>

<summary>Answer</summary>

**Answer**: B) To send a value back to the caller.

</details>

**Question**: What will be the output of the following code?

```python
def greet(name):
    print("Hello, " + name + "!")
    
greet("Luis")
```

* A) `"Hello, stranger!"`
* B) `"Hello, Luis!"`
* C) `"Hello, name!"`
* D) `"Luis"`

<details>

<summary>Answer</summary>

**Answer**: B) `"Hello, Luis!"`

</details>

## 1.4 Error Handling

Error handling in Python is managed using the `try`, `except`, `else`, and `finally` blocks. This structure allows developers to gracefully handle errors that may occur during runtime, ensuring that the program can either recover from an issue or fail gracefully with useful feedback.

### `try` and `except`

The `try` block contains code that might raise an error. If an error occurs, the `except` block is executed, and Python will not terminate the program abruptly. You can catch specific exceptions or handle all exceptions generally.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

```python
try:
    num = int(input("Enter a number: "))
except Exception as e:
    print(f"An error occurred: {e}")
```

### `else`

The `else` block is optional and runs if no exception was raised in the try block.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Success! The result is {result}.")
```

### `finally`

The `finally` block runs regardless of whether an exception occurred or not. It’s often used for cleanup actions like closing files or database connections.

```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    file.close()
    print("File closed.")
```

### Raising exceptions

Python allows you to raise exceptions using the raise keyword, either with built-in exceptions or custom ones.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return True

try:
    check_age(16)
except ValueError as e:
    print(e)
```

### Video 1.4: Error Handling

[Video Description TBD]

**View the video here:** [LINK TBD]

### 1.4 Check for Understanding

**Question**: If the following code tries to divide by zero, which message will it print?

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

* A) It will print nothing
* B) `10`
* C) `Error: Divsion by zero is not allowed.`
* D) `None`

<details>
<summary>Answer</summary>

**Answer:** C) `Error: Division by zero is not allowed.`
</details>

### In-Depth Read: Errors and Exceptions

For a more in-depth look at Errors and Exceptions, along with plenty of examples, check out the [Python Tutorial's article on this subject](https://docs.python.org/3/tutorial/errors.html).

## 1.5 Basic Debugging

**Debugging** is the process of finding and fixing errors in your code. Two popular methods for basic debugging in Python are using **print statements** and **logging**.

### Debugging with Print Statements

Print statements are a simple way to check the values of variables and understand the flow of your program. This technique helps you see what’s happening at specific points in your code.

```python
def multiply(a, b):
    result = a * b
    print("Result is:", result)  # Print to check the result
    return result

multiply(3, 5)  # Output: Result is: 15
```

Tips for effective print debugging:

* Use descriptive messages (e.g., `"Starting loop at i=" + str(i)`).
* Print variable values and descriptions of the program state.
* Remember to remove or comment out `print` statements when you’re done!

### Debugging with Logging

The **logging** module provides more control over output and is useful for larger projects or tracking complex issues. Unlike **print**, logging allows you to set levels to distinguish between informational messages, warnings, errors, and more.

Logging Levels

* **DEBUG**: Detailed information, typically useful only for debugging.
* **INFO**: Confirmation that things are working as expected.
* **WARNING**: An indication that something unexpected happened, or indicative of future problems.
* **ERROR**: A serious problem that prevented some part of the code from running.

To use logging:

1. Import the `logging` module.
2. Set up basic configuration with `logging.basicConfig()`.
3. Use logging statements like `logging.debug()`, `logging.info()`, `logging.warning()`, and `logging.error()`.

Here's an example of using logging for debugging. Notice how each of the three steps are incorporated.

```python
# Step 1
import logging

# Step 2
logging.basicConfig(level=logging.DEBUG)

# Step 3
def multiply(a, b):
    logging.debug(f"Multiplying {a} and {b}")
    result = a * b
    logging.info(f"Result is: {result}")
    return result

multiply(3, 5)
```

### Basic Debugging Video

Let's wrap up Lesson 1's content with a short video on debugging.

**View the video here:** [LINK TBD]

### Check for Understanding

**Question**: What is the primary purpose of using `print` statements in debugging?

* A) To find and correct errors in variable values and program flow
* B) To slow down the program
* C) To remove errors automatically
* D) To show only the final output

<details>
<summary>Answer</summary>

**Answer**: A) To find and correct errors in variable values and program flow
</details>
---
This content was created by Janet Zulu, Reid Russom, and CTD volunteers. To submit feedback, please fill out the [CTD Curriculum Feedback Form](https://airtable.com/apphJi94mO4Uc7a3k/pagD3WQmswgXJvgx3/form).
