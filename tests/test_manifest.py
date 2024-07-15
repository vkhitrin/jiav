#!/usr/bin/env python

import pytest

import jiav.exceptions
from jiav.manifest import Manifest


@pytest.mark.parametrize(
    "manifest_file, valid_manifest",
    [
        (
            "tests/files/manifests/valid_single_lineinfile.yml",
            True,
        ),
        (
            "tests/files/manifests/valid_single_regexinfile.yml",
            True,
        ),
        ("tests/files/manifests/invalid_manifest.yml", False),
        (
            "tests/files/manifests/valid_multiple_steps.yml",
            True,
        ),
    ],
)
def test_validate_manifest(manifest_file: str, valid_manifest: bool) -> None:
    with open(manifest_file) as f:
        content = f.read()
        validation = True
        try:
            Manifest(manifest_text=content)
        except jiav.exceptions.InvalidManifestException:
            validation = False
        assert validation == valid_manifest


@pytest.mark.parametrize(
    "manifest_file, successful_execution",
    [
        (
            "tests/files/manifests/valid_single_lineinfile.yml",
            True,
        ),
        (
            "tests/files/manifests/valid_single_regexinfile.yml",
            True,
        ),
        ("tests/files/manifests/valid_single_regexinfile_failed_execution.yml", False),
        (
            "tests/files/manifests/valid_multiple_steps.yml",
            True,
        ),
    ],
)
def test_manifest_execution(manifest_file: str, successful_execution: bool) -> None:
    with open(manifest_file) as f:
        content = f.read()
        manifest = Manifest(manifest_text=content)
        manifest.execute_manifest()
        assert manifest.successful == successful_execution
