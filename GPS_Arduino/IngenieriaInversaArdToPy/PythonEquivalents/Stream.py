import inttypes
import Print

from enum import Enum

class LookaheadMode(Enum):
    SKIP_ALL = 1
    SKIP_NONE = 2
    SKIP_WHITESPACE = 3


NO_IGNORE_CHAR:chr = '\x01'

class Stream(Print):
    def __init__(self, _timeout, _startMillis):
        self._timeout = _timeout = 1000
        self._startMillis = _startMillis
        
    
    def timeRead():
        # Get the time it took to read the last line of input TODO
        pass
    def timePeek():
        # Peek stream with Timeout TODO
        pass 
    
    def peekNextDigit(lookahead:LookaheadMode, detectDecimal:bool):
        # Returns the next numeric digit in the stream or -1 if timeout TODO
        pass
    
    def available():
        pass
    
    def read():
        pass
    
    def peek():
        pass
    
    def setTimeout(self,timeout):
        self._timeout = timeout
    
    def getTimeout(self):
        return self._timeout
    
    def find(target:str):
        #read data from the stream until the target string is found TODO
        pass
    
    def foundTarget(target:int):
        return Stream.find(target)

    def findLenght(target:str, Lenght:int):
        pass
    
    def foundTargetLenght(target:int, Lenght:int):
        return Stream.findLenght(target,Lenght)
    
    def findChar(target:chr):
        return Stream.foundTargetLenght(target,1)
    
    def findUntil(target:str, terminator:str):
        for string in target:
            if string == terminator:
                return True
            
            else: 
                return False
            
    def foundUntil(target:str, terminator:str):
        return Stream.findUntil(target, terminator)

    def findUntilStrFound(target:str, targetLen:int, terminate:str, termLen:int):
        #read data from the stream until the target string is found or the terminator is found CHECK
        for word in target:
            if word.__len__() == targetLen:
                if word == terminate and word.__len__() == termLen:
                    return True
            
            else:
                return False
    
    def foundUntiStrFound(target:str, targetLen:int, terminate:str, terminateLen:str):
        return Stream.findUntilStrFound(target, targetLen, terminate, terminateLen)

    def parseInt(lookAhead:LookaheadMode, ignore:chr) -> int: #TODO
       # returns the first valid (long) integer value from the current position.
       # lookahead determines how parseInt looks ahead in the stream.
       # See LookaheadMode enumeration at the top of the file.
       # Lookahead is terminated by the first character that is not a valid part of an integer.
       # Once parsing commences, 'ignore' will be skipped in the stream.

        lookAhead = LookaheadMode.SKIP_ALL
        ignore = NO_IGNORE_CHAR
        pass
    
    def parseFloat(lookAhead:LookaheadMode, ignore:chr) -> float: #TODO
        #Float version of parseInt
        lookAhead = LookaheadMode.SKIP_ALL
        ignore = NO_IGNORE_CHAR
        pass
    
    def readBytes(buffer:str, lenght:int) -> int:
        for word in buffer:
            if word.__len__() == lenght:
                return lenght
    
    def BytesFound(buffer:str, lenght:int) -> int:
        return Stream.readBytes(buffer, lenght)
    
    ## readBytesUntil
    
            
        
            
    
    