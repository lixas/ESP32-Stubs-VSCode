"""
Module: 'ujson' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
def dump(obj, stream) -> str:
    """
    Serialise obj to a JSON string, writing it to the given stream.

    Parameters
    ----------
    - obj
    - stream

    http://docs.micropython.org/en/latest/library/ujson.html#ujson.dump
    """
    pass

def dumps(obj):
    """
    Return obj represented as a JSON string.

    Parameters
    ----------
    - obj

    http://docs.micropython.org/en/latest/library/ujson.html#ujson.dumps
    """
    pass

def load(stream) -> object:
    """
    Parse the given stream, interpreting it as a JSON string and deserialising the data to a Python object. The resulting object is returned.

    Parameters
    ----------
    - stream

    Parsing continues until end-of-file is encountered. A ValueError is raised if the data in stream is not correctly formed.

    http://docs.micropython.org/en/latest/library/ujson.html#ujson.load
    """
    pass

def loads(str) -> object:
    """
    Parse the JSON str and return an object. Raises ValueError if the string is not correctly formed.

    Parameters
    ----------
    - str

    http://docs.micropython.org/en/latest/library/ujson.html#ujson.loads
    """
    pass

