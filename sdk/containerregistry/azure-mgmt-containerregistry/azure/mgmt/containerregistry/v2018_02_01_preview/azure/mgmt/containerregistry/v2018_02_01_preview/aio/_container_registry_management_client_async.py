# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6272, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import ContainerRegistryManagementClientConfiguration
from .operations_async import RegistriesOperations
from .operations_async import Operations
from .operations_async import ReplicationsOperations
from .operations_async import WebhooksOperations
from .operations_async import BuildsOperations
from .operations_async import BuildStepsOperations
from .operations_async import BuildTasksOperations
from .. import models


class ContainerRegistryManagementClient(object):
    """ContainerRegistryManagementClient.

    :ivar registries: RegistriesOperations operations
    :vartype registries: azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations_async.RegistriesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations_async.Operations
    :ivar replications: ReplicationsOperations operations
    :vartype replications: azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations_async.ReplicationsOperations
    :ivar webhooks: WebhooksOperations operations
    :vartype webhooks: azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations_async.WebhooksOperations
    :ivar builds: BuildsOperations operations
    :vartype builds: azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations_async.BuildsOperations
    :ivar build_steps: BuildStepsOperations operations
    :vartype build_steps: azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations_async.BuildStepsOperations
    :ivar build_tasks: BuildTasksOperations operations
    :vartype build_tasks: azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations_async.BuildTasksOperations
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ContainerRegistryManagementClientConfiguration(subscription_id, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

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
        self.builds = BuildsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.build_steps = BuildStepsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.build_tasks = BuildTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ContainerRegistryManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)