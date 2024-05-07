#!/usr/bin/env python 


# Libraries
import os
import socket
import threading
import pandas as pd
from flask import Flask, json

# Own modules
from rpi_gps_thread import * 


# Definitions
DF_HEADERS = ["TIME", "LAT", "LON", "ALT", "SENT"]
DATA_HEADERS = ["TIME", "LAT", "LON", "ALT"]





df = pd.DataFrame(columns=DF_HEADERS)


api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps({})




if __name__ == '__main__':
    api.run()









