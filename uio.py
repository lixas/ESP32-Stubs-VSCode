"""
Module: 'uio' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class BufferedWriter:
    """
    A buffer providing higher-level access to a writeable, sequential RawIOBase object. It inherits BufferedIOBase. When writing to this object, data is normally placed into an internal buffer. The buffer will be written out to the underlying RawIOBase object under various conditions, including

    Parameters
    ----------
    - raw
    - buffer_size=DEFAULT_BUFFER_SIZE : An int containing the default buffer size used by the module’s buffered I/O classes. open() uses the file’s blksize (as obtained by os.stat()) if possible.
    """

    def flush(self):
        """
        Force bytes held in the buffer into the raw stream. A BlockingIOError should be raised if the raw stream blocks.
        """
        pass

    def write(self, b) -> int:
        """
        Write the bytes-like object, b, and return the number of bytes written. When in non-blocking mode, a BlockingIOError is raised if the buffer needs to be written out but the raw stream blocks.

        Parameters
        ----------
        - b : byte-like object to be written
        """
        pass


class BytesIO:
    """
    Create an empty BytesIO object, preallocated to hold up to alloc_size number of bytes. That means that writing that amount of bytes won’t lead to reallocation of the buffer, and thus won’t hit out-of-memory situation or lead to memory fragmentation. These constructors are a MicroPython extension and are recommended for usage only in special cases and in system-level libraries, not for end-user applications.
    """

    def close(self):
        """
        Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing) will raise a ValueError.

        As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.
        """
        pass

    def flush(self):
        """
        Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.
        """
        pass

    def getvalue(self) -> bytes:
        """
        Return bytes containing the entire contents of the buffer.
        """
        pass

    def read(self, size=-1) -> bytes:
        """
        Read and return up to size bytes. If the argument is omitted, None, or negative, data is read and returned until EOF is reached. An empty bytes object is returned if the stream is already at EOF.

        Parameters
        ----------
        - size : If the argument is positive, and the underlying raw stream is not interactive, multiple raw reads may be issued to satisfy the byte count (unless EOF is reached first). But for interactive raw streams, at most one raw read will be issued, and a short result does not imply that EOF is imminent.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
        """
        pass

    def readinto(self, b) -> int:
        """
        Read bytes into a pre-allocated, writable bytes-like object b and return the number of bytes read. For example, b might be a bytearray.

        Parameters
        ----------
        - b : bytes

        Like read(), multiple reads may be issued to the underlying raw stream, unless the latter is interactive.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
        """
        pass

    def readline(self, size=-1):
        """
        Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.

        Parameters
        ----------
        - size : number of characters to read.

        If size is specified, at most size characters will be read.
        """
        pass

    def seek(self, offset, whence=SEEK_SET) -> int:
        """
        Change the stream position to the given offset. Behaviour depends on the whence parameter. The default value for whence is SEEK_SET.
        
        Parameters
        ----------
        - offset : 
        - whence : SEEK_SET or SEEK_CUR or SEEK_END

        SEEK_SET or 0: seek from the start of the stream (the default); offset must either be a number returned by TextIOBase.tell(), or zero. Any other offset value produces undefined behaviour.
        
        SEEK_CUR or 1: “seek” to the current position; offset must be zero, which is a no-operation (all other values are unsupported).

        SEEK_END or 2: seek to the end of the stream; offset must be zero (all other values are unsupported).

        Return the new absolute position as an opaque number.
        """
        pass

    def write(self, str) -> int:
        """
        Write the string s to the stream and return the number of characters written.

        Parameters
        ---------
        - str : string to be written
        """
        pass


class FileIO:
    """
    This is type of a file open in binary mode, e.g. using open(name, "rb"). You should not instantiate this class directly.
    """
    def close(self):
        """
        Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing) will raise a ValueError.

        As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.
        """
        pass

    def flush(self):
        """
        Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.
        """
        pass

    def read(self, size=-1) -> bytes:
        """
        Read and return up to size bytes. If the argument is omitted, None, or negative, data is read and returned until EOF is reached. An empty bytes object is returned if the stream is already at EOF.

        Parameters
        ----------
        - size : If the argument is positive, and the underlying raw stream is not interactive, multiple raw reads may be issued to satisfy the byte count (unless EOF is reached first). But for interactive raw streams, at most one raw read will be issued, and a short result does not imply that EOF is imminent.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
        """
        pass

    def readinto(self, b) -> int:
        """
        Read bytes into a pre-allocated, writable bytes-like object b and return the number of bytes read. For example, b might be a bytearray.

        Parameters
        ----------
        - b : bytes

        Like read(), multiple reads may be issued to the underlying raw stream, unless the latter is interactive.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
        """
        pass

    def readline(self, size=-1):
        """
        Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.

        Parameters
        ----------
        - size : number of characters to read.

        If size is specified, at most size characters will be read.
        """
        pass

    def readlines(self, hint=-1):
        """
        Read and return a list of lines from the stream. hint can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds hint.

        Parameters
        ----------
        - hint : 

        Note that it’s already possible to iterate on file objects using for line in file: ... without calling file.readlines().
        """
        pass

    def seek(self, offset, whence=SEEK_SET) -> int:
        """
        Change the stream position to the given offset. Behaviour depends on the whence parameter. The default value for whence is SEEK_SET.
        
        Parameters
        ----------
        - offset : 
        - whence : SEEK_SET or SEEK_CUR or SEEK_END

        SEEK_SET or 0: seek from the start of the stream (the default); offset must either be a number returned by TextIOBase.tell(), or zero. Any other offset value produces undefined behaviour.
        
        SEEK_CUR or 1: “seek” to the current position; offset must be zero, which is a no-operation (all other values are unsupported).

        SEEK_END or 2: seek to the end of the stream; offset must be zero (all other values are unsupported).

        Return the new absolute position as an opaque number.
        """
        pass

    def tell(self):
        """
        Return the current stream position.
        """
        pass

    def write(self, str) -> int:
        """
        Write the string s to the stream and return the number of characters written.

        Parameters
        ---------
        - str : string to be written
        """
        pass


class IOBase:
    ''

class StringIO:
    """
    Create an empty StringIO object, preallocated to hold up to alloc_size number of bytes. That means that writing that amount of bytes won’t lead to reallocation of the buffer, and thus won’t hit out-of-memory situation or lead to memory fragmentation. These constructors are a MicroPython extension and are recommended for usage only in special cases and in system-level libraries, not for end-user applications.

    Parameters
    ----------
    - [string]

    """

    def close(self):
        """
        Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing) will raise a ValueError.

        As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.
        """
        pass

    def flush(self):
        """
        Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.
        """
        pass

    def getvalue(self):
        """
        Get the current contents of the underlying buffer which holds data.
        """
        pass

    def read(self, size=-1) -> bytes:
        """
        Read and return up to size bytes. If the argument is omitted, None, or negative, data is read and returned until EOF is reached. An empty bytes object is returned if the stream is already at EOF.

        Parameters
        ----------
        - size : If the argument is positive, and the underlying raw stream is not interactive, multiple raw reads may be issued to satisfy the byte count (unless EOF is reached first). But for interactive raw streams, at most one raw read will be issued, and a short result does not imply that EOF is imminent.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
        """
        pass

    def readinto(self, b) -> int:
        """
        Read bytes into a pre-allocated, writable bytes-like object b and return the number of bytes read. For example, b might be a bytearray.

        Parameters
        ----------
        - b : bytes

        Like read(), multiple reads may be issued to the underlying raw stream, unless the latter is interactive.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
        """
        pass

    def readline(self, size=-1):
        """
        Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.

        Parameters
        ----------
        - size : number of characters to read.

        If size is specified, at most size characters will be read.
        """
        pass

    def seek(self, offset, whence=SEEK_SET) -> int:
        """
        Change the stream position to the given offset. Behaviour depends on the whence parameter. The default value for whence is SEEK_SET.
        
        Parameters
        ----------
        - offset : 
        - whence : SEEK_SET or SEEK_CUR or SEEK_END

        SEEK_SET or 0: seek from the start of the stream (the default); offset must either be a number returned by TextIOBase.tell(), or zero. Any other offset value produces undefined behaviour.
        
        SEEK_CUR or 1: “seek” to the current position; offset must be zero, which is a no-operation (all other values are unsupported).

        SEEK_END or 2: seek to the end of the stream; offset must be zero (all other values are unsupported).

        Return the new absolute position as an opaque number.
        """
        pass

    def write(self, str) -> int:
        """
        Write the string s to the stream and return the number of characters written.

        Parameters
        ---------
        - str : string to be written
        """
        pass


class TextIOWrapper:
    """
    This is type of a file open in text mode, e.g. using open(name, "rt"). You should not instantiate this class directly.
    """

    def close(self):
        """
        Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing) will raise a ValueError.

        As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.
        """
        pass

    def flush(self):
        """
        Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.
        """
        pass

    def read(self, size=-1) -> bytes:
        """
        Read and return up to size bytes. If the argument is omitted, None, or negative, data is read and returned until EOF is reached. An empty bytes object is returned if the stream is already at EOF.

        Parameters
        ----------
        - size : If the argument is positive, and the underlying raw stream is not interactive, multiple raw reads may be issued to satisfy the byte count (unless EOF is reached first). But for interactive raw streams, at most one raw read will be issued, and a short result does not imply that EOF is imminent.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
        """
        pass

    def readinto(self, b) -> int:
        """
        Read bytes into a pre-allocated, writable bytes-like object b and return the number of bytes read. For example, b might be a bytearray.

        Parameters
        ----------
        - b : bytes

        Like read(), multiple reads may be issued to the underlying raw stream, unless the latter is interactive.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
        """
        pass

    def readline(self, size=-1):
        """
        Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.

        Parameters
        ----------
        - size : number of characters to read.

        If size is specified, at most size characters will be read.
        """
        pass

    def readlines(self, hint=-1):
        """
        Read and return a list of lines from the stream. hint can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds hint.

        Parameters
        ----------
        - hint : 

        Note that it’s already possible to iterate on file objects using for line in file: ... without calling file.readlines().
        """
        pass

    def seek(self, offset, whence=SEEK_SET) -> int:
        """
        Change the stream position to the given offset. Behaviour depends on the whence parameter. The default value for whence is SEEK_SET.
        
        Parameters
        ----------
        - offset : 
        - whence : SEEK_SET or SEEK_CUR or SEEK_END

        SEEK_SET or 0: seek from the start of the stream (the default); offset must either be a number returned by TextIOBase.tell(), or zero. Any other offset value produces undefined behaviour.
        
        SEEK_CUR or 1: “seek” to the current position; offset must be zero, which is a no-operation (all other values are unsupported).

        SEEK_END or 2: seek to the end of the stream; offset must be zero (all other values are unsupported).

        Return the new absolute position as an opaque number.
        """
        pass

    def tell(self):
        """
        Return the current stream position.
        """
        pass

    def write(self, str) -> int:
        """
        Write the string s to the stream and return the number of characters written.

        Parameters
        ---------
        - str : string to be written
        """
        pass


def open(name, mode='r', **kwargs):
    """
    Open a file. Builtin open() function is aliased to this function. All ports (which provide access to file system) are required to support mode parameter, but support for other arguments vary by port.

    Parameters
    ----------
    - name
    - mode='r'
    - **kwargs
    """
    pass

