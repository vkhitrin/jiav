##########
About jiav
##########

**J**\ira **I**\ssues **A**\uto **V**\erification.  

.. video:: _static/jiav.mp4
   :width: 600

``jiav`` is a `Python <https://www.python.org>`_ based auto verification
tool for `Jira <https://www.atlassian.com/software/jira>`_.

The primary goal is to provide a robust auto-verification
workflow while focusing on ease of use and simplicity.

Users provide a YAML-formatted comment in Jira issues, and the tool will execute it.
On successful execution, the issue will move to the desired status.

Both self-hosted and cloud Jira instances are supported.

.. toctree::
   :hidden:
   :caption: Installation
   :glob:

   installing
   installing_backends

.. toctree::
   :hidden:
   :caption: Using jiav
   :glob:

   overview
   user_guide
   getting_started 
   backends

.. toctree::
   :hidden:
   :caption: Developing jiav
   :glob:

   design_philosophy
   developing_backends
