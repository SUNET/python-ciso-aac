"""Tests for the asynchronous CISO Assistant client."""

import pytest
import respx
from httpx import Response

from ciso_assistant_client import (
    ApiToken,
    AssetWrite,
    AsyncCISOAssistantClient,
    CISOAssistantAPIError,
    CISOAssistantValidationError,
    EvidenceWrite,
    FolderWrite,
)


class TestAsyncCISOAssistantClient:
    """Tests for AsyncCISOAssistantClient."""

    async def test_client_initialization(self, base_url: str) -> None:
        """Test client initialization."""
        client = AsyncCISOAssistantClient(base_url=base_url)
        assert client.base_url == base_url
        assert client.timeout == 30.0
        assert client.follow_redirects is True
        await client.close()

    async def test_client_with_api_token(self, base_url: str, api_token: str) -> None:
        """Test client initialization with API token."""
        auth = ApiToken(token=api_token)
        client = AsyncCISOAssistantClient(base_url=base_url, auth=auth)
        assert "Authorization" in client.headers
        assert client.headers["Authorization"] == f"Token {api_token}"
        await client.close()

    async def test_context_manager(self, base_url: str) -> None:
        """Test client as async context manager."""
        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            assert client is not None

    @respx.mock
    async def test_list_folders_success(self, base_url: str, mock_paged_folders_data: dict) -> None:
        """Test listing folders successfully."""
        respx.get(f"{base_url}/api/folders/").mock(return_value=Response(200, json=mock_paged_folders_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            result = await client.list_folders()
            assert result.count == 1
            assert len(result.results) == 1
            assert result.results[0].name == "Test Folder"

    @respx.mock
    async def test_list_folders_with_params(self, base_url: str, mock_paged_folders_data: dict) -> None:
        """Test listing folders with query parameters."""
        respx.get(f"{base_url}/api/folders/").mock(return_value=Response(200, json=mock_paged_folders_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            result = await client.list_folders(limit=10, offset=5, ordering="name", search="test")
            assert result.count == 1

    @respx.mock
    async def test_list_folders_http_error(self, base_url: str) -> None:
        """Test listing folders with HTTP error."""
        respx.get(f"{base_url}/api/folders/").mock(return_value=Response(500, text="Internal Server Error"))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            with pytest.raises(CISOAssistantAPIError):
                await client.list_folders()

    @respx.mock
    async def test_list_folders_validation_error(self, base_url: str) -> None:
        """Test listing folders with validation error."""
        invalid_data = {"invalid": "data"}
        respx.get(f"{base_url}/api/folders/").mock(return_value=Response(200, json=invalid_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            with pytest.raises(CISOAssistantValidationError):
                await client.list_folders()

    @respx.mock
    async def test_get_folder_success(self, base_url: str, mock_folder_data: dict) -> None:
        """Test getting a folder successfully."""
        folder_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/folders/{folder_id}/").mock(return_value=Response(200, json=mock_folder_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            result = await client.get_folder(folder_id)
            assert result.id == folder_id
            assert result.name == "Test Folder"
            assert result.is_published is True

    @respx.mock
    async def test_get_folder_http_error(self, base_url: str) -> None:
        """Test getting a folder with HTTP error."""
        folder_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/folders/{folder_id}/").mock(return_value=Response(404, text="Not Found"))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            with pytest.raises(CISOAssistantAPIError):
                await client.get_folder(folder_id)

    @respx.mock
    async def test_api_token_header_sent(self, base_url: str, api_token: str, mock_paged_folders_data: dict) -> None:
        """Test that API token is sent in header."""
        route = respx.get(f"{base_url}/api/folders/").mock(return_value=Response(200, json=mock_paged_folders_data))

        auth = ApiToken(token=api_token)
        async with AsyncCISOAssistantClient(base_url=base_url, auth=auth) as client:
            await client.list_folders()
            assert route.called
            assert route.calls.last.request.headers["Authorization"] == f"Token {api_token}"

    @respx.mock
    async def test_create_folder_success(
        self, base_url: str, mock_folder_write_data: dict, mock_created_folder_data: dict
    ) -> None:
        """Test creating a folder successfully."""
        respx.post(f"{base_url}/api/folders/").mock(return_value=Response(201, json=mock_created_folder_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            folder_data = FolderWrite(**mock_folder_write_data)
            result = await client.create_folder(folder_data)
            assert result.id == "660e8400-e29b-41d4-a716-446655440001"
            assert result.name == "New Test Folder"
            assert result.description == "A newly created test folder"
            assert result.is_published is False

    @respx.mock
    async def test_create_folder_http_error(self, base_url: str, mock_folder_write_data: dict) -> None:
        """Test creating a folder with HTTP error."""
        respx.post(f"{base_url}/api/folders/").mock(return_value=Response(400, text="Bad Request"))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            folder_data = FolderWrite(**mock_folder_write_data)
            with pytest.raises(CISOAssistantAPIError):
                await client.create_folder(folder_data)

    @respx.mock
    async def test_create_folder_validation_error(self, base_url: str, mock_folder_write_data: dict) -> None:
        """Test creating a folder with validation error."""
        invalid_data = {"invalid": "data"}
        respx.post(f"{base_url}/api/folders/").mock(return_value=Response(201, json=invalid_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            folder_data = FolderWrite(**mock_folder_write_data)
            with pytest.raises(CISOAssistantValidationError):
                await client.create_folder(folder_data)

    @respx.mock
    async def test_delete_folder_success(self, base_url: str) -> None:
        """Test deleting a folder successfully."""
        folder_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.delete(f"{base_url}/api/folders/{folder_id}/").mock(return_value=Response(204))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            # Should not raise any exception
            await client.delete_folder(folder_id)

    @respx.mock
    async def test_delete_folder_http_error(self, base_url: str) -> None:
        """Test deleting a folder with HTTP error."""
        folder_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.delete(f"{base_url}/api/folders/{folder_id}/").mock(return_value=Response(404, text="Not Found"))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            with pytest.raises(CISOAssistantAPIError):
                await client.delete_folder(folder_id)

    @respx.mock
    async def test_list_assets_success(self, base_url: str, mock_paged_assets_data: dict) -> None:
        """Test listing assets successfully."""
        respx.get(f"{base_url}/api/assets/").mock(return_value=Response(200, json=mock_paged_assets_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            result = await client.list_assets()
            assert result.count == 1
            assert len(result.results) == 1
            assert result.results[0].name == "Test Asset"

    @respx.mock
    async def test_get_asset_success(self, base_url: str, mock_asset_data: dict) -> None:
        """Test getting an asset successfully."""
        asset_id = "770e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/assets/{asset_id}/").mock(return_value=Response(200, json=mock_asset_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            result = await client.get_asset(asset_id)
            assert result.id == asset_id
            assert result.name == "Test Asset"
            assert result.business_value == "High"

    @respx.mock
    async def test_create_asset_success(
        self, base_url: str, mock_asset_write_data: dict, mock_created_asset_data: dict
    ) -> None:
        """Test creating an asset successfully."""
        respx.post(f"{base_url}/api/assets/").mock(return_value=Response(201, json=mock_created_asset_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            asset_data = AssetWrite(**mock_asset_write_data)
            result = await client.create_asset(asset_data)
            assert result.id == "880e8400-e29b-41d4-a716-446655440002"
            assert result.name == "New Test Asset"
            assert result.business_value == "Medium"

    @respx.mock
    async def test_delete_asset_success(self, base_url: str) -> None:
        """Test deleting an asset successfully."""
        asset_id = "770e8400-e29b-41d4-a716-446655440000"
        respx.delete(f"{base_url}/api/assets/{asset_id}/").mock(return_value=Response(204))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            # Should not raise any exception
            await client.delete_asset(asset_id)

    @respx.mock
    async def test_list_evidences_success(self, base_url: str, mock_paged_evidences_data: dict) -> None:
        """Test listing evidences successfully."""
        respx.get(f"{base_url}/api/evidences/").mock(return_value=Response(200, json=mock_paged_evidences_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            result = await client.list_evidences()
            assert result.count == 1
            assert len(result.results) == 1
            assert result.results[0].name == "Test Evidence"

    @respx.mock
    async def test_get_evidence_success(self, base_url: str, mock_evidence_data: dict) -> None:
        """Test getting an evidence successfully."""
        evidence_id = "990e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/evidences/{evidence_id}/").mock(return_value=Response(200, json=mock_evidence_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            result = await client.get_evidence(evidence_id)
            assert result.id == evidence_id
            assert result.name == "Test Evidence"
            assert result.attachment == "https://example.com/evidence.pdf"

    @respx.mock
    async def test_create_evidence_success(
        self, base_url: str, mock_evidence_write_data: dict, mock_created_evidence_data: dict
    ) -> None:
        """Test creating an evidence successfully."""
        respx.post(f"{base_url}/api/evidences/").mock(return_value=Response(201, json=mock_created_evidence_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            evidence_data = EvidenceWrite(**mock_evidence_write_data)
            result = await client.create_evidence(evidence_data)
            assert result.id == "aa0e8400-e29b-41d4-a716-446655440003"
            assert result.name == "New Test Evidence"

    @respx.mock
    async def test_delete_evidence_success(self, base_url: str) -> None:
        """Test deleting an evidence successfully."""
        evidence_id = "990e8400-e29b-41d4-a716-446655440000"
        respx.delete(f"{base_url}/api/evidences/{evidence_id}/").mock(return_value=Response(204))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            # Should not raise any exception
            await client.delete_evidence(evidence_id)

    @respx.mock
    async def test_next_page_success(
        self, base_url: str, mock_paged_folders_page1: dict, mock_paged_folders_page2: dict
    ) -> None:
        """Test fetching next page successfully."""
        route1 = respx.get(f"{base_url}/api/folders/", params={"offset": 0}).mock(
            return_value=Response(200, json=mock_paged_folders_page1)
        )
        route2 = respx.get(url__regex=r".*/api/folders/\?limit=1&offset=1").mock(
            return_value=Response(200, json=mock_paged_folders_page2)
        )

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            page1 = await client.list_folders()
            assert page1.count == 3
            assert len(page1.results) == 1
            assert page1.results[0].name == "Test Folder 1"
            assert page1.next is not None
            assert route1.called

            page2 = await client.next_page(page1)
            assert page2 is not None
            assert page2.count == 3
            assert len(page2.results) == 1
            assert page2.results[0].name == "Test Folder 2"
            assert page2.previous is not None
            assert route2.called

    @respx.mock
    async def test_next_page_none_when_no_next(self, base_url: str) -> None:
        """Test next_page returns None when there's no next page."""
        data_no_next = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [],
        }
        respx.get(f"{base_url}/api/folders/").mock(return_value=Response(200, json=data_no_next))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            page = await client.list_folders()
            next_page = await client.next_page(page)
            assert next_page is None

    @respx.mock
    async def test_previous_page_success(
        self, base_url: str, mock_paged_folders_page1: dict, mock_paged_folders_page2: dict
    ) -> None:
        """Test fetching previous page successfully."""
        respx.get("https://api.example.com/api/folders/?limit=1&offset=1").mock(
            return_value=Response(200, json=mock_paged_folders_page2)
        )
        respx.get("https://api.example.com/api/folders/?limit=1&offset=0").mock(
            return_value=Response(200, json=mock_paged_folders_page1)
        )

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            # Simulate being on page 2
            page2_response = await client._client.get("https://api.example.com/api/folders/?limit=1&offset=1")
            page2_data = client._handle_response(page2_response)
            assert isinstance(page2_data, dict)
            page2 = client._validate_paged_folders(page2_data)

            assert page2.previous is not None
            page1 = await client.previous_page(page2)
            assert page1 is not None
            assert page1.count == 3
            assert page1.results[0].name == "Test Folder 1"
            assert page1.next is not None

    @respx.mock
    async def test_previous_page_none_when_no_previous(self, base_url: str, mock_paged_folders_data: dict) -> None:
        """Test previous_page returns None when there's no previous page."""
        respx.get(f"{base_url}/api/folders/").mock(return_value=Response(200, json=mock_paged_folders_data))

        async with AsyncCISOAssistantClient(base_url=base_url) as client:
            page = await client.list_folders()
            previous_page = await client.previous_page(page)
            assert previous_page is None

    @pytest.mark.asyncio
    async def test_verify_ssl_default_true(self, base_url: str) -> None:
        """Test that SSL verification is enabled by default."""
        client = AsyncCISOAssistantClient(base_url=base_url)
        assert client.verify is True
        assert client._client._transport._pool._ssl_context is not None
        await client.close()

    @pytest.mark.asyncio
    async def test_verify_ssl_can_be_disabled(self, base_url: str) -> None:
        """Test that SSL verification can be disabled."""
        client = AsyncCISOAssistantClient(base_url=base_url, verify=False)
        assert client.verify is False
        ssl_ctx = client._client._transport._pool._ssl_context
        if ssl_ctx is not None:
            assert ssl_ctx.check_hostname is False
        await client.close()
