import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to handle login action 
def login_action():
    username = username_entry.get()
    password = password_entry.get()
    if username == "" or password == "":
        result_label.config(text="Please enter both username and password.", foreground="red")
    elif username != 'mmt' or password != '123':
        messagebox.showerror("Error","Please enter correct user name and password!")
    else:
        messagebox.showinfo("Welcome")
        win.destroy()
        import main_sys
# Function to handle the "Cancel" button click
def cancel_action():
    username_entry.delete(0, tk.END)  # Clear username entry
    password_entry.delete(0, tk.END)  # Clear password entry
    result_label.config(text="", foreground="black")  # Clear result message
 #end of function   

# Create the main window
win = tk.Tk()
win.geometry("400x250")
win.title('Login Form')
# Create a LabelFrame to contain the login form
login_frame = tk.Frame(win)
login_frame.grid(row=0, column=0, padx=20, pady=20)
# Creating a label for Username
username_label = ttk.Label(login_frame, text="Username")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
# Creating an entry for Username
username_entry = ttk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)
# Creating a label for Password
password_label = ttk.Label(login_frame, text="Password")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
# Creating an entry for Password
password_entry = ttk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
# Creating a result label to display messages
result_label = ttk.Label(login_frame, text="", foreground="black")
result_label.grid(row=2, columnspan=2, pady=10)
# Creating a login button
login_button = ttk.Button(login_frame, text="Login", command=login_action)
login_button.grid(row=3, column=0, padx=10, pady=20)
# Creating a "Cancel" button and bind it to cancel_action()
cancel_button = ttk.Button(login_frame, text="Reset/Clear", command=cancel_action)
cancel_button.grid(row=3, column=1, padx=10, pady=10)

# Start the Tkinter event loop
win.mainloop()


