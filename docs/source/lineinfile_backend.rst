####################
 lineinfile Backend
####################

Looks for a line in file.

**Attributes**

.. list-table::
   :widths: 10 90
   :header-rows: 1

   -  -  Property
      -  Descrption
   -  -  path
      -  Path to a local file. **[required]**
   -  -  line
      -  Line to look in a file. **[required]**

**Examples**

Look for a single line in a file:

.. code:: yaml

   jiav:
     verification_status: "Done"
     verification_steps:
       - name: "Search for line in file"
         backend: "lineinfile"
         path: "/path/to/file"
         line: "line_in_file"
