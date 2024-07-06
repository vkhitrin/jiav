############
 User Guide
############

******
 Jira
******

To use ``jiav``, a user must have generated a Jira `personal access
token
<https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html>`_
when using a self-hosted instance or an `API token
<https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>`_
when using a Jira cloud instance.

Every Jira instance is unique and may contain various attributes, the
user must be familiar with their Jira instance.

All communication with Jira is through the `jira
<https://pypi.org/project/jira/>`_ python module.

*****
 CLI
*****

After following the :ref:`installing:Installation Guide`, the ``jiav``
command will be available.

There are several sub-commands available.

Global Flags
============

-v, --version
-------------

**Required**: False

**Description**: Prints version

**Example**:

.. code:: bash

   jiav --version

-d, --debug
-----------

**Required**: False

**Description**: Will display additional debug verbosely

**Example**:

.. code:: bash

   jiav --debug

Verify
======

Verifies Jira issues.

-f, --format
------------

**Required**: False

**Description**: Output format

**Example**:

.. code:: bash

   jiav verify --format json

-u, --username
--------------

**Required**: False

**Description**: Username to authenticate with for Jira Cloud instance

**Example**:

.. code:: bash

   jiav verify --username test@example.com

-a, --access-token
------------------

**Required**: True

**Description**: Token (API token for Jira Cloud or Personal Access
Token for self-hosted Jira)

**Example**:

.. code:: bash

   jiav verify --access-token QRaG8wgBkSGRBJfx5MKNvKMoVpxao2MUxI68MqLo

-j, --jira
----------

**Required**: True

**Description**: URL of a Jira instance to authenticate with

**Example**:

.. code:: bash

   jiav verify --jira http://localhost

-i, --issue
-----------

**Required**: True, mutually exclusive with ``--query``

**Description**: Jira issue, multiple arguments can be provided

**Example**:

.. code:: bash

   jiav verify --issue KEY-1 --issue KEY-2

-q, --query
-----------

**Required**: True, mutually exclusive with ``--issue``

**Description**: `JQL
<https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/>`_
query

**Example**:

.. code:: bash

   jiav verify --query 'issue="KEY-1"'

--allow-public-comments
-----------------------

**Required**: False

**Description**: Allow reading from public comments, **NOT SAFE**.

**Example**:

.. code:: bash

   jiav verify --allow-public-comments

--upload-attachment-unsafe
--------------------------

**Required**: False

**Description**: Uploads execution output, **NOT SAFE**, refer to
`JRASERVER-3893 <https://jira.atlassian.com/browse/JRASERVER-3893>`_

**Example**:

.. code:: bash

   jiav verify --allow-public-comments

--dry-run
---------

**Required**: False

**Description**: Run as dry run (practice run), will not update issues

**Example**:

.. code:: bash

   jiav verify --dry-run

List backends
=============

List supported backends

**Example**:

.. code:: bash

   jiav list-backends

Validate manifest
=================

Validates manifest

--from-file
-----------

**Required**: True

**Description**: Validates manifest from file

**Example**:

.. code:: bash

   jiav --debug validate-manifest --from-file='/path/to/file'
