"""
Module: 'ure' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2


def compile(regex_str, flags):
    """
    Compile regular expression, return regex object.

    Parameters
    ----------
    - regex_str
    - [flags]

    http://docs.micropython.org/en/latest/library/ure.html#ure.compile
    """
    pass

def match(regex_str, string):
    """
    Compile regex_str and match against string. Match always happens from starting position in a string.

    Parameters
    ----------
    - regex_str
    - string

    http://docs.micropython.org/en/latest/library/ure.html#ure.match
    """
    pass

def search(regex_str, string):
    """
    Compile regex_str and search it in a string. Unlike match, this will search string for first position which matches regex (which still may be 0 if regex is anchored).

    Parameters
    ----------
    - regex_str
    - string

    http://docs.micropython.org/en/latest/library/ure.html#ure.search
    """
    pass

def sub(regex_str, replace, string, count=0, flags=0):
    """
    Compile regex_str and search for it in string, replacing all matches with replace, and returning the new string.

    Parameters
    ----------
    - regex_str
    - replace
    - string
    - count=0
    - flags=0

    replace can be a string or a function. If it is a string then escape sequences of the form \<number> and \g<number> can be used to expand to the corresponding group (or an empty string for unmatched groups). If replace is a function then it must take a single argument (the match) and should return a replacement string.

    If count is specified and non-zero then substitution will stop after this many substitutions are made. The flags argument is ignored.

    Note: availability of this function depends on MicroPython port.
    """
    pass

