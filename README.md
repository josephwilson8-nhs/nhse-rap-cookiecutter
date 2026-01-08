# NHS RAP Cookiecutter Template

_A standardized project structure for NHS England Reproducible Analytical Pipelines (RAP)._

[![PyPI - Version](https://img.shields.io/pypi/v/nhs-rap-cookiecutter)](https://pypi.org/project/nhs-rap-cookiecutter/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nhs-rap-cookiecutter)](https://pypi.org/project/nhs-rap-cookiecutter/)
[![NHS RAP](https://img.shields.io/badge/NHS%20RAP-Project%20template-005EB8?logo=cookiecutter)](https://github.com/nhs-england/nhs-rap-cookiecutter)
[![tests](https://github.com/nhs-england/nhs-rap-cookiecutter/actions/workflows/tests.yml/badge.svg)](https://github.com/nhs-england/nhs-rap-cookiecutter/actions/workflows/tests.yml)

**NHS RAP Cookiecutter Template** is a tool for setting up NHS England RAP projects that incorporate best practices for reproducible analytical pipelines.

> ℹ️ This template uses UV for dependency management and Ruff for linting/formatting by default, following NHS England RAP standards.

## Installation

NHS RAP Cookiecutter requires Python 3.10+. Since this is a cross-project utility application, we recommend installing it with [pipx](https://pypa.github.io/pipx/) or [uv](https://docs.astral.sh/uv/). Installation command options:

```bash
# With pipx from PyPI (recommended)
pipx install nhs-rap-cookiecutter

# With uv from PyPI
uv tool install nhs-rap-cookiecutter

# With pip from PyPI
pip install nhs-rap-cookiecutter
```

## Starting a new project

To start a new project, run:

```bash
nhs-rap-template
```

### The resulting directory structure

The directory structure of your new project will look something like this (depending on the settings that you choose):

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         {{ cookiecutter.module_name }} and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── {{ cookiecutter.module_name }}   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations   
```

## Using unreleased changes

By default, `nhs-rap-template` will use the _project template_ version that corresponds to the _installed package_ version. To use a specific version of the project template, use the `-c/--checkout` flag to provide the branch (or tag or commit hash) of the version you'd like to use. For example to use the project template from the `main` branch:

```bash
nhs-rap-template -c main
```

## Acknowledgments

This project is a fork of [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science), adapted for NHS England Reproducible Analytical Pipeline (RAP) standards. We are grateful to the original maintainers and contributors for their excellent work in creating a standardized data science project structure.

## License

Unless stated otherwise, the codebase is released under the [MIT License](LICENSE). This covers both the codebase and any sample code in the documentation.

The **generated projects** from this template can use their own license as chosen during setup. The license you select will attribute copyright to your organization.

## Contributing

We welcome contributions! Please follow these guidelines:

### Installing development requirements

```bash
uv sync --all-extras
```

### Running the tests

```bash
uv run pytest tests
```

### Code quality

Before submitting, ensure your code passes all checks:

```bash
# Format code
uv run ruff format .

# Check linting
uv run ruff check .

# Run pre-commit hooks
uv run pre-commit run --all-files
```
