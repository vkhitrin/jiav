#################
 Ansible Backend
#################

.. note::

   This backend is shipped externally at `jiav-backend-ansible
   <https://github.com/vkhitrin/jiav-backend-ansible>`_.

.. warning::

   |  This is a risky backend since it allows users to run arbitrary
      code.
   |  **Use it at your own risk**.

Execute `Ansible <https://www.ansible.com/>`_ playbook.

`ansible-runner <https://ansible.readthedocs.io>`_ is used to execute
ansible playbooks.

Ansible backend requires the user to have Ansible configured.

**Attributes**

.. list-table::
   :widths: 10 90
   :header-rows: 1

   -  -  Property
      -  Descrption
   -  -  playbook
      -  Ansible playbook (formatted in YAML). **[required]**
   -  -  ansible_binary
      -  Path to Ansible binary.

**Examples**

Execute a single task on localhost:

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
