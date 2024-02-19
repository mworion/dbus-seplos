# -*- coding: utf-8 -*-


class Alarm:
    """
    """

    def __init__(self):
        """
        """
        self.number_of_cells: int = 0
        # equalization status
        self.cell_voltage_warning = [None] * 16
        self.cell_temperature_warning = [None] * 4
        self.ambient_temperature_warning: str = None
        self.component_temperature_warning: str = None
        self.dis_charging_current_warning: str = None
        self.pack_voltage_warning: str = None

        # warning 1
        self.voltage_sensing_failure: str = None
        self.temp_sensing_failure: str = None
        self.current_sensing_failure: str = None
        self.power_switch_failure: str = None
        self.cell_voltage_difference_sensing_failure: str = None
        self.charging_switch_failure: str = None
        self.discharging_switch_failure: str = None
        self.current_limit_switch_failure: str = None

        # warning 2
        self.cell_overvoltage: str = None
        self.cell_voltage_low: str = None
        self.pack_overvoltage: str = None
        self.pack_voltage_low: str = None

        # warning 3
        self.charging_temp_high: str = None
        self.charging_temp_low: str = None
        self.discharging_temp_high: str = None
        self.discharging_temp_low: str = None

        # warning 4
        self.ambient_temp_high: str = None
        self.ambient_temp_low: str = None
        self.component_temp_high: str = None

        # warning 5
        self.charging_overcurrent: str = None
        self.discharging_overcurrent: str = None
        self.transient_overcurrent: str = None
        self.output_short_circuit: str = None
        self.transient_overcurrent_lock: str = None
        self.output_short_circuit_lock: str = None

        # warning 6
        self.charging_high_voltage: str = None
        self.intermittent_power_supplement: str = None
        self.soc_low: str = None
        self.cell_low_voltage_forbidden_charging: str = None
        self.output_reverse_protection: str = None
        self.output_connection_failure: str = None

        # power status
        self.discharge_switch: str = None
        self.charge_switch: str = None
        self.current_limit_switch: str = None
        self.heating_limit_switch: str = None

        # equalization status
        self.cell_equalization = [None] * 16

        # system status
        self.discharge: str = None
        self.charge: str = None
        self.floating_charge: str = None
        self.standby: str = None
        self.power_off: str = None

        # disconnection status
        self.cell_disconnection = [None] * 16

        # warning 7
        self.auto_charging_wait: str = None
        self.manual_charging_wait: str = None

        # warning 8
        self.eep_storage_failure: str = None
        self.rtc_clock_failure: str = None
        self.no_calibration_of_voltage: str = None
        self.no_calibration_of_current: str = None
        self.no_calibration_of_null_point: str = None

    @staticmethod
    def stat_20bit_alarm(data: bytes, offset: int, on_off_bit: int = None, 
                         warn_bit: int = None, protection_bit: int = None) -> str:
        """
        """
        data_byte = bytes.fromhex(data.decode('ascii'))[offset]
        if on_off_bit is not None:
            return 'on' if data_byte & (1 << on_off_bit) != 0 else 'off'
        elif warn_bit is not None:
            if data_byte & (1 << warn_bit) != 0:
                return 'warning'
            if protection_bit is not None and data_byte & (1 << protection_bit) != 0:
                return 'protection'
            return 'normal'

    @staticmethod
    def stat_24byte_alarm(data: bytes, offset: int) -> str:
        """
        """
        alarm_type = bytes.fromhex(data.decode('ascii'))[offset]
        if alarm_type == 0:
            return 'normal'
        elif alarm_type == 1:
            return 'trigger_low'
        elif alarm_type == 2:
            return 'trigger_high'
        else:
            return 'trigger_other'

    def get_number_connected_cells(self) -> int:
        """
        """
        return sum(1 for x in self.cell_disconnection if x == 'normal')

    def decode_data(self, data: bytes) -> None:
        """
        """
        # number of cells
        self.number_of_cells = bytes.fromhex(data.decode('ascii'))[2]

        # info 24 byte alarm offsets
        cell_warning_byte_offset = 3
        cell_temperature_warning_byte_offset = 20
        ambient_temperature_warning_byte_offset = 24
        component_temperature_warning_byte_offset = 25
        dis_charging_current_warning_byte_offset = 26
        pack_voltage_warning_byte_offset = 27

        # info 20 bit alarm offsets
        warning_1_alarm_byte_offset = 29
        warning_2_alarm_byte_offset = 30
        warning_3_alarm_byte_offset = 31
        warning_4_alarm_byte_offset = 32
        warning_5_alarm_byte_offset = 33
        warning_6_alarm_byte_offset = 34
        power_status_byte_offset = 35
        equalization_status1_byte_offset = 36
        equalization_status2_byte_offset = 37
        system_status_byte_offset = 38
        disconnection_status1_byte_offset = 39
        disconnection_status2_byte_offset = 40
        warning_7_alarm_byte_offset = 41
        warning_8_alarm_byte_offset = 42

        # info data
        for i in range(self.number_of_cells):
            self.cell_voltage_warning[i] = self.stat_24byte_alarm(
                data=data, offset=cell_warning_byte_offset + i)

        for i in range(4):
            self.cell_temperature_warning[i] = self.stat_24byte_alarm(
                data=data, offset=cell_temperature_warning_byte_offset + i)

        self.ambient_temperature_warning = self.stat_24byte_alarm(
            data=data, offset=ambient_temperature_warning_byte_offset)

        self.component_temperature_warning = self.stat_24byte_alarm(
            data=data, offset=component_temperature_warning_byte_offset)

        self.dis_charging_current_warning = self.stat_24byte_alarm(
            data=data, offset=dis_charging_current_warning_byte_offset)

        self.pack_voltage_warning = self.stat_24byte_alarm(
            data=data, offset=pack_voltage_warning_byte_offset)

        # warning 1
        self.voltage_sensing_failure = self.stat_20bit_alarm(
            data=data, offset=warning_1_alarm_byte_offset, warn_bit=0)
        self.temp_sensing_failure = self.stat_20bit_alarm(
            data=data, offset=warning_1_alarm_byte_offset, warn_bit=1)
        self.current_sensing_failure = self.stat_20bit_alarm(
            data=data, offset=warning_1_alarm_byte_offset, warn_bit=2)
        self.power_switch_failure = self.stat_20bit_alarm(
            data=data, offset=warning_1_alarm_byte_offset, warn_bit=3)
        self.cell_voltage_difference_sensing_failure = self.stat_20bit_alarm(
            data=data, offset=warning_1_alarm_byte_offset, warn_bit=4)
        self.charging_switch_failure = self.stat_20bit_alarm(
            data=data, offset=warning_1_alarm_byte_offset, warn_bit=5)
        self.discharging_switch_failure = self.stat_20bit_alarm(
            data=data, offset=warning_1_alarm_byte_offset, warn_bit=6)
        self.current_limit_switch_failure = self.stat_20bit_alarm(
            data=data, offset=warning_1_alarm_byte_offset, warn_bit=7)

        # warning 2
        self.cell_overvoltage = self.stat_20bit_alarm(
            data=data, offset=warning_2_alarm_byte_offset, warn_bit=0,
            protection_bit=1)
        self.cell_voltage_low = self.stat_20bit_alarm(
            data=data, offset=warning_2_alarm_byte_offset, warn_bit=2,
            protection_bit=3)
        self.pack_overvoltage = self.stat_20bit_alarm(
            data=data, offset=warning_2_alarm_byte_offset, warn_bit=4,
            protection_bit=5)
        self.pack_voltage_low = self.stat_20bit_alarm(
            data=data, offset=warning_2_alarm_byte_offset, warn_bit=6,
            protection_bit=7)

        # warning 3
        self.charging_temp_high = self.stat_20bit_alarm(
            data=data, offset=warning_3_alarm_byte_offset, warn_bit=0,
            protection_bit=1)
        self.charging_temp_low = self.stat_20bit_alarm(
            data=data, offset=warning_3_alarm_byte_offset, warn_bit=2,
            protection_bit=3)
        self.discharging_temp_high = self.stat_20bit_alarm(
            data=data, offset=warning_3_alarm_byte_offset, warn_bit=4,
            protection_bit=5)
        self.discharging_temp_low = self.stat_20bit_alarm(
            data=data, offset=warning_3_alarm_byte_offset, warn_bit=6,
            protection_bit=7)

        # warning 4
        self.ambient_temp_high = self.stat_20bit_alarm(
            data=data, offset=warning_4_alarm_byte_offset, warn_bit=0,
            protection_bit=1)
        self.ambient_temp_low = self.stat_20bit_alarm(
            data=data, offset=warning_4_alarm_byte_offset, warn_bit=2,
            protection_bit=3)
        self.component_temp_high = self.stat_20bit_alarm(
            data=data, offset=warning_4_alarm_byte_offset, warn_bit=4,
            protection_bit=5)

        # warning 5
        self.charging_overcurrent = self.stat_20bit_alarm(
            data=data, offset=warning_5_alarm_byte_offset, warn_bit=0,
            protection_bit=1)
        self.discharging_overcurrent = self.stat_20bit_alarm(
            data=data, offset=warning_5_alarm_byte_offset, warn_bit=2,
            protection_bit=3)
        self.transient_overcurrent = self.stat_20bit_alarm(
            data=data, offset=warning_5_alarm_byte_offset, warn_bit=4)
        self.output_short_circuit = self.stat_20bit_alarm(
            data=data, offset=warning_5_alarm_byte_offset, warn_bit=5)
        self.transient_overcurrent_lock = self.stat_20bit_alarm(
            data=data, offset=warning_5_alarm_byte_offset, warn_bit=6)
        self.output_short_circuit_lock = self.stat_20bit_alarm(
            data=data, offset=warning_5_alarm_byte_offset, warn_bit=7)

        # warning 6
        self.charging_high_voltage = self.stat_20bit_alarm(
            data=data, offset=warning_6_alarm_byte_offset, warn_bit=0)
        self.intermittent_power_supplement = self.stat_20bit_alarm(
            data=data, offset=warning_6_alarm_byte_offset, warn_bit=1)
        self.soc_low = self.stat_20bit_alarm(
            data=data, offset=warning_6_alarm_byte_offset, warn_bit=2,
            protection_bit=3)
        self.cell_low_voltage_forbidden_charging = self.stat_20bit_alarm(
            data=data, offset=warning_6_alarm_byte_offset, warn_bit=4)
        self.output_reverse_protection = self.stat_20bit_alarm(
            data=data, offset=warning_6_alarm_byte_offset, warn_bit=5)
        self.output_connection_failure = self.stat_20bit_alarm(
            data=data, offset=warning_6_alarm_byte_offset, warn_bit=6)

        # power status
        self.discharge_switch = self.stat_20bit_alarm(
            data=data, offset=power_status_byte_offset, on_off_bit=0)
        self.charge_switch = self.stat_20bit_alarm(
            data=data, offset=power_status_byte_offset, on_off_bit=1)
        self.current_limit_switch = self.stat_20bit_alarm(
            data=data, offset=power_status_byte_offset, on_off_bit=2)
        self.heating_limit_switch = self.stat_20bit_alarm(
            data=data, offset=power_status_byte_offset, on_off_bit=3)

        # equalization status 1 + 2
        for i in range(self.number_of_cells):
            on_off_bit = i % 8
            offset = equalization_status1_byte_offset if i < 8 else equalization_status2_byte_offset
            self.cell_equalization[i] = self.stat_20bit_alarm(
                data=data, offset=offset, on_off_bit=on_off_bit)

        # system status
        self.discharge = self.stat_20bit_alarm(
            data=data, offset=system_status_byte_offset, on_off_bit=0)
        self.charge = self.stat_20bit_alarm(
            data=data, offset=system_status_byte_offset, on_off_bit=1)
        self.floating_charge = self.stat_20bit_alarm(
            data=data, offset=system_status_byte_offset, on_off_bit=2)
        self.standby = self.stat_20bit_alarm(
            data=data, offset=system_status_byte_offset, on_off_bit=4)
        self.power_off = self.stat_20bit_alarm(
            data=data, offset=system_status_byte_offset, on_off_bit=5)
        # disconnection status 1 + 2
        for i in range(self.number_of_cells):
            warn_bit = i % 8
            offset = disconnection_status1_byte_offset if i < 8 else disconnection_status2_byte_offset
            self.cell_disconnection[i] = self.stat_20bit_alarm(
                data=data, offset=offset, warn_bit=warn_bit)

        # warning 7
        self.auto_charging_wait = self.stat_20bit_alarm(
            data=data, offset=warning_7_alarm_byte_offset, warn_bit=4)
        self.manual_charging_wait = self.stat_20bit_alarm(
            data=data, offset=warning_7_alarm_byte_offset, warn_bit=5)

        # warning 8
        self.eep_storage_failure = self.stat_20bit_alarm(
            data=data, offset=warning_8_alarm_byte_offset, warn_bit=0)
        self.rtc_clock_failure = self.stat_20bit_alarm(
            data=data, offset=warning_8_alarm_byte_offset, warn_bit=1)
        self.no_calibration_of_voltage = self.stat_20bit_alarm(
            data=data, offset=warning_8_alarm_byte_offset, warn_bit=2)
        self.no_calibration_of_current = self.stat_20bit_alarm(
            data=data, offset=warning_8_alarm_byte_offset, warn_bit=3)
        self.no_calibration_of_null_point = self.stat_20bit_alarm(
            data=data, offset=warning_8_alarm_byte_offset, warn_bit=4)
