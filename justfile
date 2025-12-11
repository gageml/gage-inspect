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

# Test examples
test-examples:
    groktest .

# Build package
build:
    uv build
