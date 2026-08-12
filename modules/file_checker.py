import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib

from database import save_history


class FileCheckerWindow:

    def __init__(self, user_id):

        self.user_id = user_id

        self.window = tk.Tk()
        self.window.title("File Checker")
        self.window.geometry("900x700")
        self.window.resizable(False, False)
        self.window.configure(bg="#EAF2F8")

        # Title
        self.title_label = tk.Label(
            self.window,
            text="🛡️ File Checker",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.title_label.pack(pady=20)

        # File path label
        self.file_label = tk.Label(
            self.window,
            text="Select a file to generate its SHA-256 hash",
            font=("Arial", 12),
            bg="#EAF2F8"
        )
        self.file_label.pack(pady=10)

        # File path entry
        self.file_entry = tk.Entry(
            self.window,
            width=80,
            font=("Arial", 11)
        )
        self.file_entry.pack(pady=10)

        # Browse button
        self.browse_button = tk.Button(
            self.window,
            text="📁 Browse File",
            width=18,
            height=2,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.browse_file
        )
        self.browse_button.pack(pady=10)

        # Check button
        self.check_button = tk.Button(
            self.window,
            text="🔍 Check File",
            width=18,
            height=2,
            bg="#2ECC71",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.check_file
        )
        self.check_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(
            self.window,
            text="File Information",
            font=("Arial", 12, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.result_label.pack(pady=10)

        # Result box
        self.result_text = tk.Text(
            self.window,
            width=100,
            height=15,
            font=("Consolas", 10)
        )
        self.result_text.pack(pady=10)

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

    def browse_file(self):

        file_path = filedialog.askopenfilename()

        if file_path == "":
            return

        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def check_file(self):

        file_path = self.file_entry.get().strip()

        if file_path == "":
            messagebox.showerror(
                "Error",
                "Please select a file."
            )
            return

        try:

            sha256_hash = hashlib.sha256()

            with open(file_path, "rb") as file:

                while True:

                    data = file.read(4096)

                    if not data:
                        break

                    sha256_hash.update(data)

            file_hash = sha256_hash.hexdigest()

            result = (
                f"File Path : {file_path}\n\n"
                f"SHA-256 Hash :\n"
                f"{file_hash}\n"
            )

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)

            history_result = (
                f"File: {file_path} | "
                f"SHA-256: {file_hash}"
            )

            save_history(
                self.user_id,
                "File Checker",
                history_result
            )

        except FileNotFoundError:

            messagebox.showerror(
                "Error",
                "File not found."
            )

        except PermissionError:

            messagebox.showerror(
                "Error",
                "Permission denied."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to check file.\n\n{e}"
            )


if __name__ == "__main__":
    FileCheckerWindow(1)