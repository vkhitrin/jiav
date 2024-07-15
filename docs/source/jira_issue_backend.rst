##################
jira_issue Backend
##################

Look for a Jira issue status.

**Attributes**

.. list-table::
   :widths: 10 90
   :header-rows: 1

   -  -  Property
      -  Descrption
   -  -  issue
      -  Jira issue key. **[required]**
   -  -  regex
      -  Jira issue status. **[required]**

**Examples**

Verify issue if ``TEST-1`` issue is ``Done``.

.. code:: yaml

   jiav:
     verification_status: "Done"
     verification_steps:
       - name: Check Jira Issue
         backend: jira_issue
         issue: "TEST-1"
         status: "Done"
