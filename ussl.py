"""
Module: 'ussl' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
def wrap_socket(sock, server_side=False, keyfile=None, certfile=None, cert_reqs=CERT_NONE, ca_certs=None):
    """
    Takes a stream sock (usually usocket.socket instance of SOCK_STREAM type), and returns an instance of ssl.SSLSocket, which wraps the underlying stream in an SSL context. Returned object has the usual stream interface methods like read(), write(), etc. In MicroPython, the returned object does not expose socket interface and methods like recv(), send(). In particular, a server-side SSL socket should be created from a normal socket returned from accept() on a non-SSL listening server socket.

    Depending on the underlying module implementation in a particular MicroPython port, some or all keyword arguments above may be not supported.

    Parameters
    ----------
    - sock
    - server_side=False
    - keyfile=None
    - certfile=None
    - cert_reqs=CERT_NONE
    - ca_certs=None
    """
    pass

