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

echo "Disable dbus-seplos driver"
# handle read only mounts
bash /opt/victronenergy/swupdate-scripts/remount-rw.sh

# remove services
rm -rf /service/dbus-seplos.*

# kill driver, if running. It gets restarted by the service daemon
bash /data/etc/dbus-seplos/scripts/kill-driver.sh

echo "Disabled dbus-seplos driver"
