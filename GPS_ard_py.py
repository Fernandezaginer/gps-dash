import csv
import serial
import pynmea2

#Archivo CSV
datos = open('data.csv',"w")

def parse_nmea_sentence(sentence):
    try:
        parsed_data = pynmea2.parse(sentence)
        if isinstance(parsed_data, pynmea2.GGA):
            return parsed_data.latitude, parsed_data.longitude, parsed_data.altitude, parsed_data.horizontal_dil

    except pynmea2.ParseError:
        pass
    return None


def read_gps_data():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while True:
        sentence = ser.readline().decode("utf-8").strip()
        if sentence.startswith("$GNGGA"):
            position_data = parse_nmea_sentence(sentence)
            if position_data:
                return position_data

        

def write_gps_data():
    position = read_gps_data()

    if position is not None:
        latitude, longuitude, altitude, horizontal_dil = position
        print(f"Latitude: {latitude}, Longuitud: {longuitude},Altitud: {altitude}, Dispersion Horizontal:{horizontal_dil}")
        datos.write(f"{latitude};{longuitude};{altitude};{horizontal_dil}\n")
    else:
        print("No se pudo obtener la posicion GPS")




if __name__ == "__main__":
    datos.write("DATOS DEL MODULO GPS\n")
    datos.write("LAT;LON;ALT;DIL\n")
    while True:
        write_gps_data()


else: #in order for the function to work if the program is imported
    while True:
        write_gps_data()

