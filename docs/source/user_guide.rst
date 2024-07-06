############
 User Guide
############

******
 Jira
******

To leverage ``jiav``, a user must have generated a Jira `personal access
token
<https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html>`_.

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

.. code::

   jiav --version

-d, --debug
-----------

**Required**: False

**Description**: Will display additional debug verbosely

**Example**:

.. code::

   jiav --debug

Verify
======

Verifies Jira issues.

-f, --format
------------

**Required**: False

**Description**: Output format

**Example**:

.. code::

   jiav verify --format json

-a, --access-token
------------------

**Required**: True

**Description**: Authenticate with Jira using a personal access token

**Example**:

.. code::

   jiav verify --access-api-key QRaG8wgBkSGRBJfx5MKNvKMoVpxao2MUxI68MqLo

-j, --jira
----------

**Required**: True

**Description**: URL of a Jira instance to authenticate with

**Example**:

.. code::

   jiav verify --jira http://localhost

-i, --issue
-----------

**Required**: True, mutually exclusive with ``--query``

**Description**: Jira issue, multiple arguments can be provided

**Example**:

.. code::

   jiav verify --issue KEY-1 --issue KEY-2

-q, --query
-----------

**Required**: True, mutually exclusive with ``--issue``

**Description**: `JQL
<https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/>`_
query

**Example**:

.. code::

   jiav verify --query 'issue="KEY-1"'

--allow-public-comments
-----------------------

**Required**: False

**Description**: Allow reading from public comments, **NOT SAFE**.

**Example**:

.. code::

   jiav verify --allow-public-comments

--upload-attachment-unsafe
--------------------------

**Required**: False

**Description**: Uploads execution output, **NOT SAFE**, refer to
`JRASERVER-3893 <https://jira.atlassian.com/browse/JRASERVER-3893>`_

**Example**:

.. code::

   jiav verify --allow-public-comments

--dry-run
---------

**Required**: False

**Description**: Run as dry run (practice run), will not update issues

**Example**:

.. code::

   jiav verify --dry-run

List backends
=============

List supported backends

**Example**:

.. code::

   jiav list-backends

Validate manifest
=================

Validates manifest

--from-file
-----------

**Required**: True

**Description**: Validates manifest from file

**Example**:

.. code::

   jiav --debug validate-manifest --from-file='/path/to/file'
