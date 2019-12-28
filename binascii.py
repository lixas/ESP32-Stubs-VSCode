"""
Module: 'binascii' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
def a2b_base64(data):
    """
    Decode base64-encoded data, ignoring invalid characters in the input. Conforms to RFC 2045 s.6.8. Returns a bytes object.

    Parameters
    ----------
    - data

    http://docs.micropython.org/en/latest/library/ubinascii.html#ubinascii.a2b_base64

    """
    pass

def b2a_base64(data):
    """
    Encode binary data in base64 format, as in RFC 3548. Returns the encoded data followed by a newline character, as a bytes object.

    Parameters
    ----------
    - data

    http://docs.micropython.org/en/latest/library/ubinascii.html#ubinascii.b2a_base64
    """
    pass

def crc32(data, crc):
    """
    Compute CRC-32, the 32-bit checksum of data, starting with an initial crc

    Parameters
    ----------
    - data : a bytes-like object
    - [crc] int : initial crc sum
    """
    pass

def hexlify(data, sep):
    """
    Convert binary data to hexadecimal representation. Returns bytes string.

    Parameters
    ----------
    - data
    - [sep]

    If additional argument, sep is supplied, it is used as a separator between hexadecimal values.
    http://docs.micropython.org/en/latest/library/ubinascii.html#ubinascii.hexlify

    """
    pass

def unhexlify(data):
    """
    Convert hexadecimal data to binary representation. Returns bytes string. (i.e. inverse of hexlify)

    Parameters
    ----------
    - data

    http://docs.micropython.org/en/latest/library/ubinascii.html#ubinascii.unhexlify
    """
    pass

