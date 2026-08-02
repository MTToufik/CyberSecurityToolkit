import tkinter as tk
import random
import string
from tkinter import messagebox
from database import save_history

class PasswordGeneratorWindow:

    def __init__(self, user_id):
        self.user_id = user_id

        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("1200x800")
        self.window.resizable(False, False)
        self.window.configure(bg="#EAF2F8")

        # title

        self.title_label = tk.Label(
            self.window,
            text = "🔐 Password Generator",
            font = ("Arial", 20, "bold"),
            bg = "#EAF2F8",
            fg = "#1F4E79"
        )
        self.title_label.pack(pady=20)

         # passwprd length

        self.length_label = tk.Label(
            self.window,
            text="Password Length",
            font=("Arial", 14),
            bg = "#EAF2F8",
            fg = "#1F4E79"
        )
        self.length_label.pack(pady=10)

        # password entry length

        self.length_entry = tk.Entry(
            self.window,
            width=10,
            justify="center",
            font=("Arial", 14)
        )
        self.length_entry.pack(pady=20)

        # checkboxes 

        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        # uppercase checkbox

        self.uppercase_check = tk.Checkbutton(
            self.window,
            text= "Include Uppercase Letters",
            variable=self.uppercase_var,
            bg="#EAF2F8",
            font=("Arial", 12)
        )
        self.uppercase_check.pack(anchor="w", padx=170)

        # lowercase checkbox

        self.lowercase_check = tk.Checkbutton(
            self.window,
            text= "Include Lowercase Letters",
            variable=self.lowercase_var,
            bg="#EAF2F8",
            font=("Arial", 12)
        )
        self.lowercase_check.pack(anchor="w", padx=170)

        # numbers checkbox

        self.numbers_check = tk.Checkbutton(
            self.window,
            text= "Include Numbers",
            variable=self.numbers_var,
            bg="#EAF2F8",
            font=("Arial", 12)
        )
        self.numbers_check.pack(anchor="w", padx=170)

        # special characters checkbox

        self.special_check = tk.Checkbutton(
            self.window,
            text= "Include Special Characters (!@#$...)",
            variable=self.special_var,
            bg="#EAF2F8",
            font=("Arial", 12)
        )
        self.special_check.pack(anchor="w", padx=170)

        # gemerate button

        self.generate_button = tk.Button(
            self.window,
            text="🔄 Generate Password",
            
            width=20,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#3498DB",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.generate_password
        )
        self.generate_button.pack(pady=20)

        # Generated Password Label

        self.result_label = tk.Label(
           self.window,
           text="Generated Password",
           font=("Arial", 12, "bold"),
           bg="#EAF2F8",
           fg="#1F4E79"
        )
        self.result_label.pack() 

        # Generated Password Entry

        self.result_entry = tk.Entry(
            self.window,
            width=30,
            justify="center",
            font=("Consolas", 13)
        )
        self.result_entry.pack(pady=10)

        # password strength label

        self.strength_label = tk.Label(
            self.window,
            text="Password Strength: -",
            font=("Arial", 12, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.strength_label.pack()

        # copy button

        self.copy_button = tk.Button(
            self.window,
            text="📋 Copy to Clipboard",
            width=20,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#2ECC71",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.copy_password
        )
        self.copy_button.pack(pady=10)

        self.window.mainloop()

    def generate_password(self):

        password_length = self.length_entry.get()

        if not password_length.isdigit():
            messagebox.showerror(
                "Error", 
                "please enter a valid positive integer for password length."
            )
            return

        password_length = int (password_length)

        if password_length < 8 or password_length > 64:
            messagebox.showerror(
                "Error",
                "Password length must be between 8 and 64"
            )
            return 

        # main logic for password generation

        characters = ""

        if self.uppercase_var.get():
            characters += string.ascii_uppercase

        if self.lowercase_var.get():
            characters += string.ascii_lowercase

        if self.numbers_var.get():
            characters += string.digits

        if self.special_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror(
                "Error", 
                "Please select at least one character type."
            )
            return
        password = ""

        for i in range(password_length):
            password += random.choice(characters)

        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)

        # password strength logic

        strength = "Weak"
        color = "red"

        if password_length >=12:
            strength = "Moderate"
            color = "orange"

        if (password_length >=16
            and self.uppercase_var.get()
            and self.lowercase_var.get()
            and self.numbers_var.get()
            and self.special_var.get()):

            strength = "Strong"
            color = "green"

        self.strength_label.config(
            text=f"Password Strength: {strength}",
            fg=color
        )

        save_history(
            self.user_id,
            "Password Generator",
            password
        )


    # copied function

    def  copy_password(self):

        password = self.result_entry.get()

        if password == "":
            messagebox.showwarning(
                "Warning",
                "Please generate a password first before copying."
            )
            return
        self.window.clipboard_clear()
        self.window.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )



if __name__ == "__main__":
    PasswordGeneratorWindow()

        
