import RPi.GPIO as GPIO
import simpy
import math

if '_SPI_H_INCLUDED' not in locals():
    _SPI_H_INCLUDED:str = "_SPI_H_INCLUDED"

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
    
#import arduino.py #TODO

if '__arm__' in locals() and 'TEENSYDUINO' in locals():
    pass




if  '__has_include' in locals() and '__has_include_eventResponder.py' in locals():
    # define SPI_HAS_TRAMSFER_ASYNC = true
    #define SPI_HAS_TRANSFER_BUF
    pass


    

SPI_HAS_TRANSFER_ASYNC:int = 1

#import DMAChannel.py #TODO
#import EventResponder.py #TODO

SPI_HAS_TRANSACTION:int = 1

SPI_HAS_TRANSFER_BUF:int = 1

if 'LSBFIRST' not in locals():
    LSBFIRST:int = 0

if 'MSBFIRST' not in locals():
    MSBFIRST:int = 1
    

SPI_MODE0:hex = 0x00
SPI_MODE1:hex = 0x04
SPI_MODE2:hex = 0x08
SPI_MODE3:hex = 0x0C
SPI_CLOCK_DIV4:hex = 0X00
SPI_CLOCK_DIV16:hex = 0x01
SPI_CLOCK_DIV128:hex = 0x03
SPI_CLOCK_DIV2:hex = 0x04
SPI_CLOCK_DIV8:hex = 0x05
SPI_CLOCK_DIV32:hex = 0x06

SPI_MODE_MASK:hex = 0x0C
SPI_CLOCK_MASK:hex = 0x03
SPI_2XCLOCK_MASK:hex = 0x01



##Placas de 8 bits en avr 
if '__AVR__' in locals():
    SPI_ATOMIC_VERSION:int = 1
    
if 'EIMSK' in locals():
    SPI_AVR_EIMSK:str = 'EIMSK'

elif 'GICR' in locals():
    SPI_AVR_EIMSK:str = 'EIMSK'

elif 'GIMSK' in locals():
    SPI_AVR_EIMSK:str = 'GIMSK'


class SPISettings:
    def SPISettings(clock:int, bitOrder:int, dataMode:int, self):
        if clock.is_integer() == True:
            init_AlwaysInline(clock,bitOrder,dataMode)
        else:
            init_MightInline(clock,bitOrder,dataMode)
    
	
	
	def init_MightInline(clock:int, bitOrder:int, dataMode:int):
        init_AlwaysInline(clock, bitOrder, dataMode)
        
	def init_AlwaysInline(clock:int, bitOrder:int, dataMode:int):
		clockDiv:int = 0
        if clock.is_integer() == True:
            clockDiv = 0
			if clock >= F_CPU / 2:
				clockDiv = 0
			elif clock >= F_CPU / 4:
				clockDiv = 1
			elif clock >= F_CPU / 8:
				clockDiv = 2
			elif clock >= F_CPU / 16:
				clockDiv = 3
			elif clock >= F_CPU / 32:
				clockDiv = 4
			elif clock >= F_CPU / 64:
				clockDiv = 5
			else:
				clockDiv = 6
        else:
			clockSetting:int = F_CPU/2
            clockDiv = 0
            while clockDiv < 6 and clock < clockSetting:
                  clockSetting = clockSetting/2
                  clockDiv = clockDiv + 1
        
		if clockDiv == 6:
			clockDiv = 7
        
		clockDiv ^= 0x01 ## XOR binario

		#DE la librería Avr de arduino, importar TODO 
		#spcr = _BV(SPE) | _BV(MSTR) | ((bitOrder == LSBFIRST) ? _BV(DORD) : 0) |
		#	(dataMode & SPI_MODE_MASK) | ((clockDiv >> 1) & SPI_CLOCK_MASK);
		spsr:int = clockDiv && SPI_2XCLOCK_MASK



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
                GPIO.setup(SPI_TRANSACTION_MISMATCH_LED, GPIO.HIGH)

                inTransactionFlag:int = 1

        SPCR = settings.spcr #TODO
        SPSR = settings.spsr #TODO

    def transfer(data:int) -> int:
        SPDR:int = data
        volatile:str = "volatile"
        while not SPDR and _BV(SPIF): #TODO
            return SPDR

    def transfer16(data:int) -> int:
        InContainer:In
        OutContainer:Out
        In.val = data
        if 'SPDR' not in locals() and _BV(DORD): #TODO
            SPDR = InContainer.lsMsb.Lsb

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
            while not (SPSR & (1 << SPIF)):
                pass
            in_ = SPDR
            SPDR = out
            p[i - 1] = in_
            count -= 1
            i += 1

        while not (SPSR and (1 << SPIF)):
            pass
        p[i - 1] = SPDR

        return bytes(p)






            
	
	
	
	
	
	
	
	
	
	
	
            
            
        
            
	
            
            
    


    
    
    
