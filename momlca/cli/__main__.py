"""Entry point for ``python -m momlca.cli`` invocations."""

from __future__ import annotations

import argparse
from typing import Sequence

from momlca import __version__
from momlca.utils import configure_logging


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="momlca",
        description="Utility commands for the Molecular Machine Learning for Chemical Automation project.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Logging threshold (default: %(default)s).",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print the installed MoML-CA version and exit.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Execute the CLI with optional argument overrides."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    configure_logging(level=args.log_level)

    if args.version:
        print(f"MoML-CA {__version__}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":  # pragma: no cover - direct execution
    raise SystemExit(main())
