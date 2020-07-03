# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6282, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

from ._configuration import KustoManagementClientConfiguration
from .operations import ClustersOperations
from .operations import ClusterPrincipalAssignmentsOperations
from .operations import DatabasesOperations
from .operations import DatabasePrincipalAssignmentsOperations
from .operations import AttachedDatabaseConfigurationsOperations
from .operations import DataConnectionsOperations
from .operations import Operations
from . import models


class KustoManagementClient(object):
    """The Azure Kusto management API provides a RESTful set of web services that interact with Azure Kusto services to manage your clusters and databases. The API enables you to create, update, and delete clusters and databases.

    :ivar clusters: ClustersOperations operations
    :vartype clusters: kusto_management_client.operations.ClustersOperations
    :ivar cluster_principal_assignments: ClusterPrincipalAssignmentsOperations operations
    :vartype cluster_principal_assignments: kusto_management_client.operations.ClusterPrincipalAssignmentsOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: kusto_management_client.operations.DatabasesOperations
    :ivar database_principal_assignments: DatabasePrincipalAssignmentsOperations operations
    :vartype database_principal_assignments: kusto_management_client.operations.DatabasePrincipalAssignmentsOperations
    :ivar attached_database_configurations: AttachedDatabaseConfigurationsOperations operations
    :vartype attached_database_configurations: kusto_management_client.operations.AttachedDatabaseConfigurationsOperations
    :ivar data_connections: DataConnectionsOperations operations
    :vartype data_connections: kusto_management_client.operations.DataConnectionsOperations
    :ivar operations: Operations operations
    :vartype operations: kusto_management_client.operations.Operations
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = KustoManagementClientConfiguration(subscription_id, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

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

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> KustoManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
