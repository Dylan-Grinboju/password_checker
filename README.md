# Password Checker

This project was developed as part of the *Topics in Network Security* course at Ben-Gurion University.

## Overview
The Password Checker tool allows you to:

1. **Detect Common Passwords**: Determine if a password is commonly used and should be avoided. The check uses three different datasets of passwords, each with varying lengths. You can select which dataset to use.
2. **Estimate Brute Force Resistance**: Calculate how long it would take to brute force the password using three different levels of CPU power.

## How to Use

### Option 1: Run from Source
1. Download the following files and folder:
   - `password_checker.py`
   - `password_checker.spec`
   - The `common_passwords` folder

2. Ensure the `common_passwords` folder is located at the root of the script directory.

3. Run the script directly from the terminal:
   ```
   python password_checker.py
   ```

### Option 2: Use the Precompiled Version
1. Download the precompiled executable from the `dist` folder.
2. Run the `.exe` file (designed for Windows OS).

## Notes
- Your checked passwords are neither saved nor transmitted anywhere.
- Always exercise caution when running scripts from unknown sources. Review the code before running it to ensure safety.

## Disclaimer
This tool is intended for educational purposes only. It should not be used for illegal or unethical activities.

