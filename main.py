import tkinter as tk
from tkinter import messagebox
import sqlite3

class LoginApp:

    def __init__(self):
        # Initialize the main window
        self.login_window = tk.Tk()
        self.login_window.title('Login Application')

        # Username label and entry
        tk.Label(self.login_window, text='Username').pack()
        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.pack()

        # Password label and entry
        tk.Label(self.login_window, text='Password').pack()
        self.password_entry = tk.Entry(self.login_window, show='*')
        self.password_entry.pack()

        # Login button
        self.login_button = tk.Button(self.login_window, text='Login', command=self.login)
        self.login_button.pack()

        # Run the main loop
        self.login_window.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Connect to the SQLite database
        conn = sqlite3.connect('user_db.db')
        cursor = conn.cursor()

        # Check if the username and password are correct
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login Success", f"Welcome, {user[2]}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

        # Close the database connection
        conn.close()

# Create an instance of the LoginApp
if __name__ == "__main__":
    app = LoginApp()
