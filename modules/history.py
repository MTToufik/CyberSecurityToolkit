import tkinter as tk
from tkinter import ttk
from database import get_history


class HistoryWindow:

    def __init__(self, user_id):

        self.user_id = user_id

        self.window = tk.Tk()
        self.window.title("History")
        self.window.state("zoomed")
        self.window.resizable(True, True)
        self.window.configure(bg="#EAF2F8")

        # Title

        self.title_label = tk.Label(
            self.window,
            text="📜 History",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.title_label.pack(pady=20)


        # create a frame for the treeview

        self.history_table = ttk.Treeview(
            self.window,
            columns=("Tool", "Result", "Date"),
            show="headings",
            height=15
        )

        self.history_table.heading("Tool", text="Tool Name")
        self.history_table.heading("Result", text="Result")
        self.history_table.heading("Date", text="Date & Time")

        self.history_table.column("Tool", width=180, anchor="center")
        self.history_table.column("Result", width=420, anchor="center")
        self.history_table.column("Date", width=220, anchor="center")

        self.history_table.pack(pady=20)

        history = get_history(self.user_id)
        print("User ID:", self.user_id)
        for row in history:
            self.history_table.insert("", "end", values=row)

        # close button

        self.close_button = tk.Button(
            self.window,
            text="Close",
            width=15,
            command=self.window.destroy,
            font=("Arial", 12,"bold"),
            bg="#E74C3C",
            fg="white",
            cursor="hand2",
            relief="flat",
        )
        self.close_button.pack(pady=15)

        self.window.mainloop()


if __name__ == "__main__":
    HistoryWindow(1)