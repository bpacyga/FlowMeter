import serial
import threading as thr
import time
import global_vars

#read_data(): retrieves data from Ardiuno, updating variables
def read_data():
  new_data = {'flowrate': 0.0, 'total_vol': 0.0, 'avg_flowrate': 0.0, 'null_input': False}
  
  #read data in bytes
  flowRate = str(arduino.readline().decode("utf-8")).rstrip()
  if (flowRate == null or ''):
    new_data['null_input'] = True
    new_data['flowrate'] = 0
    new_data['total_vol'] = 0
    new_data['avg_flowrate'] = 0
  else:
    total_vol = str(arduino.readline().decode("utf-8")).rstrip()
    time = str(arduino.readline().decode("utf-8")).rstrip()
    total_flow = str(arduino.readline().decode("utf-8")).rstrip()
    #update dict with new values - test code below
    new_data['flowrate'] = float(flowRate)
    new_data['total_vol'] = long(total_vol)
    new_data['avg_flowrate'] = total_flow/time
  
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
    if(new_data['null_input'] == False):
      update_globals(g_lock, new_data['flowrate'], new_data['total_vol'], new_data['avg_flowrate'])
      update_database(new_data['flowrate'], new_data['total_vol'], new_data['avg_flowrate'])
    time.sleep(1) #change sleep seconds as needed

  #close serial port
  arduino.close()
