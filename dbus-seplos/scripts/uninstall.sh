#!/bin/bash

# remove comment for easier troubleshooting
#set -x

# disable driver
bash /data/etc/dbus-seplos/scripts/disable.sh
rm -rf /opt/victronenergy/dbus-seplos
rm -rf /opt/victronenergy/service/dbus-seplos
rm -rf /opt/victronenergy/service-templates/dbus-seplos


# restore GUI changes
bash /data/etc/dbus-seplos/scripts/restore-gui.sh

# uninstall modules
# rm -rf /data/etc/dbus-seplos
