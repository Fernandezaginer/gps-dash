

import inttypes
import Stream



if 'I2C_BUFFER_LENGTH' not in locals():
    I2C_BUFFER_LENGTH = 128


class TwoWire:
        
        def __init__(self, rxBuffer:list, txAdress, txBuffer:list, trasnmitting): 
            self.rxBuffer =  rxBuffer
            self.txAddress = txAdress
            self.txBuffer = txBuffer
            self.transmitting = trasnmitting
    
        def user_onRequest():
              pass
        
        def user_onReceive(size):
              pass
        
        def onRequestService():
            pass
        
        def onReceiveService(buffer, bufferSize):
              pass

        def begin(sda, scl, address): 
            pass
        def pins(sda, scl):
            TwoWire.begin(sda, scl)
        
        def setClock(time):
             pass
        
        def setClockStretchLimit(stretch):
             pass
        
        def beginTransmission(uint8_t):
             pass
        
        def endTransmission(uint8_t) -> int:
             pass
        def  requestFrom(uint8_t address, size_t size, bool sendStop) -> int:
             pass
        
        def status() -> int:
             pass


        def write(buff):
             pass
        def available():
             pass
        def read(buff:int):
             pass
        def peek() -> int:
             pass
             
        def flush():
             pass
        
        def onReceive(buf:int):
            pass

       
if 'NO_GLOBAL_INSTANCES' not in locals() and 'NO_GLOBAL_TWOWIRE' not in locals():
    wire:TwoWire = None