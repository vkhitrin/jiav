#!/usr/bin/env python

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
def test_validate_manifest(manifest_file: str, mock_validated_manifest: manifest.Manifest) -> None:
    with open(manifest_file) as f:
        content = f.read()
        try:
            validated_manifest = manifest.validate_manifest(text=content)
        except jiav.exceptions.InvalidManifestException:
            validated_manifest = False
        assert type(validated_manifest) is type(mock_validated_manifest)
