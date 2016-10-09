import os 
import time
import random
time.sleep(3)
f = open('database.txt', 'a')  
serial_number_file = open('serial_number.txt')
hybrid_serial_number = serial_number_file.readline()
 #data structure: serial number, test succeeded or failed
if(random.random()<0.7):
    f.write(str(hybrid_serial_number) + ',1\n')
else:
    f.write(str(hybrid_serial_number) + ',0\n')
