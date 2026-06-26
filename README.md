
# 🏋️ SmartFit Membership Assistant

A beginner-friendly Python application developed for the **CS 1101 – Programming Fundamentals** Unit 2 Assignment at the **University of the People**.

The application demonstrates the use of:

- Conditional Statements (`if`, `elif`, `else`)
- Logical Operators (`and`, `or`, `not`)
- Nested Conditional Statements
- User Input Validation
- Decision-Making Logic

---

## 📌 Project Overview

SmartFit is a digital fitness startup that helps users select the most suitable fitness program and membership plan based on their personal information.

The application asks the user for:

- Age
- Medical condition (Yes/No)
- Membership type (Basic/Premium)
- Personal training preference (Basic members only)

Based on the user's responses, the program:

- Recommends an appropriate fitness program.
- Determines membership fees.
- Provides youth discounts.
- Suggests Premium upgrades.
- Recommends medical consultation when necessary.

---

## ✨ Features

- Age-based fitness program recommendation
- Medical condition verification
- Membership selection
- Personal training option
- Youth discount for Premium members under 30
- Premium upgrade recommendation
- Free consultation recommendation
- Input validation
- Console-based interface

---

## 💻 Technologies Used

- Python 3
- PyInstaller (for executable generation)

---

## 📂 Project Structure

```
SmartFit/
│
├── sm.py
├── SmartFit_Membership_Assistant.exe
├── README.md
└── screenshots/
```

---

# 🚀 Installation & Setup

## Quick Start

Clone the repository:

```bash
git clone https://github.com/sourabghosh108-cc1/SmartFit_Membership_Assistant_v1.0.git
cd SmartFit_Membership_Assistant_v1.0
```

### Windows

Install:

- Git: https://git-scm.com/download/win
- Python 3: https://www.python.org/downloads/

Run:

```bash
python sm.py
```

---

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install git python3

git clone https://github.com/sourabghosh108-cc1/SmartFit_Membership_Assistant_v1.0.git

cd SmartFit_Membership_Assistant_v1.0

python3 sm.py
```

---

### Fedora

```bash
sudo dnf install git python3

git clone https://github.com/sourabghosh108-cc1/SmartFit_Membership_Assistant_v1.0.git

cd SmartFit_Membership_Assistant_v1.0

python3 sm.py
```

---

### Arch Linux

```bash
sudo pacman -S git python

git clone https://github.com/sourabghosh108-cc1/SmartFit_Membership_Assistant_v1.0.git

cd SmartFit_Membership_Assistant_v1.0

python sm.py
```

---

### Standalone Windows Executable

Download:

> **Google Drive:** *(Paste your download link here.)*

Then simply run:

```
SmartFit_Membership_Assistant.exe
```

---

# ▶️ Usage

Run the program and follow the on-screen prompts.

The application will ask for:

- Age
- Medical condition
- Membership type
- Personal training preference (Basic membership only)

It will then recommend a suitable fitness program, membership plan, and any applicable offers.

## 📸 Sample Output

```
========================================
 Welcome to SmartFit Fitness Assistant
========================================

Enter your age: 25

You are eligible for the Regular Fitness Program.

Do you have any medical condition? (yes/no): no

You can proceed with registration.

Choose your membership (Basic/Premium): premium

Premium plan: $60 per month.

You qualify for a youth discount! 10% off your plan.

Thank you for using the SmartFit Membership Assistant!
```

---

## 🎯 Learning Outcomes Demonstrated

- Decision making using `if`, `elif`, and `else`
- Boolean expressions using logical operators
- Nested conditional statements
- Input validation
- Real-world programming scenario

---

## 👨‍💻 Author

**Sourab Ghosh**

CS 1101 – Programming Fundamentals

University of the People

---

## 📄 License

This project was developed for educational purposes as part of a university assignment.
