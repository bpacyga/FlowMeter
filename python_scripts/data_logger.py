import serial
import threading as thr
import time

#read_data(): retrieves data from Ardiuno, updating variables
def read_data():
  new_data = {'flowrate': 0.0, 'total_vol': 0.0, 'avg_flowrate': 0.0}
  #read data in bytes
  #update dict with new values
  return new_data
  

#update_database(): connects to Thingspeak to update it with new data
def update_database(flowrate, tota_vol, avg_flowrate):
  #database implementation here

#Main Thread loop
def logger_loop():
  #open serial port
  t = thr.currentThread()

  while(getattr(t, "running", True)):
    new_data = read_data()
    update_database(new_data['flowrate'], new_data['total_vol'], new_data['avg_flowrate'])
    time.sleep(60)
