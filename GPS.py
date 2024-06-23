import serial

from ublox_gps import UbloxGps

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def run():

    try:
        print("Listening for UBX Messages")
        while True:
            try:
                geo = gps.geo_coords()
                print("Longitude: ", geo.lon) 
                print("Latitude: ", geo.lat)
                info_gps = gps.get_altitude()
                altitud = info_gps['altitude']
                print("Altitude: ", altitud)
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()


if __name__ == '__main__':
    run()


