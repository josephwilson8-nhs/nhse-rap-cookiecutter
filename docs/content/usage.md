# Usage

## Creating a New Project

To create a new NHS RAP project, run:

```bash
nhs-rap-template
```

This will prompt you for configuration options and generate a complete project structure.

## Non-Interactive Mode

For automation or CI/CD, use `--no-input` with a config file:

```bash
nhs-rap-template --no-input --config-file my-config.json
```

## Using Specific Template Versions

To use a specific version of the template:

```bash
# Use latest development version
nhs-rap-template -c main

# Use a specific tag
nhs-rap-template -c v1.0.0

# Use a specific commit
nhs-rap-template -c abc123def
```

## Configuration Options

When you run `nhs-rap-template`, you'll be prompted for:

- **Project Name**: Human-readable name (e.g., "My Analysis Project")
- **Author Details**: Your name and email
- **Organization**: Organization name and contact email (used in LICENSE)
- **Python Version**: Minimum Python version (3.10+)
- **Environment Manager**: virtualenv, conda, pipenv, uv, pixi, poetry, or none
- **Dependency File**: requirements.txt, pyproject.toml, environment.yml, Pipfile, or pixi.toml
- **PyData Packages**: Include pandas, numpy, matplotlib, etc.
- **Dataset Storage**: Azure, S3, GCS, or none
- **License**: MIT, BSD-3-Clause, or no license
- **Documentation**: mkdocs or none

## Generated Project Structure

The template creates a standardized RAP project with:

- **Data folders**: raw, interim, processed, external
- **Source code**: Python package structure with your module
- **Documentation**: MkDocs setup with NHS styling
- **Testing**: pytest configuration
- **Quality**: ruff for linting/formatting, pre-commit hooks
- **Reproducibility**: Environment management, dependency tracking

## Next Steps After Generation

After creating your project:

1. **Navigate to the project**:
   ```bash
   cd your-project-name
   ```

2. **Create environment** (if using UV):
   ```bash
   uv sync
   ```

3. **Set up pre-commit** (optional but recommended):
   ```bash
   uv run pre-commit install
   ```

4. **Start developing**:
   - Add your code to the module folder
   - Add tests to the `tests/` folder
   - Update documentation in `docs/`

## Customizing After Generation

All generated files can be customized:

- Edit `pyproject.toml` for dependencies
- Modify `Makefile` for custom commands
- Update `mkdocs.yml` for documentation structure
- Add custom pre-commit hooks in `.pre-commit-config.yaml`

## Common Workflows

### Adding Dependencies

With UV:
```bash
uv add pandas numpy
```

With pip:
```bash
pip install pandas numpy
pip freeze > requirements.txt
```

### Running Tests

```bash
make test
# or
uv run pytest tests/
```

### Building Documentation

```bash
uv run mkdocs serve
```

### Code Quality Checks

```bash
make lint    # Check code
make format  # Format code
```
