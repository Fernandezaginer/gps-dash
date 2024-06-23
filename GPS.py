import serial

from ublox_gps import UbloxGps

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def run():

    try:
        print("Listening for UBX Messages")
        while True:
            try:
                info_gps = gps.get_position()
                latitud = info_gps['latitude']
                longitud = info_gps['longitude']
                altitud_elipsoidal = info_gps['altitude']
                print("Longitude: ", longitud) 
                print("Latitude: ", latitud)
                altitud = altitud_elipsoidal - 28.0
                print("Altitude: ", altitud)
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()


if __name__ == '__main__':
    run()


