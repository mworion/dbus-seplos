Cable wiring
============

The wiring is pretty simple.

Step 1:
^^^^^^^

Basis is the wiring of a single or multiple BOX system based on a CAN interface
to the Venus GX. The first step is to unplug the CAN cable and connect as
splitter to the battery box.

.. image:: image/box.png
    :align: center
    :scale: 71%

If you have a multiple box system, you keep the addresses and the wiring of the
other boxes to the first one like before. No change in DIP switching is needed.

I use the following splitter :

https://www.amazon.de/dp/B002XRQHSC?ref_=cm_sw_r_cp_ud_dp_1SV54ZKSBCX76ZBWJSTK&th=1

which worked for me perfectly.

Step 2:
^^^^^^^

Connect the CAN cable from Venus to the left port of the splitter. From then on
the wiring is prepared to support additional RS-485 devices. attached to the
master BMS (Box).

Step 3:
^^^^^^^

To connect to the Master Box, please plug the RS-485 cable to the right port of
the splitter and the second RS-485 cable to the left over connector on the master
battery.

.. image:: image/splitter.png
    :align: center
    :scale: 71%

If you have a single box system, you can connect the RS-485 cable to the splitter.
If you have more than two boxes, no further wiring needed to be done as the master
box will be the gateway for all other boxes as well.

