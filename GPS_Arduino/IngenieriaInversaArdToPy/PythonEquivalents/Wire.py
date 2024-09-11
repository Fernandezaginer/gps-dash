import smbus2 as smbus
import time
import RPi.GPIO as GPIO

I2C_BUFFER_LENGHT = 120 

#Adress = comprobar cual es
          #Adress del gps = 0x1C(28)
          #Registro de control = 0x2A
          #0x00 == modo standby (00)
          #0x01 == modo activo  (01)
          #0x2A = 42
#Pines GPIO
sda = 2
scl = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sda,GPIO.IN) 
GPIO.setup(scl,GPIO.OUT)



class TwoWire:
     def __init__(self):
          self.rxBuffer = [0]*I2C_BUFFER_LENGHT
          self.rxBufferIndex = 0
          self.rxBufferLenght = I2C_BUFFER_LENGHT
          self.txBuffer = [0]*I2C_BUFFER_LENGHT
          self.txBufferIndex = 0
          self.txBufferLenght = I2C_BUFFER_LENGHT
          self.transmitting = 0
          
          self.txAddress = "Meter aqui Direccion I2C" #sda
          self.controlRegister = "meter registro de control" #scl
          self.standbyMode = 0x00
          self.activeMode = 0x01
          
          
     
     def begin(self):
          # iniciar bus
          try:
               bus = smbus.SMBus(1)
          except Exception as ex:
               print("bus not connected at pin 1")
               return ex
          
          bus.write_byte_data(self.txAddress,self.controlRegister,self.standbyMode)
          #Seleccionar modo activo
          bus.write_byte_data(self.txAddress, self.controlRegister, self.activeMode)
          #Seleccionar registro de configuracion 0x0E (14)
          bus.write_byte_data(self.txAddress, self.controlRegister, self.activeMode)
          
          time.sleep(0.5)
          
     
     def read_i2c_data(self,bytes):
          #iniciar bus en el puerto 1
          try:
               bus = smbus.SMBus(1)
          except Exception as ex:
               print(ex)
               return ex
          
          return bus.read_i2c_block_data(self.txAddress,self.standbyMode,bytes)
          
          