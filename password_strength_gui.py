# This is a comment

import tkinter as tk
import re

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Label(root, text="Enter Password:").pack()

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

def check_strength():
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    if score <= 2:
        result_label.config(text="❌ Weak Password", fg="red")
    elif score <= 4:
        result_label.config(text="⚠️ Medium Password", fg="orange")
    else:
        result_label.config(text="✅ Strong Password", fg="green")

tk.Button(
    root,
    text="Check Strength",
    command=check_strength
).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
