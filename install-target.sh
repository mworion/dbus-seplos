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

echo "o-o   o--o  o   o  o-o            "
echo "|  \  |   | |   | |               "
echo "|   O O--o  |   |  o-o            "
echo "|  /  |   | |   |     |           "
echo "o-o   o--o   o-o  o--o            "
echo "                                  "
echo "                                  "
echo " o-o  o--o o--o  o     o-o   o-o  "
echo "|     |    |   | |    o   o |     "
echo " o-o  O-o  O--o  |    |   |  o-o  "
echo "    | |    |     |    o   o     | "
echo "o--o  o--o o     O---o o-o  o--o  "
echo "                                  "
echo "Download latest dbus-seplos"
curl -s https://api.github.com/repos/mworion/dbus-seplos/releases/latest | grep "browser_download_url.*gz" | cut -d : -f 2,3 | tr -d \" | wget -qi -
tar -xvzf dbus-seplos.tar.gz
rm -rf /data/etc/dbus-seplos
mv ./dbus-seplos /data/etc
rm dbus-seplos.tar.gz
/data/etc/dbus-seplos/scripts/install.sh
echo "Download and copy dbus-seplos done"
