# NHS RAP Cookiecutter Template

[![PyPI - Version](https://img.shields.io/pypi/v/nhs-rap-cookiecutter)](https://pypi.org/project/nhs-rap-cookiecutter/)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-D7FF64.svg)](https://github.com/astral-sh/ruff)
[![Tests](https://github.com/nhsengland/nhs-rap-cookiecutter/actions/workflows/tests.yml/badge.svg)](https://github.com/nhsengland/nhs-rap-cookiecutter/actions/workflows/tests.yml)

A standardized project structure for NHS England Reproducible Analytical Pipelines (RAP).

!!! info "Purpose"

    This template empowers data scientists and analysts to:
    
    - Create standardized NHS RAP projects with best practices built-in
    - Choose from multiple environment managers (UV, conda, poetry, etc.)
    - Get pre-configured documentation with NHS styling
    - Start with pytest, ruff, and pre-commit hooks already set up
    - Follow NHS England RAP standards from day one

## Quick Start

Install the template tool:

```bash
pipx install nhs-rap-cookiecutter
```

Create a new project:

```bash
nhs-rap-template
```

## Key Features

- **Multiple environment managers**: UV, conda, pipenv, pixi, poetry, or virtualenv
- **Modern tooling**: Ruff for linting/formatting, pytest for testing
- **NHS branding**: Documentation with NHS England styling
- **Pre-configured**: Pre-commit hooks, CI/CD templates, and quality checks
- **Flexible**: Choose license, documentation, and data storage options

## What Gets Generated

When you create a project, you get:

```
your-project/
├── data/                  # Data folders (raw, interim, processed, external)
├── docs/                  # MkDocs documentation with NHS styling
├── models/                # Trained models and predictions
├── notebooks/             # Jupyter notebooks for exploration
├── references/            # Data dictionaries and references
├── reports/               # Generated analysis outputs
├── tests/                 # Pytest test suite
├── your_module/           # Python package with your code
├── pyproject.toml         # Project configuration
├── Makefile               # Common tasks (test, lint, docs)
└── README.md              # Project documentation
```

## Getting Started

New to the template? Start with our [Getting Started](getting_started.md) guide to install and create your first project.

## Usage Guide

Learn how to customize and use the template in the [Usage Guide](usage.md).

## Contributing

Want to improve the template? Check out our [Contributing Guide](contributing.md).

## Acknowledgments

This project is a fork of [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science), adapted for NHS England RAP standards.
