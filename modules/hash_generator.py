import hashlib
import tkinter as tk
from tkinter import messagebox
from database import save_history

# hash logic handle 

# for hash genarate fucntion

def generate_hash(text):

    text = text.encode("utf-8")

    hash_object = hashlib.sha256(text)

    return hash_object.hexdigest()



# if __name__ == "__main__":
#     password = "123456"

#     hashed_password = generate_hash(password)
#     print("original password", password)
#     print("Hasing password", hashed_password)

# function for hash verify

def verify_hash(text, stored_hash):
    

    # compare the hash with databash hash file
    new_hash = generate_hash(text)
    return new_hash == stored_hash


class HashGeneratorWindow:

    def __init__(self, user_id):

        self.user_id = user_id

        self.window = tk.Tk()
        self.window.title("Hash Generator")
        self.window.geometry("800x600")
        self.window.resizable(False, False)
        self.window.configure(bg="#EAF2F8")

        self.title_label = tk.Label(
            self.window,
            text="🔒 Hash Generator",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.title_label.pack(pady=20)

        # for text

        self.text_label = tk.Label(
            self.window,
            text="Enter Text",
            font=("Arial", 13),
            bg="#EAF2F8"
        )
        self.text_label.pack()

        # entry

        self.text_entry = tk.Entry(
            self.window,
            width=70,
            font=("Arial", 13),
            justify="left"
        )
        self.text_entry.pack(pady=10)

        # generate button

        self.generate_button = tk.Button(
            self.window,
            text="Generate Hash",
            width=20,
            height=2,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            command= self.generate_hash_button
        )
        self.generate_button.pack(pady=20)

        # Result Label

        self.result_label = tk.Label(
            self.window,
            text="Generated Hash",
            font=("Arial", 12, "bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.result_label.pack(pady=10)
        

        #result entry

        self.result_entry = tk.Entry(
            self.window,
            width=80,
            font=("Consolas", 11),
            justify="center"
        )
        self.result_entry.pack(pady=10)

        # copy button
        # Copy Button

        self.copy_button = tk.Button(
            self.window,
            text="📋 Copy Hash",
            width=18,
            height=2,
            bg="#2ECC71",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.copy_hash
        )
        self.copy_button.pack(pady=15)
         # hash verify
         
        self.verify_label = tk.Label(
            self.window,
            text="Enter Hash TO verify",
            font=("Arial",12,"bold"),
            bg="#EAF2F8",
            fg="#1F4E79"
        )
        self.verify_label.pack(pady=10)
        
         # entry
        
        self.verify_entry = tk.Entry(
            self.window,
            width=80,
            font=("Consolas", 11),
            justify="center"
        )
        self.verify_entry.pack(pady=10)

        # verify buttoon

        self.verify_button = tk.Button(
            self.window,
            text="✅ Verify Hash",
            width=18,
            height=2,
            bg="#F39C12",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.verify_hash_button
        )
        self.verify_button.pack(pady=10)

       

        

        self.window.mainloop()

    # generate hash button

    def generate_hash_button(self):
        text = self.text_entry.get()

        if text == "":
            messagebox.showerror(
                "Error",
                "Please enter some text."
            )   
            return 
        hashed_text = generate_hash(text)

        self.result_entry.delete(0,tk.END)
        self.result_entry.insert(0,hashed_text)

        # save history

        save_history(
            self.user_id,
            "Hash Generator",
            hashed_text
        )

    def copy_hash(self):
       

       hash_value = self.result_entry.get()

       if hash_value == "":
        messagebox.showwarning(
            "Warning",
            "No hash to copy."
        )
        return

       self.window.clipboard_clear()
       self.window.clipboard_append(hash_value)
       self.window.update()

       messagebox.showinfo(
           "Success",
           "Hash copied to clipboard"
       )


    def verify_hash_button(self):

        text = self.text_entry.get()
        stored_hash = self.verify_entry.get()

        if text == "" or stored_hash == "":
           messagebox.showerror(
            "Error",
            "Please enter both text and hash."
           )
           return

        if verify_hash(text, stored_hash):
            messagebox.showinfo(
            "Success",
            "✅ Hash Matched!"
           )
        else:
           messagebox.showerror(
            "Failed",
            "❌ Hash Does Not Match!"
           )

      


if __name__ == "__main__":
    HashGeneratorWindow(1)