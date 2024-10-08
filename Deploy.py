import RPi.GPIO as GPIO
import smbus2 as smbus

def read_acceration():
    bus = smbus.SMBus(0)
    data = bus.read_i2c_block_data(0x67, 0x00, 1, force=None)
    parseInt = data[0]
    return parseInt

def deploy(pin:int, targetHeight:float, currentALtitude:float):
    if(read_acceration() > 0.8 and currentALtitude > targetHeight):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

