# -*- coding: utf-8 -*-
import serial
import os
from seplos_battery import SeplosBattery
from seplos_comm import Comm
from seplos_utils import logger


class SeplosPack:
    """
    """
    BATTERY_MASTER_BAUD = 9600
    BATTERY_SLAVE_BAUD = 19200
    MAX_NUMBER_SLAVE_PACKS = 1
    POLL_INTERVAL = 3000

    def __init__(self, battery_port: str) -> None:
        """
        """
        self.battery_port = battery_port
        self.seplos_batteries = []
        self.pos_master = -1
        self.pos_slave = -1
        self.setup_batteries()

    def test_and_add_battery(self, serial_if: serial.Serial, address: int = 0) -> bool:
        """
        """
        comm = Comm(serial_if, address)
        battery = SeplosBattery(comm, port=self.battery_port)
        ok, protocol_data = battery.read_protocol_data()
        if ok:
            self.seplos_batteries.append(battery)
            logger.debug(f'Connected to battery {address}')
        else:
            logger.debug(f'Failed to connect to battery {address}')
        return ok

    def check_master(self) -> bool:
        """
        """
        logger.debug(f'Test master battery at {self.battery_port}')
        serial_if = serial.Serial(port=self.battery_port,
                                  baudrate=self.BATTERY_MASTER_BAUD,
                                  timeout=.5)
        if self.test_and_add_battery(serial_if, address=0):
            return True
        else:
            serial_if.close()
            del serial_if
            return False

    def check_slave(self) -> bool:
        """
        """
        logger.debug(f'Test slave battery at {self.battery_port}')
        serial_if = serial.Serial(port=self.battery_port,
                                  baudrate=self.BATTERY_SLAVE_BAUD,
                                  timeout=0.5)
        slave_found = False
        for address in range(1, self.MAX_NUMBER_SLAVE_PACKS + 1):
            if not self.test_and_add_battery(serial_if, address=address):
                break
            slave_found = True

        if slave_found:
            return True
        else:
            serial_if.close()
            return False

    def setup_batteries(self) -> None:
        """
        """
        logger.info(f'Checking batteries at {self.battery_port}')
        if self.check_master():
            logger.info(f'Master battery found at {self.battery_port}')
            return

        if self.check_slave():
            logger.info(f'Slave batteries found at {self.battery_port}')
