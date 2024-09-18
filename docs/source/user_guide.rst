############
 User Guide
############

.. note::

   |  Please read the :ref:`overview` section before reading this user
      guide.
   |  It contains important information regarding inteactions with Jira.

After following the :ref:`installation guide` instructions, you can use
the ``jiav`` command.

***************
 General Usage
***************

To view the help message, run the following command (applicable for
subcommands as well):

.. code:: bash

   jiav --help

To view the tools version and installed backends, run the following
command:

.. code:: bash

   jiav --version

************
 Exit Codes
************

.. list-table::
   :widths: 10 90
   :header-rows: 1

   -  -  Exit Code
      -  Description
   -  -  ``0``
      -  Successful.
   -  -  ``1``
      -  Issues connecting to Jira.
   -  -  ``2``
      -  Issues authenticating with Jira.
   -  -  ``3``
      -  JQL returned an error.
   -  -  ``4``
      -  No issues returned.
   -  -  ``5``
      -  Invalided manifest (when executing ``jiav validate-manifest``).
   -  -  ``6``
      -  No issues were verified.

*************
 Subcommands
*************

``validate-manifest``
=====================

Validate manifest locally.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   -  -  Options
      -  Environment Variable
      -  Help

   -  -  ``-f``, ``--from-file``
      -  ``JIAV_VALIDATE_MANIFEST_FROM_FILE``
      -  Path to local file to validate. **[required]**

   -  -  ``--help``
      -
      -  Show this message and exit.

Examlpe:

.. code:: bash

   jiav validate-manifest --from-file /path/to/manifest.yaml

``verify``
==========

Verifies issues in Jira.

.. list-table::
   :widths: 15 25 60
   :header-rows: 1

   -  -  Options
      -  Environment Variable
      -  Help

   -  -  ``-j``, ``--jira``
      -  ``JIAV_VERIFY_JIRA``
      -  Jira URL. **[required]**

   -  -  ``-a``, ``--access-token``
      -  ``JIAV_VERIFY_ACCESS_TOKEN``
      -  Personal Access Token (PAT) for self-hosted instances or an API
         token for cloud instances. **[required]**

   -  -  ``-u``, ``--username``
      -  ``JIAV_VERIFY_USERANME``
      -  Cloud Jira username NOTE: Not required for self-hosted
         instances.

   -  -  ``-i``, ``--issue``
      -  ``JIAV_VERIFY_ISSUE``
      -  Issue to verify. NOTE: This argument is mutually exclusive with
         arguments: [query].

   -  -  ``-q``, ``--query``
      -  ``JIAV_VERIFY_QUERY``
      -  JQL query. NOTE: This argument is mutually exclusive with
         arguments: [issue].

   -  -  ``--upload-attachment``

      -  ``JIAV_VERIFY_UPLOAD_ATTACHMENT``

      -  Uploads attachment of execution, this is not safe since all
         users who can access the ticket will be able to view it; refer
         to https://jira.atlassian.com/browse/JRASERVER-3893

   -  -  ``--allow-public-comments``

      -  ``JIAV_VERIFY_ALLOW_PUBLIC_COMMENTS``

      -  Allows to read manifest from non-private comments; this is
         potentially dangerous since unexpected users will be able to
         provide a manifest.

   -  -  ``--no-comment-on-failure``
      -  ``JIAV_VERIFY_NO_COMENT_ON_FAILURE``
      -  Do not post a comment on failed manifest execution.

   -  -  ``--dry-run``
      -  ``JIAV_VERIFY_DRY_RUN``
      -  Execute manifest without updating issues.

   -  -  ``--debug``
      -  ``JIAV_VERIFY_DEBUG``
      -  Enable debug logging.

   -  -  ``--format``
      -  ``JIAV_VERIFY_FORMAT``
      -  Output format. (table|json|yaml)

   -  -  ``--help``
      -
      -  Show this message and exit.

Examlpe:

.. code:: bash

   jiav verify --jira "http://example.com/jira" -a "<ACCESS_TOKEN>" -i 'EXAMPLE-1' --allow-public-comments --upload-attachment
