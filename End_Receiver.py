#!/usr/bin/env python
import time
import serial
import RPi.GPIO as GPIO

# set GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)

# set info
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1             
 )
counter=0       
      
while 1:
    #Send write counter back to transmitter if desired
    #ser.write(str.encode('Write counter: %d \n'%(counter)))
    #time.sleep(1)
    #counter += 1

    #read incoming information
    x=ser.readline().strip()
    
    #print info to screen
    print(x)

    #blink LED if obtained line is 'a'
    if x == 'a':
        GPIO.output(23,GPIO.HIGH)
        time.sleep(3)
    else:
        GPIO.output(23,GPIO.LOW)