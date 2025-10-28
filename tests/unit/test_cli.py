"""Smoke tests for the command-line interface."""

from __future__ import annotations

import pytest

from momlca.cli.__main__ import main


def test_cli_version_flag(capsys: pytest.CaptureFixture[str]) -> None:
    """The --version flag should emit the current package version."""
    exit_code = main(["--version"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "MoML-CA" in captured.out
