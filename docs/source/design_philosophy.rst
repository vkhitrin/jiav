###################
 Design Philosophy
###################

**********
 Overview
**********

The goal of this project is to implement an 'auto verification'
workflow, which aims to be generic.

'auto verification' is a procedure where an automated workflow will
fetch and verify issues seamlessly.

****************************
 Auto Verification Workflow
****************************

.. image:: _static/Flow.jpeg

***********
 jiav flow
***********

-  Access the Jira instance using a personal access key
-  Recurse over Jira issues (provided by JQL or manually)
-  In each issue, recurse the comments from the last to first
-  if a valid jiav manifest is found and is in a private comment (or
   public if the user opted in)
-  if there is a match, execute the jiav manifest's commands via the
   specified backend
-  if the execution is successful, verify the issue

Step 1 - Jira Issues Of Interest (“The what”)
=============================================

Issues are marked as 'Issues Of Interest' by the user.

Marked issues are at the center of the workflow.

Automation workflows will go through all relevant issues and will
attempt to perform a user-defined logic in an automated way to try to
verify the issue. Having user-defined input is beneficial due to the
following:

1. Lowering the barrier of entry - this will allow people from different
backgrounds to set rules which are performed in an automated way without
being proficient in the workflow.

2. ‘Truly generic’ - define a robust software-like interface (set of
rules/API) which will allow automation to scale with use cases without
enforcing hard coded scenarios.

Step 2 - CI auto-verification Of Issues Of Interest (“The why”)
===============================================================

CI is an integral part of product development.

Engineers maintain robust CI infrastructures for their products and
strive to have automation for each supported use case that is being
provided/sold to the customers/community.

CI is being run and validated on each release which is deemed worthy by
the engineers. Leveraging the CI for each release will allow engineers
to execute automation to check and validate issues with minimal
interaction for each release.

Step 3 - auto-verification Procedure (“The how”)
================================================

Based on user-defined logic, procedures will be executed and will be
handled accordingly.
