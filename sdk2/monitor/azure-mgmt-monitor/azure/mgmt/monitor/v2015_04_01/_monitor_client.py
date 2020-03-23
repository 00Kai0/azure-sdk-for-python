# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import MonitorClientConfiguration
from .operations import ActivityLogsOperations
from .operations import AutoscaleSettingsOperations
from .operations import EventCategoriesOperations
from .operations import Operations
from .operations import TenantActivityLogsOperations
from . import models


class MonitorClient(object):
    """Monitor Management Client.

    :ivar activity_logs: ActivityLogsOperations operations
    :vartype activity_logs: azure.mgmt.monitor.v2015_04_01.operations.ActivityLogsOperations
    :ivar autoscale_settings: AutoscaleSettingsOperations operations
    :vartype autoscale_settings: azure.mgmt.monitor.v2015_04_01.operations.AutoscaleSettingsOperations
    :ivar event_categories: EventCategoriesOperations operations
    :vartype event_categories: azure.mgmt.monitor.v2015_04_01.operations.EventCategoriesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.monitor.v2015_04_01.operations.Operations
    :ivar tenant_activity_logs: TenantActivityLogsOperations operations
    :vartype tenant_activity_logs: azure.mgmt.monitor.v2015_04_01.operations.TenantActivityLogsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MonitorClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.activity_logs = ActivityLogsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.autoscale_settings = AutoscaleSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.event_categories = EventCategoriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tenant_activity_logs = TenantActivityLogsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MonitorClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
