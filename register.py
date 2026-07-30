import tkinter as tk
from tkinter import messagebox 
from database import insert_user
from modules.hash_generator import generate_hash
#from login import LoginWindow

# class for register window


class RegisterWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Register")
        self.window.geometry("1200x800")
        self.window.resizable(False, False)

        # label for the title
        self.title_label = tk.Label(
            self.window,
            text="Create New Account",
            font=("Arial", 18,"bold")
        )
        self.title_label.pack(pady=20)

        # label for the username
        self.username_label = tk.Label(
            self.window,
            text="Username"
        )
        self.username_label.pack()

        # entry for the username
        self.username_entry = tk.Entry(
            self.window,
            width=35
        )
        self.username_entry.pack(pady=5)

        # label for the email

        self.email_label = tk.Label(
            self.window,
            text="Email"
        )
        self.email_label.pack(pady=(15,0))

        # entry for the email

        self.email_entry = tk.Entry(
            self.window,
            width=35
        )
        self.email_entry.pack(pady=5)

        # label for the password

        self.password_label = tk.Label(
            self.window,
            text="Password"
        )
        self.password_label.pack(pady=(15,0))

        # entry for the password
        self.password_entry = tk.Entry(
            self.window,
            width=35,
            show="*"
        )
        self.password_entry.pack(pady=5)

        # confirm password label

        self.confirm_label = tk.Label(
            self.window,
            text="Confirm Password"
        )
        self.confirm_label.pack(pady=(15,0))

        # entry for the confirm password
        self.confirm_entry = tk.Entry(
            self.window,
            width=35,
            show="*"
        )
        self.confirm_entry.pack(pady=5)

        # Register button

        self.register_button = tk.Button(
            self.window,
            text="Register",
            width=15,
            command=self.register_user
        )
        self.register_button.pack(pady=20)

        # login label

        self.login_label = tk.Label(
            self.window,
            text="Already have an account? Login here."
        )
        self.login_label.pack(pady=10)

        # login button

        self.login_button = tk.Button(
            self.window,
            text="Login",
            width=20,
            command=self.open_login
        )
        self.login_button.pack(pady=10)

        self.window.mainloop()

    # function to register user

    def register_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()
        if not username or not email or not password or not confirm_password:
            messagebox.showerror("Error", "All field are required")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Password do not match.")
            return

        # generated password hash
        hashed_password = generate_hash(password)
        # save users to database

        success = insert_user(username,email,hashed_password)

        if success:
            messagebox.showinfo("success", "Registration completed successfully")

        else:
            messagebox.showerror(
                "Error",
                "Username or email already exists"
            )
        #messagebox.showinfo("Success", "Validation completed successfully")

    def open_login(self):
        from login import LoginWindow
        self.window.destroy()
        LoginWindow()


        
        