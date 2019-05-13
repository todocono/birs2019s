import time, serial
from serial.tools import list_ports

# use the following to see all the serial ports:
# python -m serial.tools.list_ports

# for my computer, that's:
port = "/dev/tty.usbmodem143102"
baud = 115200  # that is the default to talk with microbit

s = serial.Serial(port)
s.baudrate = 115200
refresh_serial = 1000
current_milli_time = lambda: int(round(time.time() * 1000))
prev_milli = current_milli_time()

while True:
    current_milli = current_milli_time()
    if current_milli - prev_milli  > refresh_serial:
        current_milli_time = lambda: int(round(time.time() * 1000))
        # if there is any incoming communication
        while s.in_waiting:
            print(s.readline().decode())
        #data = s.readline()
        #data = int(data[0:4])
        #print(data.decode())
        s.write(b'PC.') # s.write(str.encode('PC.'))
        s.flush()
        time.sleep(0.01)    # to avoid buffer overflow
