"""
Module: 'btree' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
DESC = 2
INCL = 1
def open(stream, *, flags=0, pagesize=0, cachesize=0, minkeypage=0):
    """
    Open a database from a random-access stream (like an open file). All other parameters are optional and keyword-only, and allow to tweak advanced parameters of the database operation

    Parameters
    ----------
    - stream : 
    - flags=0 : Currently unused.
    - pagesize=0 : Page size used for the nodes in BTree. Acceptable range is 512-65536. If 0, a port-specific default will be used, optimized for port’s memory usage and/or performance.
    - cachesize=0 : Suggested memory cache size in bytes. For a board with enough memory using larger values may improve performance. Cache policy is as follows: entire cache is not allocated at once; instead, accessing a new page in database will allocate a memory buffer for it, until value specified by cachesize is reached. Then, these buffers will be managed using LRU (least recently used) policy. More buffers may still be allocated if needed (e.g., if a database contains big keys and/or values). Allocated cache buffers aren’t reclaimed.
    - minkeypage=0 : Minimum number of keys to store per page. Default value of 0 equivalent to 2.

    Returns a BTree object, which implements a dictionary protocol (set of methods), and some additional methods described below.

    http://docs.micropython.org/en/latest/library/btree.html#btree.open
    """
    pass

