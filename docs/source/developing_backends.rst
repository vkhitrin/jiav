#####################
 Developing Backends
#####################

.. note::

   Backend implementation might be changed/enhanced in the future.

Due to the unlimited amount of possible use cases and implementations
available, we want to expose the ability for developers to create custom
:ref:`backends:jiav Backends`.

****************
 Implementation
****************

Currently, all allowed backends must reside in a static directory
``jiav/api/backends/``.

Each backend should inherit from ``BaseBackend`` object under the path
``jiav/api/backends/__init__.py``.

There are several methods that are inherited from ``BaseBackend``, some
of them will be overridden when developing a custom backend.

All backends should accept various attributes that are validated
according to `JSON schema <https://json-schema.org/>`_. Schemas are
stored under the ``jiav/api/schemas/`` directory.

*************************************
 Developing a custom example backend
*************************************

In this section, we will create an example backend that executes basic
shell commands.

First, we'll create a python file containing our code,
``jiav/api/backends/example_backend.py``.

We will import all of the required and recommended ``jiav``
dependencies:

   .. code:: python

      # Import BaseBackend
      from jiav.api.backends import BaseBackend

      # Import JSON schema to be used in validation
      from jiav.api.schemas.example import schema

      # Import global jiav logger
      from jiav import logger

      # Import namedtuple
      from collections import namedtuple

      # Import subprocess
      import subprocess

The backend should also subscribe to the global logger to allow debug
info:

   .. code:: python

      # Subsribe to global logger
      jiav_logger = logger.subscribe_to_logger()

In the current implementation of backends, we need to create a mock step
that will be used during JSON schema validation when constructing an
initial object:

   .. code:: python

      # Mock step that will be used when initializing an initial object
      MOCK_STEP = {"cmd": "true", "rc": 0}

Now we can create our backend object:

   .. code:: python

      # Our backend object
      class ExampleBackend(BaseBackend):
          def __init__(self):
              # Name of the backend will be added to the list of exposed backends
               self.name = 'example'
              # JSON schema to validate backend
              self.schema = schema
              # Verification step supplied by the user
          self.step = MOCK_STEP
              # When not parsed yet, will use MOCK_STEP
              self.step = MOCK_STEP
              super().__init__(self.name,
                               self.schema,
                               self.step)

We override the ``execute_backend`` method with our backend's logic.

As of now, jiav requires the backend to return a ``namedtuple`` with the
following keys:

-  successful - Boolean that represents if the backend executed
   successfully

-  output - String/List containing execution output

-  errors - String/List containing errors

   .. code:: python

      # Overrdie method of BaseBackend
      def execute_backend(self):
          # Parse required arguments
          cmd = self.step["cmd"]
          rc = self.step["rc"]
          # Execute command
          shell_run = Popen(
              cmd,
              stdout=subprocess.PIPE,
              stderr=subprocess.PIPE,
              shell=True,
              universal_newlines=True,
          )
          output, errors = shell_run.communicate()
          s_rc = shell_run.returncode
          # If executed return code equals desired return code
          jiav_logger.debug("CMD: {}".format(cmd))
          jiav_logger.debug("OUTPUT: {}".format(output).rstrip())
          jiav_logger.debug("Return code: {}".format(s_rc))
          if rc == s_rc:
              successful = True
              jiav_logger.debug(
                  "Command executed successfully with the " "expected return code"
              )
          else:
              successful = False
              jiav_logger.error("Command failed to execute with the " "expected return code")
              jiav_logger.error("Expected return code: {}".format(rc))
              if errors:
                  jiav_logger.error("Error: {}".format(errors))
          # create a namedtuple to hold
          # Create a namedtuple to hold the execution result output and errors
          result = namedtuple("result", ["successful", "output", "errors"])
          self.result = result(successful, output, errors)

**View full** :download:`jiav/api/backends/example_backend.py
<_static/example_backend.py>`.

We will also create a schema file that will validate the backend
attributes supplied by the user, ``jiav/api/schema/example_schema.py``.

   .. code:: python

      schema = {
          "type": "object",
          "required": ["cmd", "rc"],
          "properties": {"cmd": {"type": "string"}, "rc": {"type": "integer"}},
          "additionalProperties": False,
      }

**View full** :download:`jiav/api/backends/example_schema.py
<_static/example_schema.py>`.

Now we will be able to leverage our ``example`` backend in the following
way:

   .. code:: yaml

      jiav:
        verification_steps:
          - name: test backend
            backend: example
            cmd: echo test
            rc: 0
