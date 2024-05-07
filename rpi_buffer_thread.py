#!/usr/bin/env python



def rpi_buffer_thread_fnc():


    import socket
    import os
    import time
    import pandas as pd
    from io import StringIO
    import ast

    READER_PORT = 8000
    SERVER_PORT = 8001
    SHOW_PORT = 8002


    global send_list
    send_list = []

    # Listen to data_reader and data_show:
    ip = socket.gethostbyname(socket.gethostname())
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind((ip, SERVER_PORT))
    print("\n\nBuffer server started OK ...")

    # Send to data_show
    def socket_send(string):
        socket.sendto(bytes(string, "utf-8"), (ip, SHOW_PORT))




    # -----------------------------------------------------
    #                 PROCESS DATA READER
    # -----------------------------------------------------

    def process_reader(data):
        global send_list
        send_list.append(data)



    # -----------------------------------------------------
    #                  PROCESS DATA SHOW
    # -----------------------------------------------------

    def process_show(data):
        if data == "get_new_df":
            global send_list
            socket_send(str(send_list))
            send_list = []
        else:
            pass



    # -----------------------------------------------------
    #                        LOOP
    # -----------------------------------------------------


    while True:
        data, add = socket.recvfrom(65536)
        #print(add)
        data = data.decode("utf-8")
        if add[1] == READER_PORT:
            process_reader(data)
        if add[1] == SHOW_PORT:
            process_show(data)

    socket.close()
