# Show this help
help:
    just -l

# Initialize the project for development
init:
    uv venv
    uv pip install -e .[dev]

# Run tests
test: _venv
    uv run pytest

# Run tests with coverage
test-coverage: _venv
    uv run coverage run --source src -m pytest
    uv run coverage report -m

# Build package
build: _venv
    uv build

# Build and publish
publish version: (_release version)
    uv publish dist/gage_inspect-{{version}}.tar.gz* dist/gage_inspect-{{version}}-*.whl

# Fail with message if .venv doesn't exist
_venv:
    #!/usr/bin/sh
    if ! test -e .venv; then
        echo "Missing .venv - Did you run 'just init'?"
        exit 1
    fi

# Fail if a release for version doesn't exist
_release version:
    #!/usr/bin/sh
    if ! test -e dist/gage_inspect-{{version}}-*.whl; then
        echo "A release for {{version}} does't exist in dist - did you run 'just build'"
        exit 1
    fi
