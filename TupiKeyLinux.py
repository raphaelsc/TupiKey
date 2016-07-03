import fcntl
import os
import time

KDSETLED = 0x4B32
KDGETLED = 0x4B31
SCR_LED  = 0x01
NUM_LED  = 0x02
CAP_LED  = 0x04

console_fd = os.open('/dev/console', os.O_NOCTTY)

def turn_all_on():
    all_on = SCR_LED | NUM_LED | CAP_LED
    fcntl.ioctl(console_fd, KDSETLED, all_on)

def turn_all_off():
    all_off = 0
    fcntl.ioctl(console_fd, KDSETLED, all_off)

# Turn on caps lock
#fcntl.ioctl(console_fd, KDSETLED, 0x04)

# Turn off caps lock
#fcntl.ioctl(console_fd, KDSETLED, 0)

def blink_all_leds():
    turn_all_off()
    turn_all_on()
    time.sleep(1)
    turn_all_off()

def transmit_byte(byte):
    assert(byte <= 0xFF)
    for i in reversed(range(0, 8)):
        bit = (byte >> i) & 0x01;
        if bit == 0:
            fcntl.ioctl(console_fd, KDSETLED, NUM_LED)
        else:
            fcntl.ioctl(console_fd, KDSETLED, CAP_LED)
        time.sleep(1)
        turn_all_off()

def transmit_string(string):
    for byte in string:
        transmit_byte(byte)

blink_all_leds()
transmit_byte(0xAA)
blink_all_leds()