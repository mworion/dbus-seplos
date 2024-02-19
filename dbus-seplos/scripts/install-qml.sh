#!/bin/bash

# remove comment for easier troubleshooting
#set -x

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



# stop gui
svc -d /service/gui
# sleep 1 sec
sleep 1
# start gui
svc -u /service/gui