import RPi.GPIO as GPIO
import simpy
import math
import time
import psutil


if '_SPI_H_INCLUDED' not in locals():
    _SPI_H_INCLUDED:str = "_SPI_H_INCLUDED"

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
    
#import arduino.py #TODO

if '__arm__' in locals() and 'TEENSYDUINO' in locals():
    pass 



if  '__has_include' in locals() and '__has_include_eventResponder.py' in locals():
    SPI_HAS_TRAMSFER_ASYNC:bool = True
    SPI_HAS_TRANSFER_BUF:bool = True


def _BV(var):
    return (1 << var)


    

SPI_HAS_TRANSFER_ASYNC:int = 1

#import DMAChannel.py #TODO
#import EventResponder.py #TODO

SPI_HAS_TRANSACTION:int = 1

SPI_HAS_TRANSFER_BUF:int = 1

if 'LSBFIRST' not in locals():
    LSBFIRST:int = 0

if 'MSBFIRST' not in locals():
    MSBFIRST:int = 1
    

SPI_MODE0 = 0x00
SPI_MODE1 = 0x04
SPI_MODE2 = 0x08
SPI_MODE3 = 0x0C
SPI_CLOCK_DIV4 = 0X00
SPI_CLOCK_DIV16 = 0x01
SPI_CLOCK_DIV128 = 0x03
SPI_CLOCK_DIV2 = 0x04
SPI_CLOCK_DIV8 = 0x05
SPI_CLOCK_DIV32 = 0x06

SPI_MODE_MASK = 0x0C
SPI_CLOCK_MASK = 0x03
SPI_2XCLOCK_MASK = 0x01

##PINES 
SPI_TRANSACTION_MISMATCH_LED:int = 5



##Placas de 8 bits en avr 
if '__AVR__' in locals():
    SPI_ATOMIC_VERSION:int = 1
    
if 'EIMSK' in locals():
    SPI_AVR_EIMSK:str = 'EIMSK'

elif 'GICR' in locals():
    SPI_AVR_EIMSK:str = 'EIMSK'

elif 'GIMSK' in locals():
    SPI_AVR_EIMSK:str = 'GIMSK'

#Velocidad de la cpu

cpufreq = psutil.cpu_freq()

class SPISettings:
    def SPISettings(clock:int, bitOrder:int, dataMode:int, self):
        if clock.is_integer() == True:
            init_AlwaysInline(clock,bitOrder,dataMode)
        else:
            init_MightInline(clock,bitOrder,dataMode)
    
	
	
	def init_MightInline(clock:int, bitOrder:int, dataMode:int):
        init_AlwaysInline(clock, bitOrder, dataMode)
        
	def init_AlwaysInline(clock:int, bitOrder:int, dataMode:int):
		clockDiv = 0
        if clock.is_integer() == True:
            clockDiv = 0
			if clock >= cpufreq / 2:
				clockDiv = 0
			elif clock >=  cpufreq / 4:
				clockDiv = 1
			elif clock >= cpufreq / 8:
				clockDiv = 2
			elif clock >= cpufreq / 16:
				clockDiv = 3
			elif clock >= cpufreq / 32:
				clockDiv = 4
			elif clock >= cpufreq / 64:
				clockDiv = 5
			else:
				clockDiv = 6
        else:
		    clockSetting:int = cpufreq/2
            clockDiv = 0
            while clockDiv < 6 and clock < clockSetting:
                  clockSetting = clockSetting/2
                  clockDiv = clockDiv + 1
        
		if clockDiv == 6:
			clockDiv = 7
        
		clockDiv ^= 0x01 ## XOR binario

		# De la librería Avr de arduino, importar TODO 
		# spcr = _BV(SPE) | _BV(MSTR) | ((bitOrder == LSBFIRST) ? _BV(DORD) : 0) |
		#	(dataMode & SPI_MODE_MASK) | ((clockDiv >> 1) & SPI_CLOCK_MASK);
		spsr = clockDiv & SPI_2XCLOCK_MASK #Formato binario



	spcr:int = None
    spsr:int = None

class LsbMsb:
    Lsb:int
    Msb:int

class In:
    val:int
    lsMsb:LsbMsb

class Out:
    val:int
    lsMsb:LsbMsb



   

class SPIClass: #Avr 
    
    def begin():
        pass
    def usingInterrupt(interruptNumber:int):
        pass #registra cosas que usan la libreria SPI, sirve para prevenir conflictos
        
    def beginTransaction(settings:SPISettings):
        if interruptMode > 0: #Localizar origen de la variable TODO
            if SPI_AVR_EIMSK in locals():
                pass
            if interruptMode == 1:
                interruptSave = SPI_AVR_EIMSK
                # SPI_AVR_EIMSK &= ~interruptMask TODO  ver de donde viene esto     
            else:
                tmp:int = SREG #TODO 
                cli() #TODO 
                interruptSave = tmp
        if 'SPI_TRANSACTION_MISMATCH_LED' in locals():
            if(inTransactionFlag):
                GPIO.setup(SPI_TRANSACTION_MISMATCH_LED, GPIO.OUT)
                GPIO.output(SPI_TRANSACTION_MISMATCH_LED, GPIO.HIGH)

                inTransactionFlag:int = 1

        SPCR = settings.spcr #TODO
        SPSR = settings.spsr #TODO

    def transfer(data:int) -> int:
        SPDR:int = data
        volatile:str = "volatile"
        while  (~SPDR)&_BV(SPIF): #TODO
            return SPDR

    def transfer16(data:int) -> int:
        InContainer:In
        OutContainer:Out
        In.val = data
        if 'SPDR' not in locals() and _BV(DORD) in locals(): #TODO
            SPDR = InContainer.lsbMsb.Lsb

            while not 'SPSR' in locals() and _BV(SPIF): #TODO
                OutContainer.lsMsb.Lsb = SPDR

        else:
            SPDR = InContainer.lsMsb.Msb
            while(not 'SPSR' in locals() and _BV(SPIF)): #TODO
                OutContainer.lsMsb.Msb = SPDR
                SPDR = InContainer.lsMsb.Lsb
                while not 'SPSR' in locals() and _BV(SPIF): #TODO
                    OutContainer.lsMsb.Lsb = SPDR

        return OutContainer.val

    def StaticTransfer(buf, count):
        if count == 0:
            return

        p = bytearray(buf)
        SPDR = p[0]

        i = 1
        while count > 1:
            out = p[i]
            while  ~(SPSR & (1 << SPIF)):
                pass
            in_:int = SPDR
            SPDR = out
            p[i - 1] = in_
            count -= 1
            i += 1

        while  ~(SPSR&_BV(SPIF)): #TODO 
            pass
        p[i - 1] = SPDR

    def setTransferWriteFill(ch:int):
         _transferWriteFill:int = ch
    
    def transfer(buf,retbuf,count:int):
        pass

    def endTransaction():
        if 'SPI_TRANSACTION_MISMATCH_LED' in locals():
            if inTransactionflag == 0: #TODO define variable
                GPIO.setup(SPI_TRANSACTION_MISMATCH_LED, GPIO.OUT)
                GPIO.output(SPI_TRANSACTION_MISMATCH_LED, GPIO.HIGH)

            inTransactionflag = 0
    
        if interruptMode > 0: #TODO
            if 'SPI_AVR_EIMSK' in locals():
                if interruptMode == 1:
                    SPI_AVR_EIMSK = interruptSave #TODO 
                else:
                    SREG = interruptSave
    
    end() ## finalizar el buf SPI #TODO

    def setBitOrder(bitOrder:int):
        if bitOrder == LSBFIRST:
            SPCR = SPCR | _BV(SPCR)
        
        else:
            SPCR = SPCR & ~_BV(DORD)

    def setDataMode(datamode:int):
        SPCR = (SPCR & ~SPI_MODE_MASK)| datamode

    def setClockDivider(clockDiv:int):
        SPCR = (SPCR & ~SPI_CLOCK_MASK)|clockDiv
        SPSR = (SPSR & ~SPI_2XCLOCK_MASK)|(clockDiv & SPI_CLOCK_MASK)

    def attachInterrupt():
        SPCR = SPIE | _BV(SPIE)
    def detatchInterrupt():
        SPCR = SPCR & ~_BV(SPIE)
    
    def Teensyduino_Test_constinit(instance:int,index:int) -> int:
        pass
    

    




                
                






            
	
	
	
	
	
	
	
	
	
	
	
            
            
        
            
	
            
            
    


    
    
    
