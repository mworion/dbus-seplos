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

import logging
from src.seplos_utils import roundSec, DRIVER_VERSION, logger


def test_roundSec_1():
    digits = 2
    value = 1.234567
    result = roundSec(value, digits)
    assert result == 1.23


def test_roundSec_2():
    digits = 2
    value = None
    result = roundSec(value, digits)
    assert result is None


def test_driver_version_1():
    result = DRIVER_VERSION
    assert result is not None


def test_driver_version_2():
    result = DRIVER_VERSION
    assert isinstance(result, str)


def test_logger_1():
    result = logger
    assert result is not None


def test_logger_2():
    result = logger
    assert isinstance(result, logging.Logger)
