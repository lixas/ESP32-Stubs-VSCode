"""
Module: 'ubluetooth' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class BLE:
    """Returns the singleton BLE object."""

    def active(active):
        """
        Optionally changes the active state of the BLE radio, and returns the current state.
        The radio must be made active before using any other methods on this class.

        Parameters
        ----------
        bool 'activate' : State of radio
        """
        pass

    def config(param):
        """
        Get or set configuration values of the BLE interface. To get a value the parameter name should be quoted as a string, and just one parameter is queried at a time. To set values use the keyword syntax, and one ore more parameter can be set at a time.

        Parameters
        ----------
        str 'mac' : Returns the device MAC address. If a device has a fixed address (e.g. PYBD) then it will be returned. Otherwise (e.g. ESP32) a random address will be generated when the BLE interface is made active.
        
        str 'rxbuf': Set the size in bytes of the internal buffer used to store incoming events. This buffer is global to the entire BLE driver and so handles incoming data for all events, including all characteristics. Increasing this allows better handling of bursty incoming data (for example scan results) and the ability for a central role to receive larger characteristic values.
        """
        pass

    def gap_advertise():
        """
        Starts advertising at the specified interval. To stop advertising, set interval_us to None.

        Parameters
        ----------
        int "interval_us" : interval in microseconds. This interval will be rounded down to the nearest 625us
        adv_data=None
        resp_data=None
        connectable=True
        """
        pass

    def gap_connect():
        pass

    def gap_disconnect():
        pass

    def gap_scan():
        pass

    def gattc_discover_characteristics():
        pass

    def gattc_discover_descriptors():
        pass

    def gattc_discover_services():
        pass

    def gattc_read():
        pass

    def gattc_write():
        pass

    def gatts_notify():
        pass

    def gatts_read():
        pass

    def gatts_register_services():
        pass

    def gatts_set_buffer():
        pass

    def gatts_write():
        pass

    def irq():
        pass

FLAG_NOTIFY = 16
FLAG_READ = 2
FLAG_WRITE = 8

class UUID:
    """
    Creates a UUID instance with the specified value.

    The value can be either:

    A 16-bit integer. e.g. 0x2908.
    A 128-bit UUID string. e.g. '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'.
    """
