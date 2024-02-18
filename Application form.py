import tkinter
from tkinter import ttk


def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        #User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nation_combobox.get()

        # Course info
        registration_status = reg_status_var.get()
        numcourses = numcourses_spinbox.get()

        
        print("First name: ", firstname, "Last name: ", lastname)
        print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
        print("#Courses: ", numcourses)
        print("Registration status: ", registration_status)
        print("----------------------------------------------")
    else:
        print("Error")

window = tkinter.Tk()
window.title("Application Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr", "Ms", "Dr"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=3)

age_label =tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to= 110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nation_label = tkinter.Label(user_info_frame, text="Nationality")
nation_combobox = ttk.Combobox(user_info_frame, values= ["Pakistan", "India", "Kenya", "Britain", "America", "China"])
nation_label.grid(row=2, column=1)
nation_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving course info
course_frame = tkinter.Label(frame)
course_frame.grid(row=1, column=0, sticky='new', padx=20, pady=10)

register_label =tkinter.Label(course_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value= "Not Registered")
register_check = tkinter.Checkbutton(course_frame, text="Currently Registered",
                                     variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
register_label.grid(row=0, column=0)
register_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(course_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(course_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept term
terms_frame =tkinter.LabelFrame(frame, text= "Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

accept_var = tkinter.StringVar(value= "Not Accepted")

term_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions",
                                 variable= accept_var, onvalue="Accepted", offvalue="Not Accepted")
term_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text= "Enter Data", command= enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=20)

window.mainloop()