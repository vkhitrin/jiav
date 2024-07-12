###############
 jiav Backends
###############

Backends in ``jiav`` are used to execute various verification steps.

Each backend represents a different way of executing a user-defined
logic.

Developers are able to extend ``jiav`` with custom backends, refer to
:ref:`developing_backends:Developing Backends`.

.. toctree::
   :maxdepth: 1
   :caption: Available backends

   ansible_backend
   lineinfile_backend
   regexinfile_backend
   command_backend
   jira_issue_backend
