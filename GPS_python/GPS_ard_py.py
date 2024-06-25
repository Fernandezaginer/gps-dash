import serial 
import pynmea2


def parse_nmea_sentence(sentence):
    try:
        msg = pynmea2.parse(sentence)
        return msg
    except pynmea2.ParseError:
        return None


def read_gps_data():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    while True:  # always running
        sentence = ser.readline().decode('utf-8').strip()
        if sentence.startswith("$GNGGA"):
            print(sentence)
            position_data = parse_nmea_sentence(sentence)
            if position_data is not None:
                return position_data


if __name__ == "__main__":
    while True:
        position = read_gps_data()
        if position:
            latitude = position.latitude
            longitude = position.longitude
            altitude = position.altitude
             print(f"Latitud: {latitude:.9f}, Longuitud: {longitude:.9f}, Altitud: {altitude:.9f}")
        else:
            print("No se pudo encontrar la posicion del GPS.")


