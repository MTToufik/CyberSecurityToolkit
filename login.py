
import tkinter as tk
import os
from tkinter import messagebox

from database import login_user
from modules.hash_generator import verify_hash
from register import RegisterWindow
from dashboard import DashboardWindow


class LoginWindow:

    def __init__(self):

        # Main Window
        self.window = tk.Tk()
        self.window.title("Cyber Security ToolKit")
        self.window.state("zoomed")
        self.window.resizable(True, True)

        # Colors
        self.bg_color = "#EAF2F8"
        self.card_color = "white"
        self.primary_color = "#1F4E79"
        self.button_color = "#3498DB"
        self.register_color = "#2ECC71"

        self.window.configure(bg=self.bg_color)

        # Icon
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "assets", "icon.ico")

        try:
            self.window.iconbitmap(icon_path)
        except Exception:
            print("Icon could not be loaded.")

       
        # Main Center Container
       

        self.main_frame = tk.Frame(
            self.window,
            bg=self.bg_color
        )

        self.main_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

       
        # Login Card
       

        self.card_frame = tk.Frame(
            self.main_frame,
            bg=self.card_color,
            bd=2,
            relief="groove",
            padx=50,
            pady=40
        )
        self.card_frame.pack()

        
        # Title
        

        self.title_label = tk.Label(
            self.card_frame,
            text="Cyber Security ToolKit",
            font=("Arial", 24, "bold"),
            bg=self.card_color,
            fg=self.primary_color
        )
        self.title_label.pack(pady=(0, 10))

        # Subtitle
        self.subtitle_label = tk.Label(
            self.card_frame,
            text="Login to access your security tools",
            font=("Arial", 11),
            bg=self.card_color,
            fg="#555555"
        )
        self.subtitle_label.pack(pady=(0, 30))

        
        # Username
       

        self.username_label = tk.Label(
            self.card_frame,
            text="Username",
            font=("Arial", 12, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            anchor="w"
        )
        self.username_label.pack(
            fill="x",
            pady=(0, 5)
        )

        self.username_entry = tk.Entry(
            self.card_frame,
            width=35,
            font=("Arial", 13),
            relief="solid",
            bd=1
        )
        self.username_entry.pack(
            ipady=8,
            pady=(0, 20)
        )

        
        # Password
       

        self.password_label = tk.Label(
            self.card_frame,
            text="Password",
            font=("Arial", 12, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            anchor="w"
        )
        self.password_label.pack(
            fill="x",
            pady=(0, 5)
        )

        self.password_entry = tk.Entry(
            self.card_frame,
            width=35,
            font=("Arial", 13),
            show="*",
            relief="solid",
            bd=1
        )
        self.password_entry.pack(
            ipady=8,
            pady=(0, 25)
        )

       
        # Login Button
        

        self.login_button = tk.Button(
            self.card_frame,
            text="LOGIN",
            width=30,
            height=2,
            bg=self.button_color,
            fg="white",
            activebackground="#2980B9",
            activeforeground="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.login
        )
        self.login_button.pack(pady=(0, 25))

        
        # Register Text
        

        self.register_label = tk.Label(
            self.card_frame,
            text="Don't have an account?",
            font=("Arial", 10),
            bg=self.card_color,
            fg="#555555"
        )
        self.register_label.pack(pady=(0, 8))

       
        # Register Button
       

        self.register_button = tk.Button(
            self.card_frame,
            text="CREATE ACCOUNT",
            width=30,
            height=2,
            bg=self.register_color,
            fg="white",
            activebackground="#27AE60",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.open_register
        )
        self.register_button.pack()

        # Press Enter to Login
        self.window.bind(
            "<Return>",
            lambda event: self.login()
        )

        # Focus on Username Entry
        self.username_entry.focus()

        self.window.mainloop()


    
    # Login Function
   

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror(
                "Error",
                "Please enter username and password"
            )
            return

        user = login_user(username)

        if user is None:
            messagebox.showerror(
                "Error",
                "Username not found"
            )
            return

        stored_hash = user[3]

        if verify_hash(password, stored_hash):

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            self.window.destroy()
            DashboardWindow(user[0])

        else:
            messagebox.showerror(
                "Error",
                "Incorrect Password"
            )


    
    # Open Register Window
    

    def open_register(self):

        self.window.destroy()
        RegisterWindow()

