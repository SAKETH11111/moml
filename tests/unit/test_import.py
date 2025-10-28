"""Basic smoke tests for the momlca package."""

from packaging.version import Version

from momlca import __version__


def test_version_semver() -> None:
    """Ensure the package exposes a semantic version string."""
    version = Version(__version__)
    assert version.base_version
