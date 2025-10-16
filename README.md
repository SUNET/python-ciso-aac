# python-ciso-assistant-client

A Python HTTP client library for the CISO Assistant API, providing both synchronous and asynchronous interfaces with full type safety.

## Features

- 🔄 Both synchronous and asynchronous clients
- 🔒 Full type safety with Pydantic models
- ✅ Comprehensive test coverage (46 tests, 100% passing)
- 🔐 API token authentication support
- 🎯 Clean, minimal API
- 📦 Context manager support for automatic cleanup
- 🚀 Support for Folders, Assets, and Evidences endpoints

## Installation

```bash
pip install python-ciso-assistant-client
```

Or with uv:

```bash
uv pip install python-ciso-assistant-client
```

## Quick Start

### Synchronous Client

```python
from ciso_assistant_client import CISOAssistantClient, ApiToken

# Basic usage
with CISOAssistantClient(base_url="https://your-ciso-instance.com") as client:
    # List folders
    folders = client.list_folders(limit=100)
    for folder in folders.results:
        print(f"{folder.id}: {folder.name}")
    
    # List assets
    assets = client.list_assets(limit=50, search="server")
    for asset in assets.results:
        print(f"{asset.name}: {asset.business_value}")
    
    # List evidences
    evidences = client.list_evidences(limit=20)
    for evidence in evidences.results:
        print(f"{evidence.name}: {evidence.attachment}")
```

### Authentication

```python
from ciso_assistant_client import CISOAssistantClient, ApiToken

# With API Token
auth = ApiToken(token="your-api-token-here")
with CISOAssistantClient(base_url="https://your-ciso-instance.com", auth=auth) as client:
    folders = client.list_folders()
```

### Creating Resources

```python
from ciso_assistant_client import CISOAssistantClient, ApiToken, FolderWrite, AssetWrite, EvidenceWrite

auth = ApiToken(token="your-api-token")
with CISOAssistantClient(base_url="https://ciso.example.com", auth=auth) as client:
    # Create a folder
    folder = FolderWrite(name="My Folder", description="Test folder")
    created_folder = client.create_folder(folder)
    print(f"Created folder: {created_folder.id}")
    
    # Create an asset
    asset = AssetWrite(
        name="Production Server",
        business_value="Critical",
        type="Primary",
        folder=created_folder.id
    )
    created_asset = client.create_asset(asset)
    
    # Create evidence
    evidence = EvidenceWrite(
        name="Security Audit 2024",
        folder=created_folder.id,
        attachment="https://example.com/audit.pdf"
    )
    created_evidence = client.create_evidence(evidence)
```

### Asynchronous Client

```python
from ciso_assistant_client import AsyncCISOAssistantClient, ApiToken

async def main():
    auth = ApiToken(token="your-api-token")
    async with AsyncCISOAssistantClient(base_url="https://ciso.example.com", auth=auth) as client:
        # List resources
        folders = await client.list_folders(limit=100)
        assets = await client.list_assets(limit=50)
        evidences = await client.list_evidences(limit=20)
        
        # Get specific resources
        folder = await client.get_folder("folder-uuid")
        asset = await client.get_asset("asset-uuid")
        evidence = await client.get_evidence("evidence-uuid")
```

## API Coverage

The client currently supports full CRUD operations for:

- **Folders**: `list_folders()`, `get_folder()`, `create_folder()`, `delete_folder()`
- **Assets**: `list_assets()`, `get_asset()`, `create_asset()`, `delete_asset()`
- **Evidences**: `list_evidences()`, `get_evidence()`, `create_evidence()`, `delete_evidence()`

All methods support both synchronous and asynchronous usage.

## Development

### Setup

```bash
# Install dependencies
uv sync

# Install in editable mode
uv pip install -e .
```

### Running Tests

```bash
# Run all tests
make test

# Run with pytest directly
uv run pytest tests/ -v
```

### Code Quality

```bash
# Format and lint code
make reformat

# Type checking
make typecheck

# Run all checks
make reformat && make test && make typecheck
```

### Building Package

```bash
# Build distribution packages
make build

# Clean build artifacts
make clean
```

## Requirements

- Python 3.11 or higher
- httpx >= 0.28.1
- pydantic >= 2.12.1

## License

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

For development guidelines, see [DEVELOPMENT.md](DEVELOPMENT.md).

## Links

- [Development Documentation](./DEVELOPMENT.md)
- [CISO Assistant API Documentation](https://github.com/intuitem/ciso-assistant-community)
