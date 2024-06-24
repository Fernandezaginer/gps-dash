import serial
import pynmea2

def parse_nmea_sentence(sentence):
    try:
        parsed_data = pynmea2.parse(sentence)
        if isinstance(parsed_data, pynmea2.GGA):
            return parsed_data.latitude, parsed_data.longitude, parsed_data.altitude
    except pynmea2.ParseError:
        pass
    return None

def read_gps_data(serial_port):
    ser = serial.Serial('/dev/ttyACM0', 115200)
        while True:
            sentence = ser.readline().decode("utf-8").strip()
            if sentence.startswith("$GNGGA"):
                position_data = parse_nmea_sentence(sentence)
                if position_data:
                    return position_data

if __name__ == "__main__":
    
    position = read_gps_data(serial_port)
    if position:
        latitude, longitude, altitude = position
        print(f"Latitud: {latitude:.6f}, Longitud: {longitude:.6f}, Altitud: {altitude:.2f} metros")
    else:
        print("No se pudo obtener la posición GPS.")
