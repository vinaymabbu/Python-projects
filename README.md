
# 🐍 Python Mini Projects

Welcome to my collection of beginner-friendly Python command-line tools. These are small, interactive projects designed to build practical coding skills.

---

## 📋 Table of Contents

- [🔐 Password Generator](#-password-generator)
- [✅ To-Do List Manager](#-to-do-list-manager)
- [🧠 Python Trivia Game](#-python-trivia-game)
- [📦 Installation](#-installation)
- [▶️ How to Run](#-how-to-run)
- [🛠 Technologies Used](#-technologies-used)
- [💡 What You Learn](#-what-you-learn)
- [🚀 Future Improvements](#-future-improvements)
- [📬 Contact](#-contact)

---

## 🔐 Password Generator

A customizable password generator that helps users create strong passwords based on their preferences.

### 🎯 Features

- User-defined password length
- Options to include:
  - Uppercase letters
  - Special characters
  - Numbers
- Always includes lowercase characters by default
- Ensures the final password has at least one of each selected character type
- Uses Python's built-in `string` and `random` modules

### 🧠 How It Works

1. Prompts user to input desired password length.
2. Asks whether to include uppercase letters, special characters, and digits.
3. Builds a character pool based on selected options.
4. Guarantees inclusion of at least one character from each selected type.
5. Randomly selects characters to complete the password.
6. Returns a secure, randomized password.

### 💻 Usage

```bash
python password_generator.py
```

---

## ✅ To-Do List Manager

A simple command-line task manager that allows users to track their daily tasks, with support for saving data persistently using a JSON file.

### 🎯 Features

- View all tasks with status (pending or completed)
- Create new tasks with custom descriptions
- Mark specific tasks as complete
- Automatically saves and loads tasks from a file (`todo_list.json`)
- Graceful error handling for file operations and user inputs

### 🧠 How It Works

1. Loads existing tasks from `todo_list.json` (or creates it if not found).
2. Shows a menu with 4 options:
   - View tasks
   - Create task
   - Complete task
   - Exit
3. Tasks are stored as dictionaries with:
   - `"description"` – the task text
   - `"complete"` – `True` or `False` status
4. When the user marks a task as complete, it updates the file.

### 💻 Usage

```bash
python todo_list.py
```

---

## 🧠 Python Trivia Game

An interactive quiz game that tests the user's knowledge of Python basics with randomly selected questions.

### 🎯 Features

- Stores questions and answers in a Python dictionary
- Randomly selects 5 out of 10 predefined questions per session
- Accepts user input and compares it with the correct answer (case-insensitive)
- Displays final score out of 5 at the end

### 🧠 How It Works

1. Loads a dictionary of 10 Python-related questions with one-word answers.
2. Randomly picks 5 questions.
3. Asks each question and accepts the user’s typed answer.
4. Compares with the correct answer and updates the score.
5. Shows the total correct answers at the end of the quiz.

### 💻 Usage

```bash
python python_trivia_game.py
```

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/python-mini-projects.git
```

2. Navigate to the project folder:

```bash
cd python-mini-projects
```

---

## ▶️ How to Run

You can run any script directly using Python 3:

```bash
python password_generator.py
python todo_list.py
python python_trivia_game.py
```

---

## 🛠 Technologies Used

- Python 3.x
- Standard Libraries Only:
  - `random`
  - `string`
  - `json`

> No external dependencies needed

---

## 💡 What You Learn

These mini-projects help you build understanding of:
- Conditional logic and loops
- Functions and modular code design
- File handling (read/write JSON)
- Error handling and input validation
- User interaction via command-line
- Dictionary, list, and string operations

---

## 🚀 Future Improvements

- Add a simple GUI using Tkinter or PyQt for each project
- Encrypt saved passwords securely
- Allow category filters and deadlines in the To-Do List
- Add levels or categories in the Trivia Game
- Export trivia scores and task reports

---

## 📬 Contact

**Created by [Your Name or GitHub Handle]**

- GitHub: [github.com/your-username](https://github.com/your-username)

> Feel free to ⭐ the repo if you find it useful!
