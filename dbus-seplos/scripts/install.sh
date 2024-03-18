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

echo "Install dbus-seplos"
# remount rw
bash /opt/victronenergy/swupdate-scripts/remount-rw.sh

# remove old symlinks
rm -rf /opt/victronenergy/service-templates/dbus-seplos
rm -rf /opt/victronenergy/dbus-seplos

# make sure all necessary files are executable
chmod +x /data/etc/dbus-seplos/scripts/*.sh
chmod +x /data/etc/dbus-seplos/src/*.py
chmod +x /data/etc/dbus-seplos/service/run
chmod +x /data/etc/dbus-seplos/service/log/run

# install by copying files
mkdir /opt/victronenergy/service-templates/dbus-seplos
cp -rf /data/etc/dbus-seplos/service/* /opt/victronenergy/service-templates/dbus-seplos
mkdir /opt/victronenergy/dbus-seplos
cp -rf /data/etc/dbus-seplos /opt/victronenergy

# enable driver for serial-starter
mkdir -p /data/conf/serial-starter.d
cp /data/etc/dbus-seplos/scripts/dbus-seplos.conf /data/conf/serial-starter.d/dbus-seplos.conf

if [$1 == "gui"]; 
then
    # install gui qml
    bash /data/etc/dbus-seplos/scripts/install-gui.sh
    echo "Installed GUI"

# add install-script to rc.local to be ready for firmware update
filename=/data/rc.local
if [ ! -f "$filename" ]; then
    echo "#!/bin/bash" > "$filename"
    chmod 755 "$filename"
fi

if ! grep -qxF "bash /data/etc/dbus-seplos/scripts/install.sh" $filename;
then
    echo "bash /data/etc/dbus-seplos/scripts/install.sh" >> $filename
fi

# kill driver, if running. It gets restarted by the service daemon
bash /data/etc/dbus-seplos/scripts/kill-driver.sh

echo "Installed dbus-seplos"
