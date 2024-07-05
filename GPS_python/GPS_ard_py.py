import serial 
import pynmea2

def parse_nmea_sentence(sentence):
    try: 
        parsed_data = pynmea2.parse(sentence)
        if isinstance(parsed_data, pynmea2.GGA) == True:
            return parsed_data
    except pynmea2.ParseError:
        pass
        return None


def read_gps_data():
    ser = serial.Serial('COM3', 115200)
    while True:
        sentence = ser.readline().decode("utf-8")
        if  sentence.startswith("$GNGGA"):
            position_data = parse_nmea_sentence(sentence)
            if position_data:
                return position_data


if __name__ == "__main__":
    while True:
        position = read_gps_data()
        if position:
            # latitude,longuitude,altitude = position
            print(f"Latitud: {position.latitude:.9f}, Longuitud: {position.longitude:.9f}, Altitud: {position.altitude:.9f}")
        else:
            print("No se pudo enecontrar la posicion GPS.")