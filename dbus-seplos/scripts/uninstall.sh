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
# (c) 2024 by mworion
# Licence MIT
#
###########################################################

# disable driver
bash /data/etc/dbus-seplos/scripts/disable.sh
rm -rf /opt/victronenergy/dbus-seplos
rm -rf /opt/victronenergy/service/dbus-seplos
rm -rf /opt/victronenergy/service-templates/dbus-seplos


# restore GUI changes
bash /data/etc/dbus-seplos/scripts/restore-gui.sh

# uninstall modules
# rm -rf /data/etc/dbus-seplos
