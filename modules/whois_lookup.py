import tkinter as tk
from tkinter import messagebox
import whois
from database import save_history

class WhoisLookupWindow:

    def __init__(self, user_id):

        self.user_id = user_id

        self.window = tk.Tk()
        self.window.title("WHOIS Lookup")
        self.window.geometry("900x650")
        self.window.resizable(False, False)
        self.window.configure(bg="#EAF2F8")


        self.title_label = tk.Label(
            self.window,
            text="🌐 WHOIS Lookup",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.title_label.pack(pady=20)

        self.domain_label = tk.Label(
            self.window,
            text="Enter Domain Name",
            font=("Arial", 12),
            bg="#EAF2F8"
        )
        self.domain_label.pack()

        self.domain_entry = tk.Entry(
            self.window,
            width=60,
            font=("Arial", 13)
        )
        self.domain_entry.pack(pady=10)

        # lookup button
        self.lookup_button = tk.Button(
            self.window,
            text="🔎 Lookup",
            width=20,
            height=2,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.lookup_domain
        )
        self.lookup_button.pack(pady=20)

        self.result_label = tk.Label(
            self.window,
            text="WHOIS Information",
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

    def lookup_domain(self):
        print("Lookup button clicked")
        domain = self.domain_entry.get().strip()
        print("Domain:", domain)
        if domain == "":
            messagebox.showerror(
            "Error",
            "Please enter a domain name."
            )
            return

        try:
            domain_info = whois.whois(domain)
            print("WHOIS DATA:", domain_info)
            result = (
                f"Domain Name     : {domain_info.domain_name}\n"
                f"Registrar       : {domain_info.registrar}\n"
                f"Creation Date   : {domain_info.creation_date}\n"
                f"Expiration Date : {domain_info.expiration_date}\n"
                f"Name Servers    : {domain_info.name_servers}\n"
            )

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)
            save_history(
                self.user_id,
                "WHOIS Lookup",
                result
            )

        except Exception as e:

            print("WHOIS ERROR:", e)

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(
            tk.END,
            f"WHOIS lookup failed.\n\n{e}"
            )