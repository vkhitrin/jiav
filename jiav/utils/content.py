#!/usr/bin/env python
"""
Copyright 2022 Vadim Khitrin <me@vkhitrin.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import tempfile
from datetime import datetime

from iteration_utilities import deepflatten  # pyright: reportGeneralTypeIssues=false


def get_current_timestamp():
    """
    Get current timestamp

    Returns:
        current_timestamp - A formatted string of current time:
                            <month><day><year><hour><minutes><seconds>
    """
    current_timestamp = datetime.now().strftime("%m%d%Y%H%M%S")
    return current_timestamp


def write_content_to_tempfile(content):
    """
    Write content to temporary file

    Parameters:
        content - Content to write

    Returns:
        temp_file - temporary file
    """
    # If we receive an output that contains a list
    # flatten it to a single list
    if isinstance(content, list):
        content = list(deepflatten(content, depth=1))
    # Create temporary file
    temp_file = tempfile.NamedTemporaryFile(
        prefix=f"jiav_{get_current_timestamp()}_", suffix=".txt", mode="w+t"
    )
    # Write content to temporary file
    temp_file.writelines(content)
    # Commit changes to file
    temp_file.seek(0)
    return temp_file
