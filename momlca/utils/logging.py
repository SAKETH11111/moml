"""Logging utilities used across MoML-CA modules."""

from __future__ import annotations

import logging
from typing import Iterable, Mapping

__all__ = ["configure_logging"]


def configure_logging(
    level: str = "INFO",
    *,
    fmt: str = "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
    extra_handlers: Iterable[logging.Handler] | None = None,
    logger_overrides: Mapping[str, str] | None = None,
) -> None:
    """Configure root logging for interactive and batch workflows.

    Parameters
    ----------
    level:
        Default severity threshold applied to the root logger.
    fmt:
        Format string used for log records.
    datefmt:
        Datetime format applied to the ``asctime`` field.
    extra_handlers:
        Additional logging handlers to attach to the root logger.
    logger_overrides:
        Mapping from logger name prefixes to custom logging levels. This is
        useful when silencing noisy third-party libraries.
    """

    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format=fmt,
        datefmt=datefmt,
        force=True,
    )

    root_logger = logging.getLogger()

    if extra_handlers:
        for handler in extra_handlers:
            root_logger.addHandler(handler)

    if logger_overrides:
        for logger_name, logger_level in logger_overrides.items():
            resolved_level = getattr(logging, logger_level.upper(), logger_level)
            logging.getLogger(logger_name).setLevel(resolved_level)
