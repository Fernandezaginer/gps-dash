#!/usr/bin/env python



def rpi_buffer_thread_fnc():


    import socket
    import os
    import time
    import pandas as pd
    from io import StringIO
    import ast
    import defines



    global send_list
    send_list = []

    # Listen to data_reader and data_show:
    ip = socket.gethostbyname(socket.gethostname())
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("\n\nBuffer server started OK ...")
    socket.bind((ip, defines.BUFFER_PORT))

    # Send to data_show
    def socket_send(string):
        socket.sendto(bytes(string, "utf-8"), (ip, defines.REQUEST_PORT))




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
        if add[1] == defines.READER_PORT:
            process_reader(data)
            print("+ buffer")
        if add[1] == defines.REQUEST_PORT:
            process_show(data)
            print("- buffer")

    socket.close()
