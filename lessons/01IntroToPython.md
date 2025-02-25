# Lesson 1 — Introduction to Python

Welcome to **Python Essentials** with Code the Dream!

## 👀 How to Follow This Content

* Start by reading the lesson's **learning objective** in the `Lesson Overview` section. Each weekly assignment will measure your skill related to the learning objective.
* Lessons are split into **subsections**, labeled like this: `1.1`, `1.2`, etc.
* Several subsections also have a short **supplemental video** that will help you understand the content in that subsection.
* At the end of each subsection, you'll find a multiple-choice **"Check for Understanding"** question. Complete the question and review the material if your answer is not correct!
* After reading through the lesson content and correctly answering the "Check for Understanding" questions, complete the **Weekly Assignment**.

If you have questions at any point, ask a question in the `discussion` Slack channel or reach out to your mentor!

## Lesson Overview

**Learning objective:** Students will learn the basics of Python programming, including variables, data types, operators, control flow statements, and functions. They will also practice debugging their code.

Topics:

- **Setting Up Your Python Environment**:  
  Installing Python, pip, and your IDE. We recommend the VS Code IDE. It's ok to use another IDE if you are comfortable with it. Verifying installations and creating `.py` files.
- **Python Basics**:  
  Variables, data types (integers, floats, strings, booleans), data conversion (explicit and implicit), and operators (arithmetic, comparison, logical).
- **Block Structure and Indentation**:  
  Understanding Python’s indentation-based syntax for defining blocks like functions, loops, and conditionals.
- **Control Flow**:  
  Conditional statements (`if`, `elif`, `else`), loops (`for`, `while`), and controlling loops with `break` and `continue`.
- **Functions**:  
  Defining and calling functions, parameters, return values, and handling dynamic arguments with `*args` and `**kwargs`.
- **Debugging**:  
  - **Error Handling**: Introduction to `try`, `except` for handling runtime errors.  
  - **Basic Debugging**: Using print statements and the `logging` module to debug code effectively.

## 1.1 Setting up your environment 


### Install Python

You can download Python from the official website: [python.org](https://www.python.org/downloads/).

Follow the installation instructions for your operating system:

1. **Install Python:**
   Follow the installation instructions for your operating system.  For this class, we require Python 3.  The previous version (Python 2) is significantly different and is deprecated.

   - **For Windows**
       - If you are using Windows, it is common to use the Windows Subsystem for Linux for development. WSL is not recommended for this class.** Later lessons use `matplotlib for graphs`. It is difficult to do the configuration needed to get graphs to show in the WSL environment. Windows users should install in Windows native.
       - Follow the instructions on the website. Make sure to check the option to **Add Python to PATH** during installation.
       - Windows users should have Git for Windows installed, and should use Git Bash for all subsequent steps.  If python hangs when you run it in a git bash window, add the following line to ~/.bash_profile: `alias python='winpty python.exe'`

   - **For macOS**:
      - macOS typically comes with Python pre-installed. To ensure you are using Python 3, download the latest version of Python from [python.org](https://www.python.org/downloads/).
      - Follow the installation instructions. You can also use **Homebrew** to install Python by running the following command in the terminal:
          ```bash
          brew install python
          ```
    - **For Linux**:
       - Most Linux distributions come with Python pre-installed, but you need to have Python 3 for the class. To install or upgrade Python 3, you can use the package manager:
       - For **Debian/Ubuntu** systems:
          ```bash
          sudo apt update
          sudo apt install python3
          ```
        - For **Fedora**:
          ```bash
          sudo dnf install python3
          ```
        - For **Arch Linux**:
          ```bash
          sudo pacman -S python
          ```


2. **Verify Python Installation**:
    After installation, you can verify that Python is installed correctly, and that you have Python 3, by opening a terminal or command prompt and running:
   
    ```bash
    python --version
    ```
    Some systems install Python as python3 to differentiate it from a previous installation of Python 2, which is deprecated.:
    ```bash
    python3 --version
    ```
    This should display the installed version of Python. For example, you might see:
    ```
    Python 3.9.7
    ```

    At this point, you can try the Python Interactive Shell.  You type `python` or `python3` without arguments.  This brings up a command line into which you can type code, which is then executed as each statement is completed.  The code is not preserved, of course, but this is a good way to try many of the ideas below.  Ctrl-D exits the shell.

3. **Install pip**

    **Pip** is Python’s package installer, and it is included automatically with Python versions 3.4 and above. It allows you to easily install and manage Python libraries and packages from the Python Package Index (PyPI).

    #### Verify if pip is installed:
    To check if **pip** is installed, open a terminal or command prompt and type:

    ```bash
    pip --version
    ```

    Systems which install Python as `python3` will install pip as `pip3` instead:

    ```bash
    pip3 --version
    ```

    This should display the installed version of pip. If pip is not installed or you encounter an error, you may need to reinstall Python and ensure that the box for **Add Python to PATH** is checked.

    #### Upgrading pip:
    If you already have pip installed but want to make sure it’s up to date, run the following command:

    ```bash
    python -m pip install --upgrade pip
    ```

    Or, for Python 3:

    ```bash
    python3 -m pip install --upgrade pip
    ```

4. **Create a Working Folder**
    - Your assignments will use a git repository, and the instructions for setting up that repository are included in the first lesson.  You should also have a separate folder to try the code samples from the lessons.  This working folder should be outside of the cloned repository on your computer.  For example, you could create a folder called `python_class`.  Inside that folder, create a folder called `working` to use for lesson code samples.  When you do the first assignment, you will also clone a repository called `python_homework` inside the `python_class` folder.  Your lessons and assignments will require some packages to be added to Python using pip.  These should be installed into a virtual environment -- a collection of packages specifically for your project.  (The JavaScript and Rails package managers set up a virtual environment automatically, but it requires several additional steps for Python.) 
    
    Create a folder, cd to that folder, and then do the following:
    - Install the virtualenv package: `pip install virtualenv` (or perhaps `pip3 insall virtualenv`).
    - Then, create the virtual environment.
        - Windows users enter the following commands:
        ```bash
        python -m venv .venv
        source .venv/Scripts/activate
        code .
        ```
        - Mac and Linux users enter the following commands:
            ```bash
            python3 -m venv .venv
            source .venv/bin/activate
            code .
            ```
    Once your virtual environment is activated, you see `.venv` as part of your terminal prompt.  Be sure that is present for all subsequent work.  When you create a new terminal session, you have to activate the virtual environment again.  When the virtual environment is active, you can always use the commands `python` and `pip`, that is, you don't need `python3` or `pip3`.

5. **Set Up VSCode for Python**
    - Some developers may choose an alternate editor, such as PyCharm, but VSCode works well, and the instructions below describe what you need to do.
    - Be sure to install the Python extension for VSCode.
    - Windows developers: You should add the following lines to your `~/.bashrc` file (creating the file if it does not exist):
    ```bash
    if [ -f ./.venv/Scripts/activate ]; then
        source ./.venv/Scripts/activate
    fi
    ```
    - In the VSCode command palette (Ctrl-Shift-P) go to `Python: Select Interpreter` and choose the one that has `.venv` in it.
    - When you open a VSCode terminal, you should see a `(.venv)` as part of the prompt.  This is how you know that the virtual environment is active.  You want it to be active before installing packages such as pandas or numpy.

        
## 1.2 Python Basics

### If you are a JavaScript Developer

You have a head start.  All the basic structures of programming (loops, conditional statements, variables, and so on) are in Python.  But, Python syntax is different.  You'll have to adjust to the differences.  You may want to read [this summary](https://www.freecodecamp.org/news/learn-python-for-javascript-developers-handbook/). (This is optional.)

### A Cheat Sheet

Here is [a one page summary of the Python syntax](https://quickref.me/python.html).  You may want to have it on hand.

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

Here are some general rules for Python variable naming.
- Lowercase: Use lowercase letters for variable names.
- Underscores: Separate words in variable names with underscores (_).
- Descriptive: Choose meaningful names that clearly indicate the variable's purpose.
- Avoid single-character names: Except for simple loop counters (e.g., i, j, k).

### Data Types in Python

**Data types** specify the kind of data is stored in a variable. Common data types include:

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
is_empty = not bool("")  # True 
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

### 🎬 Video 1.2: Data Types and Conversion

Learn how to work with data types in Python in our first video, which covers essential type conversions with `int()`, `float()`, `str()`, and `bool()`, practical examples of when to use them, and tips to avoid common pitfalls.  In general, you are not required to view the videos for this class, as the lesson text covers the same information, but the videos may help you learn and remember.

**[Watch the video here.](https://youtu.be/v5NBGGHKJtI)**

## 1.3 Operators in Python

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
### Check for Understanding

**Question:** What type of data is stored in the variable `age` in the following code?

```python
age = 28
```

* A) String
* B) Integer
* C) Float
* D) Boolean
  
<details>

<summary>View answer</summary>

**Answer**: B) Integer

</details>

**Question:** Which of the following data types would you use to store the value `"Hello, World!"`?

* A) Integer
* B) Float
* C) String
* D) Boolean

<details>

<summary>View answer</summary>

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

<summary>View answer</summary>

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

<summary>View answer</summary>

**Answer:** B) `1`

</details>

## 1.4 Block Structure and Indentations 

In Python, indentation plays a crucial role in the syntax of the language. Unlike many other programming languages, which use braces {} or other markers to denote code blocks, Python uses indentation to group statements and define the scope of loops, functions, classes, and conditional statements.

**Why Indentation Matters in Python**

* **Defining Code Blocks:** Indentation tells Python where a block of code begins and ends.
* **Enforcing Readability:** The clean and readable structure makes Python code easier to follow.

**Key Concepts:**

* **Indentation in Control Structures:** 
    * All code under control structures (such as `if`, `else`, `for`, `while`, and function definitions) must be indented.  You always put a colon `:` before starting an indented block on the next line.

* **Consistent Indentation:**
    * Consistency is key. Python does not allow mixing tabs and spaces. Use either spaces or tabs but never both. 
    * The Python community’s standard is to use 4 spaces per indentation level.

**Block Structure Example:**

```python
def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
```
In the above example:

The function check_number defines the first level of indentation.
The if, elif, and else blocks define additional indentation levels for the code that falls under each condition.
Indentation Error Example:


```python
def check_number(num):if num > 0:  # This will raise an error because it's not indented properly
    print("Positive number") 
```
In the above case, Python will raise an error stating: IndentationError: expected an indented block.

Using Indentation with Loops:

```python
for i in range(3):
    print("Loop iteration:", i)  # This line is inside the for loop
```
Any line that is indented under the for statement is part of the loop.


In many programming languages the format and structure makes code more easily readable.  Structure is even more critical in Python.  Read [this article from Geeks for Geeks](https://www.geeksforgeeks.org/indentation-in-python/) to gain an understanding of the importance of indentation, format, and structure when writing code blocks in Python. 

## 1.5 Control Flow

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
# range(stop) where stop is greater than the last number generated
# range(start, stop) starts with a number other 0
# range(start, stop, step) uses the specified step size instead of 1 
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

### Check for Understanding

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

<summary>View answer</summary>

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

<summary>View answer</summary>

**Answer**: B) `0 1 2`

</details>

### Long Lines 

If you need to split a line for readability, you put a backslash `\` at the end of the line.  You don't need to indent the line after the backslash.  Python concatenates the two lines (or more, if the next line also has a backslash.)  If you do indent, Python includes the indentations.  Long strings can also be created another way.  You start and end them with three quotes. `"""`  Python concatenates them, including the line feeds, spaces, and indentations."

## 🎬 Video 1.5: Loops and Conditionals

Our next video is a breakdown breakdown of  common situations in which someone might use loops, how to control loop behavior with `break` and `continue`, and loop nesting.

**[Watch the video here](https://youtu.be/VUwzi5TVMzM).**

## 1.6 Functions

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

### Using *args and **kwargs

Functions can be made more flexible by allowing them to handle an arbitrary number of arguments.

**What are *args?**

*args allows a function to accept any number of positional arguments, which are collected into a tuple.  A tuple is an immutable, ordered data structure.  Tuples are covered in detail in lesson2.

**Example:**

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10
```

**Key Points:**

* Use *args when the exact number of arguments isn't known beforehand.
* The collected arguments are treated as a tuple.

**What are **kwargs?**

**kwargs allows a function to accept any number of keyword arguments, which are collected into a dictionary.  A dictionary is an associative array similar to a Hash in Ruby or an object in JavaScript.  Dictionaries are covered in detail in lesson 2.

**Example:**

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Janet", role="Developer", age=25)
```

**Key Points:**

* Use **kwargs when you expect dynamic named parameters.
* The collected arguments are treated as a dictionary.

**Combining *args and **kwargs**

You can use both together to handle a mix of positional and keyword arguments.

**Example:**

```python
def mixed_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mixed_function(1, 2, 3, name="Janet", role="Developer")
```

**Output:**

```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Janet', 'role': 'Developer'}
```

**Another Example**

```python
def mixed_function_2(*args, a_value="default"):
    print(f"args are {args} and a_value is {a_value}")

mixed_function_2(1, 2, 3, a_value="override")
```

In this case, a_value is a keyword argument, because it comes after the `*args`.  In the example (this is not always so) a_value has a default value.  The keyword is given explicitly here, instead of using `**kwargs`.  When the keyword is given explicitly, the value is not delivered in a dictionary.  It is accessed using the keyword as a variable name. 

Functions are always declared with named positional arguments (if any) first, then the `*args` (if this is used), then the explicitly named keyword arguments (if any), and then in last place `**kwargs` (if this is used).  When a function with keyword arguments is called, the order in which the keyword arguments is given doesn't matter (except they should come after the positional arguments.) 

### Variable Scope

If a variable is declared inside a function, it is local to that function.  For example, this code gives an error:

```python
def set_name():
    name="James"

set_name()
print(name)
```
The name variable is declared inside the function, and is not defined outside.  Also note the results below:
```python
name = "Hima"

def set_name():
    name="James"

set_name()
print(name) # Prints "Hima"

def set_name_2(name):
    name = "Nguyen"

set_name_2()
print(name) # Prints "Hima"
```

Python acts as if the `name=` statement inside each function is the declaration for a new local variable called `name`.  The first `name=` statement in the script above is for a global variable.

A function *can* access global variables.  For example, suppose we add this code to the script above.

```python
def print_global_name():
    print(name) # Prints "Hima"
```

And, a function *can* change values stored in global variables (although this is typically bad practice).  As in this code:
```python
this_list=[0,1] # a global
def change_list():
    this_list[1]=17 # Does change this_list[1] for the this_list global
```
Indentation blocks in Python have no effect on variable scope.

### 🎬 Video 1.6: Functions

Our supplemental video for this section overviews functions, arguments, and parameters; along with two sets of example code.

**[Watch the video here](https://youtu.be/89cGQjB5R4M?feature=shared).**

### Check for Understanding

**Question**: What is the purpose of the `return` statement in a function?

* A) To stop the function
* B) To send a value back to the caller
* C) To print a message
* D) To define a variable

<details>

<summary>View answer</summary>

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

<summary>View answer</summary>

**Answer**: B) `"Hello, Luis!"`

</details>

## 1.7 Basic Debugging

**Debugging** is the process of finding and fixing errors in your code. Two popular methods for basic debugging in Python are using **print statements** and **logging**.

### Debugging with Print Statements

Print statements are a simple way to check the values of variables and understand the flow of your program. This technique helps you see what’s happening at specific points in your code.

```python
def multiply(a, b):
    result = a * b
    print("Result is: ", result)  # Print to check the result
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

### For Further Investigation: Using the Debugger

VSCode with the Python plugin provides a debugger.  You can set breakpoints, step in or over function calls, display or change the values of variables, and so on.  You will need to learn to use a debugger eventually, although it is not required for this course.  If you want to check this out, see [this link](https://code.visualstudio.com/docs/python/python-quick-start#_debug) for a description, and [here](https://www.youtube.com/watch?v=b4p-SBjHh28) is a video that shows the process.

### 🎬 Video 1.7: Basic Debugging

Let's wrap up this section with a short video on debugging.

**[View the video here!](https://youtu.be/R4pCjyknKD0?feature=shared)**

### Check for Understanding

**Question**: What is the primary purpose of using `print` statements in debugging?

* A) To find and correct errors in variable values and program flow
* B) To slow down the program
* C) To remove errors automatically
* D) To show only the final output

<details>
<summary>View answer</summary>

**Answer**: A) To find and correct errors in variable values and program flow
</details>
---

## 1.8 Error Handling

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

### 🎬 Video 1.8 Error Handling

Our final video of Lesson 1 covers error handling with `try` and  `except` blocks.

**[View the video here](https://youtu.be/NIWwJbo-9_8?feature=shared).**



### Check for Understanding

**Question**: If the following code tries to divide by zero, which message will it print?

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

* A) It will print nothing
* B) `10`
* C) `Error: Division by zero is not allowed.`
* D) `None`

<details>
<summary>View answer</summary>

**Answer:** C) `Error: Division by zero is not allowed.`
</details>

## 1.9 String Operations

In Python, everything is an object, and each object is an instance of a class.  Each class provides methods for the object.  Try the following.  Open a `.py` file in VSCode, and declare a string, like:
```
my_string = "abc"
```
Then, on the next line, type `my_string.`.  As you type the dot, VSCode prompts you with a pulldown that has many methods for this instance of the `str` class, such as lower(), upper(), split(), join(), strip(), and so on.  You can check out the reference [here.](https://docs.python.org/3/library/string.html)

You can also use formatted strings.  These do variable substitution to compose a string.  Each of the values is converted to a string and added to the result.  Formatted strings have an `f` just before the first double quote, as follows:
```
name = "Ed"
count = 6
kind_of_object = "apples"
print(f"{name} has {count} {kind_of_object}.") # Prints "Ed has 6 apples."
```
You can also add format indications, for example to show two decimal places:
```
cost = 22/7
print(f"The pie cost ${cost:.2f}.")
```

## 🎉 Congratulations on finishing your first lesson in Python Essentials!

Your next step is to complete the coding assignment. As always, reach out to your mentor if you have questions, and take time to celebrate your hard work. 

---
This content was written by Janet Zulu, Reid Russom, and CTD volunteers—with special thanks to the brain trust of John McGarvey, Rebecca Callari-Kaczmarczyk, Tom Arns, and Josh Sternfeld. To submit feedback, please fill out the **[CTD Curriculum Feedback Form](https://forms.gle/RZq5mav7wotFxyie6)**.
