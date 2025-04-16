import serial
import threading as thr
import time
import global_vars

#read_data(): retrieves data from Ardiuno, updating variables
def read_data():
  new_data = {'flowrate': 0.0, 'total_vol': 0.0, 'avg_flowrate': 0.0}
  
  #read data in bytes
  flowRate = arduino.readline().decode("utf-8")
  if (flowRate == null):
    
  #update dict with new values - test code below
  new_data['flowrate'] = flowRate
  new_data['total_vol'] = 5.1
  new_data['avg_flowrate'] = 0.96
  
  return new_data

#update_globals(): once lock is aquired, allows other thread to receive new data
def update_globals(g_lock, flowrate, total_vol, avg_flowrate):
  with g_lock:
    global_vars.g_flowrate = flowrate
    global_vars.g_total_vol = total_vol
    global_vars.g_avg_flowrate = avg_flowrate

#update_database(): connects to Thingspeak to update it with new data
def update_database(flowrate, total_vol, avg_flowrate):
  #database implementation here - below is test code
  print(f"{flowrate} {total_vol} {avg_flowrate}")

#Main Thread loop
def logger_loop(g_lock):
  #open serial port
  t = thr.currentThread()
  
  #connect to the arduino on COM5
  arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

  while(getattr(t, "running", True)):
    new_data = read_data()
    update_globals(g_lock, new_data['flowrate'], new_data['total_vol'], new_data['avg_flowrate'])
    update_database(new_data['flowrate'], new_data['total_vol'], new_data['avg_flowrate'])
    time.sleep(1) #change sleep seconds as needed

  #close serial port
  arduino.close()
