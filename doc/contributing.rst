Contributing
============

Thank you for your interest about rivalcfg. You will find here all useful
information to contribute.


Questions
---------

If you have any question, you can:

* `open an issue <https://github.com/flozz/rivalcfg/issues>`_ on Github,
* or `asking on Gitter <https://gitter.im/rivalcfg/Lobby>`_ (I am not always
  available for chatting but I try to answer to everybody).


Unsupported devices
-------------------

You just bought a brand new SteelSeries mouse and it is not supported by
rivalcfg? The first thing to do is to check if someone else already reported
this on the issue tracker on Github:

* https://github.com/flozz/rivalcfg/issues

If not, open an issue providing the following information:

* The mouse ``vendor_id``, ``product_id`` and ``product_string``. On Linux you
  will find this information with the following command::

     lsusb -d 1038:

  Example result for a Rival 100::

     Bus 005 Device 009: ID 1038:1702 SteelSeries ApS SteelSeries Rival 100 Gaming Mouse

* When possible, a link to the product description (open the SteelSeries
  website or any other online shop)

Then, it depend...

Sometime SteelSeries release new mice that are identical to an exiting model
but only will some aesthetic changes (like the Rival 100, Rival 100 Dota
2 Edition, and so on). In that case, I will be easy to support your mouse.

And sometime it is a new model that will need some reverse engineering... This
can only be done by someone that own the mouse. It can be you (it is easier
than you think), it can be me (if I can find someone that can lend me the
mouse) or it can be any other contributor.

You can also consider supporting the project using the ``Sponsor`` button on
Github to allow me to buy new SteelSeries mice in order to support them in
rivalcfg.


Bugs
----

Rivalcfg does not work? Please `open an issue
<https://github.com/flozz/rivalcfg/issues>`_ on Github with as much information
as possible:

* How you installed rivalcfg,
* What is your operating system / Linux distribution (and its version),
* Which SteelSeries mouse you have trouble with,
* All the error messages outputted by rivalcfg,
* ...


Pull Requests
-------------

Please consider `filing a bug <https://github.com/flozz/rivalcfg/issues>`_
before start working on a new feature or on the support of a new mouse. This
will allow us to discuss the best way to make it. This is of course not
necessary if you just want to fix typo in the documentation or small errors in
the code.

Please note that your code must pass tests and follow the coding style defined
in by the `pep8 <https://pep8.org/>`_.


Running The Tests
-----------------

You will first have to install `nox <https://nox.thea.codes/>`_::

    pip install nox

Then you can check for lint error::

    nox --session lint

or run the tests::

    nox --session test

To run the tests only for a specific Python version, you can use following
commands (the corresponding Python interpreter must be installed)::

    nox --session test-2.7
    nox --session test-3.5
    nox --session test-3.6
    nox --session test-3.7
    nox --session test-3.8

