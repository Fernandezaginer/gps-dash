import serial
import pynmea2


def parse_nmea_sentence(sentence):
    try:
        parsed_data = pynmea2.parse(sentence)
        if isinstance(parsed_data, pynmea2.GGA):
            return parsed_data.latitude, parsed_data.longitude, parsed_data.altitude, parsed_data.horizontal_dil
    except pynmea2.ParseError:
        pass
    return None


def read_gps_data():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    while True:
        sentence = ser.readline().decode("utf-8").strip()
        if sentence.startswith("$GNGGA"):
            position_data = parse_nmea_sentence(sentence)
            if position_data:
                return position_data

if __name__ == "__main__":
    while True:
        position = read_gps_data()

        if position:
            latitude, longitude, altitude, relative_accuracy = position
            print(f"Latitud: {latitude:.9f}, Longitud: {longitude:.9f}, Altitud: {altitude:.2f}, Precision Horizontal:{relative_accuracy}")

        else:
            print("No se pudo obtener la posición GPS.")

else:
    while True:
        position = read_gps_data()
        if position is not None:
            latitude, longitude, altitude, relative_accuracy = position
            print(f"Latitud: {latitude:.9f}, longitud: {longitude:.9f}, Altitud: {altitude:.2f}, Precision Horizontal:{relative_accuracy}")

        else:
            print("No se pudo obtener la posicion GPS.")