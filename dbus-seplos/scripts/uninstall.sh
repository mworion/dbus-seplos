#!/bin/bash

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

echo "Install dbus-seplos"
# disable driver
bash /data/etc/dbus-seplos/scripts/disable.sh

# remove copied files
rm -rf /service/dbus-seplos.*

# remove logs
rm -rf /var/log/dbus-seplos.ttyUSB*

# remove serial starter extension
filename=/data/conf/serial-starter.d/dbus-seplos.conf
if [ -f "$filename" ];
then
    rm "$filename"
fi

# remove symlinks (soft links)
rm -rf /opt/victronenergy/service-templates/dbus-seplos
rm -rf /opt/victronenergy/dbus-seplos

# restore GUI changes
bash /data/etc/dbus-seplos/scripts/restore-gui.sh

# remove install-script from rc.local
filename=/data/rc.local
if [ -f "$filename" ];
then
  sed -i "/bash \/data\/etc\/dbus-seplos\/scripts\/install.sh/d" $filename
fi

echo "Uninstalled dbus-seplos"

