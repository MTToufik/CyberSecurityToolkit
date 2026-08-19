import tkinter as tk
import socket
import platform
from database import save_history

class NetworkInfoWindow:

    def __init__(self,user_id):

        self.user_id = user_id

        self.window = tk.Tk()
        self.window.title("Network Information")
        self.window.state("zoomed")
        self.window.resizable(True, True)
        self.window.configure(bg="#EAF2F8")


        self.title_label = tk.Label(
            self.window,
            text="💻 Network Information",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.title_label.pack(pady=20)

        self.show_button = tk.Button(
            self.window,
            text="💻 Show Information",
            width=20,
            height=2,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.show_network_info
        )
        self.show_button.pack(pady=20)

        self.result_text = tk.Text(
            self.window,
            width=80,
            height=18,
            font=("Consolas", 11),
            state="disabled"
        )
        self.result_text.pack(pady=20)

        # Close button
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
    # get network information function

    def show_network_info(self):

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        operating_system = platform.system()
        os_version = platform.version()
        processor = platform.processor()

        information = (
            f"Host Name   :{hostname}\n"
            f"IP Address  : {ip_address}\n"
            f"Operating System   : {operating_system}\n"
            f"OS Version  : {os_version}\n"
            f"Processor   : {processor}"
        )

        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, information)
        self.result_text.config(state="disabled")

        save_history(
            self.user_id,
            "Network Info",
            information
        )


if __name__ == "__main__":

    NetworkinfoWindow()
    
        

      