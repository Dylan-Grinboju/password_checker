# Password Checker

This project was developed as part of the *Topics in Network Security* course at Ben-Gurion University.

## Overview
The Password Checker tool provides the following features:

1. **Detect Common Passwords**: Identify if a password is commonly used and should be avoided. The tool uses three datasets of varying sizes, allowing you to choose the one that suits your needs.
2. **Estimate Brute Force Resistance**: Calculate the estimated time required to brute force the password using three different levels of computational power.

### Purpose
This tool was created to raise awareness about the importance of strong and secure passwords. It is my first program written in Python, and through this project, I aimed to deepen my understanding of the language. Initially, the tool was designed as a CLI program without a graphical user interface (GUI). However, to make it more accessible to less tech-savvy users, I developed a GUI version and provided a precompiled executable for easy use without requiring scripts.

## How to Use

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

## Notes
- Your checked passwords are neither saved nor transmitted anywhere.
- Always exercise caution when running scripts from unknown sources. Review the code before execution to ensure safety.

## Disclaimer
This tool is intended for educational purposes only. It should not be used for illegal or unethical activities.
