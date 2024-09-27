import serial
from time import sleep


ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    line = ser.readline()
    print(line)
    sleep(1)
    


