############################################################
# -*- coding: utf-8 -*-
#
#  o-o   o--o  o   o  o-o
#  |  \  |   | |   | |
#  |   O O--o  |   |  o-o
#  |  /  |   | |   |     |
#  o-o   o--o   o-o  o--o
#
#
#   o-o  o--o o--o  o     o-o   o-o
#  |     |    |   | |    o   o |
#   o-o  O-o  O--o  |    |   |  o-o
#      | |    |     |    o   o     |
#  o--o  o--o o     O---o o-o  o--o
#
# python-based service for victron cerbo > v3.00
#
# (c) 2025 by mworion
# Licence MIT
#
###########################################################

from seplos_protocol import int_from_ascii
from seplos_utils import roundSec


class Telemetry:
    """
    """
    # data offsets
    cell_number_offset = 4
    cell_voltage_offset = 6
    temps_offset = 72
    dis_charge_current_offset = 96
    total_pack_voltage_offset = 100
    remain_capacity_offset = 104
    battery_capacity_offset = 110
    soc_offset = 114
    rated_capacity_offset = 118
    cycles_offset = 122
    soh_offset = 126
    port_voltage_offset = 130

    def __init__(self):
        """
        """
        # from pack
        self.number_of_cells: int = None
        self.cell_voltage = [None] * 16
        self.temperature = [None] * 4
        self.environ_temperature: float = None
        self.power_temperature: float = None
        self.dis_charge_current: float = None
        self.total_pack_voltage: float = None
        self.remain_capacity: float = None
        self.battery_capacity: float = None
        self.soc: float = None
        self.rated_capacity: float = None
        self.cycles: int = None
        self.soh: float = None
        self.port_voltage: float = None

        # calculated
        self.delta_cell_voltage: float = None
        self.lowest_cell_vid: int = None
        self.lowest_cell_voltage: float = None
        self.highest_cell_vid: int = None
        self.highest_cell_voltage: float = None
        self.lowest_cell_tid: int = None
        self.lowest_cell_temperature: float = None
        self.highest_cell_tid: int = None
        self.highest_cell_temperature: float = None
        self.dis_charge_power: float = None

    def get_lowest_cell_voltage(self) -> (int, float):
        """
        """
        if None in self.cell_voltage:
            return None, None
        lowest_cell = self.cell_voltage.index(min(self.cell_voltage))
        lowest_cell_voltage = self.cell_voltage[lowest_cell]
        return lowest_cell, lowest_cell_voltage

    def get_highest_cell_voltage(self) -> (int, float):
        """
        """
        if None in self.cell_voltage:
            return None, None
        highest_cell = self.cell_voltage.index(max(self.cell_voltage))
        highest_cell_voltage = self.cell_voltage[highest_cell]
        return highest_cell, highest_cell_voltage

    def get_lowest_cell_temperature(self) -> (int, float):
        """
        """
        if None in self.temperature:
            return None, None
        lowest_cell = self.temperature.index(min(self.temperature))
        lowest_cell_temp = self.temperature[lowest_cell]
        return lowest_cell, lowest_cell_temp

    def get_highest_cell_temperature(self) -> (int, float):
        """
        """
        if None in self.temperature:
            return None, None
        highest_cell = self.temperature.index(max(self.temperature))
        highest_cell_temp = self.temperature[highest_cell]
        return highest_cell, highest_cell_temp

    def decode_data(self, data) -> None:
        """
        """
        self.number_of_cells = int_from_ascii(data=data, offset=self.cell_number_offset, size=2)

        for i in range(self.number_of_cells):
            voltage = int_from_ascii(data, self.cell_voltage_offset + i * 4) / 1000
            self.cell_voltage[i] = voltage

        for i in range(0, 4):
            temp = (int_from_ascii(data, self.temps_offset + i * 4) - 2731) / 10
            self.temperature[i] = temp

        self.lowest_cell_vid, self.lowest_cell_voltage = self.get_lowest_cell_voltage()
        self.highest_cell_vid, self.highest_cell_voltage = self.get_highest_cell_voltage()

        if self.lowest_cell_voltage is not None and self.highest_cell_voltage is not None:
            diff = self.highest_cell_voltage - self.lowest_cell_voltage
            self.delta_cell_voltage = roundSec(diff, 3)
        else:
            self.delta_cell_voltage = None

        self.lowest_cell_tid, self.lowest_cell_temperature = self.get_lowest_cell_temperature()
        self.highest_cell_tid, self.highest_cell_temperature = self.get_highest_cell_temperature()

        self.environ_temperature = (int_from_ascii(data, self.temps_offset + 4 * 4) - 2731) / 10
        self.power_temperature = (int_from_ascii(data, self.temps_offset + 5 * 4) - 2731) / 10

        self.dis_charge_current = int_from_ascii(data, self.dis_charge_current_offset, signed=True) / 100
        self.total_pack_voltage = int_from_ascii(data, self.total_pack_voltage_offset) / 100
        self.dis_charge_power = roundSec((self.dis_charge_current * self.total_pack_voltage), 3)

        self.rated_capacity = int_from_ascii(data, self.rated_capacity_offset) / 100
        self.battery_capacity = int_from_ascii(data, self.battery_capacity_offset) / 100
        self.remain_capacity = int_from_ascii(data, self.remain_capacity_offset) / 100

        self.soc = int_from_ascii(data, self.soc_offset) / 10
        self.cycles = int_from_ascii(data, self.cycles_offset)
        self.soh = int_from_ascii(data, self.soh_offset) / 10

        self.port_voltage = int_from_ascii(data, self.port_voltage_offset) / 100
