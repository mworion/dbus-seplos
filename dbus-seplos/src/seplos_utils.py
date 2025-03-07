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
import time
import datetime

DRIVER_VERSION = '0.2.0'
SERIAL_TIMEOUT = 2

logging.Formatter.converter = time.gmtime
timeTag = datetime.datetime.utcnow().strftime('%Y-%m-%d')
logging.basicConfig(level=logging.WARNING,
                    format='[%(asctime)s.%(msecs)03d]'
                           '[%(levelname)1.1s]'
                           '[%(filename)15.15s]'
                           '[%(lineno)4s]'
                           ' %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    )

logger = logging.getLogger('dbus-seplos')


def roundSec(value: float, digits: int) -> float:
    """
    """
    if value is None:
        return None
    return round(value, digits)
