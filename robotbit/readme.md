

## Instructions to flash micropython.hex
https://uflash.readthedocs.io/en/latest/

## BBS content about how robotbit.hex (customized micropython with API for peripherals)
https://bbs.kittenbot.cn/forum.php?mod=viewthread&tid=251

To flash robotbit.hex, the syntax should be (Kudos @Tristan @Anand):
$ uflash -r robotbit.hex

## Original content to install / run code with ampy
https://learn.adafruit.com/sino-bit-micropython/running-code-with-ampy

ampy --port <serial port name> put scroll.py main.py

## To see your serial ports (besides of checking control panel or ls /dev)
python -m serial.tools.list_ports

## In macos, to talk over serial, do:
screen <serial port name> 115200
(And to kill the task, CTRL + k, CTRL + a, CTRL + k , choose y)
