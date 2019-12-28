"""
Module: 'ustruct' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
def calcsize(fmt) -> int:
    """
    Return the number of bytes needed to store the given fmt.

    Parameters
    ----------
    - fmt

    http://docs.micropython.org/en/latest/library/ustruct.html#ustruct.calcsize
    """
    pass

def pack(fmt, v1, v2):
    """
    Pack the values v1, v2, ... according to the format string fmt. The return value is a bytes object encoding the values.

    Parameters
    ----------
    - fmt
    - v1
    - v2
    - ...

    http://docs.micropython.org/en/latest/library/ustruct.html#ustruct.pack
    """
    pass

def pack_into(fmt, buffer, offset, v1, v2):
    """
    Pack the values v1, v2, ... according to the format string fmt into a buffer starting at offset. offset may be negative to count from the end of buffer.

    Parameters
    ----------
    - fmt
    - buffer
    - offset
    - v1
    - v2
    - ...

    http://docs.micropython.org/en/latest/library/ustruct.html#ustruct.pack_into
    """
    pass

def unpack(fmt, data) -> tuple:
    """
    Unpack from the data according to the format string fmt. The return value is a tuple of the unpacked values.

    Parameters
    ----------
    - fmt
    - data

    http://docs.micropython.org/en/latest/library/ustruct.html#ustruct.unpack
    """
    pass

def unpack_from(fmt, data, offset=0) -> tuple:
    """
    Unpack from the data starting at offset according to the format string fmt. offset may be negative to count from the end of buffer. The return value is a tuple of the unpacked values.

    Parameters
    ----------
    - fmt
    - data
    - offset=0

    http://docs.micropython.org/en/latest/library/ustruct.html#ustruct.unpack_from
    """
    pass

