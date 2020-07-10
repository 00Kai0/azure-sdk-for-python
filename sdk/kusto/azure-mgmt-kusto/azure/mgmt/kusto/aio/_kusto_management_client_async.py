# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import KustoManagementClientConfiguration
from .operations_async import ClustersOperations
from .operations_async import ClusterPrincipalAssignmentsOperations
from .operations_async import DatabasesOperations
from .operations_async import DatabasePrincipalAssignmentsOperations
from .operations_async import AttachedDatabaseConfigurationsOperations
from .operations_async import DataConnectionsOperations
from .operations_async import Operations
from .. import models


class KustoManagementClient(object):
    """The Azure Kusto management API provides a RESTful set of web services that interact with Azure Kusto services to manage your clusters and databases. The API enables you to create, update, and delete clusters and databases.

    :ivar clusters: ClustersOperations operations
    :vartype clusters: azure.mgmt.kusto.aio.operations_async.ClustersOperations
    :ivar cluster_principal_assignments: ClusterPrincipalAssignmentsOperations operations
    :vartype cluster_principal_assignments: azure.mgmt.kusto.aio.operations_async.ClusterPrincipalAssignmentsOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.kusto.aio.operations_async.DatabasesOperations
    :ivar database_principal_assignments: DatabasePrincipalAssignmentsOperations operations
    :vartype database_principal_assignments: azure.mgmt.kusto.aio.operations_async.DatabasePrincipalAssignmentsOperations
    :ivar attached_database_configurations: AttachedDatabaseConfigurationsOperations operations
    :vartype attached_database_configurations: azure.mgmt.kusto.aio.operations_async.AttachedDatabaseConfigurationsOperations
    :ivar data_connections: DataConnectionsOperations operations
    :vartype data_connections: azure.mgmt.kusto.aio.operations_async.DataConnectionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.kusto.aio.operations_async.Operations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = KustoManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.clusters = ClustersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cluster_principal_assignments = ClusterPrincipalAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.database_principal_assignments = DatabasePrincipalAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.attached_database_configurations = AttachedDatabaseConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_connections = DataConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "KustoManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
