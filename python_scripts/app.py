from tkinter import *
from tkinter import ttk
import serial

#create_widgets(): Populates TKInter GUI
def create_widgets():
  ttk.Label(frame, text="Water Flow Sensor").grid(column=1, row=0)
  ttk.Label(frame, text="Flow Rate: ").grid(column=0, row=1)
  ttk.Label(frame, text="Total Volume: ").grid(column=1, row=1)
  ttk.Label(frame, text="Average Flow Rate: ").grid(column=2, row=1)
  ttk.Button(frame, text="Quit", command=lambda: shutdown_app(root)).grid(column=1, row=2)

#shutdown_app(): Handles shutdown of serial and database connection
def shutdown_app(root):
  print(type(root))
  root.after(0, root.destroy)

#initialize TKInter Window
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
create_widgets()

#Establish database connection

#Establish Thread for reading serial data

#Begin Displaying TKInter Window
root.mainloop()
