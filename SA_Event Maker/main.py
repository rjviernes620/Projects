#Author: Roel-Junior Alejo Viernes 

from icalendar import *
from datetime import *
from tkinter import *

#GUI
root = Tk()

event_details = {}

root.title("SA Event Maker")
root.geometry("500x500")

logo = PhotoImage(file="MASTER LOGO_2022 K-01.png")
logo_label = Label(root, image=logo)
logo_label.grid(row=0, column=0, columnspan=2)

welcome = Label(root, text="Welcome to the SA Event Maker")
welcome.grid()

event_name = Entry(root, width=30)
event_name.grid(row=0, column=1, padx=20)

event_name_label = Label(root, text="Event Name")
event_name_label.grid(row=0, column=0)

event_date = Entry(root, width=30)
event_date.grid(row=1, column=1, padx=20)

event_date_label = Label(root, text="Event Date")
event_date_label.grid(row=1, column=0)

event_time = Entry(root, width=30)
event_time.grid(row=2, column=1, padx=20)

event_time_label = Label(root, text="Event Time")
event_time_label.grid(row=2, column=0)

campus = Label(root, text="Choose from one of the following sites")
campus.grid(row=3, column=0)
campus_options = ["Greenwich", "Avery Hill", "Medway", "Bathway", "External Location"]

campus_var = StringVar(root)
campus_var.set(campus_options[0])

campus_menu = OptionMenu(root, campus_var, *campus_options)
campus_menu.grid(row=3, column=1)


def text_to_dict():
    acknowledgment = Label(root, text="Please wait while the ics file is produced")
    acknowledgment.grid(row=2, column=1, pady=10)
    event_details["event_name"] = event_name.get()
    done = Label(root, text="Done!")
    done.grid(row=3, column=1, pady=10)


done_button = Button(root, text="Done", fg = "blue", command=text_to_dict)
done_button.grid(row=1, column=1, pady=10)
root.mainloop()