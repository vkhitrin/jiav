#################
 Getting Started
#################

If you do not have access to a Jira instance or you wish to attempt this
tool in an isolated environment, this guide will help you get started
with a containerized self-hosted version of a `standalone Jira Server
<https://github.com/Addono/docker-jira-software-standalone>`_.

To start a container, use `docker <https://www.docker.com>`_ (or a
compatible container engine like `podman <https://podman.io>`_):

.. note::

   Run the container in the foreground, or else it will exit after
   bootstrapping.

   It might take a few minutes until the Jira will be available on
   ``http://<HOST>:2990/jira``

#. Start the container:

   .. code:: bash

      docker run -it -p 2990:2990 --name jira addono/jira-software-standalone --version 8.14.0

#. |  Login with default credentials:
   |  username: ``admin``
   |  password: ``admin``

#. After logging in, `create
   <https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/>`_
   or `import
   <https://confluence.atlassian.com/confeval/jira-software-evaluator-resources/jira-software-importing-from-other-tools>`_
   a project.

#. `Create a Jira issue
   <https://support.atlassian.com/jira-service-management-cloud/docs/create-issues-and-sub-tasks/#Createanissueandasubtask-Createanissue>`_.

#. `Generate a personal access token
   <https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html>`_.

#. Post a ``jiav`` comment.

#. Execute the tool.
