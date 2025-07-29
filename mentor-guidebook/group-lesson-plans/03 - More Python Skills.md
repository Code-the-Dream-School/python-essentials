# Week 3: More Python Skills — Group Mentor Guide


Welcome to Week 3 of the Python 100 course! This week, students are learning:

- How to write and call custom functions
- How to use conditional statements (`if`, `elif`, `else`)
- How to work with different data types: strings, lists, booleans, and dictionaries
- How to use the built-in `input()` function

Students are working in the `03_more_python_skills.ipynb` notebook on Deepnote.

## 🧊 Warm-Up (5–10 minutes)

Choose one:

**👋 Relationship-Building**  
- What’s a small but satisfying skill you’ve learned in the last year?  
- What kind of tasks do you always try to automate (or wish you could)?

**💡 Check for Understanding (from last week)**  
- What’s a variable?  
- How do you store multiple values in a list?  
- What does `print()` do, and when should we use it?

## 🧭 Explore vs. Apply — Session Formats

**Explore Sessions** → Walk through function syntax, logic branching, and user input.  
**Apply Sessions** → Debug student functions, write small programs together, or test edge cases.

## ⏱️ Sample Timing for 1-Hour Session

| Time      | Activity                         |
|-----------|----------------------------------|
| 0:00–0:10 | Warm-up + review last week       |
| 0:10–0:30 | Explore: walk through new syntax |
| 0:30–0:50 | Apply: function remix & examples |
| 0:50–1:00 | Wrap-up + final questions        |

## ❓ Check for Understanding (Ask 2–3)

- What’s the difference between a function and a variable?
- How do we “call” or run a function after defining it?
- When would we use `elif` instead of just `if`/`else`?
- What happens if we try to access a list item that doesn’t exist?

## 🧑‍🏫 Explore Prompts

Use these to help students see how the parts connect:

- Let’s write a function called `greet_user(name)` that prints a custom message.  
- What happens if we call a function without passing in a parameter?  
- Let’s take a program that uses lots of `print()`s and refactor it with `return`.

🧑‍💻 *Mini-Demo Ideas:*  

    def add_two(num):
        return num + 2

    print(add_two(5))   # prints 7

    def describe_pet(name, species):
        if species == "dog":
            return f"{name} is a very good dog."
        elif species == "cat":
            return f"{name} is a mysterious cat."
        else:
            return f"{name} is a lovely {species}."

    pet_description = describe_pet("Cleo", "cat")
    print(pet_description)

## 🛠️ Apply Prompts (Live Coding & Troubleshooting)

### 🔧 Assignment Hotspots
- Students write a function but forget to call it  
- Forgetting `return` or confusing it with `print()`  
- Using `input()` but not converting to the correct data type (e.g. integer)  
- Syntax errors from missing colons or indentation in `if`/`elif` blocks  
- Hardcoding values instead of using function parameters

### ✅ Try This Live

**Let’s walk through creating a “Guess the Number” helper function:**

    def check_guess(guess, correct_number):
        if guess == correct_number:
            return "You got it!"
        elif guess < correct_number:
            return "Too low!"
        else:
            return "Too high!"

Ask:
* How can we make this case-insensitive?
* How could we turn this into a full guessing game loop?

## 💬 Engagement Strategies (for quiet groups)

* “Can someone suggest a function we could write together?”  
* “Try breaking the function on purpose — what kind of error do we get?”  
* “Write a custom function that takes your name and favorite food and returns a message!”

## 💡 Optional Challenges

- Write a function that counts how many times a letter appears in a word  
- Make a function that takes a list and returns the last item  
- Bonus: Use `input()` to build a Mad Libs–style sentence generator

✅ Mentor To-Do  
- [ ] Run a session using this guide  
- [ ] Let students debug, explore, or build on their code  
- [ ] Submit your [Mentor Session Report](https://airtable.com/appoSRJMlXH9KvE6w/shrp0jjRtoMyTXRzh)
