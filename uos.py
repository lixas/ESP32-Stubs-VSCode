"""
Module: 'uos' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class VfsFat:
    """
    Create a filesystem object that uses the FAT filesystem format. Storage of the FAT filesystem is provided by block_dev. Objects created by this constructor can be mounted using mount().
    """

    def chdir(self):
        pass

    def getcwd(self) -> str:
        pass

    def ilistdir(self):
        pass

    def mkdir(self):
        pass

    def mkfs(self):
        pass

    def mount(self):
        pass

    def open(self):
        pass

    def remove(self):
        pass

    def rename(self):
        pass

    def rmdir(self):
        pass

    def stat(self):
        pass

    def statvfs(self):
        pass

    def umount(self):
        pass


class VfsLfs2:
    """
    Create a filesystem object that uses the littlefs v2 filesystem format. Storage of the littlefs filesystem is provided by block_dev, which must support the extended interface. Objects created by this constructor can be mounted using mount().
    """

    def chdir(self):
        pass

    def getcwd(self) -> str:
        pass

    def ilistdir(self):
        pass

    def mkdir(self):
        pass

    def mkfs(self):
        pass

    def mount(self):
        pass

    def open(self):
        pass

    def remove(self):
        pass

    def rename(self):
        pass

    def rmdir(self):
        pass

    def stat(self):
        pass

    def statvfs(self):
        pass

    def umount(self):
        pass

def chdir(path):
    """
    Change current directory.

    Parameters
    ----------
    - path : 

    http://docs.micropython.org/en/latest/library/uos.html#uos.chdir
    """
    pass

def dupterm(stream_object, index=0):
    """
    Duplicate or switch the MicroPython terminal (the REPL) on the given stream-like object. The stream_object argument must be a native stream object, or derive from uio.IOBase and implement the readinto() and write() methods. The stream should be in non-blocking mode and readinto() should return None if there is no data available for reading.

    Parameters
    ----------
    - stream_object
    - index=0

    After calling this function all terminal output is repeated on this stream, and any input that is available on the stream is passed on to the terminal input.

    The index parameter should be a non-negative integer and specifies which duplication slot is set. A given port may implement more than one slot (slot 0 will always be available) and in that case terminal input and output is duplicated on all the slots that are set.

    If None is passed as the stream_object then duplication is cancelled on the slot given by index.

    The function returns the previous stream-like object in the given slot.

    http://docs.micropython.org/en/latest/library/uos.html#uos.dupterm
    """
    pass

def dupterm_notify(param):
    """
    unknown
    """
    pass

def getcwd() -> str:
    """
    Get the current directory.

    http://docs.micropython.org/en/latest/library/uos.html#uos.getcwd
    """
    pass

def ilistdir(dir):
    """
    This function returns an iterator which then yields tuples corresponding to the entries in the directory that it is listing. With no argument it lists the current directory, otherwise it lists the directory given by dir.

    Parameters
    ----------
    - [dir] : 

    The tuples have the form (name, type, inode[, size]):

    'name' is a string (or bytes if dir is a bytes object) and is the name of the entry;

    'type' is an integer that specifies the type of the entry, with 0x4000 for directories and 0x8000 for regular files;

    'inode' is an integer corresponding to the inode of the file, and may be 0 for filesystems that don’t have such a notion.

    Some platforms may return a 4-tuple that includes the entry’s size. For file entries, size is an integer representing the size of the file or -1 if unknown. Its meaning is currently undefined for directory entries.
    """
    pass

def listdir(dir):
    """
    With no argument, list the current directory. Otherwise list the given directory.

    Parameters
    ----------
    - [dir] : 

    http://docs.micropython.org/en/latest/library/uos.html#uos.listdir
    """
    pass

def mkdir(path):
    """
    Create a new directory.

    Parameters
    ----------
    - path

    http://docs.micropython.org/en/latest/library/uos.html#uos.mkdir
    """
    pass

def mount(fsobj, mount_point, *, readonly):
    """
    Mount the filesystem object fsobj at the location in the VFS given by the mount_point string. fsobj can be a a VFS object that has a mount() method, or a block device. If it’s a block device then the filesystem type is automatically detected (an exception is raised if no filesystem was recognised). mount_point may be '/' to mount fsobj at the root, or '/<name>' to mount it at a subdirectory under the root.

    Parameters
    ----------
    - fsobj
    - mount_point
    - readonly

    If readonly is True then the filesystem is mounted read-only.

    During the mount process the method mount() is called on the filesystem object.

    Will raise OSError(EPERM) if mount_point is already mounted.

    http://docs.micropython.org/en/latest/library/uos.html#uos.mount
    """
    pass

def remove(path):
    """
    Remove a file.

    Parameters
    ----------
    - path

    http://docs.micropython.org/en/latest/library/uos.html#uos.remove
    """
    pass

def rename(old_path, new_path):
    """
    Rename a file.

    Parameters
    ----------
    - old_path
    - new_path

    http://docs.micropython.org/en/latest/library/uos.html#uos.rename
    """
    pass

def rmdir(path):
    """
    Remove a directory.

    Parameters
    ----------
    - path

    http://docs.micropython.org/en/latest/library/uos.html#uos.rmdir
    """
    pass

def stat(path):
    """
    Get the status of a file or directory.

    Parameters
    ----------
    - path

    http://docs.micropython.org/en/latest/library/uos.html#uos.stat
    """
    pass

def statvfs(path) -> tuple:
    """
    Get the status of a fileystem.

    Parameters
    ----------
    - path

    Returns a tuple with the filesystem information in the following order:

    - f_bsize – file system block size
    - f_frsize – fragment size
    - f_blocks – size of fs in f_frsize units
    - f_bfree – number of free blocks
    - f_bavail – number of free blocks for unprivileged users
    - f_files – number of inodes
    - f_ffree – number of free inodes
    - f_favail – number of free inodes for unprivileged users
    - f_flag – mount flags
    - f_namemax – maximum filename length

    Parameters related to inodes: f_files, f_ffree, f_avail and the f_flags parameter may return 0 as they can be unavailable in a port-specific implementation.

    http://docs.micropython.org/en/latest/library/uos.html#uos.statvfs
    """
    pass

def umount(mount_point):
    """
    Unmount a filesystem. mount_point can be a string naming the mount location, or a previously-mounted filesystem object. During the unmount process the method umount() is called on the filesystem object.

    Parameters
    ----------
    - mount_point

    Will raise OSError(EINVAL) if mount_point is not found.
    http://docs.micropython.org/en/latest/library/uos.html#uos.umount
    """
    pass

def uname() -> tuple:
    """
    Return a tuple (possibly a named tuple) containing information about the underlying machine and/or its operating system. The tuple has five fields in the following order, each of them being a string:

    - sysname – the name of the underlying system
    - nodename – the network name (can be the same as sysname)
    - release – the version of the underlying system
    - version – the MicroPython version and build date
    - machine – an identifier for the underlying hardware (eg board, CPU)
    """
    pass

def urandom(n):
    """
    Return a bytes object with n random bytes. Whenever possible, it is generated by the hardware random number generator.

    Parameters
    ----------
    - n

    http://docs.micropython.org/en/latest/library/uos.html#uos.urandom
    """
    pass

