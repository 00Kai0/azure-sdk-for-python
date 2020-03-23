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

from ._configuration_async import MonitorClientConfiguration
from .operations_async import GuestDiagnosticsSettingsAssociationOperations
from .operations_async import GuestDiagnosticsSettingsOperations
from .. import models


class MonitorClient(object):
    """Monitor Management Client.

    :ivar guest_diagnostics_settings_association: GuestDiagnosticsSettingsAssociationOperations operations
    :vartype guest_diagnostics_settings_association: azure.mgmt.monitor.v2018_06_01_preview.aio.operations_async.GuestDiagnosticsSettingsAssociationOperations
    :ivar guest_diagnostics_settings: GuestDiagnosticsSettingsOperations operations
    :vartype guest_diagnostics_settings: azure.mgmt.monitor.v2018_06_01_preview.aio.operations_async.GuestDiagnosticsSettingsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription Id.
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
        self._config = MonitorClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.guest_diagnostics_settings_association = GuestDiagnosticsSettingsAssociationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.guest_diagnostics_settings = GuestDiagnosticsSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MonitorClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
