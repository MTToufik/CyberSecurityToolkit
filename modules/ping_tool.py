import tkinter as tk
from tkinter import messagebox
import subprocess
from database import save_history

class PingToolWindow:

    def __init__(self, user_id):

        self.user_id = user_id

        # create window

        self.window = tk.Tk()
        self.window.title("Ping Tool")
        self.window.geometry("800x600")
        self.window.configure(bg="#EAF2F8")
        self.window.resizable(False, False)

        # title label

        self.title_label = tk.Label(
            self.window,
            text="📡 Ping Tool",
            font=("Arial",20,"bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.title_label.pack(pady=20)

        # target label

        self.target_label = tk.Label(
            self.window,
            text="Enter IP Address or Domain",
            font=("Arial",12),
            bg="#EAF2F8"
        )
        self.target_label.pack()

        # target entry

        self.target_entry = tk.Entry(
            self.window,
            width=50,
            font=("Arial",12)
        )
        self.target_entry.pack(pady=10)

        # ping button

        self.ping_button = tk.Button(
            self.window,
            text="📡 Ping",
            width=20,
            height=2,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.ping_host
        )
        self.ping_button.pack(pady=20)

        # result label

        self.result_label = tk.Label(
            self.window,
            text="Ping Result",
            font=("Arial", 12, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.result_label.pack(pady=10)

        #result text widgt

        self.result_text = tk.Text(
            self.window,
            width=80,
            height=15,
            font=("Consolas", 10)
        )
        self.result_text.pack(pady=10)

        self.window.mainloop()

    def ping_host(self):

        target = self.target_entry.get()

        if target == "":
            messagebox.showerror(
                "Error",
                "Please enter an ip address or domain"
            )
            return

        try:
            result = subprocess.check_output(
                ["ping", target],
                text = True
            )
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)

            # save short history
            history_result = f"Ping Success: {target}"

            save_history(
                self.user_id,
                "Ping Tool",
                history_result
            )

        except subprocess.CalledProcessError:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(
                tk.END,
                "Ping Failed, Please check the IP address or domain"
            )
            history_result = f"Ping Failed: {target}"

            save_history(
                self.user_id,
                "Ping Tool",
                history_result
            )
                
                                    

      

if __name__ == "__main__":
    PingToolWindow(1)
 



