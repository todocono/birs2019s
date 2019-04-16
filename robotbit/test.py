# Write your code here :-)

from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
        break
    elif button_a.is_pressed():
        display.scroll("now is differnt")
    elif button_b.is_pressed():
        display.scroll("B")
    sleep(100)
