#################
 Ansible Backend
#################

**********
 Overview
**********

.. note::

   This backend is shipped externally at `jiav-backend-ansible
   <https://github.com/vkhitrin/jiav-backend-ansible>`_.

.. warning::

   |  This is a risky backend since it allows users to run arbitrary
      code.
   |  **Use it at your own risk**.

``jiav`` can execute `Ansible <https://www.ansible.com/>`_ playbooks
**locally** (from the same host executing ``jiav``).

Ansible backend requires the user to have Ansible configured.

`ansible-runner
<https://ansible.readthedocs.io/projects/runner/en/latest/>`_ is used to
execute ansible playbooks.

*********
 Example
*********

Basic scenario
==============

Execute an `Ansible playbook
<https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html>`_
with a single task on localhost:

   .. code:: yaml

      jiav:
        verification_status: "Done"
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
        verification_status: "Done"
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
