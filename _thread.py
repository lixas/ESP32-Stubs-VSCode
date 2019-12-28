"""
Module: '_thread' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class LockType:
    """
    This module provides low-level primitives for working with multiple threads (also called light-weight processes or tasks) — multiple threads of control sharing their global data space. For synchronization, simple locks (also called mutexes or binary semaphores) are provided. The threading module provides an easier to use and higher-level threading API built on top of this module.

    https://docs.python.org/3.9/library/_thread.html#module-_thread
    """
    ''
    def acquire(self, waitflag=1, timeout=-1):
        """
        Without any optional argument, this method acquires the lock unconditionally, if necessary waiting until it is released by another thread (only one thread at a time can acquire a lock — that’s their reason for existence).

        Parameters
        ----------
        - waitflag=1
        - timeout=-1

        If the integer waitflag argument is present, the action depends on its value: if it is zero, the lock is only acquired if it can be acquired immediately without waiting, while if it is nonzero, the lock is acquired unconditionally as above.

        If the floating-point timeout argument is present and positive, it specifies the maximum wait time in seconds before returning. A negative timeout argument specifies an unbounded wait. You cannot specify a timeout if waitflag is zero.

        The return value is True if the lock is acquired successfully, False if not.
        """
        pass

    def locked(self) -> bool:
        """
        Return the status of the lock: True if it has been acquired by some thread, False if not.
        """
        pass

    def release(self):
        """
        Releases the lock. The lock must have been acquired earlier, but not necessarily by the same thread.
        """
        pass

def allocate_lock():
    """
    Return a new lock object. Methods of locks are described below. The lock is initially unlocked.
    """
    pass

def exit():
    """
    Raise the SystemExit exception. When not caught, this will cause the thread to exit silently.
    """
    pass

def get_ident() -> int:
    """
    Return the ‘thread identifier’ of the current thread. This is a nonzero integer. Its value has no direct meaning; it is intended as a magic cookie to be used e.g. to index a dictionary of thread-specific data. Thread identifiers may be recycled when a thread exits and another thread is created.
    """
    pass

def stack_size(size):
    """
    Return the thread stack size used when creating new threads. The optional size argument specifies the stack size to be used for subsequently created threads, and must be 0 (use platform or configured default) or a positive integer value of at least 32,768 (32 KiB). If size is not specified, 0 is used. If changing the thread stack size is unsupported, a RuntimeError is raised. If the specified stack size is invalid, a ValueError is raised and the stack size is unmodified. 32 KiB is currently the minimum supported stack size value to guarantee sufficient stack space for the interpreter itself. Note that some platforms may have particular restrictions on values for the stack size, such as requiring a minimum stack size > 32 KiB or requiring allocation in multiples of the system memory page size - platform documentation should be referred to for more information (4 KiB pages are common; using multiples of 4096 for the stack size is the suggested approach in the absence of more specific information)

    Parameters
    ----------
    - [size]
    """
    pass

def start_new_thread(function, args, kwargs):
    """
    Start a new thread and return its identifier. The thread executes the function function with the argument list args (which must be a tuple). The optional kwargs argument specifies a dictionary of keyword arguments. When the function returns, the thread silently exits. When the function terminates with an unhandled exception, a stack trace is printed and then the thread exits (but other threads continue to run).

    Parameters
    ----------
    - function
    - args
    -[kwargs]
    """
    pass

