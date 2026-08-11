import tkinter as tk 

from tkinter import messagebox
import socket

from database import save_history


class PortScannerWindow:

    def __init__(self, user_id):

        self.user_id = user_id

        self.window = tk.Tk()
        self.window.title("Port Scanner")
        self.window.geometry("1200x800")
        self.window.resizable(False,False)
        self.window.configure(bg="#EAF2F8")

        self.title_label = tk.Label(
            self.window,
            text="🔍 Port Scanner",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.title_label.pack(pady=20)

        self.target_label = tk.Label(
            self.window,
            text="Enter IP Address or Domain",
            font=("Arial", 12),
            bg="#EAF2F8"
        )
        self.target_label.pack()

        self.target_entry = tk.Entry(
            self.window,
            width=60,
            font=("Arial", 13)
        )
        self.target_entry.pack(pady=10)

        self.port_label = tk.Label(
            self.window,
            text="Enter Port Range",
            font=("Arial", 12),
            bg="#EAF2F8"
        )
        self.port_label.pack()

        self.port_entry = tk.Entry(
            self.window,
            width=30,
            font=("Arial", 13),
            justify="center"
        )
        self.port_entry.insert(0, "1-100")
        self.port_entry.pack(pady=10)

        # scan button

        self.scan_button = tk.Button(
            self.window,
            text="🔍 Scan Ports",
            width=20,
            height=2,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.scan_ports
        )
        self.scan_button.pack(pady=20)

        # result box 

        self.result_label = tk.Label(
            self.window,
            text="Scan Result",
            font=("Arial", 12, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.result_label.pack(pady=10)

        self.result_text = tk.Text(
            self.window,
            width=100,
            height=20,
           font=("Consolas", 10)
        )
        self.result_text.pack(pady=10)

        #close button

        self.close_button = tk.Button(
            self.window,
            text="Close",
            width=18,
            height=2,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.window.destroy
        )
        self.close_button.pack(pady=10)


        self.window.mainloop()

    # Port scanning logig

    def scan_ports(self):

        target = self.target_entry.get().strip()


        if target =="":
            messagebox.showerror(
                "Error",
                "Please enter an IP address or domain"

            )
            return

        try:
            target_ip = socket.gethostbyname(target)

        except socket.gaierror:

            messagebox.showerror(
                "Error",
                "Invalid IP address or domain"
            )
            return

        #get port range

        port_range = self.port_entry.get().strip()

        try:
            start_port, end_port = map(
                int,
                port_range.split("-")
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter port range like 1-100."
            )
            return
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            messagebox.showerror(
                "Error",
                "Invalid port range"
            )
            return

        self.result_text.delete("1.0",tk.END)

        self.result_text.insert(
            tk.END,
            f"Target: {target}\n"
            f"IP Address: {target_ip}\n"
            f"Port Range: {start_port}-{end_port}\n\n"

        )

        open_ports = []

        for port in range(start_port,end_port + 1 ):
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.2)

            result = sock.connect_ex(
                (target_ip,port)
            )

            if result == 0:
                open_ports.append(port)

                self.result_text.insert(
                    tk.END,
                    f"port {port}: OPEN\n"
                )
            sock.close()

        self.result_text.insert(
            tk.END,
            "\nScan Completed.\n"
        ) 

        if open_ports:
            history_result = (
                f"Target: {target} | "
                f"Open Ports: {open_ports}"
            ) 
        else:
            history_result = (
                f"Target: {target} | "
                "No open ports found"
            ) 

        save_history(
            self.user_id,
            "Port Scanner",
            history_result
        )
            



    