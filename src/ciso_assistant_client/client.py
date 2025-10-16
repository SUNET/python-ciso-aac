"""HTTP client for the CISO Assistant API."""

from abc import ABC
from ssl import SSLContext
from typing import Any, TypeVar

import httpx
from pydantic import ValidationError

from .exceptions import CISOAssistantAPIError, CISOAssistantValidationError
from .models import (
    ApiToken,
    AssetRead,
    AssetWrite,
    EvidenceRead,
    EvidenceWrite,
    FolderRead,
    FolderWrite,
    PagedAssetRead,
    PagedEvidenceRead,
    PagedFolderRead,
)
from .models.base import BasePagedRead

# TypeVar for maintaining type in pagination methods
PagedT = TypeVar("PagedT", bound=BasePagedRead)


class BaseCISOAssistantClient(ABC):
    """Base class for CISO Assistant API clients."""

    def __init__(
        self,
        base_url: str,
        timeout: float = 30.0,
        headers: dict[str, str] | None = None,
        follow_redirects: bool = True,
        auth: ApiToken | None = None,
        verify: SSLContext | str | bool = True,
    ) -> None:
        """Initialize the base CISO Assistant client.

        Args:
            base_url: Base URL for the API
            timeout: Request timeout in seconds
            headers: Optional custom headers
            follow_redirects: Whether to follow redirects
            auth: Optional API token credentials
            verify: SSL verification. Can be:
                - True: verify SSL certificates (default)
                - False: disable SSL verification
                - str: path to CA bundle file
                - SSLContext: custom SSL context
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.headers = headers or {}
        self.follow_redirects = follow_redirects
        self.verify = verify

        # Add authentication header if provided
        if auth:
            self.headers["Authorization"] = f"Token {auth.token}"

    @staticmethod
    def _handle_response(response: httpx.Response) -> dict[str, Any] | list[Any]:
        """Handle HTTP response and raise errors if needed.

        Args:
            response: HTTP response

        Returns:
            JSON response data

        Raises:
            CISOAssistantAPIError: If the API returns an error
        """
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise CISOAssistantAPIError(
                f"API request failed with status {e.response.status_code}: {e.response.text}"
            ) from e

        return response.json()

    @staticmethod
    def _validate_paged_folders(data: dict[str, Any]) -> PagedFolderRead:
        """Validate and return paged folders response.

        Args:
            data: Response data

        Returns:
            Validated paged folder schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return PagedFolderRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    @staticmethod
    def _validate_folder(data: dict[str, Any]) -> FolderRead:
        """Validate and return folder response.

        Args:
            data: Response data

        Returns:
            Validated folder schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return FolderRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    @staticmethod
    def _validate_folder_write(data: dict[str, Any]) -> FolderRead:
        """Validate and return folder write response.

        Note: The API returns FolderRead schema even for write operations.

        Args:
            data: Response data

        Returns:
            Validated folder schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return FolderRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    @staticmethod
    def _validate_paged_assets(data: dict[str, Any]) -> PagedAssetRead:
        """Validate and return paged assets response.

        Args:
            data: Response data

        Returns:
            Validated paged asset schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return PagedAssetRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    @staticmethod
    def _validate_asset(data: dict[str, Any]) -> AssetRead:
        """Validate and return asset response.

        Args:
            data: Response data

        Returns:
            Validated asset schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return AssetRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    @staticmethod
    def _validate_asset_write(data: dict[str, Any]) -> AssetRead:
        """Validate and return asset write response.

        Note: The API returns AssetRead schema even for write operations.

        Args:
            data: Response data

        Returns:
            Validated asset schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return AssetRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    @staticmethod
    def _validate_paged_evidences(data: dict[str, Any]) -> PagedEvidenceRead:
        """Validate and return paged evidences response.

        Args:
            data: Response data

        Returns:
            Validated paged evidence schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return PagedEvidenceRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    @staticmethod
    def _validate_evidence(data: dict[str, Any]) -> EvidenceRead:
        """Validate and return evidence response.

        Args:
            data: Response data

        Returns:
            Validated evidence schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return EvidenceRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    @staticmethod
    def _validate_evidence_write(data: dict[str, Any]) -> EvidenceRead:
        """Validate and return evidence write response.

        Note: The API returns EvidenceRead schema even for write operations.

        Args:
            data: Response data

        Returns:
            Validated evidence schema

        Raises:
            CISOAssistantValidationError: If validation fails
        """
        try:
            return EvidenceRead.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e


class CISOAssistantClient(BaseCISOAssistantClient):
    """Synchronous HTTP client for the CISO Assistant API."""

    def __init__(
        self,
        base_url: str,
        timeout: float = 30.0,
        headers: dict[str, str] | None = None,
        follow_redirects: bool = True,
        auth: ApiToken | None = None,
        verify: SSLContext | str | bool = True,
    ) -> None:
        """Initialize the CISO Assistant client.

        Args:
            base_url: Base URL for the API
            timeout: Request timeout in seconds
            headers: Optional custom headers
            follow_redirects: Whether to follow redirects
            auth: Optional API token credentials
            verify: SSL verification. Can be:
                - True: verify SSL certificates (default)
                - False: disable SSL verification
                - str: path to CA bundle file
                - SSLContext: custom SSL context
        """
        super().__init__(base_url, timeout, headers, follow_redirects, auth, verify)
        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
            headers=self.headers,
            follow_redirects=self.follow_redirects,
            verify=self.verify,
        )

    def __enter__(self) -> "CISOAssistantClient":
        """Enter context manager."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Exit context manager."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def list_folders(
        self,
        limit: int | None = None,
        offset: int = 0,
        ordering: str | None = None,
        search: str | None = None,
    ) -> PagedFolderRead:
        """List folders with pagination.

        Args:
            limit: Maximum number of results (default: server default)
            offset: Offset for pagination (default: 0)
            ordering: Field to use for ordering results
            search: Search term

        Returns:
            Paged folder schema with results and count

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        params: dict[str, Any] = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if ordering is not None:
            params["ordering"] = ordering
        if search is not None:
            params["search"] = search

        response = self._client.get("/api/folders/", params=params)
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_paged_folders(data)

    def get_folder(self, folder_id: str) -> FolderRead:
        """Get folder details.

        Args:
            folder_id: Folder UUID

        Returns:
            Folder schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = self._client.get(f"/api/folders/{folder_id}/")
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_folder(data)

    def create_folder(self, folder: FolderWrite) -> FolderRead:
        """Create a new folder.

        Args:
            folder: Folder data to create

        Returns:
            Created folder schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = self._client.post("/api/folders/", json=folder.model_dump(exclude_none=True))
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_folder_write(data)

    def delete_folder(self, folder_id: str) -> None:
        """Delete a folder.

        Args:
            folder_id: Folder UUID to delete

        Raises:
            CISOAssistantAPIError: If the API request fails
        """
        response = self._client.delete(f"/api/folders/{folder_id}/")
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise CISOAssistantAPIError(
                f"API request failed with status {e.response.status_code}: {e.response.text}"
            ) from e

    def list_assets(
        self,
        limit: int | None = None,
        offset: int = 0,
        ordering: str | None = None,
        search: str | None = None,
    ) -> PagedAssetRead:
        """List assets with pagination.

        Args:
            limit: Maximum number of results (default: server default)
            offset: Offset for pagination (default: 0)
            ordering: Field to use for ordering results
            search: Search term

        Returns:
            Paged asset schema with results and count

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        params: dict[str, Any] = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if ordering is not None:
            params["ordering"] = ordering
        if search is not None:
            params["search"] = search

        response = self._client.get("/api/assets/", params=params)
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_paged_assets(data)

    def get_asset(self, asset_id: str) -> AssetRead:
        """Get asset details.

        Args:
            asset_id: Asset UUID

        Returns:
            Asset schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = self._client.get(f"/api/assets/{asset_id}/")
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_asset(data)

    def create_asset(self, asset: AssetWrite) -> AssetRead:
        """Create a new asset.

        Args:
            asset: Asset data to create

        Returns:
            Created asset schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = self._client.post("/api/assets/", json=asset.model_dump(exclude_none=True))
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_asset_write(data)

    def delete_asset(self, asset_id: str) -> None:
        """Delete an asset.

        Args:
            asset_id: Asset UUID to delete

        Raises:
            CISOAssistantAPIError: If the API request fails
        """
        response = self._client.delete(f"/api/assets/{asset_id}/")
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise CISOAssistantAPIError(
                f"API request failed with status {e.response.status_code}: {e.response.text}"
            ) from e

    def list_evidences(
        self,
        limit: int | None = None,
        offset: int = 0,
        ordering: str | None = None,
        search: str | None = None,
    ) -> PagedEvidenceRead:
        """List evidences with pagination.

        Args:
            limit: Maximum number of results (default: server default)
            offset: Offset for pagination (default: 0)
            ordering: Field to use for ordering results
            search: Search term

        Returns:
            Paged evidence schema with results and count

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        params: dict[str, Any] = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if ordering is not None:
            params["ordering"] = ordering
        if search is not None:
            params["search"] = search

        response = self._client.get("/api/evidences/", params=params)
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_paged_evidences(data)

    def get_evidence(self, evidence_id: str) -> EvidenceRead:
        """Get evidence details.

        Args:
            evidence_id: Evidence UUID

        Returns:
            Evidence schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = self._client.get(f"/api/evidences/{evidence_id}/")
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_evidence(data)

    def create_evidence(self, evidence: EvidenceWrite) -> EvidenceRead:
        """Create a new evidence.

        Args:
            evidence: Evidence data to create

        Returns:
            Created evidence schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = self._client.post("/api/evidences/", json=evidence.model_dump(exclude_none=True))
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_evidence_write(data)

    def delete_evidence(self, evidence_id: str) -> None:
        """Delete an evidence.

        Args:
            evidence_id: Evidence UUID to delete

        Raises:
            CISOAssistantAPIError: If the API request fails
        """
        response = self._client.delete(f"/api/evidences/{evidence_id}/")
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise CISOAssistantAPIError(
                f"API request failed with status {e.response.status_code}: {e.response.text}"
            ) from e

    def next_page(self, paged_result: PagedT) -> PagedT | None:
        """Fetch the next page of results.

        Args:
            paged_result: Current paged result with next URL

        Returns:
            Next page of results with same type, or None if no next page

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        if paged_result.next is None:
            return None

        response = self._client.get(paged_result.next)
        data = self._handle_response(response)
        assert isinstance(data, dict)

        # Use the same model class as the input to validate the response
        result_class = type(paged_result)
        try:
            return result_class.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    def previous_page(self, paged_result: PagedT) -> PagedT | None:
        """Fetch the previous page of results.

        Args:
            paged_result: Current paged result with previous URL

        Returns:
            Previous page of results with same type, or None if no previous page

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        if paged_result.previous is None:
            return None

        response = self._client.get(paged_result.previous)
        data = self._handle_response(response)
        assert isinstance(data, dict)

        # Use the same model class as the input to validate the response
        result_class = type(paged_result)
        try:
            return result_class.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e


class AsyncCISOAssistantClient(BaseCISOAssistantClient):
    """Asynchronous HTTP client for the CISO Assistant API."""

    def __init__(
        self,
        base_url: str,
        timeout: float = 30.0,
        headers: dict[str, str] | None = None,
        follow_redirects: bool = True,
        auth: ApiToken | None = None,
        verify: SSLContext | str | bool = True,
    ) -> None:
        """Initialize the async CISO Assistant client.

        Args:
            base_url: Base URL for the API
            timeout: Request timeout in seconds
            headers: Optional custom headers
            follow_redirects: Whether to follow redirects
            auth: Optional API token credentials
            verify: SSL verification. Can be:
                - True: verify SSL certificates (default)
                - False: disable SSL verification
                - str: path to CA bundle file
                - SSLContext: custom SSL context
        """
        super().__init__(base_url, timeout, headers, follow_redirects, auth, verify)
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout,
            headers=self.headers,
            follow_redirects=self.follow_redirects,
            verify=self.verify,
        )

    async def __aenter__(self) -> "AsyncCISOAssistantClient":
        """Enter async context manager."""
        return self

    async def __aexit__(self, *args: Any) -> None:
        """Exit async context manager."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def list_folders(
        self,
        limit: int | None = None,
        offset: int = 0,
        ordering: str | None = None,
        search: str | None = None,
    ) -> PagedFolderRead:
        """List folders with pagination.

        Args:
            limit: Maximum number of results (default: server default)
            offset: Offset for pagination (default: 0)
            ordering: Field to use for ordering results
            search: Search term

        Returns:
            Paged folder schema with results and count

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        params: dict[str, Any] = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if ordering is not None:
            params["ordering"] = ordering
        if search is not None:
            params["search"] = search

        response = await self._client.get("/api/folders/", params=params)
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_paged_folders(data)

    async def get_folder(self, folder_id: str) -> FolderRead:
        """Get folder details.

        Args:
            folder_id: Folder UUID

        Returns:
            Folder schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = await self._client.get(f"/api/folders/{folder_id}/")
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_folder(data)

    async def create_folder(self, folder: FolderWrite) -> FolderRead:
        """Create a new folder.

        Args:
            folder: Folder data to create

        Returns:
            Created folder schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = await self._client.post("/api/folders/", json=folder.model_dump(exclude_none=True))
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_folder_write(data)

    async def delete_folder(self, folder_id: str) -> None:
        """Delete a folder.

        Args:
            folder_id: Folder UUID to delete

        Raises:
            CISOAssistantAPIError: If the API request fails
        """
        response = await self._client.delete(f"/api/folders/{folder_id}/")
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise CISOAssistantAPIError(
                f"API request failed with status {e.response.status_code}: {e.response.text}"
            ) from e

    async def list_assets(
        self,
        limit: int | None = None,
        offset: int = 0,
        ordering: str | None = None,
        search: str | None = None,
    ) -> PagedAssetRead:
        """List assets with pagination.

        Args:
            limit: Maximum number of results (default: server default)
            offset: Offset for pagination (default: 0)
            ordering: Field to use for ordering results
            search: Search term

        Returns:
            Paged asset schema with results and count

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        params: dict[str, Any] = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if ordering is not None:
            params["ordering"] = ordering
        if search is not None:
            params["search"] = search

        response = await self._client.get("/api/assets/", params=params)
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_paged_assets(data)

    async def get_asset(self, asset_id: str) -> AssetRead:
        """Get asset details.

        Args:
            asset_id: Asset UUID

        Returns:
            Asset schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = await self._client.get(f"/api/assets/{asset_id}/")
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_asset(data)

    async def create_asset(self, asset: AssetWrite) -> AssetRead:
        """Create a new asset.

        Args:
            asset: Asset data to create

        Returns:
            Created asset schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = await self._client.post("/api/assets/", json=asset.model_dump(exclude_none=True))
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_asset_write(data)

    async def delete_asset(self, asset_id: str) -> None:
        """Delete an asset.

        Args:
            asset_id: Asset UUID to delete

        Raises:
            CISOAssistantAPIError: If the API request fails
        """
        response = await self._client.delete(f"/api/assets/{asset_id}/")
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise CISOAssistantAPIError(
                f"API request failed with status {e.response.status_code}: {e.response.text}"
            ) from e

    async def list_evidences(
        self,
        limit: int | None = None,
        offset: int = 0,
        ordering: str | None = None,
        search: str | None = None,
    ) -> PagedEvidenceRead:
        """List evidences with pagination.

        Args:
            limit: Maximum number of results (default: server default)
            offset: Offset for pagination (default: 0)
            ordering: Field to use for ordering results
            search: Search term

        Returns:
            Paged evidence schema with results and count

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        params: dict[str, Any] = {"offset": offset}
        if limit is not None:
            params["limit"] = limit
        if ordering is not None:
            params["ordering"] = ordering
        if search is not None:
            params["search"] = search

        response = await self._client.get("/api/evidences/", params=params)
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_paged_evidences(data)

    async def get_evidence(self, evidence_id: str) -> EvidenceRead:
        """Get evidence details.

        Args:
            evidence_id: Evidence UUID

        Returns:
            Evidence schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = await self._client.get(f"/api/evidences/{evidence_id}/")
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_evidence(data)

    async def create_evidence(self, evidence: EvidenceWrite) -> EvidenceRead:
        """Create a new evidence.

        Args:
            evidence: Evidence data to create

        Returns:
            Created evidence schema

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        response = await self._client.post("/api/evidences/", json=evidence.model_dump(exclude_none=True))
        data = self._handle_response(response)
        assert isinstance(data, dict)
        return self._validate_evidence_write(data)

    async def delete_evidence(self, evidence_id: str) -> None:
        """Delete an evidence.

        Args:
            evidence_id: Evidence UUID to delete

        Raises:
            CISOAssistantAPIError: If the API request fails
        """
        response = await self._client.delete(f"/api/evidences/{evidence_id}/")
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise CISOAssistantAPIError(
                f"API request failed with status {e.response.status_code}: {e.response.text}"
            ) from e

    async def next_page(self, paged_result: PagedT) -> PagedT | None:
        """Fetch the next page of results.

        Args:
            paged_result: Current paged result with next URL

        Returns:
            Next page of results with same type, or None if no next page

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        if paged_result.next is None:
            return None

        response = await self._client.get(paged_result.next)
        data = self._handle_response(response)
        assert isinstance(data, dict)

        # Use the same model class as the input to validate the response
        result_class = type(paged_result)
        try:
            return result_class.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e

    async def previous_page(self, paged_result: PagedT) -> PagedT | None:
        """Fetch the previous page of results.

        Args:
            paged_result: Current paged result with previous URL

        Returns:
            Previous page of results with same type, or None if no previous page

        Raises:
            CISOAssistantAPIError: If the API request fails
            CISOAssistantValidationError: If response validation fails
        """
        if paged_result.previous is None:
            return None

        response = await self._client.get(paged_result.previous)
        data = self._handle_response(response)
        assert isinstance(data, dict)

        # Use the same model class as the input to validate the response
        result_class = type(paged_result)
        try:
            return result_class.model_validate(data)
        except ValidationError as e:
            raise CISOAssistantValidationError(f"Failed to validate response: {e}") from e
