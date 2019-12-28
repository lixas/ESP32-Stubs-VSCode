"""
Module: 'uhashlib' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class sha1:
    """
    SHA1 - A previous generation algorithm. Not recommended for new usages, but SHA1 is a part of number of Internet standards and existing applications, so boards targeting network connectivity and interoperability will try to provide this.
    """
    def digest(self):
        """
        Return hash for all data passed through hash, as a bytes object. After this method is called, more data cannot be fed into the hash any longer.

        http://docs.micropython.org/en/latest/library/uhashlib.html#uhashlib.hash.digest
        """
        pass

    def update(self, data):
        """
        Feed more binary data into hash.

        Parameters
        ----------
        - data
        """
        pass


class sha256:
    """
    SHA256 - The current generation, modern hashing algorithm (of SHA2 series). It is suitable for cryptographically-secure purposes. Included in the MicroPython core and any board is recommended to provide this, unless it has particular code size constraints.
    """
    def digest(self):
        """
        Return hash for all data passed through hash, as a bytes object. After this method is called, more data cannot be fed into the hash any longer.

        http://docs.micropython.org/en/latest/library/uhashlib.html#uhashlib.hash.digest
        """
        pass

    def update(self, data):
        """
        Feed more binary data into hash.

        Parameters
        ----------
        - data
        """
        pass

