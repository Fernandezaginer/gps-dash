import spidev
import RPi.GPIO as GPIO
import asyncio
from threading import Thread

class SPIClass:
    def __init__(self, bus=0, device=0, cs_pin=8):
        self.spi = spidev.SpiDev()
        self.bus = bus
        self.device = device
        self.cs_pin = cs_pin
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 50000  # Velocidad por defecto
        self.spi.mode = 0b00  # Modo por defecto
        self._transferWriteFill = 0
        self.transfer_complete_event = asyncio.Event()

        # Configurar el pin CS
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(cs_pin, GPIO.OUT)
        GPIO.output(cs_pin, GPIO.HIGH)

    def begin(self):
        # Abrir puerto SPI
        self.spi.open(self.bus, self.device)

    def end(self):
        # Cerrar puerto SPI
        self.spi.close()
        GPIO.cleanup()

    def setBitOrder(self, order):
        # Establecer el orden de bits
        self.bit_order = order

    def setDataMode(self, mode):
        # Establecer el modo SPI
        self.spi.mode = mode

    def setClockDivider(self, divider):
        # Establecer la velocidad del reloj
        self.spi.max_speed_hz = 500000 // divider

    def transfer(self, data):
        # Transferir datos por SPI
        GPIO.output(self.cs_pin, GPIO.LOW)
        response = self.spi.xfer2([data])
        GPIO.output(self.cs_pin, GPIO.HIGH)
        return response[0]

    def transfer16(self, data):
        # Transferir datos de 16 bits por SPI
        high_byte = (data >> 8) & 0xFF
        low_byte = data & 0xFF
        GPIO.output(self.cs_pin, GPIO.LOW)
        resp = self.spi.xfer2([high_byte, low_byte])
        GPIO.output(self.cs_pin, GPIO.HIGH)
        return (resp[0] << 8) | resp[1]

    def transfer_buffer(self, buf):
        # Transferir un buffer de datos por SPI
        GPIO.output(self.cs_pin, GPIO.LOW)
        response = self.spi.xfer2(buf)
        GPIO.output(self.cs_pin, GPIO.HIGH)
        return response

    def setTransferWriteFill(self, ch):
        # Establecer el carácter de llenado de escritura
        self._transferWriteFill = ch

    def endTransaction(self):
        # Finalizar la transacción SPI
        
        pass

    # Transferencia asincrónica usando asyncio
    async def async_transfer(self, data):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self.transfer, data)

    async def async_transfer_buffer(self, buf):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self.transfer_buffer, buf)

    # Simulación de transferencia tipo DMA usando threading
    def dma_transfer(self, tx_buffer, rx_buffer, callback=None):
        def transfer_func():
            nonlocal rx_buffer
            GPIO.output(self.cs_pin, GPIO.LOW)
            rx_buffer[:] = self.spi.xfer2(tx_buffer)
            GPIO.output(self.cs_pin, GPIO.HIGH)
            if callback:
                callback()

        transfer_thread = Thread(target=transfer_func)
        transfer_thread.start()

    def dma_transfer_async(self, tx_buffer, rx_buffer):
        async def dma_transfer_coro():
            self.dma_transfer(tx_buffer, rx_buffer, lambda: self.transfer_complete_event.set())
            await self.transfer_complete_event.wait()
            self.transfer_complete_event.clear()

        return dma_transfer_coro()

# Ejemplo de uso:
#   async def main():
#        spi = SPIClass(bus=0, device=0, cs_pin=8)
#       spi.begin()
#       spi.setDataMode(0b01)
#       spi.setClockDivider(4)
#       # Transferencia sincrónica
#       response = spi.transfer(0xFF)
#       print("Respuesta Sincrónica:", response)
#
#       # Transferencia asincrónica
#       response = await spi.async_transfer(0xFF)
#       print("Respuesta Asincrónica:", response)
#
#       # Transferencia tipo DMA
#       tx_buffer = [0xFF, 0x00, 0xAA, 0x55]
#       rx_buffer = [0x00] * len(tx_buffer)
#       spi.dma_transfer(tx_buffer, rx_buffer, callback=lambda: print("Transferencia DMA Completa:", rx_buffer))
#
#       # Transferencia tipo DMA asincrónica
#        rx_buffer_async = [0x00] * len(tx_buffer)
#      await spi.dma_transfer_async(tx_buffer, rx_buffer_async)
#      print("Transferencia DMA Asincrónica Completa:", rx_buffer_async)
#   
#      spi.end()
#





    

# Ejecutar la función principal
# asyncio.run(main())
