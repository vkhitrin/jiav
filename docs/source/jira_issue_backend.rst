####################
 jira_issue Backend
####################

**********
 Overview
**********

``jiav`` can lookup a Jira issue's status to verify issues.

*********
 Example
*********

Basic scenario
==============

Verify issue if ``TEST-1`` issue is ``Done``.

   .. code:: yaml

      jiav:
        verification_status: "Done"
        verification_steps:
          - name: Check Jira Issue
            backend: jira_issue
            issue: "TEST-1"
            status: "Done"

Attributes
==========

issue
-----

Jira issue ``key``.

status
------

Jira issues's status. If this status is met, the invoking issue will be
verified.
