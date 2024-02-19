# -*- coding: utf-8 -*-
from seplos_protocol import int_from_ascii
from seplos_utils import roundSec


class Telemetry:
    """
    """
    MIN_CELL_VOLTAGE = 2.5
    MAX_CELL_VOLTAGE = 3.6

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
        self.average_cell_voltage: float = None
        self.delta_cell_voltage: float = None
        self.lowest_cell_vid: int = None
        self.lowest_cell_voltage: float = None
        self.highest_cell_vid: int = None
        self.highest_cell_voltage: float = None
        self.lowest_cell_tid: int = None
        self.lowest_cell_temperature: float = None
        self.highest_cell_tid: int = None
        self.highest_cell_temperature: float = None
        self.min_pack_voltage: float = None
        self.max_pack_voltage: float = None
        self.dis_charge_power: float = None

    def get_lowest_cell_voltage(self) -> tuple:
        """
        """
        lowest_cell = self.cell_voltage.index(min(self.cell_voltage))
        lowest_cell_voltage = self.cell_voltage[lowest_cell]
        return lowest_cell, lowest_cell_voltage

    def get_highest_cell_voltage(self) -> tuple:
        """
        """
        highest_cell = self.cell_voltage.index(max(self.cell_voltage))
        highest_cell_voltage = self.cell_voltage[highest_cell]
        return highest_cell, highest_cell_voltage

    def get_lowest_cell_temperature(self) -> tuple:
        """
        """
        lowest_cell = self.temperature.index(min(self.temperature))
        lowest_cell_temp = self.temperature[lowest_cell]
        return lowest_cell, lowest_cell_temp

    def get_highest_cell_temperature(self) -> tuple:
        """
        """
        highest_cell = self.temperature.index(max(self.temperature))
        highest_cell_temp = self.temperature[highest_cell]
        return highest_cell, highest_cell_temp

    def decode_data(self, data) -> None:
        """
        """
        # data offsets
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
        self.number_of_cells = int_from_ascii(data=data, offset=4, size=2)

        self.min_pack_voltage = self.MIN_CELL_VOLTAGE * self.number_of_cells
        self.max_pack_voltage = self.MAX_CELL_VOLTAGE * self.number_of_cells

        for i in range(self.number_of_cells):
            voltage = int_from_ascii(data, cell_voltage_offset + i * 4) / 1000
            self.cell_voltage[i] = voltage
        for i in range(0, 4):
            temp = (int_from_ascii(data, temps_offset + i * 4) - 2731) / 10
            self.temperature[i] = temp

        self.average_cell_voltage = roundSec((sum(self.cell_voltage)
                                              / len(self.cell_voltage)), 3)

        self.lowest_cell_vid, self.lowest_cell_voltage = self.get_lowest_cell_voltage()
        self.highest_cell_vid, self.highest_cell_voltage = self.get_highest_cell_voltage()
        self.delta_cell_voltage = roundSec((self.highest_cell_voltage - self.lowest_cell_voltage), 3)

        self.lowest_cell_tid, self.lowest_cell_temperature = self.get_lowest_cell_temperature()
        self.highest_cell_tid, self.highest_cell_temperature = self.get_highest_cell_temperature()

        self.environ_temperature = (int_from_ascii(data, temps_offset + 4 * 4) - 2731) / 10
        self.power_temperature = (int_from_ascii(data, temps_offset + 5 * 4) - 2731) / 10

        self.dis_charge_current = int_from_ascii(data, dis_charge_current_offset, signed=True) / 100
        self.total_pack_voltage = int_from_ascii(data, total_pack_voltage_offset) / 100
        self.dis_charge_power = roundSec((self.dis_charge_current * self.total_pack_voltage), 3)

        self.rated_capacity = int_from_ascii(data, rated_capacity_offset) / 100
        self.battery_capacity = int_from_ascii(data, battery_capacity_offset) / 100
        self.remain_capacity = int_from_ascii(data, remain_capacity_offset) / 100

        self.soc = int_from_ascii(data, soc_offset) / 10
        self.cycles = int_from_ascii(data, cycles_offset)
        self.soh = int_from_ascii(data, soh_offset) / 10

        self.port_voltage = int_from_ascii(data, port_voltage_offset) / 100
