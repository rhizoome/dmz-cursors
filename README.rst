===========
DMZ-Cursors
===========

DMZ Cursors in size 24, 28, 32, 40, 48, 56, 64, 72, 80, 88, 96

Based on `Jakub Steiner`_'s DMZ X11 Cursor theme.

.. _`Jakub Steiner`: http://jimmac.musichall.cz/

.. image:: https://1042.ch/ganwell/dmz.svg
   :width: 50%
   :align: center
   :alt: DMZ White

.. image:: https://1042.ch/ganwell/dmz-aa.svg
   :width: 50%
   :align: center
   :alt: DMZ Black

Modern-screens have various DPI, therefore we have to be more flexible in scaling
the cursor. Also with high-resolution beamers, really huge cursors can be handy,
so even the last row can see your cursor.

Install
=======

* Download dmz-white.tar.xz or dmz-black.tar.xz form releases_.

.. _releases: https://github.com/ganwell/dmz-cursors/releases

.. code-block:: bash

   tar xfJ dmz-white.tar.xz
   mkdir -p ~/.icons
   mv dmz-white ~/.icons/default

* Edit .Xresources and set the desired size (ie 48)

.. code-block:: text

   Xcursor.size: 48

Standard dmz-cursor-theme
=========================

* On `Gnome look`_

* In debian_

.. _`Gnome look`: https://www.gnome-look.org/p/999970/
.. _debian: https://packages.debian.org/jessie/gnome/dmz-cursor-theme

What I did
==========

* Generated more sizes

* Set new hotspots

* Removed animated icons

Jean-Louis Fuchs <ganwell@fangorn.ch>
