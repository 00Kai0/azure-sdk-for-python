# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import SearchIndexClientConfiguration
from .operations_async import DocumentsOperations
from .. import models


class SearchIndexClient(object):
    """Client that can be used to query an index and upload, merge, or delete documents.

    :ivar documents: DocumentsOperations operations
    :vartype documents: azure.search.documents.aio.operations_async.DocumentsOperations
    :param endpoint: The endpoint URL of the search service.
    :type endpoint: str
    :param index_name: The name of the index.
    :type index_name: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        endpoint: str,
        index_name: str,
        **kwargs: Any
    ) -> None:
        base_url = '{endpoint}/indexes(\'{indexName}\')'
        self._config = SearchIndexClientConfiguration(endpoint, index_name, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.documents = DocumentsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SearchIndexClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)