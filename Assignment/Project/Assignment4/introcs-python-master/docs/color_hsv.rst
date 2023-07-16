.. introcs documentation master file, created by
   sphinx-quickstart on Thu Jul 26 09:50:44 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. currentmodule:: introcs

HSV
===

``import introcs``

This class represents an HSV color value.  As an additive color, it has conversion 
methods for ``tkinter``, ``kivy`` and ``PIL``.  However, most of these methods require
conversion to RGB color space before use.

HSV colors are represented by a cone.  Pure color values such as red or green
are positioned at the vertical top of the cone, with a ``value`` of 1.0.

Constructor
-----------

.. autoclass:: HSV

Attributes
----------

.. autoattribute:: HSV.hue
.. autoattribute:: HSV.saturation
.. autoattribute:: HSV.value

Methods
-------

.. automethod:: HSV.glColor
.. automethod:: HSV.webColor
.. automethod:: HSV.rgba

.. toctree::
   :maxdepth: 2
   