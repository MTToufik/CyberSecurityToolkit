
import tkinter as tk
from tkinter import messagebox

from database import insert_user
from modules.hash_generator import generate_hash


class RegisterWindow:

    def __init__(self):

        
        # Main Window
        

        self.window = tk.Tk()
        self.window.title("Cyber Security ToolKit - Register")
        self.window.state("zoomed")
        self.window.resizable(True, True)

       
        # Colors
       

        self.bg_color = "#EAF2F8"
        self.card_color = "white"
        self.primary_color = "#1F4E79"
        self.button_color = "#2ECC71"
        self.login_color = "#3498DB"

        self.window.configure(bg=self.bg_color)

        
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

       
        # Register Card
       

        self.card_frame = tk.Frame(
            self.main_frame,
            bg=self.card_color,
            bd=2,
            relief="groove",
            padx=50,
            pady=30
        )
        self.card_frame.pack()

        
        # Title
       

        self.title_label = tk.Label(
            self.card_frame,
            text="Create New Account",
            font=("Arial", 24, "bold"),
            bg=self.card_color,
            fg=self.primary_color
        )
        self.title_label.pack(pady=(0, 8))

        self.subtitle_label = tk.Label(
            self.card_frame,
            text="Create an account to access the Cyber Security Toolkit",
            font=("Arial", 11),
            bg=self.card_color,
            fg="#555555"
        )
        self.subtitle_label.pack(pady=(0, 25))

        
        # Username
        

        self.username_label = tk.Label(
            self.card_frame,
            text="Username",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            anchor="w"
        )
        self.username_label.pack(fill="x", pady=(0, 5))

        self.username_entry = tk.Entry(
            self.card_frame,
            width=38,
            font=("Arial", 12),
            relief="solid",
            bd=1
        )
        self.username_entry.pack(ipady=7, pady=(0, 12))

        
        # Email
       

        self.email_label = tk.Label(
            self.card_frame,
            text="Email",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            anchor="w"
        )
        self.email_label.pack(fill="x", pady=(0, 5))

        self.email_entry = tk.Entry(
            self.card_frame,
            width=38,
            font=("Arial", 12),
            relief="solid",
            bd=1
        )
        self.email_entry.pack(ipady=7, pady=(0, 12))

       
        # Password
        

        self.password_label = tk.Label(
            self.card_frame,
            text="Password",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            anchor="w"
        )
        self.password_label.pack(fill="x", pady=(0, 5))

        self.password_entry = tk.Entry(
            self.card_frame,
            width=38,
            font=("Arial", 12),
            show="*",
            relief="solid",
            bd=1
        )
        self.password_entry.pack(ipady=7, pady=(0, 12))

        
        # Confirm Password
       

        self.confirm_label = tk.Label(
            self.card_frame,
            text="Confirm Password",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            anchor="w"
        )
        self.confirm_label.pack(fill="x", pady=(0, 5))

        self.confirm_entry = tk.Entry(
            self.card_frame,
            width=38,
            font=("Arial", 12),
            show="*",
            relief="solid",
            bd=1
        )
        self.confirm_entry.pack(ipady=7, pady=(0, 20))

      
        # Create Account Button
     

        self.register_button = tk.Button(
            self.card_frame,
            text="CREATE ACCOUNT",
            width=32,
            height=2,
            bg=self.button_color,
            fg="white",
            activebackground="#27AE60",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.register_user
        )
        self.register_button.pack(pady=(0, 20))

        
        # Login Text
       

        self.login_label = tk.Label(
            self.card_frame,
            text="Already have an account?",
            font=("Arial", 10),
            bg=self.card_color,
            fg="#555555"
        )
        self.login_label.pack(pady=(0, 8))


        # Login Button
        

        self.login_button = tk.Button(
            self.card_frame,
            text="LOGIN",
            width=32,
            height=2,
            bg=self.login_color,
            fg="white",
            activebackground="#2980B9",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.open_login
        )
        self.login_button.pack()

        # Press Enter to Register
        self.window.bind(
            "<Return>",
            lambda event: self.register_user()
        )

        # Focus on Username
        self.username_entry.focus()

        self.window.mainloop()


   
    # Register User Function
   

    def register_user(self):

        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()

        # Empty field validation
        if not username or not email or not password or not confirm_password:
            messagebox.showerror(
                "Error",
                "All fields are required."
            )
            return

        # Password matching validation
        if password != confirm_password:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        # Generate password hash
        hashed_password = generate_hash(password)

        # Save user to database
        success = insert_user(
            username,
            email,
            hashed_password
        )

        if success:

            messagebox.showinfo(
                "Success",
                "Registration completed successfully!"
            )

            # Clear fields after successful registration
            self.username_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.confirm_entry.delete(0, tk.END)

        else:

            messagebox.showerror(
                "Error",
                "Username or email already exists."
            )


   
    # Open Login Window
    

    def open_login(self):

        from login import LoginWindow

        self.window.destroy()
        LoginWindow()


if __name__ == "__main__":
    RegisterWindow()

