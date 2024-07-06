####################
 lineinfile Backend
####################

**********
 Overview
**********

``jiav`` can look for a line in files to verify issues.

*********
 Example
*********

Basic scenario
==============

Look for a single line in a file:

   .. code:: yaml

      jiav:
        verification_status: "Done"
        verification_steps:
          - name: Search for line in file
            backend: lineinfile
            path: '/path/to/file'
            line: 'line_in_file'

Attributes
==========

path
----

Path to a file.

line
----

Line to look in a file.
