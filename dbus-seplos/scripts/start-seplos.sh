#!/bin/bash

# remove comment for easier troubleshooting
# set -x

. /opt/victronenergy/serial-starter/run-service.sh

app="python /opt/victronenergy/dbus-seplos/src/seplos_run.py"
start $tty
