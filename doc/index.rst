Welcome to dbus-seplos !
========================

.. image:: image/overview.png
    :align: center
    :scale: 71%

The basic idea is that MW4 will try to generate "digital twin" for the mount. All
parameter changes for the mount will be sent to it and changes of it's state are
polled to make status visible in MW4. Therefore regular polling of data is needed.

Overview
--------

Known limitations
-----------------
updater application. Please do not interrupt this automation.

Reporting issues
----------------
To have an eye on your setup here are some topics which you could check:

- Mount connection available and stable. Wifi might have performance problems.
  Look for right network settings in mount and local setup.

- Good counter check is review settings, status bars, message window if something
  is going wrong.

To improve quality and usability any feedback is highly welcome! To maintain a good
transparency and professional work for my, please respect the following
recommendations how to feed back.

.. note:: Please report issues / bugs here:

          https://github.com/mworion/MountWizzard4/issues.

          And if you have feature requests discussions or for all other topics of
          interest there is a good place to start here:

          https://github.com/mworion/MountWizzard4/discussions


In case of a bug report please have a good description (maybe a screenshot if it‘s
related to GUI) and add the log file(s). Normally you just could drop the log file
(or PNG in case of a screen shot) directly to the webpage issues on GitHub. In
some cases GitHub does not accept the file format (unfortunately for example FITs
files). I this case, please zip them and drop the zipped file. This will work. If
you have multiple files, please don‘t zip them to one file! I need them separated
and zipped causes more work.

If changes are made due to a feedback, new releases will have a link to the closed
issues on GitHub.


.. toctree::
    :maxdepth: 2

    changelog/index
