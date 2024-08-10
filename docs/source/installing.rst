####################
 Installation Guide
####################

.. warning::

   Only Python3.8 and above is supported.

*********************
 Install From Remote
*********************

Install from `PyPi <https://pypi.org>`_ using ``pip3``:

.. code::

   pip3 install jiav

Or ``pipx``:

.. code::

   pipx install jiav

*********************
 Install From Source
*********************

Clone the repository from remote:

.. code:: bash

   git clone https://github.com/vkhitrin/jiav.git
   cd jiav

Install ``jiav`` from cloned repo using ``pip``:

.. code:: bash

   pip3 install .

Or `pipx <https://pipx.pypa.io>`_:

.. code:: bash

   pipx install .

As part of development, use `poetry <https://python-poetry.org>`_:

.. code:: bash

   poetry install --with=main,dev,types

***********
 Uninstall
***********

Uninstall using ``pip3``:

.. code:: bash

   pip3 uninstall jiav

Or ``pipx``:

.. code:: bash

   pipx uninstall jiav
