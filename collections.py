"""
Module: 'collections' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class OrderedDict:
    """
    Return an instance of a dict subclass, supporting the usual dict methods. An OrderedDict is a dict that remembers the order that keys were first inserted. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.

    Parameters
    ----------
    - [items] : 

    http://docs.micropython.org/en/latest/library/ucollections.html#ucollections.OrderedDict
    """

    def clear(self):
        """
        Remove all elements from the deque leaving it with length 0.

        https://docs.python.org/3/library/collections.html#collections.deque.clear
        """
        pass

    def copy(self):
        """
        Create a shallow copy of the deque.

        https://docs.python.org/3/library/collections.html#collections.deque.copy
        """
        pass

    def fromkeys(self, iterable):
        """
        

        Parameters
        ----------
        - iterable : 
        """
        pass

    def get():
        pass

    def items():
        pass

    def keys():
        pass

    def pop(self, ):
        """
        Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

        """
        pass

    def popitem(self, last=True) -> dict:
        """
        The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if 'last' is true or FIFO order if false.

        Parameters
        ----------
        - last = true : order of return

        https://docs.python.org/3/library/collections.html#collections.OrderedDict.popitem

        """
        pass

    def setdefault():
        pass

    def update():
        pass

    def values():
        pass


class deque:
    """
    Deques (double-ended queues) are a list-like container that support O(1) appends and pops from either side of the deque. New deques are created using the following arguments:

    Parameters
    ----------

    - iterable : must be the empty tuple, and the new deque is created empty.
    - maxlen : must be specified and the deque will be bounded to this maximum length. Once the deque is full, any new items added will discard items from the opposite end.
    - [flags] : can be 1 to check for overflow when adding items.

    As well as supporting bool and len.

    """
    
    
    def append(self, x):
        """
        Add x to the right side of the deque. Raises IndexError if overflow checking is enabled and there is no more room left.

        Parameters
        ----------
        - x

        http://docs.micropython.org/en/latest/library/ucollections.html#ucollections.deque.append
        """
        pass

    def popleft(self):
        """
        Remove and return an item from the left side of the deque. Raises IndexError if no items are present.

        http://docs.micropython.org/en/latest/library/ucollections.html#ucollections.deque.popleft

        """
        pass

def namedtuple(name, fields):
    """
    This is factory function to create a new namedtuple type with a specific name and set of fields. A namedtuple is a subclass of tuple which allows to access its fields not just by numeric index, but also with an attribute access syntax using symbolic field names

    Parameters
    ----------
    - name : name of the tuple
    - fields : sequence of strings specifying field names.

    http://docs.micropython.org/en/latest/library/ucollections.html#ucollections.namedtuple

    """
    pass

