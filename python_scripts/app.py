from tkinter import *
from tkinter import ttk
import serial

#initialize TKInter Window
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
create_widgets()

#Establish database connection

#Establish Thread for reading serial data

#Begin Displaying TKInter Window
root.mainloop()

#create_widgets(): Populates TKInter GUI
create_widgets():
  ttk.Label(frm, text="Water Flow Sensor").grid(column=1, row=0)
  ttk.Label(frame, text="Flow Rate: ").grid(column=0, row=1)
  ttk.Label(frame, text="Total Volume: ").grid(column=1, row=1)
  ttk.Label(frame, text="Average Flow Rate: ").grid(column=2, row=1)
  ttk.Button(frame, text="Quit", command=exit(root)).grid(column=1, row=0)

#exit(): Handles shutdown of serial and database connection
def exit(root):
  root.destroy
