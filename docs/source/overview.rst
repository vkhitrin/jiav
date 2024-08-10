########
Overview
########

***********************
Communication With Jira
***********************

``jiav`` interacts with Jira instances using REST API using the `jira
<https://jira.readthedocs.io>`_ python library.

Self-hosted
===========

Self-hosted Jira instances require "Personal Access Tokens" (PAT) which
are available starting from release `8.14
<https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html>`_.

Cloud
=====

Cloud Jira instances require Username + `API token
<https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>`_.

Issue workflow
==============

.. warning::

   |  Understanding Jira Issue Workflow is **critical** in order to use
      ``jiav`` successfully.
   |  Please refer to a detailed explanation in Jira's `documentation
      <https://support.atlassian.com/jira-cloud-administration/docs/work-with-issue-workflows/>`_.

``jiav`` will attempt to trasnsition an issue from its current status to
the desired status based on the ``jiav`` manifest.

On a succesful execution, the issue will be transitioned to the
``verified_status`` provided in the manifest.

If a transition is not possible, the tool will raise an exception and
the issue will remain in its current status.

********
Manifest
********

``jiav`` manifest is a YAML-based input used by the tool to achieve an
automatic verification workflow.

Goals
=====

-  Human-readable and machine-readable.
-  Extendable.
-  Robust.

Structure
=========

All manifests are enforced by a schema using `jsonschema
<https://json-schema.org/>`_.

The root manifests contains the following properties

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   -  -  Property
      -  Type
      -  Descrption

   -  -  jiav
      -  Object
      -  The root key of the manifest. **[required]**

   -  -  verified_status
      -  String
      -  The status to transition the issue to on successful
         verification. **[required]**

   -  -  verification_steps

      -  Array

      -  A list of verification steps. Verification steps describe list
         of checks that need to be done in order to verify the issue.
         Each step refers to a backend that will perform the
         verification. **[required]**

Each backend step contains its own set of properties. Please refer to
the backend documentation for more information.

Manifest Example
================

.. code:: yaml

   ---
   jiav:
     verified_status: "Done"
     verification_steps:
       - name: "Check for feature completion"
         backend: "jira_issue"
         issue: "MYPROJECT-20"
         status: "Done"
       - name: "Ensure JUnit XML reported no failures"
         backend: "regexinfile"
         path: "/path/to/junit.xml"
         regex: 'failures="0"'

In the example above, we cover a hyptothetical scenario where we want to
verify that a feature is completed, and the testing is successful. First
we look that the issue ``MYPROJECT-20`` is marked as ``Done``.
Afterwards, we look at a JUnit XML file and ensure that there are no
failures.
