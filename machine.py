"""
Module: 'machine' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class ADC:
    ''
    ATTN_0DB = 0
    ATTN_11DB = 3
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    WIDTH_9BIT = 0
    def atten():
        pass

    def read():
        pass

    def read_u16():
        pass

    def width():
        pass


class DAC:
    ''
    def write():
        pass

DEEPSLEEP = 4
DEEPSLEEP_RESET = 4
EXT0_WAKE = 2
EXT1_WAKE = 3
HARD_RESET = 2

class I2C:
    ''
    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
        pass

PIN_WAKE = 2

class PWM:
    ''
    def deinit():
        pass

    def duty():
        pass

    def freq():
        pass

    def init():
        pass

PWRON_RESET = 1

class Pin:
    ''
    IN = 1
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    PULL_DOWN = 1
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4
    def init():
        pass

    def irq():
        pass

    def off():
        pass

    def on():
        pass

    def value():
        pass


class RTC:
    ''
    def datetime():
        pass

    def init():
        pass

    def memory():
        pass


class SDCard:
    ''
    def deinit():
        pass

    def info():
        pass

    def ioctl():
        pass

    def readblocks():
        pass

    def writeblocks():
        pass

SLEEP = 2
SOFT_RESET = 5

class SPI:
    ''
    LSB = 1
    MSB = 0
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Signal:
    ''
    def off():
        pass

    def on():
        pass

    def value():
        pass

TIMER_WAKE = 4
TOUCHPAD_WAKE = 5

class Timer:
    ''
    ONE_SHOT = 0
    PERIODIC = 1
    def deinit():
        pass

    def init():
        pass

    def value():
        pass


class TouchPad:
    ''
    def config():
        pass

    def read():
        pass


class UART:
    ''
    INV_CTS = 1048576
    INV_RTS = 8388608
    INV_RX = 524288
    INV_TX = 4194304
    def any():
        pass

    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def sendbreak():
        pass

    def write():
        pass

ULP_WAKE = 6

class WDT:
    ''
    def feed():
        pass

WDT_RESET = 3
def deepsleep():
    pass

def disable_irq():
    pass

def enable_irq():
    pass

def freq():
    pass

def idle():
    pass

def lightsleep():
    pass

mem16 = None
mem32 = None
mem8 = None
def reset():
    pass

def reset_cause():
    pass

def sleep():
    pass

def time_pulse_us():
    pass

def unique_id():
    pass

def wake_reason():
    pass

