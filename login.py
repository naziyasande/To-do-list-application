from tkinter import *

logged_in = False  # Initialize the login status as False

def is_logged_in():
    return logged_in


def login():
    # Check the username and password
    username = username_entry.get()
    password = password_entry.get()

    if username == "username" and password == "password":
        login.logged_in = True
        # Successful login, open the to-do list application
        root.destroy()
        import todo_list  # Import your to-do list application script
    else:
        # Show an error message for invalid login
        error_label.config(text="Invalid login credentials")

root = Tk()

root.title("To-Do List Login")
root.geometry("400x200+450+250")  # Adjust the size and position as needed
root.configure(bg="pink")  # Set background color to pink

# Create a frame to hold your widgets
frame = Frame(root, bg="pink")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Label for "Username"
username_label = Label(frame, text="Username:", font=("arial", 14, "bold"), bg="pink", fg="white",background="dark green")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Entry field for "Username"
username_entry = Entry(frame, font=("Arial", 14), width=12)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Label for "Password"
password_label = Label(frame, text="Password:", font=("arial", 14, "bold"), bg="pink", fg="white",background="dark green")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

# Entry field for "Password"
password_entry = Entry(frame, show="*", font=("Arial", 14), width=12)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login Button
login_button = Button(frame, text="Login", width=15, command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=20)

# Error Label
error_label = Label(frame, text="", fg="red", bg="pink")
error_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
