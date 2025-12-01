# Show this help
help:
    just -l

# Initialize the project for development
init:
    uv venv
    uv pip install -e .[dev]

# Run tests
test:
    uv run pytest

# Run tests with coverage
test-coverage:
    uv run coverage run --source src -m pytest
    uv run coverage report -m

# Build package
build:
    uv build

# Publish a release
publish version:
    uv publish dist/gage_inspect-{{version}}.tar.gz* dist/gage_inspect-{{version}}-*.whl
