"""
Module: 'uselect' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

POLLIN = 1
POLLOUT = 4
POLLERR = 8
POLLHUP = 16

def poll():
    """
    Create an instance of the Poll class.

    http://docs.micropython.org/en/latest/library/uselect.html#uselect.poll
    """
    pass

def select(rlist, wlist, xlist, timeout):
    """
    Wait for activity on a set of objects.

    Parameters
    ----------
    - rlist
    - wlist
    - xlist
    - [timeout]

    This function is provided by some MicroPython ports for compatibility and is not efficient. Usage of Poll is recommended instead.
    """
    pass

