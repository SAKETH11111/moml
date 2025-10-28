"""Smoke tests for the MoML package."""

import importlib


def test_import_moml() -> None:
    module = importlib.import_module("moml")
    assert module.__name__ == "moml"
