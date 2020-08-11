# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6272, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

from ._configuration import ContainerRegistryManagementClientConfiguration
from .operations import RegistriesOperations
from .operations import Operations
from .operations import ReplicationsOperations
from .operations import WebhooksOperations
from .operations import RunsOperations
from .operations import TasksOperations
from . import models


class ContainerRegistryManagementClient(object):
    """ContainerRegistryManagementClient.

    :ivar registries: RegistriesOperations operations
    :vartype registries: azure.mgmt.containerregistry.v2018_09_01.operations.RegistriesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerregistry.v2018_09_01.operations.Operations
    :ivar replications: ReplicationsOperations operations
    :vartype replications: azure.mgmt.containerregistry.v2018_09_01.operations.ReplicationsOperations
    :ivar webhooks: WebhooksOperations operations
    :vartype webhooks: azure.mgmt.containerregistry.v2018_09_01.operations.WebhooksOperations
    :ivar runs: RunsOperations operations
    :vartype runs: azure.mgmt.containerregistry.v2018_09_01.operations.RunsOperations
    :ivar tasks: TasksOperations operations
    :vartype tasks: azure.mgmt.containerregistry.v2018_09_01.operations.TasksOperations
    :param subscription_id: The Microsoft Azure subscription ID.
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
        self._config = ContainerRegistryManagementClientConfiguration(subscription_id, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.registries = RegistriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replications = ReplicationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.webhooks = WebhooksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.runs = RunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tasks = TasksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ContainerRegistryManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
