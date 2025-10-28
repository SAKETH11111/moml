"""Command-line interface for MoML."""

from __future__ import annotations

import typer

app = typer.Typer(help="MoML command line interface")


@app.callback()
def main(ctx: typer.Context) -> None:
    """Base command for MoML."""
    ctx.obj = ctx.obj or {}


def run() -> None:
    """Entrypoint for the CLI."""
    app()


if __name__ == "__main__":  # pragma: no cover
    run()
