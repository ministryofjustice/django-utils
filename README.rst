Django Utils
============

A set of utilities for MoJ Django-based services:

* ping.json view for IRaT support
* healthcheck.json view for IRaT support with extensible healthchecks
* template context processors for common variables
* template tags for form field and value processing and adding Sentry JS exception handling

healthcheck.json
----------------

Django settings:

.. code-block:: python

    HEALTHCHECKS = [
        'moj_utils.healthcheck_registry.database_healthcheck',
        # override default list of healthcheck callables
    ]
    AUTODISCOVER_HEALTHCHECKS = True  # whether to autodiscover and load healthcheck.py from all installed apps

Installation
------------

At the moment, the only way to install the library is from github

.. code-block:: bash

    pip install git+https://github.com/ministryofjustice/django-utils.git

Copyright
---------

Copyright |copy| 2015 HM Government (Ministry of Justice Digital Services). See
LICENSE for further details.

.. |copy| unicode:: 0xA9 .. copyright symbol
