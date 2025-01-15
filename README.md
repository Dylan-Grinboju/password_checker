# Password Checker

This project was developed as part of the *Topics in Network Security* course at Ben-Gurion University.

## Overview
The Password Checker tool provides the following features:

1. **Detect Common Passwords**: Identify if a password is commonly used and should be avoided. The tool uses three datasets of varying sizes, allowing you to choose the one that suits your needs.
2. **Estimate Brute Force Resistance**: Calculate the estimated time required to brute force the password using three different levels of computational power.

### Purpose
This tool was created to raise awareness about the importance of strong and secure passwords. It is my first program written in Python, and through this project, I aimed to deepen my understanding of the language. Initially, the tool was designed as a CLI program without a graphical user interface (GUI). However, to make it more accessible to less tech-savvy users, I developed a GUI version and provided a precompiled executable for easy use without requiring scripts.

### The Making Of
The creation process involved the following steps:
1. Researched brute-force attacks and dictionary attacks.
2. Downloaded repositories containing extensive lists of common passwords and calculated three levels of brute-force resistance to simulate.
3. Implemented a basic input system that receives the password and checks it against the lists or calculates the time to brute-force it.
4. Added variations to the dictionary attack, including checking the password as all-caps, in 'leet speak,' reversed, and more.
5. Developed a user-friendly GUI.
6. Researched and implemented the precompiled executable.
7. Uploaded the project to Git and created this README.

## How to Run

### Option 1: Run from Source
1. Download the following files and folder:
   - `password_checker.py`
   - `password_checker.spec`
   - The `common_passwords` folder

2. Ensure the `common_passwords` folder is located in the root directory of the script.

3. Open a terminal at the root of the script.

4. Execute the script directly from the terminal:
   ```
   python password_checker.py
   ```

### Option 2: Use the Precompiled Version
1. Download the precompiled executable from the `dist` folder.
2. Run the `.exe` file (compatible with Windows OS).

## How to Use
Simply enter the password you want to check in the text box. Then, choose the level of computational power you want to simulate for brute-forcing your password, or check if the password is common enough to be part of one of the datasets.

## Notes
- Your checked passwords are neither saved nor transmitted anywhere.
- Always exercise caution when running scripts from unknown sources. Review the code before execution to ensure safety.

## Disclaimer
This tool is intended for educational purposes only. It should not be used for illegal or unethical activities.

