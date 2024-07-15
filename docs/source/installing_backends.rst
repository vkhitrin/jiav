#####################
 Installing Backends
#####################

.. note::

   Please ensure ``jiav`` is installed; refer to :ref:`Installation
   Guide`.

Vadlid backends can be installed in an environment containing ``jiav``.
Backend authors can distribute backends as PyPI packages or as source
code.

Exameple of installing remote :ref:`Ansible Backend`:

Using ``pip3``:

.. code:: bash

   pip3 install jiav-ansible-backend

Or ``pipx``:

.. code:: bash

   pipx inject jiav jiav-ansible-backend

For a list of available backends, refer to :ref:`Backends`.
