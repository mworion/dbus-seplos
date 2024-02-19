# -*- coding: utf-8 -*-
import logging
import time
import datetime

DRIVER_VERSION = '0.0.1'

logging.Formatter.converter = time.gmtime
timeTag = datetime.datetime.utcnow().strftime('%Y-%m-%d')
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s.%(msecs)03d]'
                           '[%(levelname)1.1s]'
                           '[%(filename)15.15s]'
                           '[%(lineno)4s]'
                           ' %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    )

logger = logging.getLogger('Seplos')


def roundSec(value: float, digits: int) -> float:
    """
    """
    if value is None:
        return None
    return round(value, digits)
