
import inttypes

# import Wstring 
# import Printable

DEC = 10 
HEX = 16
OCT = 8
BIN = 2

class Print:
    #constructor
    def __init__(self, write_error = 1):
        self.write_error = write_error
    
    #private
    def printNumber(long, uint):
        pass #TODO 

    def printFloat(double, uint):
        pass #TODO 
    
    #public
    def setWriteError(self, err):
        if err == None:
            err = 1

        else:
            self.write_error = err

    
    def getWriteError(self) -> int:
        return self.write_error

    def clearWriteError(self):
        Print.clearWriteError(0)


    def write(text:str):
        if text == None:
            return 0
        else:
            return text.__len__()
    
    def availableForWrite() -> int:
        return 0
    
    def print(txt:str, mode:int):
        return txt.__len__()

    def println(txt:str, mode:int):
        return txt.__len__() + 1 #the '/n'
    
    def flush():
        pass 


 

        
