# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class FrontendEndpointsOperations(object):
    """FrontendEndpointsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.frontdoor.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_front_door(
        self,
        resource_group_name,  # type: str
        front_door_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.FrontendEndpointsListResult"]
        """Lists all of the frontend endpoints within a Front Door.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param front_door_name: Name of the Front Door which is globally unique.
        :type front_door_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FrontendEndpointsListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.frontdoor.models.FrontendEndpointsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FrontendEndpointsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_front_door.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
                    'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('FrontendEndpointsListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_front_door.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        front_door_name,  # type: str
        frontend_endpoint_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FrontendEndpoint"
        """Gets a Frontend endpoint with the specified name within the specified Front Door.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param front_door_name: Name of the Front Door which is globally unique.
        :type front_door_name: str
        :param frontend_endpoint_name: Name of the Frontend endpoint which is unique within the Front
         Door.
        :type frontend_endpoint_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FrontendEndpoint, or the result of cls(response)
        :rtype: ~azure.mgmt.frontdoor.models.FrontendEndpoint
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FrontendEndpoint"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
            'frontendEndpointName': self._serialize.url("frontend_endpoint_name", frontend_endpoint_name, 'str', max_length=255, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FrontendEndpoint', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}'}  # type: ignore

    def _enable_https_initial(
        self,
        resource_group_name,  # type: str
        front_door_name,  # type: str
        frontend_endpoint_name,  # type: str
        custom_https_configuration,  # type: "_models.CustomHttpsConfiguration"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._enable_https_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
            'frontendEndpointName': self._serialize.url("frontend_endpoint_name", frontend_endpoint_name, 'str', max_length=255, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(custom_https_configuration, 'CustomHttpsConfiguration')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _enable_https_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/enableHttps'}  # type: ignore

    def begin_enable_https(
        self,
        resource_group_name,  # type: str
        front_door_name,  # type: str
        frontend_endpoint_name,  # type: str
        custom_https_configuration,  # type: "_models.CustomHttpsConfiguration"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Enables a frontendEndpoint for HTTPS traffic.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param front_door_name: Name of the Front Door which is globally unique.
        :type front_door_name: str
        :param frontend_endpoint_name: Name of the Frontend endpoint which is unique within the Front
         Door.
        :type frontend_endpoint_name: str
        :param custom_https_configuration: The configuration specifying how to enable HTTPS.
        :type custom_https_configuration: ~azure.mgmt.frontdoor.models.CustomHttpsConfiguration
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._enable_https_initial(
                resource_group_name=resource_group_name,
                front_door_name=front_door_name,
                frontend_endpoint_name=frontend_endpoint_name,
                custom_https_configuration=custom_https_configuration,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
            'frontendEndpointName': self._serialize.url("frontend_endpoint_name", frontend_endpoint_name, 'str', max_length=255, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$'),
        }

        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_enable_https.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/enableHttps'}  # type: ignore

    def _disable_https_initial(
        self,
        resource_group_name,  # type: str
        front_door_name,  # type: str
        frontend_endpoint_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-05-01"
        accept = "application/json"

        # Construct URL
        url = self._disable_https_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
            'frontendEndpointName': self._serialize.url("frontend_endpoint_name", frontend_endpoint_name, 'str', max_length=255, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _disable_https_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/disableHttps'}  # type: ignore

    def begin_disable_https(
        self,
        resource_group_name,  # type: str
        front_door_name,  # type: str
        frontend_endpoint_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Disables a frontendEndpoint for HTTPS traffic.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param front_door_name: Name of the Front Door which is globally unique.
        :type front_door_name: str
        :param frontend_endpoint_name: Name of the Frontend endpoint which is unique within the Front
         Door.
        :type frontend_endpoint_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._disable_https_initial(
                resource_group_name=resource_group_name,
                front_door_name=front_door_name,
                frontend_endpoint_name=frontend_endpoint_name,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'frontDoorName': self._serialize.url("front_door_name", front_door_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]+([-a-zA-Z0-9]?[a-zA-Z0-9])*$'),
            'frontendEndpointName': self._serialize.url("frontend_endpoint_name", frontend_endpoint_name, 'str', max_length=255, min_length=1, pattern=r'^[a-zA-Z0-9]+(-*[a-zA-Z0-9])*$'),
        }

        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_disable_https.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/disableHttps'}  # type: ignore
