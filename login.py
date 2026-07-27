import tkinter as tk
import os

# create class for the each program 

class LoginWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cyber Security ToolKit")
        self.window.geometry("1200x800")
        self.window.resizable(False, False)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "assets", "icon.ico")
        try:
            self.window.iconbitmap(icon_path)
        except Exception as e:
            print("Icon could not be loaded.")
        #self.window.iconbitmap("assets/icon.ico")

        # label for the title

        self.title_label = tk.Label(
            self.window,
            text="Cyber Security ToolKit",
            font=("Arial", 20, "bold")
        )
        self.title_label.pack(pady=20)

        # label for the username
        
        self.username_label = tk.Label(
            self.window,
            text="Username"
        )
        self.username_label.pack(pady=10)

        # entry for the username

        self.username_entry = tk.Entry(
            self.window,
            width=35
        )
        self.username_entry.pack(pady=5)

        # label for the password

        self.password_label = tk.Label(
            self.window,
            text="password"
        )
        self.password_label.pack(pady=(15,0))

        # entry for the password
        self.password_entry = tk.Entry(
            self.window,
            width=35,
            show="*"
        )
        self.password_entry.pack(pady=5)

        # button for the login

        self.login_button = tk.Button(
            self.window,
            text="Login",
            width=15,

        )
        self.login_button.pack(pady=20)

        # label for the register

        self.register_label = tk.Label(
            self.window,
            text="Don't have an account? Register here.",
            fg="blue"
        )
        self.register_label.pack(pady=10)

        # button for the register

        self.register_button = tk.Button(
            self.window,
            text="Register",
            width= 20
        )
        self.register_button.pack(pady=10)
        self.window.mainloop()