

import threading

from rpi_buffer_thread import *
from rpi_gps_thread import *


t = threading.Thread(target=rpi_buffer_thread_fnc, daemon=True)
t.start()


t1 = threading.Thread(target=rpi_gps_thread_fnc, daemon=True)
t1.start()


t.join() # Wait until completed
t1.join() # Wait until completed



