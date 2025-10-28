"""Tests for logging helpers."""

from __future__ import annotations

import logging

from momlca.utils.logging import configure_logging


def test_configure_logging_custom_override() -> None:
    """configure_logging should set the requested logger level."""
    configure_logging(level="WARNING", logger_overrides={"momlca": "DEBUG"})

    assert logging.getLogger().level == logging.WARNING
    assert logging.getLogger("momlca").level == logging.DEBUG
