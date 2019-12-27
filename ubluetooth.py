"""
Module: 'ubluetooth' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

FLAG_READ = 2
FLAG_WRITE = 8
FLAG_NOTIFY = 16

class UUID:
    """
    Creates a UUID instance with the specified value.

    The value can be either:

    - A 16-bit integer. e.g. 0x2908.
    - A 128-bit UUID string. e.g. '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'.
    """
    pass


class BLE:
    """
    This module provides an interface to a Bluetooth controller on a board. Currently this supports Bluetooth Low Energy (BLE) in Central, Peripheral, Broadcaster, and Observer roles, and a device may operate in multiple roles concurrently.

    This API is intended to match the low-level Bluetooth protocol and provide building-blocks for higher-level abstractions such as specific device types.

    Returns
    -------
    - Singleton BLE object.
    
    http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE
    
    """

    def active(self, activate):
        """
        Optionally changes the active state of the BLE radio, and returns the current state.
        The radio must be made active before using any other methods on this class.

        Parameters
        ----------
        - bool 'activate' : State of radio

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.active

        """
        pass

    def config(self, param):
        """
        Get or set configuration values of the BLE interface. To get a value the parameter name should be quoted as a string, and just one parameter is queried at a time. To set values use the keyword syntax, and one ore more parameter can be set at a time. 

        Parameter
        ----------
        - str 'mac' : Returns the device MAC address. If a device has a fixed address (e.g. PYBD) then it will be returned. Otherwise (e.g. ESP32) a random address will be generated when the BLE interface is made active.
        - str 'rxbuf': Set the size in bytes of the internal buffer used to store incoming events. This buffer is global to the entire BLE driver and so handles incoming data for all events, including all characteristics. Increasing this allows better handling of bursty incoming data (for example scan results) and the ability for a central role to receive larger characteristic values.

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.config

        """
        pass

    def gap_advertise(self, interval_us, adv_data=None, resp_data=None, connectable=True):
        """
        Starts advertising at the specified interval. To stop advertising, set interval_us to None.

        Parameters
        ----------
        - interval_us : interval in microseconds. This interval will be rounded down to the nearest 625us
        - adv_data=None
        - resp_data=None
        - connectable=True

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gap_advertise

        """
        pass

    def gap_connect(self, addr_type, addr, scan_duration_ms=2000):
        """
        Connect to a peripheral. On success, the _IRQ_PERIPHERAL_CONNECT event will be raised.

        Parameters
        ----------
        - addr_type
        - addr
        - scan_duration_ms=2000

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gap_connect

        """
        pass

    def gap_disconnect(self, conn_handle):
        """
        Disconnect the specified connection handle. On success, the _IRQ_PERIPHERAL_DISCONNECT event will be raised. Returns False if the connection handle wasn’t connected, and True otherwise.

        Parameters
        ----------
        - conn_handle

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gap_disconnect

        """
        pass

    def gap_scan(self, duration_ms, interval_us, window_us):
        """
        Run a scan operation lasting for the specified duration (in milliseconds). To scan indefinitely, set duration_ms to 0. To stop scanning, set duration_ms to None.
        Use interval_us and window_us to optionally configure the duty cycle. The scanner will run for window_us microseconds every interval_us microseconds for a total of duration_ms milliseconds. The default interval and window are 1.28 seconds and 11.25 milliseconds respectively (background scanning).
        For each scan result, the _IRQ_SCAN_RESULT event will be raised.
        When scanning is stopped (either due to the duration finishing or when explicitly stopped), the _IRQ_SCAN_COMPLETE event will be raised.

        Parameters
        ----------
        - duration_ms
        - [interval_us]
        - [window_us]

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gap_scan

        """
        pass

    def gattc_discover_characteristics(self, conn_handle, start_handle, end_handle):
        """
        Query a connected peripheral for characteristics in the specified range.For each characteristic discovered, the _IRQ_GATTC_CHARACTERISTIC_RESULT event will be raised.

        Parameters
        ----------
        - conn_handle
        - start_handle
        - end_handle

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gattc_discover_characteristics

        """
        pass

    def gattc_discover_descriptors(self, conn_handle, start_handle, end_handle):
        """
        Query a connected peripheral for descriptors in the specified range. For each descriptor discovered, the _IRQ_GATTC_DESCRIPTOR_RESULT event will be raised.

        Parameters
        ----------
        - conn_handle
        - start_handle
        - end_handle

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gattc_discover_descriptors

        """
        pass

    def gattc_discover_services(self, conn_handle):
        """
        Query a connected peripheral for its services. For each service discovered, the _IRQ_GATTC_SERVICE_RESULT event will be raised.
        
        Parameters
        ----------
        - conn_handle

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gattc_discover_services

        """
        pass

    def gattc_read(self, conn_handle, value_handle):
        """
        Issue a remote read to a connected peripheral for the specified characteristic or descriptor handle. On success, the _IRQ_GATTC_READ_RESULT event will be raised.
        
        Parameters
        ----------
        - conn_handle
        - value_handle

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gattc_read

        """
        pass

    def gattc_write(self, conn_handle, value_handle, data, mode=0):
        """
        Issue a remote write to a connected peripheral for the specified characteristic or descriptor handle.

        The argument mode specifies the write behaviour, with the currently supported values being:

        mode=0 (default) is a write-without-response: the write will be sent to the remote peripheral but no confirmation will be returned, and no event will be raised.
        
        mode=1 is a write-with-response: the remote peripheral is requested to send a response/acknowledgement that it received the data.
        If a response is received from the remote peripheral the _IRQ_GATTC_WRITE_STATUS event will be raised.

        Parameters
        ----------
        - conn_handle
        - value_handle
        - data
        - mode=0

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gattc_write

        """
        pass

    def gatts_notify(self, conn_handle, value_handle, data):
        """
        Notifies a connected central that this value has changed and that it should issue a read of the current value from this peripheral. If data is specified, then the that value is sent to the central as part of the notification, avoiding the need for a separate read request. Note that this will not update the local value stored.

        Parameters
        ----------
        - conn_handle
        - value_handle
        - [data]

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gatts_notify

        """
        pass

    def gatts_read(self, conn_handle):
        """
        Reads the local value for this handle (which has either been written by gatts_write or by a remote central)

        Parameters
        ----------
        - conn_handle

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gatts_read

        """
        pass

    def gatts_register_services(self, services_definition) -> list:
        """
        Configures the peripheral with the specified services, replacing any existing services.

        Parameters
        ----------
        - services_definition : two-element tuple containing a UUID and a list of characteristics. The flags are a bitwise-OR combination of the ubluetooth.FLAG_READ, ubluetooth.FLAG_WRITE and ubluetooth.FLAG_NOTIFY.

        Return
        ------
        Value is a list (one element per service) of tuples (each element is a value handle). Characteristics and descriptor handles are flattened into the same tuple, in the order that they are defined.

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gatts_register_services

        """
        pass

    def gatts_set_buffer(self, value_handle, len, append=False):
        """
        Sets the internal buffer size for a value in bytes. This will limit the largest possible write that can be received. The default is 20.

        Setting append to True will make all remote writes append to, rather than replace, the current value. At most len bytes can be buffered in this way. When you use gatts_read, the value will be cleared after reading. This feature is useful when implementing something like the Nordic UART Service.

        Parameters
        ----------
        - value_handle
        - len
        - append=False

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gatts_set_buffer

        """
        pass

    def gatts_write(self, value_handle, data):
        """
        Writes the local value for this handle, which can be read by a central.

        Parameters
        ----------
        - value_handle
        - data

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.gatts_write

        """
        pass

    def irq(self, handler, trigger=0xffff):
        """
        Registers a callback for events from the BLE stack. The handler takes two arguments, event (which will be one of the codes below) and data (which is an event-specific tuple of values).

        The optional trigger parameter allows you to set a mask of events that your program is interested in. The default is all events.

        Parameters
        ----------
        - handler
        - trigger=0xffff

        http://docs.micropython.org/en/latest/library/ubluetooth.html#ubluetooth.BLE.irq

        """
        pass
