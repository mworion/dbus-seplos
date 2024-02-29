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

# remount rw
bash /opt/victronenergy/swupdate-scripts/remount-rw.sh

# remove old files
rm -rf /opt/victronenergy/service/dbus-seplos
rm -rf /opt/victronenergy/service-templates/dbus-seplos
rm -rf /opt/victronenergy/dbus-seplos

# make sure all files are executable
chmod +x /data/etc/dbus-seplos/scripts/*.sh
chmod +x /data/etc/dbus-seplos/src/*.py
chmod +x /data/etc/dbus-seplos/service/run
chmod +x /data/etc/dbus-seplos/service/log/run

# install new files
cp -rf /data/etc/dbus-seplos/service /opt/victronenergy/service-templates/dbus-seplos
mkdir -p /data/conf/serial-starter.d
cp -rf /data/etc/dbus-seplos/scripts/dbus-seplos.conf /data/conf/serial-starter.d/dbus-seplos.conf
mkdir /opt/victronenergy/dbus-seplos
cp -rf /data/etc/dbus-seplos/* /opt/victronenergy/dbus-seplos

# install gui qml
bash /data/etc/dbus-seplos/scripts/install-qml.sh

# kill driver, if running. It gets restarted by the service daemon
pkill -f "supervise dbus-seplos.*"
pkill -f "multilog .* /var/log/dbus-seplos.*"
pkill -f "python .*/seplos_run.py"