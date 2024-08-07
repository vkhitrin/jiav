#################
 Command Backend
#################

**********
 Overview
**********

.. note::

   This backend is shipped externally at `jiav-backend-command
   <https://github.com/vkhitrin/jiav-backend-command>`_.

.. warning::

   |  This is a risky backend since it allows users to run arbitrary
      code.
   |  **Use it at your own risk**.

``jiav`` can execute commands to verify issues.

*********
 Example
*********

Basic scenario
==============

Execute a single command and expect a return code equal to 0:

   .. code:: yaml

      jiav:
        verification_status: "Done"
        verification_steps:
          - name: Check the existence of a command
            backend: shell
            cmd:
              - which
              - openstack
            rc: 0

Negative Testing Scenario
=========================

Execute a command and expect to fail with a return code of 1:

   .. code:: yaml

      jiav:
        verification_status: "Done"
        verification_steps:
          - name: Check the existence of a command
            backend: shell
            cmd: which openstack
            rc: 1

Attributes
==========

cmd
---

Shell command to execute.

rc
--

Return code of the executed command.
