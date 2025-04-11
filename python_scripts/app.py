from tkinter import *
from tkinter import ttk
import threading as thr
from data_logger import *

#create_widgets(): Populates TKInter GUI
def create_widgets(flowrate, total_vol, avg_flowrate):
  ttk.Label(frame, text = "Water Flow Sensor").grid(column=1, row=0)
  ttk.Label(frame, textvariable = flowrate).grid(column=0, row=1)
  ttk.Label(frame, textvariable = total_vol).grid(column=1, row=1)
  ttk.Label(frame, textvariable = avg_flowrate).grid(column=2, row=1)
  #new button here for refreshing data
  ttk.Button(frame, text="Quit", command=lambda: shutdown_app(root, t)).grid(column=1, row=2)

  flowrate.set("Flow Rate: N/A")
  total_vol.set("Total Volume: N/A")
  avg_flowrate.set("Average Flow Rate: N/A")

#refresh_data(): once lock is aquired, reads global vars to update text
def refresh_data():
  #use mutex lock, set the variables
  
  #update StringVars()

#shutdown_app(): Handles shutdown of serial and database connection
def shutdown_app(root, t):
  t.running = False
  t.join()
  root.after(0, root.destroy)

#initialize TKInter Window
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

flowrate = StringVar()
total_vol = StringVar()
avg_flowrate = StringVar()
create_widgets(flowrate, total_vol, avg_flowrate)

#Establish database connection

#Establish Thread for reading serial data
t = thr.Thread(target=logger_loop, args=())
t.start()

#Begin Displaying TKInter Window
root.mainloop()
