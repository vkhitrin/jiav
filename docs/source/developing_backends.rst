#####################
 Developing Backends
#####################

Due to the unlimited amount of possible use cases and implementations
available, we want to expose the ability for developers to create custom
:ref:`backends`.

********************
 What Is A Backend?
********************

A backend is a Python package that declares an `entry_point
<https://packaging.python.org/en/latest/specifications/entry-points/>`_
in the ``jiav.backend`` group.

That entry point should reference a subclass of the
``jiav.backend.BaseBackend`` abstract base class. This allows jiav
to discover installed backends and instantiate a selected backend at
run-time.

****************
 Implementation
****************

All backends are epxected to share the custom ``jiav.backend.Result``
interface, populate it and return it at the end:

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   -  -  Attribute
      -  Type
      -  Descrption

   -  -  successful
      -  boolean
      -  Represents if the backend executed successfully.

   -  -  errors
      -  List[str]
      -  List of strings containing errors.

   -  -  output
      -  List[str]
      -  List of strings containing output.

All baceknds inherit from ``BaseBackend`` and must implement the
following methods:

-  ``validate_schema`` - validate a schema using `jsonschema
   <https://json-schema.org>`_.
-  ``execute_backend`` - Executes the backend, return a ``Result``.

All backends are expected to subscribe to the global logger
``jiav.logger`` to log information.

*****************************************
 Developing A Custom ``example`` Backend
*****************************************

.. note::

   Based on a backend `template
   <https://github.com/vkhitrin/jiav-backend-template>`_.

In this section, we will create an ``example`` backend that checks if an
environment variable is set.

#. Your backend must register an entry point in the ``jiav.backend``
   group, using the packaging software you use to build your project.
   With Poetry, you can define the entry point in your
   ``pyproject.toml`` file:

   .. code::

      [tool.poetry.plugins."jiav.backend"]
      example = "jiav_example.ExampleBackend"

#. Ensure that your class is discovarable in the `jiav_example`
   namespace, populate ``src/jiav_example/__init__.py``:

   .. code:: python

      from jiav_example.backend import ExampleBackend

      __all__ = ["ExampleBackend"]

#. Create a ``src/jiav_example/backend.py`` and import all dependencies

   .. code:: python

      import os
      # Global logger
      from jiav import logger
      # Required interafces
      from jiav.backend import BaseBackend, Result
      # Type enforcement
      from typing import List

#. Subscribe to the global logger:

   .. code:: python

      jiav_logger = logger.subscribe_to_logger()

#. In the current implementation of backends, we need to create a mock
   step that will be used during JSON schema validation when
   constructing an initial object:

   .. code:: python

      # Mock step that will be used when initializing an initial object
      MOCK_STEP = {"example": "example"}

#. define the schema that will be used to validate the step supplied by
   the user:

   .. code:: python

      SCHEMA = {
          "type": "object",
          "required": ["example"],
          "properties": {"example": {"type": "string"}},
          "additionalProperties": False,
      }

#. Create an initial ``ExampleBackend`` interface which inherits from
   ``BaseBackend``:

   .. code:: python

      class ExampleBackend(BaseBackend):
          """
          ExampleBackend object

          An example backend for jiav

          Attributes:
              name   - Backend name
              schema - json_schema to be used to verify that the supplied step is
                       valid according to the backends's requirements
              step   - Backend excution instructions
          """

          MOCK_STEP = {"example": "example"}
          SCHEMA = {
              "type": "object",
              "required": ["example"],
              "properties": {"example": {"type": "string"}},
              "additionalProperties": False,
          }

          def __init__(self) -> None:
              self.name = "example"
              self.schema = self.SCHEMA
              self.step = self.MOCK_STEP
              super().__init__(name=self.name, schema=self.schema, step=self.step)

#. Implement `execute_backend` method that will execute the backend and
   return a ``Result``:

   .. code:: python

      # Overrdie method of BaseBackend
      def execute_backend(self) -> None:
          """
          Execute backend

          Returns a namedtuple describing the jiav manifest execution
          """
          # Parse required arugments
          example: str = self.step["example"]
          output: List = []
          errors: List = []
          successful: bool = False
          jiav_logger.debug(f"Example: {example}")
          try:
              os.environ["JIAV_EXAMPLE"] = example
              successful = True
              jiav_logger.debug(
                  f"Environment variable 'JIAV_EXAMPLE' was set to '{example}'"
              )
              output.append(f"Environment variable 'JIAV_EXAMPLE' was set to '{example}'")
          except Exception as e:
              jiav_logger.error(e.text)
              errors.append(e.text)
          self.result = Result(successful, output, errors)

#. Install the package and verify ``example`` backend is registered in
   ``jiav``:

   .. code:: bash

      jiav --version
      jiav, version 0.3.0

      Installed Backends:
        - example, version {'version': '0.1.0', 'class': 'jiav_example.ExampleBackend'}
        - jira_issue, version {'version': '0.3.0', 'class': 'jiav_jira_issue.JiraIssueBackend'}
        - lineinfile, version {'version': '0.3.0', 'class': 'jiav_lineinfile.LineInFileBackend'}
        - regexinfile, version {'version': '0.3.0', 'class': 'jiav_regexinfile.RegexInFileBackend'}

#. Create a test manifest ``/tmp/example_manifest.yaml``, and verify
   that it is valid

   .. code:: shell

      cat << EOF > /tmp/example_manifest.yaml
      jiav:
        verified_status: "Done"
        verification_steps:
          - name: "Example"
            backend: example
            example: "example"
      EOF
      export JIAV_EXAMPLE="/tmp/example_manifest.yaml"
      jiav validate-manifest --from-file="/tmp/example_manifest.yaml"
