Driver installation
===================
.. note:: The driver does not do any setup of your BMS/Battery. You need to have
          a working battery system before you start.

.. note:: The driver is not a replacement for a BMS. It is a tool to monitor your
          battery system. You should always have a working BMS based on CAN
          installed and active.

.. warning:: The driver is only tested with Venus OS > 3.00 and < v3.3. It will
             not work with Venus OS other than that. Secondly it is only tested
             with Seplos BMS hardware v2 and firmware 16.06. I do not know if it
             works with version 3 of the hardware.

Install or update over SSH
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note:: Requires root access.

Log into your Venus OS device using a SSH client like Putty or bash and run
these commands to start the installer:

.. code-block:: bash

   wget -O /tmp/install.sh https://raw.githubusercontent.com/mworion/dbus-seplos/master/install-target.sh
   bash /tmp/install.sh

The installer will download the latest released version of the driver and installs
it on your system. The location of the install will be in

.. code-block:: bash

   /data/etc/dbus-seplos

The installer will also create a service file for the driver and enable it. All
the installations to the system will be done from this origin with symlinks.

In addition the installer will add lines to

.. code-block:: bash

   /data/rc.local

to keep the installation persistent over reboots und firmware updates of the venus
system. Uninstall will remove this entry.

Furthermore the installer will add the following file:

.. code-block:: bash

   /data/conf/serial-starter.d/dbus-seplos.conf

to enable the serial starter daemon to recognize and integrate dbus-seplos
auto-detect for the RS-485 interface.

Last the installer will backup / add some files to the GUI system to make the GUI
aware of the more detailed information provided by dbus-seplos. Uninstall will
remove these files and changes.

You could customize the installation by editing the script. All scripts are located
in the same directory:

.. code-block:: bash

   /data/etc/dbus-seplos/scripts

Settings
^^^^^^^^
Basically no settings could be made as the driver is designed to be plug and play.

Behavior
^^^^^^^^
dbus-seplos will start automatically after installation. The master battery will
be detected and the driver will start to collect data. If you have multiple
batteries, dbus-seplos will detect them and add as much Slave devices as needed.
The addresses selected with the dip switches on the hardware will be used to
identify the driver battery connection. Any change in DIP settings will change
the order and ID of the driver data stored in the dbus system.


