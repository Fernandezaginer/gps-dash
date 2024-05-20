

# Libraries
import os
import time
import threading


# Custom modules:
from rpi_buffer_thread import *
from rpi_gps_thread import *
from rpi_server import *


def run():

    t2 = threading.Thread(target=rpi_gps_thread_fnc, daemon=True)
    t2.start()

    t1 = threading.Thread(target=rpi_buffer_thread_fnc, daemon=True)
    t1.start()

    rest_api_server_fnc()

    t1.join()
    t2.join()




# Prevent dash app from opening many times

TMP_DIR = "./tmps"

if not os.path.exists(TMP_DIR):
    os.makedirs(TMP_DIR)
files = os.listdir(TMP_DIR)
if files == []:
    open(os.path.join(TMP_DIR, str(time.time()) + ".tim"), "w").content
    run()
else:
    file = files[0]
    time_stamp = int(file.split(".")[0])
    if time.time() > time_stamp + 15:
        print(time_stamp)
        run()
        os.remove(os.path.join(TMP_DIR, file))
        open(os.path.join(TMP_DIR, str(time.time()) + ".tim"), "w").close()
    else:
        os.remove(os.path.join(TMP_DIR, file))
        open(os.path.join(TMP_DIR, str(time.time()) + ".tim"), "w").close()




