# Import BaseBackend
# Import subprocess
import subprocess

# Import namedtuple
from collections import namedtuple

# Import global jiav logger
from jiav import logger
from jiav.api.backends import BaseBackend

# Import JSON schema to be used in validation
from jiav.api.schemas.example import schema

# Subsribe to global logger
jiav_logger = logger.subscribe_to_logger()

# Mock step that will be used when initalizing an initial object
MOCK_STEP = {"cmd": "[true]", "rc": 0}


# Our backend object
class ExampleBackend(BaseBackend):
    def __init__(self):
        # Name of the backend, will be added to list of exposed backends
        self.name = "example"
        # JSON schema to validate backend
        self.schema = schema
        # Verification step supplied by user
        # When not parsed yet, will use MOCK_STEP
        self.step = MOCK_STEP
        super().__init__(self.name, self.schema, self.step)

    # Overrdie method of BaseBackend
    def execute_backend(self):
        # Parse required arugments
        cmd = [str(_cmd) for _cmd in self.step["cmd"]]
        rc = self.step["rc"]
        # Execute command
        shell_run = subprocess.Popen(
            args=cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
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
            jiav_logger.error(
                "Command failed to execute with the " "expected return code"
            )
            jiav_logger.error("Expected return code: {}".format(rc))
            if errors:
                jiav_logger.error("Error: {}".format(errors))
        # Create a namedtuple to hold the execution result output and errors
        result = namedtuple("result", ["successful", "output", "errors"])
        self.result = result(successful, output, errors)
