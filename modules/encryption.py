import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

from database import save_history


class EncryptionWindow:

    def __init__(self, user_id):

        self.user_id = user_id

        self.window = tk.Tk()
        self.window.title("Encryption Tool")
        self.window.state("zoomed")
        self.window.resizable(True, True)
        self.window.configure(bg="#EAF2F8")

        # Title
        self.title_label = tk.Label(
            self.window,
            text="🔐 Encryption Tool",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.title_label.pack(pady=20)

        # Text label
        self.text_label = tk.Label(
            self.window,
            text="Enter Text",
            font=("Arial", 12, "bold"),
            bg="#EAF2F8"
        )
        self.text_label.pack()

        # Text input
        self.text_entry = tk.Entry(
            self.window,
            width=80,
            font=("Arial", 12)
        )
        self.text_entry.pack(pady=10)

        # Generate key
        self.key_button = tk.Button(
            self.window,
            text="🔑 Generate Key",
            width=20,
            height=2,
            bg="#9B59B6",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.generate_key
        )
        self.key_button.pack(pady=10)

        # Key label
        self.key_label = tk.Label(
            self.window,
            text="Encryption Key",
            font=("Arial", 12, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.key_label.pack(pady=10)

        self.key_entry = tk.Entry(
            self.window,
            width=80,
            font=("Consolas", 10)
        )
        self.key_entry.pack(pady=10)

        # Encrypt button
        self.encrypt_button = tk.Button(
            self.window,
            text="🔒 Encrypt",
            width=18,
            height=2,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.encrypt_text
        )
        self.encrypt_button.pack(pady=10)

        # Decrypt button
        self.decrypt_button = tk.Button(
            self.window,
            text="🔓 Decrypt",
            width=18,
            height=2,
            bg="#2ECC71",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.decrypt_text
        )
        self.decrypt_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(
            self.window,
            text="Result",
            font=("Arial", 12, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.result_label.pack(pady=10)

        self.result_entry = tk.Entry(
            self.window,
            width=80,
            font=("Consolas", 10)
        )
        self.result_entry.pack(pady=10)

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

    def generate_key(self):

        key = Fernet.generate_key()

        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key.decode())

    def encrypt_text(self):

        text = self.text_entry.get().strip()
        key = self.key_entry.get().strip()

        if text == "":
            messagebox.showerror(
                "Error",
                "Please enter text."
            )
            return

        if key == "":
            messagebox.showerror(
                "Error",
                "Please generate or enter an encryption key."
            )
            return

        try:

            fernet = Fernet(key.encode())

            encrypted = fernet.encrypt(
                text.encode()
            ).decode()

            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, encrypted)

            save_history(
                self.user_id,
                "Encryption",
                f"Text encrypted successfully"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Encryption failed.\n\n{e}"
            )

    def decrypt_text(self):

        encrypted_text = self.result_entry.get().strip()
        key = self.key_entry.get().strip()

        if encrypted_text == "":
            messagebox.showerror(
                "Error",
                "No encrypted text found."
            )
            return

        if key == "":
            messagebox.showerror(
                "Error",
                "Please enter the encryption key."
            )
            return

        try:

            fernet = Fernet(key.encode())

            decrypted = fernet.decrypt(
                encrypted_text.encode()
            ).decode()

            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, decrypted)

            save_history(
                self.user_id,
                "Encryption",
                "Text decrypted successfully"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                "Invalid key or encrypted text."
            )


if __name__ == "__main__":
    EncryptionWindow(1)