#Author: Roel-Junior Alejo Viernes 

from icalendar import *
from datetime import *
from tkinter import *

#GUI
root = Tk()
root.title("SA Event Maker")
root.geometry("500x500")

#Variables
shift_name = StringVar()
campus = StringVar()
event_description = StringVar()
event_start_date = StringVar()
event_start_time = StringVar()
event_end_date = StringVar()
event_end_time = StringVar()
event_organizer = StringVar()
event_organizer_email = StringVar()
