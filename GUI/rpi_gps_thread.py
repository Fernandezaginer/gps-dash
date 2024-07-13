#!/usr/bin/env python 



def rpi_gps_thread_fnc():

    import socket
    import time
    import defines


    # Definitions
    DF_HEADERS = ["TIME", "LAT", "LON", "ALT", "SENT"]



    def socket_send(string):
        ip = socket.gethostbyname(socket.gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((ip, defines.READER_PORT))
        s.sendto(bytes(string, "utf-8"), (ip, defines.BUFFER_PORT))
        s.close()



    while(True):
        socket_send(str({"TIME" : time.time(), "LAT" : 0.0, "LON" : 0.0, "ALT": 0.0, "SENT" : False}))
        time.sleep(1)




