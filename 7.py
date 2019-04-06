import serial
import serial.tools.list_ports
import time

ser=serial.Serial(port='COM3')
time.sleep(2)
ser.write("1".encode())
time.sleep(2)
ser.write("2".encode())
time.sleep(2)
ser.write("3".encode())
time.sleep(2)
ser.write("2".encode())
time.sleep(2)
ser.write("4".encode())
time.sleep(2)
ser.write("2".encode())
time.sleep(2)
