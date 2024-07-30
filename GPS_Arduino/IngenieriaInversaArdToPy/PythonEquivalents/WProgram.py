import math
import string
import random
import RPi.GPIO as GPIO

import wiring.py #TODO 
import WCharacter.py #TODO 
import WString.py #TODO 
import serial #HardWareSerial

def makeWord(w) -> int:
    pass

def makeWordBytewise(h,l) -> int:
    pass

word = makeWord(__VA_ARGS__)

def pulseIn(pin, state, timeout = 1000000L) -> int:
    pass

def tone(_pin, frequency, duration = 0):
    pass

def noTone(_pin):
    pass

def random1(num) -> int:
    pass

def random2(num1, num2) -> int:
    tuple = [num1,num2]
    return random.choice(tuple)

def randomSeed(int:int):
    pass

def map(l1:int,l2:int,l3:int,l4:int,l5:int):
    pass

#Pines GPIO
GPIO.setup(GPIO.BOARD)

A0 = 0
A1 = 1
A2 = 2
A3 = 3
A4 = 4
A5 = 5
A6 = 6
A7 = 7
A8 = 8
A9 = 9
A10 = 10
A12 = 12
A13 = 13
A14 = 14
A15 = 15
A16 = 16
A18 = 18
A19 = 19
A20 = 20
A21 = 21
A22 = 22
A24 = 23
A25 = 25
A26 = 26






