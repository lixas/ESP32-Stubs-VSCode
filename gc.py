"""
Module: 'gc' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
def collect():
    """
    Run a garbage collection.

    http://docs.micropython.org/en/latest/library/gc.html#gc.collect

    """
    pass

def disable():
    """
    Disable automatic garbage collection. Heap memory can still be allocated, and garbage collection can still be initiated manually using gc.collect().

    http://docs.micropython.org/en/latest/library/gc.html#gc.disable

    """
    pass

def enable():
    """
    Enable automatic garbage collection.

    http://docs.micropython.org/en/latest/library/gc.html#gc.enable

    """
    pass

def isenabled() -> boolean:
    """
    Returns the state of garbage collector

    """
    pass

def mem_alloc():
    """
    Return the number of bytes of heap RAM that are allocated.

    http://docs.micropython.org/en/latest/library/gc.html#gc.mem_alloc

    """
    pass

def mem_free():
    """
    Return the number of bytes of available heap RAM, or -1 if this amount is not known.

    http://docs.micropython.org/en/latest/library/gc.html#gc.mem_free

    """
    pass

def threshold(amount):
    """
    Set or query the additional GC allocation threshold. 

    Parameters
    ----------
    - [amount] : 
    
    Normally, a collection is triggered only when a new allocation cannot be satisfied, i.e. on an out-of-memory (OOM) condition. If this function is called, in addition to OOM, a collection will be triggered each time after amount bytes have been allocated (in total, since the previous time such an amount of bytes have been allocated) amount is usually specified as less than the full heap size, with the intention to trigger a collection earlier than when the heap becomes exhausted, and in the hope that an early collection will prevent excessive memory fragmentation. This is a heuristic measure, the effect of which will vary from application to application, as well as the optimal value of the amount parameter.

    Calling the function without argument will return the current value of the threshold. A value of -1 means a disabled allocation threshold.

    http://docs.micropython.org/en/latest/library/gc.html#gc.threshold
    
    """
    pass

