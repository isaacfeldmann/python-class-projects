from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('mercyhurst.db')   # creates/connects to database
cursor = conn.cursor()

#  creating a table within the database
cursor.execute('CREATE TABLE IF NOT EXISTS student_info (fname TEXT, lname TEXT, '
               'email TEXT, dob TEXT, cyber TEXT, ds TEXT, gender TEXT)')

window = Tk()  # creating a window for GUI

window.title('student form')
window.geometry('500x400')
#window.resizable('False', 'True')

frame = Frame(window)
frame.pack()

#  font values
label_font = ('Times', 14, 'bold')

entry_font = ('Times', 14, 'normal')

#  first name entry box
fname = Label(frame, text='First name:', font=label_font)
fname.grid(row=0, column=0)
fname_entry = Entry(frame, bd=2, font=entry_font)
fname_entry.grid(row=0, column=1)

#  last name entry box
lname = Label(frame, text='Last name:', font=label_font)
lname.grid(row=1, column=0)
lname_entry = Entry(frame, bd=2, font=entry_font)
lname_entry.grid(row=1, column=1)

#  email entry box
email_label = Label(frame, text='Email:', font=label_font)
email_label.grid(row=2, column=0)
email_entry = Entry(frame, bd=2, font=entry_font)
email_entry.grid(row=2, column=1)

#  birthday entry box
dob_label = Label(frame, text='Date of birth:', font=label_font)
dob_label.grid(row=3, column=0)
dob_entry = Entry(frame, bd=2, font=entry_font)
dob_entry.grid(row=3, column=1)

major_label = Label(frame, text='Major:', font=label_font)
major_label.grid(row=5, column=0)

#  major/minor checkboxes
cyber_var = IntVar()
dataScience_var = IntVar()

check_cyber = Checkbutton(frame, text='Cyber', variable=cyber_var, onvalue=1, offvalue=0)
check_cyber.grid(row=5, column=1)
check_ds = Checkbutton(frame, text='Data science', variable=dataScience_var, onvalue=1, offvalue=0)
check_ds.grid(row=5, column=2)

#  gender selection buttons
gender_label = Label(frame, text='Gender:', font=label_font)
gender_label.grid(row=6, column=0)
gender_var = IntVar()
gender_male = Radiobutton(frame, text='Male', variable=gender_var, value=1, font=label_font)
gender_male.grid(row=6, column=1)
gender_female = Radiobutton(frame, text='Female', variable=gender_var, value=2, font=label_font)
gender_female.grid(row=6, column=2)

#  entering the data into database


def submit_data():
    #  print('back end logic goes here')
    first_name = fname_entry.get()
    if not first_name.isalpha():
        print('invalid first name')
        messagebox.showerror('Invalid first name', 'Do not use characters or numbers in first name')
        return
    last_name = lname_entry.get()
    if not last_name.isalpha():
        print('invalid last name')
        messagebox.showerror('Invalid last name', 'Do not use characters or numbers in last name')
        return
    email = email_entry.get()
    dob = dob_entry.get()
    iscyber = cyber_var.get()
    isds = dataScience_var.get()
    gender = gender_var.get()

    insert_command = (f"INSERT INTO student_info VALUES ('{first_name}', '{last_name}', '{email}', '{dob}', "
                      f"'{iscyber}', '{isds}', '{gender}')")
    cursor.execute(insert_command)
    conn.commit()
    messagebox.showinfo('Success', f' Congratulations {first_name}! Your data has been submitted to the database')


def view_records():
    print('show records')
    records_window = Toplevel()
    conn = sqlite3.connect('mercyhurst.db')  # creates/connects to database
    cursor = conn.cursor()
    treev = ttk.Treeview(records_window, columns=('fname', 'lname', 'email', 'dob', 'iscyber', 'isds', 'gender'))
    treev.column('0', width=80)
    treev.column('1', width=125)
    treev.column('2', width=175)
    treev.column('3', width=80)
    treev.column('4', width=50)
    treev.column('5', width=80)
    treev.column('6', width=70)

    cursor.execute('SELECT * FROM student_info')
    rows = cursor.fetchall()
    for item in rows:
        print(item)
    treev.heading('#1', text='First Name')
    treev.heading('#2', text='Last Name')
    treev.heading('#3', text='Email')
    treev.heading('#4', text='Date of Birth')
    treev.heading('#5', text='Cyber')
    treev.heading('#6', text='Data Science')
    treev.heading('#7', text='Gender')

    for row in rows:
        treev.insert(parent='', index='end', values=row)

    treev.pack()

#  submit button
submit_button = Button(frame, text='Submit', font=label_font, command=submit_data)
submit_button.grid(row=7, columnspan=4)

records_button = Button(frame, text='View Records', font=label_font, command=view_records)
records_button.grid(row=8, columnspan=4)
window.mainloop()  # keep this line at the end
