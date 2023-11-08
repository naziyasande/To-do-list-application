from tkinter import *
from tkinter import messagebox 
import sqlite3 as sql
from datetime import datetime
import login

def add_task():
    # Check if the user is logged in
    if not login.logged_in:
        messagebox.showinfo('Login Required', 'Please log in first.')
        return

    task_string = task_field.get()
    task_date = date_field.get()
    task_time = time_field.get()

    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Task Field is Empty.')
    else:
        task_with_datetime = f'{task_string} - Date: {task_date}, Time: {task_time}'
        tasks.append(task_with_datetime)

        try:
            the_cursor.execute('INSERT INTO tasks (title, date, time) VALUES (?, ?, ?)', (task_string, task_date, task_time))
            connection.commit()  # Commit changes to the database
        except sqlite3.Error as e:
            print("SQLite error:", e)

        list_update()
        task_field.delete(0, 'end')
        date_field.delete(0, 'end')
        time_field.delete(0, 'end')
def list_update():
    clear_list()

    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:  
        the_value = task_listbox.get(task_listbox.curselection())  
        if the_value in tasks:
            tasks.remove(the_value)  
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (the_value.split(' - ')[0],))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box:
        while(len(tasks) != 0):  
            tasks.pop()  
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    the_connection.commit()
    the_cursor.close()
    guiWindow.destroy()

def retrieve_database():
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in the_cursor.execute('select title, date, time from tasks'):  
        tasks.append(f'{row[0]} - Date: {row[1]}, Time: {row[2]}')

guiWindow = Tk()
guiWindow.title("To-Do List")
guiWindow.geometry("670x400+550+250")
guiWindow.resizable(0, 0)
guiWindow.configure(bg="#B5E5CF")

the_connection = sql.connect('listOfTasks.db')
the_cursor = the_connection.cursor()
the_cursor.execute('create table if not exists tasks (title text, date text, time text)')

tasks = []

functions_frame = Frame(guiWindow, bg="pink")
functions_frame.pack(side="top", expand=True, fill="both")

task_label = Label(functions_frame, text="Enter the Task:", font=("arial", "14", "bold"), background="dark green", foreground="white")
task_label.place(x=20, y=20)

task_field = Entry(functions_frame, font=("Arial", "14"), width=42, foreground="black", background="white")
task_field.place(x=180, y=20)

add_button = Button(functions_frame, text="Add Task", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=add_task)
del_button = Button(functions_frame, text="Delete Task", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=delete_task)
del_all_button = Button(functions_frame, text="Delete All Tasks", width=15, font=("arial", "14", "bold"), bg='#D4AC0D', command=delete_all_tasks)
exit_button = Button(functions_frame, text="Exit", width=52, bg='#D4AC0D', font=("arial", "14", "bold"), command=close)

add_button.place(x=20, y=90)
del_button.place(x=240, y=90)
del_all_button.place(x=460, y=90)
exit_button.place(x=20, y=330)

date_label = Label(functions_frame, text="Enter the Date:", font=("arial", "14", "bold"), background="dark green", foreground="white")
date_label.place(x=20, y=55)
date_field = Entry(functions_frame, font=("Arial", "14"), width=12, foreground="black", background="white")
date_field.place(x=180, y=55)

time_label = Label(functions_frame, text="Enter the Time:", font=("arial", "14", "bold"), background="dark green", foreground="white")
time_label.place(x=350, y=55)
time_field = Entry(functions_frame, font=("Arial", "14"), width=10, foreground="black", background="white")
time_field.place(x=510, y=55)

task_listbox = Listbox(functions_frame, width=57, height=7, font="bold", selectmode='SINGLE', background="WHITE", foreground="BLACK", selectbackground="#D4AC0D", selectforeground="BLACK")
task_listbox.place(x=17, y=140)

retrieve_database()
list_update()

if __name__ == "__main__":
    login.logged_in = False  # Initialize the login status

guiWindow.mainloop()
the_connection.commit()
the_cursor.close()
