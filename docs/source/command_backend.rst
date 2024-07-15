#################
 command Backend
#################

.. note::

   This backend is shipped externally at `jiav-backend-command
   <https://github.com/vkhitrin/jiav-backend-command>`_.

.. warning::

   |  This is a risky backend since it allows users to run arbitrary
      code.
   |  **Use it at your own risk**.

Execute shell commands.

**Attributes**

.. list-table::
   :widths: 10 90
   :header-rows: 1

   -  -  Property
      -  Descrption
   -  -  cmd
      -  Shell command to execute. **[required]**
   -  -  rc
      -  Expected return code. **[required]**

**Examples**

Execute a single command and expect a return code equal to ``0``:

.. code:: yaml

   jiav:
     verification_status: "Done"
     verification_steps:
       - name: Check the existence of a command
         backend: shell
         cmd:
           - which
           - ls
         rc: 0

Execute a command and expect to fail with a return code of ``1``:

.. code:: yaml

   jiav:
     verification_status: "Done"
     verification_steps:
       - name: Check the existence of a command
         backend: shell
         cmd:
           - which
           - ls
         rc: 1
