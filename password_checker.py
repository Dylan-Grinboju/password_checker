import os
import sys
import tkinter as tk
from tkinter import ttk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def load_password_library(file_path):
    file_path = resource_path(file_path)
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return set()
       
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return set(line.strip() for line in file)

def check_password(password, common_passwords):
    if password in common_passwords:
        return f"Password is too common (exact match found in library)."
    
    if password[::-1] in common_passwords:
        return f"Password is too common (reverse match found in library)."
    
    if password.lower() in common_passwords:
        return f"Password is too common (lowercase match found in library)."
    if password.upper() in common_passwords:
        return f"Password is too common (uppercase match found in library)."
    
    leet_speak = password.replace('4', 'A').replace('3', 'e').replace('1', 'l').replace('0', 'o').replace('5', 's').replace('7', 't').replace('@', 'a')
    if leet_speak in common_passwords:
        return f"Password is too common (leet speak match found in library)."
    
    # check if password has a sequence or sub sequence from the file 'sequences'
    sequences_path = resource_path("common_passwords/sequences.txt")
    with open(sequences_path, 'r', encoding='utf-8', errors='ignore') as file:
        sequences = set(line.strip() for line in file)
                
    min_length_for_sequence = 5
    normalized_password = password.lower() 
    for seq in sequences:
        for i in range(len(seq) - min_length_for_sequence+1):
            substring = seq[i:i+min_length_for_sequence]
            if substring in normalized_password:
                return f"Password contains common sequence: '{substring}'"
            
    return "Password does not match or resemble common passwords."

def calculate_time_to_brute_force(password, brute_force_power):
    num_of_digits = sum(c.isdigit() for c in password)
    num_of_uppercase_letters = sum(c.isupper() for c in password)
    num_of_lowercase_letters = sum(c.islower() for c in password)
    num_of_symbols = len(password) - num_of_digits - num_of_uppercase_letters - num_of_lowercase_letters
    total_combinations = 10**num_of_digits * 26**num_of_uppercase_letters * 26**num_of_lowercase_letters * 30**num_of_symbols # 30 symbols: !@#$%^&*()_+-={}[]|:;"'<>,.?/~
    time_to_crack = total_combinations / brute_force_power # in seconds
    print_statement = "Estimated time to brute force: "
    if time_to_crack < 60:
        return f"{print_statement}{time_to_crack:.2f} seconds."
    time_to_crack /= 60
    if time_to_crack < 60:
        return f"{print_statement}{time_to_crack:.2f} minutes."
    time_to_crack /= 60
    if time_to_crack < 24:
        return f"{print_statement}{time_to_crack:.2f} hours."
    time_to_crack /= 24
    if time_to_crack < 30:
        return f"{print_statement}{time_to_crack:.2f} days."
    time_to_crack /= 30.5
    if time_to_crack < 12:
        return f"{print_statement}{time_to_crack:.2f} months."
    time_to_crack /= 12
    return f"{print_statement}{time_to_crack:.2f} years."

def check_password_gui():
    password = password_entry.get().strip()
    library_choice = library_var.get()

    if library_choice == "Small":
        library_path = "common_passwords/small.txt"
    elif library_choice == "Medium":
        library_path = "common_passwords/medium.txt"
    elif library_choice == "Large":
        library_path = "common_passwords/large.txt"
    else:
        result_label.config(text="Error: Invalid library choice.")
        return

    common_passwords = load_password_library(library_path)
    if not common_passwords:
        result_label.config(text="Error: No common passwords loaded.")
        return

    result = check_password(password, common_passwords)
    result_label.config(text=result)

def calculate_brute_force_gui():
    password = password_entry.get().strip()
    power_choice = power_var.get()

    if power_choice == "Smartphone":
        brute_force_power = 5*10**5 # Snapdragon 8 Elite
    elif power_choice == "Home Computer":
        brute_force_power = 5*10**10 # RTX 5090
    elif power_choice == "Server":
        brute_force_power = 2*10**14 # AMD EPYC 9965
    else:
        result_label.config(text="Error: Invalid power choice.")
        return

    time_to_crack = calculate_time_to_brute_force(password, brute_force_power)
    result_label.config(text=time_to_crack)

root = tk.Tk()
root.title("Password Checker")

style = ttk.Style()
style.configure("TLabel", padding=6)
style.configure("TButton", padding=6)
style.configure("TRadiobutton", padding=6)

main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(main_frame, text="Enter a password to check:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
password_entry = ttk.Entry(main_frame)
password_entry.grid(row=0, column=1, padx=10, pady=10, sticky=(tk.W, tk.E))

ttk.Label(main_frame, text="Choose the sample size for the password library:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
library_var = tk.StringVar(value="Small")
ttk.Radiobutton(main_frame, text="Small", variable=library_var, value="Small").grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
ttk.Radiobutton(main_frame, text="Medium", variable=library_var, value="Medium").grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)
ttk.Radiobutton(main_frame, text="Large", variable=library_var, value="Large").grid(row=1, column=3, padx=10, pady=10, sticky=tk.W)

ttk.Label(main_frame, text="Choose the computer power:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
power_var = tk.StringVar(value="Smartphone")
ttk.Radiobutton(main_frame, text="Smartphone", variable=power_var, value="Smartphone").grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
ttk.Radiobutton(main_frame, text="Home Computer", variable=power_var, value="Home Computer").grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)
ttk.Radiobutton(main_frame, text="Server", variable=power_var, value="Server").grid(row=2, column=3, padx=10, pady=10, sticky=tk.W)

ttk.Button(main_frame, text="Check Password", command=check_password_gui).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
ttk.Button(main_frame, text="Calculate Brute Force Time", command=calculate_brute_force_gui).grid(row=3, column=2, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(main_frame, text="")
result_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

root.mainloop()