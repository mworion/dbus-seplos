#!/bin/bash

# remove comment for easier troubleshooting
#set -x

# handle read only mounts
bash /opt/victronenergy/swupdate-scripts/remount-rw.sh

# remove services
rm -rf /service/dbus-seplos.*

# kill driver, if running
pkill -f "supervise dbus-seplos.*"
pkill -f "multilog .* /var/log/dbus-seplos.*"
pkill -f "python .*/dbus-seplos.py"
