"""
Module: 'esp32' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class Partition:
    ''
    BOOT = 0
    RUNNING = 1
    TYPE_APP = 0
    TYPE_DATA = 1
    def find():
        pass

    def get_next_update():
        pass

    def info():
        pass

    def ioctl():
        pass

    def readblocks():
        pass

    def set_boot():
        pass

    def writeblocks():
        pass


class ULP:
    ''
    RESERVE_MEM = 0
    def load_binary():
        pass

    def run():
        pass

    def set_wakeup_period():
        pass

WAKEUP_ALL_LOW = None
WAKEUP_ANY_HIGH = None
def hall_sensor():
    pass

def raw_temperature():
    pass

def wake_on_ext0():
    pass

def wake_on_ext1():
    pass

def wake_on_touch():
    pass

