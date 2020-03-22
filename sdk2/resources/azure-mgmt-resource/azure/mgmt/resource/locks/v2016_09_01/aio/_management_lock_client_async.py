# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import ManagementLockClientConfiguration
from .operations_async import AuthorizationOperationsOperations
from .operations_async import ManagementLocksOperations
from .. import models


class ManagementLockClient(object):
    """Azure resources can be locked to prevent other users in your organization from deleting or modifying resources.

    :ivar authorization_operations: AuthorizationOperationsOperations operations
    :vartype authorization_operations: azure.mgmt.resource.locks.v2016_09_01.aio.operations_async.AuthorizationOperationsOperations
    :ivar management_locks: ManagementLocksOperations operations
    :vartype management_locks: azure.mgmt.resource.locks.v2016_09_01.aio.operations_async.ManagementLocksOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ManagementLockClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.authorization_operations = AuthorizationOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_locks = ManagementLocksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ManagementLockClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
