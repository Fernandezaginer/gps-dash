import GPS_Arduino.IngenieriaInversaArdToPy.PythonEquivalents.SparkFun_ublox_GNSS_library as GNSS
import GPS_Arduino.IngenieriaInversaArdToPy.PythonEquivalents.Wire as Wire
import time


myGNSS = GNSS.SFE_UBLOX_GNSS()
time.sleep(1)

#wire.begin()
i2c = Wire.TwoWire(0x46)
i2c.begin()

while True:
    lat = myGNSS.getLatitude()
    alt = myGNSS.getAltitude()
    lon = myGNSS.getLonguitude()
    
    print("latitude:" + lat + "\n")
    print("altitude" + alt+ "\n")
    print("longuitude" + lon+ "\n")
