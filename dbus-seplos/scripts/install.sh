#!/bin/bash

# remove comment for easier troubleshooting
#set -x

bash /opt/victronenergy/swupdate-scripts/remount-rw.sh

rm -rf /opt/victronenergy/service/dbus-seplos
rm -rf /opt/victronenergy/service-templates/dbus-seplos
rm -rf /opt/victronenergy/dbus-seplos

# install
chmod +x /data/etc/dbus-seplos/scripts/*.sh
chmod +x /data/etc/dbus-seplos/src/*.py
chmod +x /data/etc/dbus-seplos/service/run
chmod +x /data/etc/dbus-seplos/service/log/run

cp -rf /data/etc/dbus-seplos/service /opt/victronenergy/service-templates/dbus-seplos
mkdir -p /data/conf/serial-starter.d
cp -rf /data/etc/dbus-seplos/scripts/dbus-seplos.conf /data/conf/serial-starter.d/dbus-seplos.conf

mkdir /opt/victronenergy/dbus-seplos
cp -rf /data/etc/dbus-seplos/* /opt/victronenergy/dbus-seplos

bash /data/etc/dbus-seplos/scripts/install-qml.sh


# kill driver, if running. It gets restarted by the service daemon
pkill -f "supervise dbus-seplos.*"
pkill -f "multilog .* /var/log/dbus-seplos.*"
pkill -f "python .*/dbus-seplos.py"