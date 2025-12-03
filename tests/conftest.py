"""Test fixtures for CISO Assistant client tests."""

import pytest


@pytest.fixture
def mock_folder_data() -> dict:
    """Return mock folder data."""
    return {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "parent_folder": None,
        "content_type": "folder",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "is_published": True,
        "name": "Test Folder",
        "description": "Test folder description",
        "builtin": False,
    }


@pytest.fixture
def mock_paged_folders_data(mock_folder_data: dict) -> dict:
    """Return mock paged folders data."""
    return {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [mock_folder_data],
    }


@pytest.fixture
def mock_paged_folders_page1() -> dict:
    """Return mock paged folders data for page 1."""
    return {
        "count": 3,
        "next": "https://api.example.com/api/folders/?limit=1&offset=1",
        "previous": None,
        "results": [
            {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "parent_folder": None,
                "content_type": "folder",
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "is_published": True,
                "name": "Test Folder 1",
                "description": "Test folder description",
                "builtin": False,
            }
        ],
    }


@pytest.fixture
def mock_paged_folders_page2() -> dict:
    """Return mock paged folders data for page 2."""
    return {
        "count": 3,
        "next": "https://api.example.com/api/folders/?limit=1&offset=2",
        "previous": "https://api.example.com/api/folders/?limit=1&offset=0",
        "results": [
            {
                "id": "660e8400-e29b-41d4-a716-446655440001",
                "parent_folder": None,
                "content_type": "folder",
                "created_at": "2024-01-02T00:00:00Z",
                "updated_at": "2024-01-02T00:00:00Z",
                "is_published": False,
                "name": "Test Folder 2",
                "description": "Second test folder",
                "builtin": False,
            }
        ],
    }


@pytest.fixture
def base_url() -> str:
    """Return base URL for tests."""
    return "https://api.example.com"


@pytest.fixture
def api_token() -> str:
    """Return API token for tests."""
    return "test-api-token-12345"


@pytest.fixture
def mock_folder_write_data() -> dict:
    """Return mock folder write data."""
    return {
        "name": "New Test Folder",
        "description": "A newly created test folder",
        "parent_folder": None,
        "is_published": False,
    }


@pytest.fixture
def mock_created_folder_data() -> dict:
    """Return mock created folder response data."""
    return {
        "id": "660e8400-e29b-41d4-a716-446655440001",
        "parent_folder": None,
        "content_type": "folder",
        "created_at": "2024-01-02T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z",
        "is_published": False,
        "name": "New Test Folder",
        "description": "A newly created test folder",
        "builtin": False,
    }


@pytest.fixture
def mock_asset_data() -> dict:
    """Return mock asset data."""
    return {
        "id": "770e8400-e29b-41d4-a716-446655440000",
        "folder": {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "str": "Test Folder",
        },
        "parent_assets": [],
        "children_assets": [],
        "owner": [],
        "filtering_labels": [],
        "type": "Primary",
        "security_exceptions": [],
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "name": "Test Asset",
        "description": "Test asset description",
        "business_value": "High",
        "reference_link": "https://example.com",
    }


@pytest.fixture
def mock_paged_assets_data(mock_asset_data: dict) -> dict:
    """Return mock paged assets data."""
    return {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [mock_asset_data],
    }


@pytest.fixture
def mock_asset_write_data() -> dict:
    """Return mock asset write data."""
    return {
        "name": "New Test Asset",
        "description": "A newly created test asset",
        "business_value": "Medium",
        "type": "Support",
        "folder": "550e8400-e29b-41d4-a716-446655440000",
        "parent_assets": [],
        "reference_link": None,
        "filtering_labels": [],
        "is_published": False,
    }


@pytest.fixture
def mock_created_asset_data() -> dict:
    """Return mock created asset response data."""
    return {
        "id": "880e8400-e29b-41d4-a716-446655440002",
        "folder": "550e8400-e29b-41d4-a716-446655440000",
        "parent_assets": [],
        "children_assets": [],
        "owner": [],
        "filtering_labels": [],
        "type": "Support",
        "security_exceptions": [],
        "created_at": "2024-01-03T00:00:00Z",
        "updated_at": "2024-01-03T00:00:00Z",
        "name": "New Test Asset",
        "description": "A newly created test asset",
        "business_value": "Medium",
        "reference_link": None,
    }


@pytest.fixture
def mock_evidence_data() -> dict:
    """Return mock evidence data."""
    return {
        "id": "990e8400-e29b-41d4-a716-446655440000",
        "attachment": "https://example.com/evidence.pdf",
        "size": "2048",
        "folder": "550e8400-e29b-41d4-a716-446655440000",
        "applied_controls": [],
        "requirement_assessments": [],
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "name": "Test Evidence",
        "description": "Test evidence description",
        "link": "https://example.com/link",
        "is_published": False,
    }


@pytest.fixture
def mock_paged_evidences_data(mock_evidence_data: dict) -> dict:
    """Return mock paged evidences data."""
    return {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [mock_evidence_data],
    }


@pytest.fixture
def mock_evidence_write_data() -> dict:
    """Return mock evidence write data."""
    return {
        "name": "New Test Evidence",
        "description": "A newly created test evidence",
        "attachment": "https://example.com/new-evidence.pdf",
        "link": None,
        "folder": "550e8400-e29b-41d4-a716-446655440000",
        "applied_controls": [],
        "requirement_assessments": [],
        "is_published": False,
    }


@pytest.fixture
def mock_created_evidence_data() -> dict:
    """Return mock created evidence response data."""
    return {
        "id": "aa0e8400-e29b-41d4-a716-446655440003",
        "attachment": "https://example.com/new-evidence.pdf",
        "size": "4096",
        "folder": "550e8400-e29b-41d4-a716-446655440000",
        "applied_controls": [],
        "requirement_assessments": [],
        "created_at": "2024-01-04T00:00:00Z",
        "updated_at": "2024-01-04T00:00:00Z",
        "name": "New Test Evidence",
        "description": "A newly created test evidence",
        "link": None,
        "is_published": False,
    }
