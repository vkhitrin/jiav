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

import pytest

import jiav.exceptions
from jiav.api import manifest


@pytest.mark.parametrize(
    "manifest_file, validation",
    [
        (
            "tests/files/manifests/valid_single_lineinfile.yml",
            manifest.Manifest(manifest=""),
        ),
        (
            "tests/files/manifests/valid_single_regexinfile.yml",
            manifest.Manifest(manifest=""),
        ),
        ("tests/files/manifests/invalid_manifest.yml", False),
        (
            "tests/files/manifests/valid_multiple_steps.yml",
            manifest.Manifest(manifest=""),
        ),
    ],
)
def test_validate_manifest(manifest_file, validation):
    with open(manifest_file) as f:
        content = f.read()
        try:
            validated_manifest = manifest.validate_manifest(text=content)
        except jiav.exceptions.InvalidManifestException:
            validated_manifest = False
        assert type(validated_manifest) == type(validation)
