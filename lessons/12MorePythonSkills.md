
# **Lesson 12 — More Python Skills**

## **Lesson Overview**
**Learning objective:** In this lesson, students will learn and apply key advanced Python concepts including decorators, list comprehensions, closures, and custom class definitions. They will learn how to write cleaner, more modular code using these features and gain insight into how such patterns are used in real-world frameworks like Dash.

### **Topics:**
1. Decorators
2. List Comprehensions
3. Closures
4. Declaring Custom Classes

---

## **10.1 Python Decorators**

### **Overview**
Python classifies functions as first class citizens, which means that you are able to apply one function to another function. Decorators allow this to be clearer and easier to read.

### **Key techniques**
Decorators are functions that can be called in a unique way, and accept a function as an input.

```python

def decorator(func):
    def wrapper():
        print ("Hello!")
        func()
        print ("World")
@decorator
def name():
    print("John")
```

Note in this example the output:
```
Hello!
John
World!
```

Why did we get this result? The answer is because @decorator called the function using the decorator function. It is effectively equivalent to calling
```python
decorator(name())
```
but is much clearer and easier to understand.

In this example the function is fairly trivial, however in the next section we can dig into a more useful way to use this.

### **Example code**

Here is an example of a decorator that allows us to benchmark different sections of code. We need to allow all functions to go into this decorator, and it will print out the time it took for a function to complete.
```python
import time

def timer(func):
    ## Output the time the inner function takes
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print ("Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def time_consuming_function(...):
    ...
```

Sometimes you need to have a decorator that itself has arguments.  In this case, you need two levels of wrapping:

```Python
def wrap_output(before, after):
    def decorator_wrap_output(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return before + result + after
        return wrapper
    return decorator_wrap_output

@wrap_output("begin:", ":end")
def hello():
    return "Hello, World!"

print(hello()) # Will print "begin:Hello, World!:end"
```

Decorators are often used in another way.  They register a function that is to be called by system code.  For example, in the lesson on Dash, you had the following lines:

```Python
@app.callback(
    Output("stock-price", "figure"),
    [Input("stock-dropdown", "value")]
)
def update_graph(symbol):
```
The `app.callback` method runs before `update_graph()` is ever called.  It records the fact that `update_graph()`, as wrappered by the `app.callback` wrapper function, is to be called whenever the stock dropdown changes.  You could do something like this, registering the functions to be wrapped, as follows:

```Python
callback_dict={}

def wrap_output(before, after,greeting_type):
    def decorator_wrap_output(func):
        callback_dict[greeting_type] = func
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return before + result + after
        callback_dict[greeting_type]=wrapper
        return wrapper
    return decorator_wrap_output

@wrap_output("begin:", ":end","for_hello")
def hello():
    return "Hello, World!"

@wrap_output("begin:", ":end","for_goodbye")
def goodbye():
    return "Goodbye, World!"

print(callback_dict["for_hello"]()) # Will print "begin:Hello, World!:end"

print(callback_dict["for_goodbye"]()) # Will print "begin:Goodbye, World!:end"
```

Here, the decorated functions, in their wrappered form, get registered for callbacks in `callback_dict`.  This is like what Dash is doing when you use the decorator `@app.callback`.

---

## **10.2 Python List Comprehensions**

### **Overview**  
A list comprehension is a fast way to generate a list.  For example, suppose you want a list of the integers from 0 to 19.  You could do

```Python
integer_list=[]
for x in range(20):
    integer_list.append(x)
```
but, with Python, you can use a list comprehension as a shorthand:
```Python
integer_list = [x for x in range(20)]
```
Or, to get just the odd ones:
```Python
odd_list = [x for x in range(20) if x%2 != 0]
```
Or, to get the squares of the odd ones:
```Python
odd_squares_list = [x**2 for x in range(20) if x%2 !=0]
# or
odd_squares_list = [x**2 for x in odd_list]
```

### **Generator Expressions**

A generator expression is just like a list comprehension, except that you use parentheses instead of square brackets.  A generator expression is an `iterable`, meaning you can use it in a `for` loop.  Like so:

```python
odd_squares_generator = (x**2 for x in range(20) if x%2 !=0)

for y in odd_squares_generator:
    print(y)

```

---

## **10.3 Python Closures**

A Python closure is a way of wrappering information by returning a function that has access to that information.  This provides some protection for the stuff you wrapper.  For example:

```Python
def make_secret(secret):
    def did_you_guess(guess):
        if guess == secret:
            print("You got it!")
        else:
            print("Nope")
    return did_you_guess

game1 = make_secret("swordfish")
game2 = make_secret("magic")

game1("magic") # Prints nope
game1("swordfish") # Prints you got it
game2("magic") # Prints you got it
```

Of course, the wrappered function could also store data, but you may need the `nonlocal` keyword.  This makes the variable still wrappered within the outer function, but accessible within the inner function:
```Python
def make_secret(secret):
    bad_guesses = 0
    def did_you_guess(guess):
        nonlocal bad_guesses
        if guess == secret:
            print("You got it!")
        else:
            bad_guesses+=1
            print(f"Nope, bad guesses: {bad_guesses}")
    return did_you_guess

game1 = make_secret("swordfish")
game1("magic") # Prints nope, bad guesses 1
game1("magic") # Prints nope, bad guesses 2
```

---

## **10.4 Declaring Custom Classes in Python**

Just about everything in Python is an object, which is an instance of a class.  Most of the Python libraries you have used so far are implemented as collections of classes.  You need to be able to declare your own classes, so that you can minimize code repetition by implementing capabilites once for collections of objects that share the same set of attributes and methods.  Each such object is an instance of the class.  You declare them as follows:

```Python
class Dog:
    count = 0
    def __init__(self, name, age):
        self.name=name
        self._age = age
        Dog.count+=1
    def call_dog(self):
        print(f"Come here, {self.name}!")
    def speak(self):
        print("bark bark bark")
    @classmethod
    def set_dog_count(cls,value):
        cls.count=value

dog1 = Dog("Spot", 2)
dog1.call_dog()
dog1.speak()
print("dog1's name is {dog1.name}.")
print(f"{Dog.count} dogs.")

dog2 = Dog("Wally", 4)
dog2.call_dog()

Dog.set_dog_count(5)
```
We have:
- The declaration of a class with name Dog.  Class names are capitalized.
- An `__init__` function.  You don't have to have one for the class, but usually you'll want one, to set up the instance variables.
- Instance variables `self.name` and `self._age`.  The values differ for each instance of the class.
- A class variable called `Dog.count`.  There is one value for the class itself.
- A couple of instance methods, call_dog() and speak().  Note that they are always passed the value of `self`, so as to give access to instance variables.
- A class method, `set_dog_count`.  This is a class method, not an instance method, meaning that we don't need to have an instance of Dog to call the method.  It is declared using the `@classmethod` decorator.

The methods of the class always have at least one argument, `self`, although they may have more.  When the method is invoked, though, `self` is not included.  So, you have `dog1.call_dog()`, which doesn't include the `self` argument.

Python doesn't really have encapsulation of data within instances of a class.  You can read or change `dog1.name` and `dog1._age` from outside of the class.  However, the underscore for `_age` means that it would be poor form to access this variable from outside the class.  It is supposed to be "protected", so you shouldn't do such access.

Suppose you want a class that is like the Dog class, but perhaps a little different in behavior.  You can use inheritance:

```Python
class BigDog(Dog):
    def __init__(self, name, age): # The init function isn't necessary here, actually.  If you leave it out, Dog.__init__ is used.
        super().__init__(name, age) # Or, BigDog could have other instance variables you initialize after calling the __init__ for super().
    def fetch(self):
        print("Got it.")
    def speak(self):
        print("Woof Woof Woof")
    def speak_verbose(self):
        super().speak()
        self.speak()

dog3 = BigDog("Butch", 3)
dog3.call_dog()
dog3.speak()
dog3.speak_verbose()
```

Here, the `call_dog()` method is inherited from the Dog superclass.  The `speak()` method overrides the one in the superclass.  The `speak_verbose()` method calls the `speak()` method of the superclass and then the `speak()` method of the class.

A useful attribute of every class and instance is `__dict__`.

```python
print(Dog.__dict__) # prints stuff for the Dog class, including its methods
print(dog1.__dict__) # prints the attributes of the instance and their values.
```

You can also create classes from system classes:

```Python
class Shout(str):
   def __new__(cls, content):
      return str.__new__(cls, content.upper())

x = Shout("hello there")
print(x) # prints HELLO THERE
```
In this case, the subclass overrides the `__new__` method of the `str` class, and not the `__init__` method, because strings are immutable. 

## **Summary**

In this lesson, you learned:
1. How to use Python Decorators
2. How to use Python List Comprehensions
3. Closures in Python
4. Declaring and Using Custom Python Classes
