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
import sys
import os
from unittest.mock import Mock, patch
import unittest.mock as mock
import pytest

sys.modules['dbus.mainloop.glib'] = Mock()
sys.modules['gi.repository'] = Mock()
sys.modules['seplos_dbus'] = Mock()

from src.seplos_run import get_port, main


def test_get_port_1():
    parameters = ['seplos_run.py', 'ttyUSB0']
    result = get_port(parameters)
    assert result == '/dev/ttyUSB0'


def test_get_port_2():
    parameters = ['seplos_run.py']
    result = get_port(parameters)
    assert result == ''


def test_main_1():
    parameters = []
    with pytest.raises(SystemExit) as e:
        with mock.patch.object(os.path, 'exists',
                               return_value=False):
            main(parameters)
            assert e.type == SystemExit
            assert e.value.code == 1


class Test2:
    seplos_batteries = []

    def __init__(self, battery_port):
        pass


@patch('src.seplos_run.SeplosPack', Test2)
def test_main_2():
    parameters = []

    with pytest.raises(SystemExit) as e:
        with mock.patch.object(os.path, 'exists',
                               return_value=True):
            main(parameters)
            assert e.type == SystemExit
            assert e.value.code == 1


class Test3:
    seplos_batteries = [1]
    POLL_INTERVAL = 3000

    def __init__(self, battery_port):
        pass


class Test4:
    def __init__(self, dummy):
        pass

    def setup_vedbus_pack(self):
        return False


@patch('src.seplos_run.SeplosPack', Test3)
@patch('src.seplos_run.DBUS_SEPLOS', Test4)
def test_main_3():
    parameters = []

    with pytest.raises(SystemExit) as e:
        with mock.patch.object(os.path, 'exists',
                               return_value=True):
            main(parameters)
            assert e.type == SystemExit
            assert e.value.code == 1


class Test5:
    def __init__(self, dummy):
        pass

    def setup_vedbus_pack(self):
        return True


@patch('src.seplos_run.SeplosPack', Test3)
@patch('src.seplos_run.DBUS_SEPLOS', Test5)
def test_main_4():
    parameters = []

    with mock.patch.object(os.path, 'exists',
                           return_value=True):
        main(parameters)
