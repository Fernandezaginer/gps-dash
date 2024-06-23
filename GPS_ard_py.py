from serial import Serial
from pyubx2 import UBXReader, NMEA_PROTOCOL, UBX_PROTOCOL

while True:
    with Serial('/dev/ttyACM0', 38400, timeout=3) as stream:
      ubr = UBXReader(stream, protfilter=NMEA_PROTOCOL | UBX_PROTOCOL)
      raw_data, parsed_data = ubr.read()
      if parsed_data is not None:
        print(parsed_data)
