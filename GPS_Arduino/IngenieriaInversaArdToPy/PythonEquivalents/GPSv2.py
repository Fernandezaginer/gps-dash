import Wire
import time
import SparkFun_ublox_GNSS_library as ubloxGPS
import serial


port = 'devttyACM0'
myGNSS = ubloxGPS.SFE_UBLOX_GNSS()

time.sleep(1)

try:
    ser = serial.Serial(port,115200)
except Exception as ex:
    print(ex)

i2c = Wire.TwoWire()
i2c.begin()


if myGNSS.begin() == False:
    try:
        ser.write("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing.")
    except Exception as ex:
        print("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing.")

myGNSS.setI2COutput(ubloxGPS.COM_TYPE_UBX)

while True:
    if myGNSS.getPVT():
        latitude = myGNSS.getLatitude()
        try:
            ser.write("lat:")
            ser.write(latitude/10**7)
            ser.print("degrees")
        except Exception as ex:
            print("lat" + latitude/10**7+ "degrees")


        longitude = myGNSS.getLonguitude()

        try:
            ser.write("long:")
            ser.write(longitude/10**7)
            ser.write("degrees")
        except Exception as ex:
            print("long" + longitude/10**7+ "degrees")

        altitude = myGNSS.getAltitude()
        try:
            ser.write("alt:")
            ser.write(altitude)
            ser.write("degrees")
        except Exception as ex:
            print("altitude"+altitude/10**8+"degrees")

