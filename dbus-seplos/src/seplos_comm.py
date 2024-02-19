# -*- coding: utf-8 -*-
import serial
import time
from seplos_utils import logger
from seplos_protocol import is_valid_hex_string, is_valid_frame, is_valid_length
from seplos_protocol import encode_cmd


class Comm:
    """
    """
    NUMBER_OF_RETRIES = 5

    def __init__(self, serial_if: serial.Serial, address: int = 0):
        self.serial_if = serial_if
        self.address = address

    def read_serial_data(self, command: bytes, response_length: int):
        """
        """
        retries = self.NUMBER_OF_RETRIES
        data = None
        while retries > 0:
            self.serial_if.flushOutput()
            self.serial_if.flushInput()
            self.serial_if.write(command)
            try:
                data_raw = self.serial_if.read_until(b'\r')
                data = data_raw[13: -5]

            except serial.serialutil.SerialException:
                logger.debug(f'Serial exception from {self.address}')
                continue

            else:
                if not is_valid_length(data, response_length):
                    continue
                if not is_valid_frame(data=data_raw):
                    continue
                if not is_valid_hex_string(data):
                    continue
                break

            finally:
                retries -= 1

        if retries > 0:
            return True, data
        else:
            logger.debug(f'Exceeded retries from {self.address}')
            return False, data
