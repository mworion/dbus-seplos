#!/bin/bash

# remove comment for easier troubleshooting
#set -x

# kill driver, if running. It gets restarted by the service daemon
pkill -f "python .*/dbus-seplos.py"
