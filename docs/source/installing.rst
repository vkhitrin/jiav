####################
 Installation Guide
####################

***************
 Prerequisites
***************

.. warning::

   Only Python3.8 and above is supported

Make sure Python3 and pip are installed on the system level or inside a
`virtual environment <https://virtualenv.pypa.io/en/latest/>`_
(recommended).

**************
 Installation
**************

Install from source
===================

Clone repository from remote:

.. code::

   git clone https://github.com/vkhitrin/jiav.git

Install ``jiav`` from cloned repo:

.. code::

   cd jiav
   pip3 install .

Install from remote
===================

.. note::

   jiav is currently not hosted on PyPI

Install from remote repository:

.. code::

   pip3 install git+https://github.com/vkhitrin/jiav

Uninstall
=========

In order to uninstall the tool from system:

.. code::

   pip3 uninstall jiav
