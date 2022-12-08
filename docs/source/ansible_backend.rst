#################
 Ansible Backend
#################

**********
 Overview
**********

.. note::

   This backend is shipped externally at `jiav-backend-ansible
   <https://github.com/vkhitrin/jiav-backend-ansible>`_.

.. note::

   This is a risky backend since it allows users to run arbitrary code,
   and use it at your own risk

``jiav`` can execute `Ansible <https://www.ansible.com/>`_ playbooks
**locally**.

Ansible backend requires the user to have Ansible configured on the
system or in the virtual environment.

*********
 Example
*********

Basic scenario
==============

Execute a single playbook with a single task on localhost:

   .. code:: yaml

      jiav:
        verified_status: 'Done'
        verification_steps:
          - name: ansible test
            backend: ansible
            playbook:
              - hosts: localhost
                tasks:
                  - shell: which openstack

Multiple Plays Scenario
=======================

Execute a playbook on several hosts:

   .. code:: yaml

      jiav:
        verification_steps:
          - name: ansible test
            backend: ansible
            playbook:
              - hosts: localhost
                tasks:
                  - shell: which openstack
              - hosts: tester
                tasks:
                  - shell: which ls

Attributes
==========

playbook
--------

Ansible playbook (formatted in YAML) that will be executed.
