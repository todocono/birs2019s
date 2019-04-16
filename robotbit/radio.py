# A micro:bit Firefly.
# By Nicholas H.Tollervey. Released to the public domain.
# modified by Rodolfo Cossovich for BIRS 2019 @NYU Shanghai
import radio
import time
import random
# from microbit import display, Image, button_a, sleep  # this is a way to do it
from microbit import *
import robotbit

buf = bytearray(1)
d = ''
#start the serial port
uart.init(baudrate=115200)
# while not uart.any():
#    pass
# The radio won't work unless it's switched on.
radio.config(group=0)  # default group
radio.config(power=7)  # max 7
radio.on()
display.scroll("H!")

# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send('3,1300,900;5,400,50')  # force to send a sequence over radio
    if button_b.was_pressed():
         uart.write('3,1300,900;5,400,50')  # send over serial
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming:
        #if incoming[-1] == '.':  # if the last character is a .
        new = incoming.split(';')
        #display.show(new)  # something to be careful is that show is iterative
        for i in range(len(new)):
            #display.scroll(new[i])
            each = new[i].split(',')
            for j in range(len(each)):
                display.scroll(each[j])
            # sleep(1)  # this is in miliseconds
            # time.sleep(3) # this is in seconds because it uses the imported time
    if uart.any():
        uart.readinto(buf, 1)
        d = d + str(buf[0])
        if buf[0] == ord('.'):
            display.show(d)
            d = ''
        #sleep(20)
    #incoming_serial = uart.readall()
    #if incoming_serial:
        # if incoming_serial[-1] == '.':
    #    display.scroll(incoming_serial)
    sleep(1)
'''
    if incoming[-1] == '.':
        # If there's an incoming "flash" message display
        # the firefly flash animation after a random short
        # pause.
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        # Randomly re-broadcast the flash message after a
        # slight delay.
        if random.randint(0, 9) == 0:
            sleep(500)
            radio.send('flash')  # a-ha
'''
