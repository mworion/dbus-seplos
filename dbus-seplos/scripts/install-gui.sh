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

echo "Install GUI"
# backup old PageBattery.qml once. New firmware upgrade will remove the backup
if [ ! -f /opt/victronenergy/gui/qml/PageBattery.qml.backup ]; then
    cp /opt/victronenergy/gui/qml/PageBattery.qml /opt/victronenergy/gui/qml/PageBattery.qml.backup
fi

# copy new PageBattery.qml
cp /data/etc/dbus-seplos/qml/PageBattery.qml /opt/victronenergy/gui/qml/
# copy new PageBatteryCellVoltages
cp /data/etc/dbus-seplos/qml/PageBatteryCellVoltages.qml /opt/victronenergy/gui/qml/
# copy new PageBatteryTemperatures
cp /data/etc/dbus-seplos/qml/PageBatteryTemperatures.qml /opt/victronenergy/gui/qml/

bash /data/etc/dbus-seplos/scripts/restart-gui.sh

echo "GUI installed"