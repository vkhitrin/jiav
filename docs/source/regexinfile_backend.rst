#####################
 regexinfile Backend
#####################

Look for a `regex (regular expression)
<https://en.wikipedia.org/wiki/Regular_expression>`_ in file.

Regex is checked using `re.search
<https://docs.python.org/3/library/re.html#re.search>`_.

**Attributes**

.. list-table::
   :widths: 10 90
   :header-rows: 1

   -  -  Property
      -  Descrption
   -  -  path
      -  Path to a local file. **[required]**
   -  -  regex
      -  Regex to look in a file. **[required]**

**Examples**

Look for a regex in a file:

.. code:: yaml

   jiav:
     verification_status: "Done"
     verification_steps:
       - name: "Search for a regex in file"
         backend: "lineinfile"
         path: "/path/to/file"
         regex: "^.*hello.*$"
