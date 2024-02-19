# -*- coding: utf-8 -*-
import sys
import os
import time
from dbus.mainloop.glib import DBusGMainLoop
if sys.version_info.major == 2:
    import gobject
else:
    from gi.repository import GLib as gobject
from seplos_dbus import DBUS
from seplos_pack import SeplosPack
from seplos_utils import logger


def get_port() -> str:
    """
    """
    if len(sys.argv) == 2:
        logger.info(f"Getting port {sys.argv[1]}")
        return '/dev/' + sys.argv[1]
    else:
        return ''


def main():
    """
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
    helper = DBUS(seplos_pack)
    if not helper.setup_vedbus_pack():
        logger.error('Failed to setup dbus')
        sys.exit(1)

    gobject.timeout_add(seplos_pack.POLL_INTERVAL,
                        lambda: helper.publish_battery_pack(main_loop))

    try:
        main_loop.run()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
