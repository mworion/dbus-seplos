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
import time
from dbus.mainloop.glib import DBusGMainLoop
if sys.version_info.major == 2:
    import gobject
else:
    from gi.repository import GLib as gobject
from seplos_dbus import DBUS_SEPLOS
from seplos_pack import SeplosPack
from seplos_utils import logger


def get_port() -> str:
    """
    The port argument is the link in the /dev folder. So the first
    USB serial port will be TTYUSB0.
    """
    if len(sys.argv) == 2:
        logger.info(f"Getting port {sys.argv[1]}")
        return '/dev/' + sys.argv[1]
    else:
        return ''


def main():
    """
    When seplos_run is called, the caller routine adds the actual used
    serial port as argument. For this port all testing is done. Once a
    positive test is done, seplos_dbus will occupy this port for the
    whole lifecycle.
    """
    port = get_port()
    time.sleep(3)
    if not os.path.exists(port):
        logger.error(f'Port {port} does not exist')
        sys.exit(1)

    seplos_pack = SeplosPack(battery_port=port)
    if len(seplos_pack.seplos_batteries) == 0:
        logger.error('No batteries found')
        sys.exit(1)

    DBusGMainLoop(set_as_default=True)
    main_loop = gobject.MainLoop()
    helper = DBUS_SEPLOS(seplos_pack)
    if not helper.setup_vedbus_pack():
        logger.error('Failed to setup dbus')
        sys.exit(1)

    gobject.timeout_add(seplos_pack.POLL_INTERVAL,
                        lambda: helper.publish_battery_pack(main_loop))
    logger.info(f'seplos-dbus started on port {port}')

    try:
        main_loop.run()
    except KeyboardInterrupt:
        pass
    logger.info('seplos-dbus stopped')


if __name__ == '__main__':
    main()
