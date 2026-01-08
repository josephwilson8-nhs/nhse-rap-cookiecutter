# Getting Started

This guide will help you install **NHS RAP Cookiecutter Template** and create your first project.

## Prerequisites

| Requirement | Version | Description |
|-------------|---------|-------------|
| **Python** | 3.10+ | Required for running the template tool |
| **Git** | Latest | Version control system for your projects |
| **uv** (Recommended) | Latest | Fast Python package manager |

## Installation

Choose your preferred installation method:

=== "pipx (Recommended)"

    Since this is a command-line tool, pipx is the recommended installation method:

    ```bash
    pipx install nhs-rap-cookiecutter
    ```

=== "uv"

    ```bash
    uv tool install nhs-rap-cookiecutter
    ```

=== "pip"

    ```bash
    pip install nhs-rap-cookiecutter
    ```

cd /home/jowi60/side_projects/nhs-rap-cookie-cutter && ls -la *.yml 2>/dev/null || echo "No .yml files in root"! tip "Why pipx or uv tool?"
    `pipx` and `uv tool` install command-line tools in isolated environments, preventing dependency conflicts with your other Python projects.

## Creating Your First Project

Once installed, create a new project:

```bash
nhs-rap-template
```

You'll be prompted for:

- Project name
- Author information  
- Organization details
- Technical configuration (Python version, environment manager, etc.)

### Example Session

```bash
$ nhs-rap-template
project_name [project_name]: My NHS Analysis
repo_name [my_nhs_analysis]: 
module_name [my_nhs_analysis]: 
author_name [Your Name]: Jane Smith
author_email [your.email@example.com]: jane.smith@nhs.net
organization_name [Your Organization]: NHS England
organization_email [contact@example.com]: datascience@nhs.net
description [A short description of the project.]: Analysis of patient outcomes
python_version_number [3.10]: 3.11
Select environment_manager:
1 - virtualenv
2 - conda
3 - pipenv
4 - uv
5 - pixi
6 - poetry
7 - none
Choose from 1, 2, 3, 4, 5, 6, 7 [1]: 4
...
```

## Quick Start After Creation

After your project is created:

```bash
# Navigate to your project
cd my_nhs_analysis

# Set up environment (if using UV)
uv sync

# Install pre-commit hooks
uv run pre-commit install

# Run tests
uv run pytest tests/

# Build documentation
uv run mkdocs serve
```

## Next Steps

- Read the [Usage Guide](usage.md) for detailed information on using the template
- Explore the generated project structure
- Check out [Contributing](contributing.md) if you want to improve the template

## Development Setup

For contributing to the template tool itself:

```bash
git clone https://github.com/nhsengland/nhs-rap-cookiecutter.git
cd nhs-rap-cookiecutter
uv sync --all-extras
uv run pre-commit install
```

Then make your changes and run tests:

```bash
uv run pytest tests/
```
