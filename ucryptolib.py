"""
Module: 'ucryptolib' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

MODE_ECB = 1    """Electronic Code Book (ECB)"""
MODE_CBC = 2    """Cipher Block Chaining (CBC)"""
MODE_CTR = 6    """Counter mode (CTR)"""

class aes:
    """
    Initialize cipher object, suitable for encryption/decryption. Note: after initialization, cipher object can be use only either for encryption or decryption. Running decrypt() operation after encrypt() or vice versa is not supported.
    
    Parameters
    ----------
    - key : encryption/decryption key (bytes-like).
    - mode : MODE_ECB or MODE_CBC or MODE_CTR
    - [IV] : initialization vector for CBC mode.
    
    Mode explained
    ----------
    - 1 (or ucryptolib.MODE_ECB if it exists) for Electronic Code Book (ECB).
    - 2 (or ucryptolib.MODE_CBC if it exists) for Cipher Block Chaining (CBC).
    - 6 (or ucryptolib.MODE_CTR if it exists) for Counter mode (CTR).
    
    http://docs.micropython.org/en/latest/library/ucryptolib.html?highlight=ucryptolib#ucryptolib.aes.__init__
    """

    def decrypt(self, in_buf, out_buf):
        """
        Decrypt in_buf. If no out_buf is given result is returned as a newly allocated bytes object. Otherwise, result is written into mutable buffer out_buf. in_buf and out_buf can also refer to the same mutable buffer, in which case data is decrypted in-place.
        
        Parameters
        ----------
        - in_buf
        - [out_buf]
        
        http://docs.micropython.org/en/latest/library/ucryptolib.html?highlight=ucryptolib#ucryptolib.aes.decrypt
        """
        pass

    def encrypt(self, in_buf, out_buf):
        """
        Encrypt in_buf. If no out_buf is given result is returned as a newly allocated bytes object. Otherwise, result is written into mutable buffer out_buf. in_buf and out_buf can also refer to the same mutable buffer, in which case data is encrypted in-place.
        
        Parameters
        ----------
        - in_buf
        - [out_buf]
        
        http://docs.micropython.org/en/latest/library/ucryptolib.html?highlight=ucryptolib#ucryptolib.aes.encrypt
        """
        pass

