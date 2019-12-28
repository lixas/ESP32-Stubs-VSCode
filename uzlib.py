"""
Module: 'uzlib' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class DecompIO:
    """
    Create a stream wrapper which allows transparent decompression of compressed data in another stream. This allows to process compressed streams with data larger than available heap size. In addition to values described in decompress(), wbits may take values 24..31 (16 + 8..15), meaning that input stream has gzip header.
    """

    def read(self):
        pass

    def readinto(self):
        pass

    def readline(self):
        pass

def decompress(data, wbits=0, bufsize=0) -> bytes:
    """
    Return decompressed data as bytes. wbits is DEFLATE dictionary window size used during compression (8-15, the dictionary size is power of 2 of that value). Additionally, if value is positive, data is assumed to be zlib stream (with zlib header). Otherwise, if it’s negative, it’s assumed to be raw DEFLATE stream. bufsize parameter is for compatibility with CPython and is ignored.

    Parameters
    ----------
    - data
    - wbits=0
    - bufsize=0

    http://docs.micropython.org/en/latest/library/uzlib.html#uzlib.decompress
    """
    pass

