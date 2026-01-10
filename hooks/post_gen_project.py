#!/usr/bin/env python3
"""Post-generation hook to rename template files."""

from pathlib import Path

# Rename _pyproject.toml to pyproject.toml
pyproject = Path("_pyproject.toml")
if pyproject.exists():
    pyproject.rename("pyproject.toml")
