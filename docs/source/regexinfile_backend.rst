#####################
 regexinfile Backend
#####################

**********
 Overview
**********

``jiav`` can look for a `regex (regular expression)
<https://en.wikipedia.org/wiki/Regular_expression>`_ in files to verify
issues.

Regex is checked using `re.search
<https://docs.python.org/3/library/re.html#re.search>`_.

*********
 Example
*********

Basic scenario
==============

Look for a regex in a file:

   .. code:: yaml

      jiav:
        verification_status: "Done"
        verification_steps:
          - name: Search for a regex in file
            backend: lineinfile
            path: '/path/to/file'
            regex: '^.*hello.*$'

Attributes
==========

path
----

Path to a file.

regex
-----

Regex to look in a file.
