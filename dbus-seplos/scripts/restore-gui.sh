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

# restore original backup
if [ -f /opt/victronenergy/gui/qml/PageBattery.qml.backup ]; then
    echo "Restoring PageBattery.qml..."
    cp -f /opt/victronenergy/gui/qml/PageBattery.qml.backup /opt/victronenergy/gui/qml/PageBattery.qml
    echo "PageBattery.qml was restored."
fi

bash /data/etc/dbus-seplos/scripts/restart-gui.sh
