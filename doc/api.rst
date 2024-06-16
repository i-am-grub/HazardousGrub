Plugin API 
==============

RotorHazard makes use of externally loaded plugins to extend its functionality and behavior.

.. comment

    The following determines what modules from this repo will be documented

.. automodule::
    :toctree: _autosummary
    :template: full-mod-template.rst
    :recursive:

    rhapi

.. autosummary::
    :toctree: _autosummary
    :template: partial-mod-template.rst
    :recursive:

    Database
    data_export
    data_import
    EventActions
    eventmanager
    HeatGenerator
    led_event_manager
    Results
    RHRace
    RHUI
    RHUtils
    VRxControl
    sensor
