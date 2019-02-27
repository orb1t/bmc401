#!/usr/bin/env python
import os
import sys
import time
import serial
import RPi.GPIO as GPIO

# Pin Definitions
PTT = 17 # LOW = TX, HIGH = RX
PD = 27  # LOW = Sleep, HIHJ = Normal
HILO = 22 # LOW = 0.5W, Float = 1W

def cmnd(c):
  try:
    while True:
      ser.write(c)
      time.sleep(1)
      x=ser.readline()
      print x
      if x.startswith('+') or x.startswith("S="):
          break
  except KeyboardInterrupt:
    pass

##################################################
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PD, GPIO.OUT)
GPIO.setup(PTT, GPIO.OUT)
#GPIO.setup(HILO, GPIO.OUT)
#GPIO.output(HILO, GPIO.LOW)

ser = serial.Serial(
               port='/dev/ttyAMA0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )

if len(sys.argv) == 1:
    print "no arguments"
elif sys.argv[1] == "init":
    print "init"
    GPIO.output(PTT, GPIO.HIGH)
    GPIO.output(PD, GPIO.HIGH)
    cmnd('AT+DMOCONNECT\r\n')
    os.system('gpio -g mode 18 alt5') # sets GPIO 18 pin to ALT 5 mode = GPIO_GEN1
    GPIO.setup(HILO, GPIO.OUT)
    GPIO.output(HILO, GPIO.LOW)
elif sys.argv[1] == "scan":
    freq = float(sys.argv[2])
    print "scan %.4f" % freq
    cmnd("S+%.4f\r\n" % freq)
elif sys.argv[1] == "freq":
    freq = float(sys.argv[2])
    print "freq %.4f" % freq
    cmnd("AT+DMOSETGROUP=0,%.4f,%.4f,0000,4,0000\r\n" % (freq, freq))
elif sys.argv[1] == "tx":
    print "tx"
    GPIO.output(PD, GPIO.HIGH)
    GPIO.output(PTT, GPIO.LOW)
elif sys.argv[1] == "rx":
    print "rx"
    GPIO.output(PD, GPIO.HIGH)
    GPIO.output(PTT, GPIO.HIGH)
elif sys.argv[1] == "stby":
    print "standby"
    GPIO.output(PD, GPIO.LOW)
    GPIO.output(PTT, GPIO.HIGH)
elif sys.argv[1] == "power":
    p = GPIO.LOW
    if sys.argv[2] == "high":
      p = GPIO.HIGH
    elif sys.argv[2] == "low":
      p = GPIO.LOW
    print "power %s" % sys.argv[2]
    GPIO.setup(HILO, GPIO.OUT)
    GPIO.output(HILO, p)
else:
    print "unknown"

# GPIO.cleanup() # cleanup all GPIO
