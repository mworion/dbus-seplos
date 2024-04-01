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

import os
from seplos_utils import logger


def get_CPU_load():
    """
    :return:
    """
    pid = os.getpid()
    command_string = f'top | grep {pid}'
    result = os.popen(command_string).readline()
    logger.info(f'CPU reading for pid {pid}: {result}')
    if not result:
        return None

    rows = result.split()
    if len(rows) > 6:
        return None

    cpu_load_percent = int(rows[6].replace('%', ''))
    logger.info(f'CPU load for pid {pid}: {cpu_load_percent}%')
    return cpu_load_percent
