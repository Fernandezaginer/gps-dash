import serial

from ublox_gps import UbloxGps

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def run():

    try:
        print("Listening for UBX Messages")
        while True:
            try:
                geo = gps.hp_geo_coords()
                print("Longitude: ", geo.lonHp) 
                print("Latitude: ", geo.latHp)
                print("Altitude: ", geo.heightHp)
                
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()


if __name__ == '__main__':
    run()
