#!/usr/bin/env python 


def rest_api_server_fnc():

  # Libraries
  import ast
  import utilities
  import defines
  import pandas as pd
  from flask import Flask


  # Definitions
  DF_HEADERS = ["TIME", "LAT", "LON", "ALT", "SENT"]


  global df_data
  df_data = pd.DataFrame(columns=DF_HEADERS)


  # Read data from the buffer socket:
  def read_data():

    # Read data from the socket:
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Socket.bind((ip, defines.REQUEST_PORT))
    Socket.sendto(bytes("get_data", "utf-8"), (ip, defines.BUFFER_PORT))
    Socket.settimeout(1.0)
    try:
      data = Socket.recv(65536)
    except:
      data = b'{}'
    data = data.decode()
    data = str(data)
    Socket.close()

    # Append to data
    global df_data
    if data[0] == "[":
      data = utilities.decode_str(data)
      df_data = pd.concat([df_data, pd.DataFrame(data)], ignore_index=True)
    else:
      df_data = pd.concat([df_data, pd.DataFrame(ast.literal_eval(data))], ignore_index=True)




  api = Flask(__name__)
  print("Flask started")


  @api.route('/get_new_data', methods=['GET'])
  def handle_request1():
    read_data()
    global df_data
    df_send = df_data[df_data["SENT"] == False]
    df_data["SENT"] = True
    return df_send.to_string()


  @api.route('/get_all_data', methods=['GET'])
  def handle_request2():
    read_data()
    global df_data
    return df_data.to_string()


  api.run(port=defines.API_PORT)




