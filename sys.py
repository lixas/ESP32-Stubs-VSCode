"""
Module: 'sys' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
argv = None
"""A mutable list of arguments the current program was started with."""

byteorder = 'little'
"""The byte order of the system ("little" or "big")."""

implementation = None
"""
Object with information about the current Python implementation. For MicroPython, it has following attributes:
- name - string “micropython”
- version - tuple (major, minor, micro), e.g. (1, 7, 0)
"""
maxsize = 2147483647
"""Maximum value which a native integer type can hold on the current platform, or maximum value representable by MicroPython integer type, if it’s smaller than platform max value (that is the case for MicroPython ports without long int support)."""

modules = None
"""Dictionary of loaded modules. On some ports, it may not include builtin modules."""

path = None
"""A mutable list of directories to search for imported modules."""

platform = 'esp32'
"""The platform that MicroPython is running on. For OS/RTOS ports, this is usually an identifier of the OS, e.g. "linux". For baremetal ports it is an identifier of a board, e.g. "pyboard" for the original MicroPython reference board. It thus can be used to distinguish one board from another. If you need to check whether your program runs on MicroPython (vs other Python implementation), use sys.implementation instead."""

stderr = None
"""Standard error stream."""

stdin = None
"""Standard input stream."""

stdout = None
"""Standard output stream."""

version = '3.4.0'
"""Python language version that this implementation conforms to, as a string."""

version_info = None
"""Python language version that this implementation conforms to, as a tuple of ints."""

def exit(retval):
    """
    Terminate current program with a given exit code. Underlyingly, this function raise as SystemExit exception. If an argument is given, its value given as an argument to SystemExit.

    Parameters
    ----------
    - retval : Return value

    http://docs.micropython.org/en/latest/library/sys.html#sys.exit

    """
    pass


def print_exception(exc, file=sys.stdout):
    """
    Print exception with a traceback to a file-like object file (or sys.stdout by default).

    Parameters
    ----------
    - exc : exception text
    - file=sys.stdout

    This is simplified version of a function which appears in the traceback module in CPython. Unlike traceback.print_exception(), this function takes just exception value instead of exception type, exception value, and traceback object; file argument should be positional; further arguments are not supported. CPython-compatible traceback module can be found in micropython-lib.
    http://docs.micropython.org/en/latest/library/sys.html#sys.print_exception

    """
    pass


