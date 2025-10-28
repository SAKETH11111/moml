"""Basic smoke tests for the momlca package."""

from momlca import __version__


def test_version_semver() -> None:
    """Ensure the package exposes a semantic version string."""
    major, minor, patch = __version__.split(".")
    assert major.isdigit()
    assert minor.isdigit()
    assert patch.isdigit()
