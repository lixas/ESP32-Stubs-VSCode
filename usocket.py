"""
Module: 'usocket' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
AF_INET = 2
AF_INET6 = 10
"""Address family types. Availability depends on a particular MicroPython port."""

IPPROTO_IP = 0
IPPROTO_TCP = 6
IPPROTO_UDP = 17
IP_ADD_MEMBERSHIP = 3
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_STREAM = 1
SOL_SOCKET = 4095
SO_REUSEADDR = 4


def getaddrinfo(host, port, af=0, type=0, proto=0, flags=0) -> tuple:
    """
    Translate the host/port argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service. Arguments af, type, and proto (which have the same meaning as for the socket() function) can be used to filter which kind of addresses are returned. If a parameter is not specified or zero, all combinations of addresses can be returned (requiring filtering on the user side).

    Parameters
    ----------
    - host
    - port
    - af=0
    - type=0
    - proto=0
    - flags=0

    The resulting list of 5-tuples has the following structure: (family, type, proto, canonname, sockaddr)

    http://docs.micropython.org/en/latest/library/usocket.html#usocket.getaddrinfo
    """
    pass


class socket:
    ''
    def accept(self):
        """
        Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.accept
        """
        pass

    def bind(self, address):
        """
        Bind the socket to address. The socket must not already be bound.

        Parameters
        ----------
        - address

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.bind
        """
        pass

    def close(self):
        """
        Mark the socket closed and release all resources. Once that happens, all future operations on the socket object will fail. The remote end will receive EOF indication if supported by protocol.

        Sockets are automatically closed when they are garbage-collected, but it is recommended to close() them explicitly as soon you finished working with them.

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.close
        """
        pass

    def connect(self, address):
        """
        Connect to a remote socket at address.

        Parameters
        - address

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.connect
        """
        pass

    def fileno(self) -> int:
        """
        Return the socket’s file descriptor (a small integer), or -1 on failure. This is useful with select.select().

        Under Windows the small integer returned by this method cannot be used where a file descriptor can be used (such as os.fdopen()). Unix does not have this limitation.
        """
        pass

    def listen(self, backlog):
        """
        Enable a server to accept connections. If backlog is specified, it must be at least 0 (if it’s lower, it will be set to 0); and specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.

        Parameters
        ----------
        - [backlog]

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.listen
        """
        pass

    def makefile(self, mode='rb', buffering=0):
        """
        Return a file object associated with the socket. The exact returned type depends on the arguments given to makefile(). The support is limited to binary modes only (‘rb’, ‘wb’, and ‘rwb’). CPython’s arguments: encoding, errors and newline are not supported.

        Parameters
        ----------
        - mode='rb'
        - buffering=0

        Difference to CPython
        ---------------------
        - As MicroPython doesn’t support buffered streams, values of buffering parameter is ignored and treated as if it was 0 (unbuffered).
        - Closing the file object returned by makefile() WILL close the original socket as well.

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.makefile
        """
        pass

    def read(self, size):
        """
        Read up to size bytes from the socket. Return a bytes object. If size is not given, it reads all data available from the socket until EOF; as such the method will not return until the socket is closed. This function tries to read as much data as requested (no “short reads”). This may be not possible with non-blocking socket though, and then less data will be returned.

        Parameters
        ----------
        - [size]

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.read
        """
        pass

    def readinto(self, buf, nbytes):
        """
        Read bytes into the buf. If nbytes is specified then read at most that many bytes. Otherwise, read at most len(buf) bytes. Just as read(), this method follows “no short reads” policy.

        Parameters
        ----------
        - buf
        - [nbytes]

        Return value: number of bytes read and stored into buf.

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.readinto
        """
        pass

    def readline(self):
        """
        Read a line, ending in a newline character.

        Return value: the line read.

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.readline
        """
        pass

    def recv(self, bufsize):
        """
        Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize.
        
        Parameters
        ----------
        - bufsize

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.recv
        """
        pass

    def recvfrom(self, bufsize):
        """
        Receive data from the socket. The return value is a pair (bytes, address) where bytes is a bytes object representing the data received and address is the address of the socket sending the data.
        
        Parameters
        ----------
        - bufsize

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.recvfrom
        """
        pass

    def send(self, bytes):
        """
        Send data to the socket. The socket must be connected to a remote socket. Returns number of bytes sent, which may be smaller than the length of data (“short write”).

        Parameters
        ----------
        - bytes

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.send
        """
        pass

    def sendall(self, bytes):
        """
        Send all data to the socket. The socket must be connected to a remote socket. Unlike send(), this method will try to send all of data, by sending data chunk by chunk consecutively.

        Parameters
        ----------
        - bytes

        The behavior of this method on non-blocking sockets is undefined. Due to this, on MicroPython, it’s recommended to use write() method instead, which has the same “no short writes” policy for blocking sockets, and will return number of bytes sent on non-blocking sockets.

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.sendall
        """
        pass

    def sendto(self, bytes, address):
        """
        Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by address.

        Parameters
        ----------
        - bytes
        - address

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.sendto
        """
        pass

    def setblocking(self, flag):
        """
        Set blocking or non-blocking mode of the socket: if flag is false, the socket is set to non-blocking, else to blocking mode.

        Parameters
        ----------
        - flag

        This method is a shorthand for certain settimeout() calls:
        - sock.setblocking(True) is equivalent to sock.settimeout(None)
        - sock.setblocking(False) is equivalent to sock.settimeout(0)

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.setblocking
        """
        pass

    def setsockopt(self, level, optname, value):
        """
        Set the value of the given socket option. The needed symbolic constants are defined in the socket module (SO_* etc.). The value can be an integer or a bytes-like object representing a buffer.

        Parameters
        - level
        - optname
        - value

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.setsockopt
        """
        pass

    def settimeout(self, value):
        """
        Set a timeout on blocking socket operations. The value argument can be a nonnegative floating point number expressing seconds, or None. If a non-zero value is given, subsequent socket operations will raise an OSError exception if the timeout period value has elapsed before the operation has completed. If zero is given, the socket is put in non-blocking mode. If None is given, the socket is put in blocking mode.

        Parameters
        ----------
        - value

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.settimeout
        """
        pass

    def write(self, buf) ->int:
        """
        Write the buffer of bytes to the socket. This function will try to write all data to a socket (no “short writes”). This may be not possible with a non-blocking socket though, and returned value will be less than the length of buf.

        Parameters
        ----------
        - buf

        Return value: number of bytes written.

        http://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.write
        """
        pass

