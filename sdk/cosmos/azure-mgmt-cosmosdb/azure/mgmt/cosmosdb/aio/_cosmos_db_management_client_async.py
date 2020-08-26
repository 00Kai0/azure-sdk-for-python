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

from ._configuration_async import CosmosDBManagementClientConfiguration
from .operations_async import DatabaseAccountsOperations
from .operations_async import Operations
from .operations_async import DatabaseOperations
from .operations_async import CollectionOperations
from .operations_async import CollectionRegionOperations
from .operations_async import DatabaseAccountRegionOperations
from .operations_async import PercentileSourceTargetOperations
from .operations_async import PercentileTargetOperations
from .operations_async import PercentileOperations
from .operations_async import CollectionPartitionRegionOperations
from .operations_async import CollectionPartitionOperations
from .operations_async import PartitionKeyRangeIdOperations
from .operations_async import PartitionKeyRangeIdRegionOperations
from .operations_async import SqlResourcesOperations
from .operations_async import MongoDBResourcesOperations
from .operations_async import TableResourcesOperations
from .operations_async import CassandraResourcesOperations
from .operations_async import GremlinResourcesOperations
from .operations_async import NotebookWorkspacesOperations
from .operations_async import PrivateLinkResourcesOperations
from .operations_async import PrivateEndpointConnectionsOperations
from .. import models


class CosmosDBManagementClient(object):
    """Azure Cosmos DB Database Service Resource Provider REST API.

    :ivar database_accounts: DatabaseAccountsOperations operations
    :vartype database_accounts: azure.mgmt.cosmosdb.aio.operations_async.DatabaseAccountsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cosmosdb.aio.operations_async.Operations
    :ivar database: DatabaseOperations operations
    :vartype database: azure.mgmt.cosmosdb.aio.operations_async.DatabaseOperations
    :ivar collection: CollectionOperations operations
    :vartype collection: azure.mgmt.cosmosdb.aio.operations_async.CollectionOperations
    :ivar collection_region: CollectionRegionOperations operations
    :vartype collection_region: azure.mgmt.cosmosdb.aio.operations_async.CollectionRegionOperations
    :ivar database_account_region: DatabaseAccountRegionOperations operations
    :vartype database_account_region: azure.mgmt.cosmosdb.aio.operations_async.DatabaseAccountRegionOperations
    :ivar percentile_source_target: PercentileSourceTargetOperations operations
    :vartype percentile_source_target: azure.mgmt.cosmosdb.aio.operations_async.PercentileSourceTargetOperations
    :ivar percentile_target: PercentileTargetOperations operations
    :vartype percentile_target: azure.mgmt.cosmosdb.aio.operations_async.PercentileTargetOperations
    :ivar percentile: PercentileOperations operations
    :vartype percentile: azure.mgmt.cosmosdb.aio.operations_async.PercentileOperations
    :ivar collection_partition_region: CollectionPartitionRegionOperations operations
    :vartype collection_partition_region: azure.mgmt.cosmosdb.aio.operations_async.CollectionPartitionRegionOperations
    :ivar collection_partition: CollectionPartitionOperations operations
    :vartype collection_partition: azure.mgmt.cosmosdb.aio.operations_async.CollectionPartitionOperations
    :ivar partition_key_range_id: PartitionKeyRangeIdOperations operations
    :vartype partition_key_range_id: azure.mgmt.cosmosdb.aio.operations_async.PartitionKeyRangeIdOperations
    :ivar partition_key_range_id_region: PartitionKeyRangeIdRegionOperations operations
    :vartype partition_key_range_id_region: azure.mgmt.cosmosdb.aio.operations_async.PartitionKeyRangeIdRegionOperations
    :ivar sql_resources: SqlResourcesOperations operations
    :vartype sql_resources: azure.mgmt.cosmosdb.aio.operations_async.SqlResourcesOperations
    :ivar mongo_db_resources: MongoDBResourcesOperations operations
    :vartype mongo_db_resources: azure.mgmt.cosmosdb.aio.operations_async.MongoDBResourcesOperations
    :ivar table_resources: TableResourcesOperations operations
    :vartype table_resources: azure.mgmt.cosmosdb.aio.operations_async.TableResourcesOperations
    :ivar cassandra_resources: CassandraResourcesOperations operations
    :vartype cassandra_resources: azure.mgmt.cosmosdb.aio.operations_async.CassandraResourcesOperations
    :ivar gremlin_resources: GremlinResourcesOperations operations
    :vartype gremlin_resources: azure.mgmt.cosmosdb.aio.operations_async.GremlinResourcesOperations
    :ivar notebook_workspaces: NotebookWorkspacesOperations operations
    :vartype notebook_workspaces: azure.mgmt.cosmosdb.aio.operations_async.NotebookWorkspacesOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.cosmosdb.aio.operations_async.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.cosmosdb.aio.operations_async.PrivateEndpointConnectionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
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
        self._config = CosmosDBManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.database_accounts = DatabaseAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.database = DatabaseOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.collection = CollectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.collection_region = CollectionRegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.database_account_region = DatabaseAccountRegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.percentile_source_target = PercentileSourceTargetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.percentile_target = PercentileTargetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.percentile = PercentileOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.collection_partition_region = CollectionPartitionRegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.collection_partition = CollectionPartitionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.partition_key_range_id = PartitionKeyRangeIdOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.partition_key_range_id_region = PartitionKeyRangeIdRegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_resources = SqlResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.mongo_db_resources = MongoDBResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.table_resources = TableResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cassandra_resources = CassandraResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gremlin_resources = GremlinResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notebook_workspaces = NotebookWorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "CosmosDBManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
