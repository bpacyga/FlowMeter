import serial
import threading as thr
import time

#read_data(): retrieves data from Ardiuno, updating variables
def read_data():
  new_data = {'flowrate': 0.0, 'total_vol': 0.0, 'avg_flowrate': 0.0}
  
  #read data in bytes
  
  #update dict with new values - test code below
  new_data['flowrate'] = 0.52
  new_data['total_vol'] = 5.1
  new_data['avg_flowrate'] = 0.96
  
  return new_data

#update_globals(): once lock is aquired, allows other thread to receive new data
def update_globals(flowrate, total_vol, avg_flowrate):
  #use mutex lock, set the variables

#update_database(): connects to Thingspeak to update it with new data
def update_database(flowrate, total_vol, avg_flowrate):
  #database implementation here - below is test code
  print(f"{flowrate} {total_vol} {avg_flowrate}")

#Main Thread loop
def logger_loop():
  #open serial port
  t = thr.currentThread()

  while(getattr(t, "running", True)):
    new_data = read_data()
    update_globals(new_data['flowrate'], new_data['total_vol'], new_data['avg_flowrate'])
    update_database(new_data['flowrate'], new_data['total_vol'], new_data['avg_flowrate'])
    time.sleep(3) #change sleep seconds as needed

  #close serial port
