import tkinter as tk
from tkinter import messagebox

from modules.password_generator import PasswordGeneratorWindow
from modules.history import HistoryWindow
from modules.hash_generator import HashGeneratorWindow
from modules.ping_tool import PingToolWindow
from modules.network_info import NetworkInfoWindow
from modules.whois_lookup import WhoisLookupWindow
from modules.port_scanner import PortScannerWindow
from modules.file_checker import FileCheckerWindow
from modules.encryption import EncryptionWindow

class DashboardWindow:

    # Function to create a rounded rectangle
    def round_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):

        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]

        return canvas.create_polygon(
            points,
            smooth=True,
            **kwargs
        )

    def __init__(self, user_id):

        self.user_id = user_id

        # Create Window
        self.window = tk.Tk()
        self.window.title("Cyber Security ToolKit - Dashboard")

        # # Get screen size 

        # screen_width = self.window.winfo_screenwidth()
        # screen_height = self.window.winfo_screenheight()

        # # window size to 80% of screen

        # window_width = int(screen_width * 0.90)
        # window_height = int(screen_height * 0.90)
        # # calculate center position

        # x = (screen_width - window_width) // 2
        # y = (screen_height  - window_height) // 2

        # # set responsive window size
        # self.window.geometry(
        #     f"{window_width}x{window_height}+{x}+{y}"
        # ) 
        # #self.window.geometry("1200x800")
        self.window.state("zoomed")
        self.window.resizable(True, True)
        self.window.configure(bg="#EAF2F8")

        
        # Rounded Header
    

        self.header_canvas = tk.Canvas(
            self.window,
            width=500,
            height=90,
            bg="#EAF2F8",
            highlightthickness=0
        )
        self.header_canvas.pack(pady=20)

        self.round_rectangle(
            self.header_canvas,
            10, 10, 490, 80,
            radius=30,
            fill="#1F4E79",
            outline="#1F4E79"
        )

        self.header_canvas.create_text(
            250,
            45,
            text="Cyber Security Toolkit",
            font=("Arial", 22, "bold"),
            fill="white"
        )


        # Welcome Label
        

        self.welcome_label = tk.Label(
            self.window,
            text="Welcome To Dashboard",
            font=("Arial", 15, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.welcome_label.pack(pady=15)


        # Button Frame
    

        self.button_frame = tk.Frame(
            self.window,
            bg="#EAF2F8"
        )
        self.button_frame.pack(pady=20)

        # common button style
        button_style ={

            "width": 22,
            "height": 2,
            "font": ("Arial", 10, "bold"),
            "bg": "#3498DB",
            "fg": "white",
            "activebackground": "#2980B9",
            "activeforeground": "white",
            "relief": "flat",
            "cursor": "hand2"
        }

        # Password Generator
        self.password_button = tk.Button(
            self.button_frame,
            text="🔑  Password Generator",
            command= self.open_password_generator,
            **button_style
            
        )
        self.password_button.grid(row=0, column=0, padx=10, pady=10)

        # Hash Generator

        self.hash_button = tk.Button(
            self.button_frame,
            text="🔒   Hash Generator",
            command = self.open_hash_generator,
            **button_style
        )
        self.hash_button.grid(row=0, column=1, padx=10, pady=10)

        # ping tool

        self.ping_button = tk.Button(
             self.button_frame,
             text="📡  Ping Tool",
             command=self.open_ping_tool,
                **button_style
        )
        self.ping_button.grid(row=1, column=0, padx=10, pady=10)

        # port scanner

        self.port_button = tk.Button(
            self.button_frame,
            text="🔍  Port Scanner",
            command=self.open_port_scanner,
            **button_style
        )
        self.port_button.grid(row=1, column=1, padx=10, pady=10)

        # whois lookup

        self.whois_button = tk.Button(
            self.button_frame,
            text="🌐  WHOIS LookUP",
            command=self.open_whois_lookup,
            **button_style
        )
        self.whois_button.grid(row=2, column=0, padx=10, pady=10)

        # network info

        self.network_button = tk.Button(
            self.button_frame,
            text="💻   Network Info",
            command=self.open_network_info,
            **button_style
        )
        self.network_button.grid(row=2, column=1, padx=10, pady=10)

        # file checker button

        self.file_checker_button = tk.Button(
            self.button_frame,
            text="🛡️ File Checker",
            command=self.open_file_checker,
            **button_style
        )
        self.file_checker_button.grid(row=3, column=0, padx=10, pady=10)

        # encryption 

        # encryption button

        self.encryption_button = tk.Button(
            self.button_frame,
            text="🔐  Encryption",
            command=self.open_encryption,
            **button_style
        )
        self.encryption_button.grid(row=3, column=1, padx=10, pady=10)

        # history button

        self.history_button = tk.Button(
            self.button_frame,
            text="📜  History",
            command=self.open_history_window,
            **button_style
        )
        self.history_button.grid(row=4, column=0, padx=10, pady=10)

        # logout button
        self.logout_button = tk.Button(
            self.button_frame,
            text="🚪  Logout",
            command=self.logout,
            **button_style
            
        )
        self.logout_button.grid(row=5,column=0,columnspan=2, pady=25)

        self.window.mainloop()

    def open_password_generator(self):
        PasswordGeneratorWindow(self.user_id)

    def open_history_window(self):
        HistoryWindow(self.user_id)

    def open_network_info(self):
        NetworkInfoWindow(self.user_id)

    def open_hash_generator(self):
        HashGeneratorWindow(self.user_id)

    def open_ping_tool(self):
        PingToolWindow(self.user_id)

    def open_whois_lookup(self):
        WhoisLookupWindow(self.user_id)

    def open_port_scanner(self):
        PortScannerWindow(self.user_id)

    def open_file_checker(self):
        FileCheckerWindow(self.user_id)

    def open_encryption(self):
        EncryptionWindow(self.user_id)


    def logout(self):

        confirm = messagebox.askyesno(
        "Logout",
        "Are you sure you want to logout?"
        )

        if confirm:
            self.window.destroy()
            from login import LoginWindow
            LoginWindow()

   
        
