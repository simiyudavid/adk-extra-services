# ADK Extra Services

A Python package providing additional service implementations for the Google ADK framework. This package includes implementations for various services like artifacts, sessions, and memory that are not included in the core ADK package.

## Features

- **S3ArtifactService**: Store and manage artifacts using AWS S3 or compatible storage (like MinIO)
- Future additions planned for sessions and memory services

## Installation

```bash
pip install adk-extra-services
```

## Examples

- **Artifacts**: Detailed guide and example for S3 artifacts in [examples/artifacts/README.md](examples/artifacts/README.md)
- **Sessions**: Usage of session services in [examples/sessions/README.md](examples/sessions/README.md)
- **Memory**: Usage of memory services in [examples/memory/README.md](examples/memory/README.md)

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/edu010101/adk-extra-services.git
cd adk-extra-services

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
