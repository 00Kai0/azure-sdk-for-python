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

from ._configuration import NetworkManagementClientConfiguration
from .operations import AvailableEndpointServicesOperations
from .operations import PrivateEndpointsOperations
from .operations import AvailablePrivateEndpointTypesOperations
from .operations import PrivateDnsZoneGroupsOperations
from .operations import PrivateLinkServicesOperations
from . import models


class NetworkManagementClient(object):
    """Network Client.

    :ivar available_endpoint_services: AvailableEndpointServicesOperations operations
    :vartype available_endpoint_services: azure.mgmt.network.v2020_03_01.operations.AvailableEndpointServicesOperations
    :ivar private_endpoints: PrivateEndpointsOperations operations
    :vartype private_endpoints: azure.mgmt.network.v2020_03_01.operations.PrivateEndpointsOperations
    :ivar available_private_endpoint_types: AvailablePrivateEndpointTypesOperations operations
    :vartype available_private_endpoint_types: azure.mgmt.network.v2020_03_01.operations.AvailablePrivateEndpointTypesOperations
    :ivar private_dns_zone_groups: PrivateDnsZoneGroupsOperations operations
    :vartype private_dns_zone_groups: azure.mgmt.network.v2020_03_01.operations.PrivateDnsZoneGroupsOperations
    :ivar private_link_services: PrivateLinkServicesOperations operations
    :vartype private_link_services: azure.mgmt.network.v2020_03_01.operations.PrivateLinkServicesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
        self._config = NetworkManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.available_endpoint_services = AvailableEndpointServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoints = PrivateEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.available_private_endpoint_types = AvailablePrivateEndpointTypesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_dns_zone_groups = PrivateDnsZoneGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_services = PrivateLinkServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> NetworkManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
