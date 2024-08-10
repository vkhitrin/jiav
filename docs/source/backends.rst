##########
 Backends
##########

Backends in ``jiav`` are used to execute various verification steps.

Each backend represents a distinct method of executing user-defined
logic.

Developers are able to extend ``jiav`` with custom backends, refer to
:ref:`developing backends`.

.. toctree::
   :maxdepth: 1
   :caption: Builtin Backends

   lineinfile_backend
   regexinfile_backend
   jira_issue_backend

.. toctree::
   :maxdepth: 1
   :caption: External Backends

   ansible_backend
   command_backend
