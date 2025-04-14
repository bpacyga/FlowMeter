from tkinter import *
from tkinter import ttk
import serial

#pip install pyserial requests if you dont have it  
import time		 #Thingspeak
import requests  #Thingspeak


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

# Need to make an HTTP request since we are sending from Python
# Student licenses allow a piece of data per second, might want to limit with an average per second from flowMeter.ino
#comm = serial.serial('COM5', 115200) # Confirm com port for laptop being used since we cant send from arduino
									 # Maybe suggest attached ESP32 or device change next semester for direct comms
#thingspeakKey = 0E4NVRSW981M90O9	 # General API key, can be regenerated on site 

#while True:							 #
#	try:
#		if com.in_waiting:		     #Checking Serial for data

#		flowrate = ser.readline().decode('utf-8').strip()
#        print(f"Flow Rate: {flowrate}")
		
#		url = 'https://api.thingspeak.com/update.json'
#		params = {
#			'api_key': thingspeakKey,
#			'field1': flowrate
#		}
		
#		response = requests.post(url, data=params) # System response for debugging 
#		print(response.text)


#Establish Thread for reading serial data

#Begin Displaying TKInter Window
root.mainloop()
