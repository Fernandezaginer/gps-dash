import RPi.GPIO as GPIO
import simpy
import math
import time
import psutil
from enum import Enum


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





class SPIClassAVR: #Avr

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

    def Teensyduino_Test_constinit(instance:int,index:int):
        pass

    interruptMode:int
    interruptMask:int
    interruptSave:int

    if SPI_TRANSACTION_MISMATCH_LED in locals():
        inTransactionFlag:int

    _transferWriteFill:int


    elif '__arm__' in locals() and 'TEENSYDUINO' in locals() and KINETISK in locals():
        SPI_HAS_NOTUSINGINTERRUPT:int = 1
        SPI_ATOMIC_VERSION:int = 1




class SPISettings32bits:
    def SPISettings(clock:int, bitOrder:int, dataMode:int):
        if clock:
            init_AlwaysInline(clock, bitOrder, dataMode):
        else:
              initMightInline(clock, bitOrder, dataMode):

    def SPISettings4clock(self):
          init_AlwaysInline(4000000, MSBFIRST, SPI_MODE0)

    def init_MightInline(clock:int, bitOrder:int, dataMode:0):
        init_AlwaysInline(clock, bitOrder, dataMode)

    def init_AlwaysInline(clock:int , bitOrder:int, dataMode:int):
        t:int
        c:int = SPI_CTAR_FSMZ(7)
        if bitOrder == LSBFIRST:
            c = c | SPI_CTAR_LSBFE
            if clock >= F_BUS/2:
                t = SPI_CIAR_PBR(0) | SPI_CTAR_BR(0) | SPI_CTAR_DBR #TODO

            elif clock >= F_BUS/3:
                t = SPI_CTAR_PBR(1) | SPI_CTAR_BR(0) | SPI_CTAR_DBR | SPI_CTAR_CSSCK(0) #TODO

            elif clock >= F_BUS/4:
                t = SPI_CTAR_PBR(2) | SPI_CTAR_BR(0) | SPI_CTAR_DBR | SPI_CTAR_CSSCK(0);

            elif clock >= F_BUS/6:
                t = SPI_CTAR_PBR(1) | SPI_CTAR_BR(0) | SPI_CTAR_CSSCK(0)

            elif clock >= F_BUS/8:
                t = SPI_CTAR_PBR(0) | SPI_CTAR_BR(1) | SPI_CTAR_CSSCK(1)

            elif clock >= F_BUS/10:
                t = SPI_CTAR_PBR(2) | SPI_CTAR_BR(0) | SPI_CTAR_CSSCK(0)

            elif clock >= F_BUS/12:
                t = SPI_CTAR_PBR(1) | SPI_CTAR_BR(1) | SPI_CTAR_CSSCK(1)

            elif clock >= F_BUS/16:
                t = SPI_CTAR_PBR(0) | SPI_CTAR_BR(3) | SPI_CTAR_CSSCK(2)

            elif clock >= F_BUS/20:
                t = SPI_CTAR_PBR(2) | SPI_CTAR_BR(1) | SPI_CTAR_CSSCK(0)

            elif clock >= F_BUS/24:
                t = SPI_CTAR_PBR(1) | SPI_CTAR_BR(3) | SPI_CTAR_CSSCK(2)

            elif clock >= F_BUS/32:
                t = SPI_CTAR_PBR(0) | SPI_CTAR_BR(4) | SPI_CTAR_CSSCK(3)

            elif clock >= F_BUS/40:
                t = SPI_CTAR_PBR(2) | SPI_CTAR_BR(3) | SPI_CTAR_CSSCK(2)

            elif clock >= F_BUS/56:
                t = SPI_CTAR_PBR(3) | SPI_CTAR_BR(3) | SPI_CTAR_CSSCK(2)

            elif clock >= F_BUS/64:
                t = SPI_CTAR_PBR(0) | SPI_CTAR_BR(5) | SPI_CTAR_CSSCK(4)

            elif clock >= F_BUS/128:
                t = SPI_CTAR_PBR(0) | SPI_CTAR_BR(6) | SPI_CTAR_CSSCK(5)

            elif clock >= F_BUS/256:
                t = SPI_CTAR_PBR(0) | SPI_CTAR_BR(7) | SPI_CTAR_CSSCK(6)

            elif clock  >= F_BUS/384:
                t = SPI_CTAR_PBR(1) | SPI_CTAR_BR(7) | SPI_CTAR_CSSCK(6)

            elif clock >= F_BUS/512:
                t = SPI_CTAR_PBR(0) | SPI_CTAR_BR(8) | SPI_CTAR_CSSCK(7)

            elif clock >= F_BUS/640:
                t = SPI_CTAR_PBR(2) | SPI_CTAR_BR(7) | SPI_CTAR_CSSCK(6)

            else:
                t = SPI_CTAR_PBR(1) | SPI_CTAR_BR(8) | SPI_CTAR_CSSCK(7)
        else:
            for i in range(0,23):
                t = ctar_clock_table[i]
                if clock >= F_BUS/ctar_div_table[i]:
                    break

        if dataMode & 0x08:
            c = c | SPI_CTAR_CPOL

        if dataMode & 0x04:
            c = c | SPI_CTAR_CPHA
            t = (t & 0XFFFF0FF) | (t & 0x0F000) >> 4

        ctar = c | t

    ctar_div_table = [23]
    ctar_clock_table = [23]
    ctar:int
    SPIClass:SPIClassAVR

class SPI_Hardware_t:
    clock_gate_register:int
    clock_gate_mask:int
    queue_size:int
    spi_irq:int
    max_dma_count:int
    tx_dma_count:int
    tx_dma_channel:int
    dma_rxisr:int
    miso_pin:list = [CNT_MISO_PINS]
    miso_mux:list = [CNT_MISO_PINS]
    mosi_pin:list = [CNT_MOSI_PINS]
    mosi_mux:list = [CNT_MOSI_PINS]
    sck_pin:list = [CNT_SCK_PINS]
    sck_mux:list = [CNT_SCK_PINS]
    cs_pin:list = [CNT_CS_PINS]
    cs_mux:list = [CNT_CS_PINS]
    cs_mask:list = [CNT_CS_PINS]

class DMAState(Enum): #LASTLINEWROTEN



class SPIClassTeensy:
    if '__MK20DX128__' in locals() or '__MK20DX256__':
        CNT_MISO_PINS:int = 2
        CNT_MOSI_PINS:int = 2
        CNT_SCK_PINS:int = 2
        CNT_CS_PINS:int = 9

    elif '__MK64FX512__' in locals() or '__MK66FX1M0__' in locals():
        CNT_MISO_PINS:int = 4
        CNT_MOSI_PINS:int = 4
        CNT_SCK_PINS:int = 3
        CNT_CS_PINS:int = 11

    spi0_hardware:SPI_Hardware_t
    spi1_hardware:SPI_Hardware_t
    spi2_hardware:SPI_Hardware_t























































