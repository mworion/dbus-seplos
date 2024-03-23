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
# (c) 2024 by mworion
# Licence MIT
#
###########################################################

from src.seplos_telemetry import Telemetry


def test_get_lowest_cell_voltage_1():
    telemetry = Telemetry()
    telemetry.cell_voltage = [
        3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5,
        2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7
    ]
    result = telemetry.get_lowest_cell_voltage()
    assert result == (15, 1.7)


def test_get_highest_cell_voltage_1():
    telemetry = Telemetry()
    telemetry.cell_voltage = [
        3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5,
        2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7
    ]
    result = telemetry.get_highest_cell_voltage()
    assert result == (0, 3.2)


def test_get_lowest_cell_temperature_1():
    telemetry = Telemetry()
    telemetry.temperature = [1.0, 2.0, 3.0, 4.0]
    result = telemetry.get_lowest_cell_temperature()
    assert result == (0, 1.0)


def test_get_highest_cell_temperature_1():
    telemetry = Telemetry()
    telemetry.temperature = [1.0, 2.0, 3.0, 4.0]
    result = telemetry.get_highest_cell_temperature()
    assert result == (3, 4.0)


def test_decode_data_1():
    data = ""
    telemetry = Telemetry()
    telemetry.decode_data(data)
    assert telemetry.number_of_cells == 0
