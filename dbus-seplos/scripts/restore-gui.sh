#!/bin/bash

# remove comment for easier troubleshooting
#set -x

# restore original backup
if [ -f /opt/victronenergy/gui/qml/PageBattery.qml.backup ]; then
    cp -f /opt/victronenergy/gui/qml/PageBattery.qml.backup /opt/victronenergy/gui/qml/PageBattery.qml
    echo "PageBattery.qml was restored."
fi

#stop gui
svc -d /service/gui
#sleep 1 sec
sleep 1
#start gui
svc -u /service/gui
