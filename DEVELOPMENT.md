# Development Context for python-ciso-assistant-client

> **For LLMs:** Read this entire document to understand the project state. All code is complete, tested, and follows project conventions. When making changes: (1) run `make reformat` after modifications, (2) run `make test` to verify tests pass, (3) run `make typecheck` to verify type safety, (4) maintain the existing architecture patterns (ABC base class, static validation methods, etc.).

## Project Overview
This is a Python HTTP client library for the CISO Assistant API, built with httpx and pydantic. The library provides both synchronous and asynchronous clients with full type safety and comprehensive test coverage.

**Current Status:** ✅ Production-ready with comprehensive tests (58 tests, all passing)

**Current Implementation:** Folders, Assets, and Evidences API endpoints (full CRUD) with pagination support

## What Has Been Built

### 1. Core Implementation (src/ciso_assistant_client/)
- **models/** - Pydantic models organized by resource type:
  - **base.py** - Base models: `ApiToken`, `BasePagedRead`, `BaseDetail`, `BaseWrite`
  - **folders.py** - Folder models: `FolderRead`, `FolderWrite`, `PagedFolderRead`
  - **assets.py** - Asset models: `AssetRead`, `AssetWrite`, `PagedAssetRead`
  - **evidences.py** - Evidence models: `EvidenceRead`, `EvidenceWrite`, `PagedEvidenceRead`
  - **__init__.py** - Exports all models for easy importing

- **client.py** - HTTP client implementation with ABC base class:
  - `BaseCISOAssistantClient` - Abstract base class containing:
    - Common initialization logic (base_url, timeout, headers, follow_redirects, auth, verify)
    - API Token authentication support via Authorization header
    - SSL certificate verification control (supports bool, str path, or SSLContext)
    - Static response handling method (`_handle_response`)
    - Static validation methods for all response types
  - `CISOAssistantClient` - Synchronous client using `httpx.Client`
    - Context manager support (`__enter__`/`__exit__`)
    - Folder methods: `list_folders()`, `get_folder()`, `create_folder()`, `delete_folder()`
    - Asset methods: `list_assets()`, `get_asset()`, `create_asset()`, `delete_asset()`
    - Evidence methods: `list_evidences()`, `get_evidence()`, `create_evidence()`, `delete_evidence()`
    - Pagination methods: `next_page()`, `previous_page()`
  - `AsyncCISOAssistantClient` - Asynchronous client using `httpx.AsyncClient`
    - Async context manager support (`__aenter__`/`__aexit__`)
    - Same 14 API methods with async/await

- **exceptions.py** - Custom exception hierarchy:
  - `CISOAssistantError` - Base exception
  - `CISOAssistantAPIError` - HTTP/API errors
  - `CISOAssistantValidationError` - Pydantic validation errors

- **__init__.py** - Clean public API exports with `__all__`
- **py.typed** - Type checking marker for mypy/pyright

### 2. API Endpoints Implemented
Based on ciso-aa.yaml specification:

**Folders (Complete CRUD):**
1. **GET /api/folders/** - List folders with pagination (limit, offset, ordering, search)
2. **GET /api/folders/{id}/** - Get folder details
3. **POST /api/folders/** - Create new folder
4. **DELETE /api/folders/{id}/** - Delete folder

**Assets (Complete CRUD):**
5. **GET /api/assets/** - List assets with pagination (limit, offset, ordering, search)
6. **GET /api/assets/{id}/** - Get asset details
7. **POST /api/assets/** - Create new asset
8. **DELETE /api/assets/{id}/** - Delete asset

**Evidences (Complete CRUD):**
9. **GET /api/evidences/** - List evidences with pagination (limit, offset, ordering, search)
10. **GET /api/evidences/{id}/** - Get evidence details
11. **POST /api/evidences/** - Create new evidence
12. **DELETE /api/evidences/{id}/** - Delete evidence

### 3. Test Suite (tests/)
- **conftest.py** - Pytest fixtures with mock data for all API responses
- **test_client.py** - 29 tests for `CISOAssistantClient` (synchronous)
- **test_async_client.py** - 29 tests for `AsyncCISOAssistantClient` (asynchronous)

Test coverage includes:
- Client initialization and configuration
- API Token authentication and header verification
- SSL certificate verification control
- Context manager functionality
- All 12 API endpoints (folders, assets, evidences)
- Pagination methods (`next_page()`, `previous_page()`)
- Success cases with data validation
- HTTP error handling (404, 400, 500)
- Pydantic validation errors
- Query parameter handling
- Create, read, and delete operations

All 58 tests pass using respx for HTTP mocking.

## Dependencies
**Core:**
- httpx >= 0.28.1 - HTTP client
- pydantic >= 2.12.1 - Data validation

**Dev:**
- pytest >= 8.3.4 - Test framework
- pytest-asyncio >= 0.25.2 - Async test support
- respx >= 0.22.0 - HTTP mocking for tests

## Code Quality
- All code passes `ruff check` and `ruff format`
- Follows type hints throughout (Python 3.11+)
- No code duplication (shared logic in BaseCISOAssistantClient ABC)
- Clean separation of sync/async implementations

## Project Structure
```
python-ciso-aac/
├── src/ciso_assistant_client/
│   ├── __init__.py        # Public API exports
│   ├── client.py          # BaseCISOAssistantClient, CISOAssistantClient, AsyncCISOAssistantClient
│   ├── exceptions.py      # Custom exceptions
│   ├── models/            # Pydantic schemas organized by resource
│   │   ├── __init__.py    # Model exports
│   │   ├── base.py        # Base models (ApiToken, BasePagedRead, BaseDetail, BaseWrite)
│   │   ├── folders.py     # Folder models
│   │   ├── assets.py      # Asset models
│   │   └── evidences.py   # Evidence models
│   └── py.typed           # Type marker
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Pytest fixtures
│   ├── test_client.py     # Sync client tests (29 tests)
│   └── test_async_client.py  # Async client tests (29 tests)
├── ciso-aa.yaml           # API specification (source of truth)
├── pyproject.toml         # Project config with BSD-2-Clause license
├── LICENSE                # BSD 2-Clause License
├── README.md              # User documentation
├── DEVELOPMENT.md         # This file - development documentation
├── Makefile               # Dev commands (test, reformat, typecheck, build, clean)
├── ruff.toml              # Ruff linter configuration
└── ruff-extended.toml     # Extended ruff checks
```

## Common Commands
```bash
# Install in editable mode
uv pip install -e .

# Run tests
make test

# Format and lint
make reformat

# Type checking
make typecheck

# Build package
make build

# Clean build artifacts
make clean

# Sync dependencies
uv sync

# Update dependencies
make update_deps
```

## Design Decisions
1. **ABC Base Class** - Extracted all common logic (response handling, validation, auth) into `BaseCISOAssistantClient` to eliminate duplication between sync and async clients
2. **Static Methods** - Validation and response handling are static since they don't need instance state
3. **Context Managers** - Both clients support context managers for automatic cleanup
4. **Separate Validation Methods** - Each response type has its own validation method for clarity and error handling
5. **Type Safety** - Full type hints with proper return types and pydantic validation
6. **API Token Model** - Authentication token is represented as a Pydantic model for type safety and validation
7. **Runtime Type Assertions** - Use `assert isinstance()` to help mypy understand union types from `_handle_response`

## Architecture Patterns to Follow
When extending this codebase:
- **Add new endpoints:** Implement in both `CISOAssistantClient` and `AsyncCISOAssistantClient`, add validation method to `BaseCISOAssistantClient` if needed
- **Add new models:** Create Pydantic models in `models.py`, export in `__init__.py`
- **Add new exceptions:** Inherit from `CISOAssistantError` in `exceptions.py`
- **Write tests:** Mirror structure in `test_client.py` and `test_async_client.py` with respx mocking
- **Error handling:** Use `_handle_response()` for HTTP errors, wrap pydantic validation in try/except for `CISOAssistantValidationError`

## Example Usage
```python
# Synchronous
from ciso_assistant_client import CISOAssistantClient, ApiToken

with CISOAssistantClient(base_url="https://ciso.example.com") as client:
    folders = client.list_folders(limit=100)
    for folder in folders.results:
        print(f"{folder.id}: {folder.name}")
    
    folder = client.get_folder("550e8400-e29b-41d4-a716-446655440000")

# With API Token
auth = ApiToken(token="your-api-token-here")
with CISOAssistantClient(base_url="https://ciso.example.com", auth=auth) as client:
    folders = client.list_folders(limit=100)

# Disable SSL verification (for testing/development)
with CISOAssistantClient(
    base_url="https://ciso.example.com",
    auth=auth,
    verify=False
) as client:
    folders = client.list_folders()

# Use custom CA bundle
with CISOAssistantClient(
    base_url="https://ciso.example.com",
    auth=auth,
    verify="/path/to/ca-bundle.crt"
) as client:
    folders = client.list_folders()

# Asynchronous
from ciso_assistant_client import AsyncCISOAssistantClient

async with AsyncCISOAssistantClient(base_url="https://ciso.example.com") as client:
    folders = await client.list_folders(limit=100)
    folder = await client.get_folder("550e8400-e29b-41d4-a716-446655440000")
```

## Adding New Endpoints

### Step 1: Identify the endpoint in ciso-aa.yaml
Look at the OpenAPI spec to understand:
- Path and HTTP method
- Request parameters (query, path, body)
- Response schema
- Authentication requirements

### Step 2: Add Pydantic models (if needed)
Create a new file in `models/` directory for the resource:
```python
# models/new_resource.py
from pydantic import Field
from .base import BaseDetail, BasePagedRead, BaseWrite

class NewResourceRead(BaseDetail):
    """New resource read schema."""
    # Add resource-specific fields
    specific_field: str = Field(..., description="Specific field")

class PagedNewResourceRead(BasePagedRead):
    """Paginated resource list response."""
    results: list[NewResourceRead] = Field(..., description="List of resources")

class NewResourceWrite(BaseWrite):
    """New resource write schema."""
    # Add resource-specific fields
    specific_field: str = Field(..., description="Specific field")
```

Then export in `models/__init__.py`:
```python
from .new_resource import NewResourceRead, NewResourceWrite, PagedNewResourceRead

__all__ = [
    # ... existing exports
    "NewResourceRead",
    "NewResourceWrite",
    "PagedNewResourceRead",
]
```

### Step 3: Add validation method to base class
In `client.py`, add static validation method to `BaseCISOAssistantClient`:
```python
@staticmethod
def _validate_paged_resources(data: dict[str, Any]) -> PagedNewResourceRead:
    """Validate and return paged resources response."""
    try:
        return PagedNewResourceRead.model_validate(data)
    except ValidationError as e:
        raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e
```

### Step 4: Implement in sync client
Add method to `CISOAssistantClient`:
```python
def list_resources(self, limit: int | None = None, offset: int = 0) -> PagedNewResourceRead:
    """List resources with pagination."""
    params: dict[str, Any] = {"offset": offset}
    if limit is not None:
        params["limit"] = limit
    
    response = self._client.get("/api/resources/", params=params)
    data = self._handle_response(response)
    assert isinstance(data, dict)
    return self._validate_paged_resources(data)
```

### Step 5: Implement in async client
Add same method to `AsyncCISOAssistantClient` with async/await:
```python
async def list_resources(self, limit: int | None = None, offset: int = 0) -> PagedNewResourceRead:
    """List resources with pagination."""
    params: dict[str, Any] = {"offset": offset}
    if limit is not None:
        params["limit"] = limit
    
    response = await self._client.get("/api/resources/", params=params)
    data = self._handle_response(response)
    assert isinstance(data, dict)
    return self._validate_paged_resources(data)
```

### Step 6: Export in __init__.py
Add new models to `__all__`:
```python
__all__ = [
    # ... existing exports
    "NewResourceRead",
    "PagedNewResourceRead",
]
```

### Step 7: Write tests
Add test fixtures in `conftest.py`:
```python
@pytest.fixture
def mock_resource_data() -> dict:
    """Return mock resource data."""
    return {
        "id": "550e8400-e29b-41d4-a716-446655440001",
        "name": "Test Resource",
    }
```

Add tests in `test_client.py` and `test_async_client.py`:
```python
@respx.mock
def test_list_resources_success(self, base_url: str, mock_paged_resources_data: dict) -> None:
    """Test listing resources successfully."""
    respx.get(f"{base_url}/api/resources/").mock(return_value=Response(200, json=mock_paged_resources_data))
    
    with CISOAssistantClient(base_url=base_url) as client:
        result = client.list_resources()
        assert result.count == 1
```

### Step 8: Run quality checks
```bash
make reformat && make test && make typecheck
```

## Next Steps / TODO
Endpoints to implement (from ciso-aa.yaml):
- ✅ ~~Folders endpoints (list, get, create, delete)~~ - **Completed**
- ✅ ~~Assets endpoints (list, get, create, delete)~~ - **Completed**
- ✅ ~~Evidences endpoints (list, get, create, delete)~~ - **Completed**
- Applied Controls endpoints (list, get, create, update, delete)
- Risk Assessments endpoints
- Threats endpoints
- Risk Scenarios endpoints
- Security Measures endpoints
- Compliance Assessments endpoints
- Users and User Groups endpoints
- And ~480 more endpoints from the OpenAPI spec

Potential improvements:
- Add retry logic with exponential backoff
- Add rate limiting support
- Add request/response logging/debugging hooks
- Add pagination helpers for iterating through all results
- Add more comprehensive error messages
- Add response caching options
- Add request timeout customization per method
- Consider adding batch operations
- Add CLI interface for testing

## API Notes
- The API uses Django REST Framework
- All endpoints return JSON
- Authentication via API Token in Authorization header with "Token" prefix
- UUIDs are used for resource identifiers
- Pagination uses limit/offset pattern (not cursor-based)
- Date/time fields use ISO 8601 format
- Most endpoints support filtering via query parameters (ordering, search, etc.)

## Development Workflow
1. **Before making changes:** Run `make test` and `make typecheck` to ensure baseline is passing
2. **Make changes:** Follow existing patterns and conventions
3. **Format code:** Run `make reformat` (runs ruff check + format + extended checks)
4. **Run tests:** Run `make test` to verify changes
5. **Type check:** Run `make typecheck` to verify type safety
6. **Build package:** Run `make build` to create distribution packages (tests are excluded)
7. **Install package:** Run `uv pip install -e .` if you added new files/modules

**After any code changes, always run:** `make reformat && make test && make typecheck`

## Build Configuration
The package uses hatchling as the build backend:
- **pyproject.toml** - Configures hatchling to only package `src/ciso_assistant_client`
- Build output includes only source code, LICENSE, and README
- Use `make build` to create wheel and source distribution
- Use `make clean` to remove build artifacts

## Key Files to Review
- `src/ciso_assistant_client/client.py` - Main client implementation (read this first)
- `src/ciso_assistant_client/models/` - All Pydantic schemas organized by resource
  - `base.py` - Base models with common patterns
  - `folders.py`, `assets.py`, `evidences.py` - Resource-specific models
- `ciso-aa.yaml` - Source of truth for API specification (20,964 lines, 500+ operations)
- `tests/conftest.py` - Mock data fixtures
- `tests/test_client.py` - Example test patterns

## OpenAPI Specification
The `ciso-aa.yaml` file contains the complete OpenAPI 3.0.3 specification for CISO Assistant API v0.7.0:
- 500+ operations across many resource types
- Comprehensive schema definitions
- Two authentication schemes: knoxApiToken (header) and cookieAuth (cookie)
- Rich filtering, pagination, and search capabilities

Use this specification as the source of truth when implementing new endpoints.
