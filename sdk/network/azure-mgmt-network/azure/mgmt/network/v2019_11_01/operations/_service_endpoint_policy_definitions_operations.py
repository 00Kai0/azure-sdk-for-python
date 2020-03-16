# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ServiceEndpointPolicyDefinitionsOperations(object):
    """ServiceEndpointPolicyDefinitionsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2019_11_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _delete_initial(
        self,
        resource_group_name,  # type: str
        service_endpoint_policy_name,  # type: str
        service_endpoint_policy_definition_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        # Construct URL
        url = self._delete_initial.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceEndpointPolicyName': self._serialize.url("service_endpoint_policy_name", service_endpoint_policy_name, 'str'),
            'serviceEndpointPolicyDefinitionName': self._serialize.url("service_endpoint_policy_definition_name", service_endpoint_policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName}'}

    def begin_delete(
        self,
        resource_group_name,  # type: str
        service_endpoint_policy_name,  # type: str
        service_endpoint_policy_definition_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes the specified ServiceEndpoint policy definitions.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_endpoint_policy_name: The name of the Service Endpoint Policy.
        :type service_endpoint_policy_name: str
        :param service_endpoint_policy_definition_name: The name of the service endpoint policy
     definition.
        :type service_endpoint_policy_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            service_endpoint_policy_name=service_endpoint_policy_name,
            service_endpoint_policy_definition_name=service_endpoint_policy_definition_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'location'},  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName}'}

    def get(
        self,
        resource_group_name,  # type: str
        service_endpoint_policy_name,  # type: str
        service_endpoint_policy_definition_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ServiceEndpointPolicyDefinition"
        """Get the specified service endpoint policy definitions from service endpoint policy.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_endpoint_policy_name: The name of the service endpoint policy name.
        :type service_endpoint_policy_name: str
        :param service_endpoint_policy_definition_name: The name of the service endpoint policy
         definition name.
        :type service_endpoint_policy_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceEndpointPolicyDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2019_11_01.models.ServiceEndpointPolicyDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ServiceEndpointPolicyDefinition"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceEndpointPolicyName': self._serialize.url("service_endpoint_policy_name", service_endpoint_policy_name, 'str'),
            'serviceEndpointPolicyDefinitionName': self._serialize.url("service_endpoint_policy_definition_name", service_endpoint_policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ServiceEndpointPolicyDefinition', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName}'}

    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        service_endpoint_policy_name,  # type: str
        service_endpoint_policy_definition_name,  # type: str
        service_endpoint_policy_definitions,  # type: "models.ServiceEndpointPolicyDefinition"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ServiceEndpointPolicyDefinition"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ServiceEndpointPolicyDefinition"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        # Construct URL
        url = self._create_or_update_initial.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceEndpointPolicyName': self._serialize.url("service_endpoint_policy_name", service_endpoint_policy_name, 'str'),
            'serviceEndpointPolicyDefinitionName': self._serialize.url("service_endpoint_policy_definition_name", service_endpoint_policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(service_endpoint_policy_definitions, 'ServiceEndpointPolicyDefinition')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ServiceEndpointPolicyDefinition', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ServiceEndpointPolicyDefinition', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName}'}

    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        service_endpoint_policy_name,  # type: str
        service_endpoint_policy_definition_name,  # type: str
        service_endpoint_policy_definitions,  # type: "models.ServiceEndpointPolicyDefinition"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ServiceEndpointPolicyDefinition"
        """Creates or updates a service endpoint policy definition in the specified service endpoint policy.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_endpoint_policy_name: The name of the service endpoint policy.
        :type service_endpoint_policy_name: str
        :param service_endpoint_policy_definition_name: The name of the service endpoint policy
     definition name.
        :type service_endpoint_policy_definition_name: str
        :param service_endpoint_policy_definitions: Parameters supplied to the create or update service
     endpoint policy operation.
        :type service_endpoint_policy_definitions: ~azure.mgmt.network.v2019_11_01.models.ServiceEndpointPolicyDefinition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns ServiceEndpointPolicyDefinition
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.network.v2019_11_01.models.ServiceEndpointPolicyDefinition]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ServiceEndpointPolicyDefinition"]
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            service_endpoint_policy_name=service_endpoint_policy_name,
            service_endpoint_policy_definition_name=service_endpoint_policy_definition_name,
            service_endpoint_policy_definitions=service_endpoint_policy_definitions,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('ServiceEndpointPolicyDefinition', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'},  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName}'}

    def list_by_resource_group(
        self,
        resource_group_name,  # type: str
        service_endpoint_policy_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ServiceEndpointPolicyDefinitionListResult"
        """Gets all service endpoint policy definitions in a service end point policy.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_endpoint_policy_name: The name of the service endpoint policy name.
        :type service_endpoint_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceEndpointPolicyDefinitionListResult or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2019_11_01.models.ServiceEndpointPolicyDefinitionListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ServiceEndpointPolicyDefinitionListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'serviceEndpointPolicyName': self._serialize.url("service_endpoint_policy_name", service_endpoint_policy_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ServiceEndpointPolicyDefinitionListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions'}
