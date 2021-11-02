"""Contains information and properties pertaining to Rez package."""
# pylint: disable=invalid-name,undefined-variable
name = "Test Renovate"
authors = [u"Larasika Nadela"]
description = "Library to store, modify and exchange a Context"
homepage = "UNKNOWN"
tools = []
build_requires = []
plugin_for = ["maya"]

# Pixomondo internal variable used by `rezolve_me` for dev environment.
# Overrides `requires`. Uncomment this only if needed.
requires = [
    "mock-2",
    "pytest-3.6",
]
