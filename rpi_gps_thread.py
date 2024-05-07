#!/usr/bin/env python 


def rpi_gps_thread_fnc():

    import socket
    import time


    READER_PORT = 8000
    SERVER_PORT = 8001
    SHOW_PORT = 8002


    def socket_send(string):
        ip = socket.gethostbyname(socket.gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((ip, READER_PORT))
        s.sendto(bytes(string, "utf-8"), (ip, SERVER_PORT))
        s.close()



    while(True):
        socket_send(str({"TIME" : time.time(), "LAT" : 0.0, "LON" : 0.0, "ALT": 0.0}))
        print("SEND")
        time.sleep(1)




