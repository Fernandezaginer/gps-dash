from pyubx2 import UBXReader
import serial

def parse_ubx_messages(data):
    try:
        ubx_reader = UBXReader(data)
        
        altitud = None
        longitud = None
        latitud = None
        
        for msg in ubx_reader:
            if msg.name == "NAV_POSLLH":
                altitud = msg.data["height"]
                longitud = msg.data["lon"]
                latitud = msg.data["lat"]
                break  
            
        if altitud is not None and longitud is not None and latitud is not None:
            print(f"Altitud: {altitud} metros")
            print(f"Longitud: {longitud} grados")
            print(f"Latitud: {latitud} grados")
        else:
            print("No se encontró un mensaje NAV_POSLLH válido en los datos UBX.")
            
    except Exception as e:
        print(f"Error al analizar mensajes UBX: {e}")


while True:
    ser = serial.Serial('/dev/ttyACM0', 115200)
    ubx_data = ser.readline().decode('utf-8').strip()
    parse_ubx_messages(ubx_data)
