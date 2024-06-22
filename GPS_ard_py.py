import serial

# Configura el puerto serie
ser = serial.Serial('/dev/ttyACM0', 115200)  # Ajusta el nombre del puerto según tu sistema

def read_gnss_data():
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith('$GNGGA'):
            data = line.split(',')
            latitude = float(data[2]) / 100
            longitude = float(data[4]) / 100
            altitude = float(data[9])
            print(f"Lat: {latitude:.6f} (degrees), Long: {longitude:.6f} (degrees), Alt: {altitude:.2f} (m)")

if __name__ == "__main__":
    try:
        ser.open()
        print("Leyendo datos GNSS...")
        read_gnss_data()
    except KeyboardInterrupt:
        ser.close()
        print("\n¡Lectura de datos GNSS finalizada!")
