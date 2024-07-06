####################
 Installation Guide
####################

***************
 Prerequisites
***************

.. warning::

   Only Python3.8 and above is supported.

**************
 Installation
**************

Install From Source
===================

Clone repository from remote:

.. code::

   git clone https://github.com/vkhitrin/jiav.git
   cd jiav

Install ``jiav`` from cloned repo using ``pip``:

.. code::

   pip3 install .

Or `pipx <https://pipx.pypa.io>`_:

.. code::

   pipx install .

As part of development, use `poetry <https://python-poetry.org>`_:

.. code::

   poetry install --with=main,dev

Install From Remote
===================

Install from `PyPi <https://pypi.org>`_ using ``pip3``:

.. code::

   pip3 install jiav

Or ``pipx``:

.. code::

   pipx install jiav

Uninstall
=========

Uninstall using ``pip3``:

.. code::

   pip3 uninstall jiav

Or ``pipx``:

.. code::

   pipx uninstall jiav
