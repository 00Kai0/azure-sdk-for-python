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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DataFlowsOperations(object):
    """DataFlowsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.datafactory.models
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

    def create_or_update(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        data_flow_name,  # type: str
        data_flow,  # type: "models.DataFlowResource"
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DataFlowResource"
        """Creates or updates a data flow.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param data_flow_name: The data flow name.
        :type data_flow_name: str
        :param data_flow: Data flow resource definition.
        :type data_flow: ~azure.mgmt.datafactory.models.DataFlowResource
        :param if_match: ETag of the data flow entity. Should only be specified for update, for which
         it should match existing entity or can be * for unconditional update.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataFlowResource, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.DataFlowResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DataFlowResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'dataFlowName': self._serialize.url("data_flow_name", data_flow_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(data_flow, 'DataFlowResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DataFlowResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/dataflows/{dataFlowName}'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        data_flow_name,  # type: str
        if_none_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DataFlowResource"
        """Gets a data flow.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param data_flow_name: The data flow name.
        :type data_flow_name: str
        :param if_none_match: ETag of the data flow entity. Should only be specified for get. If the
         ETag matches the existing entity tag, or if * was provided, then no content will be returned.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataFlowResource, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.DataFlowResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DataFlowResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'dataFlowName': self._serialize.url("data_flow_name", data_flow_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DataFlowResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/dataflows/{dataFlowName}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        data_flow_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a data flow.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param data_flow_name: The data flow name.
        :type data_flow_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'dataFlowName': self._serialize.url("data_flow_name", data_flow_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/dataflows/{dataFlowName}'}  # type: ignore

    def list_by_factory(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.DataFlowListResponse"]
        """Lists data flows.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DataFlowListResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.datafactory.models.DataFlowListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DataFlowListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_factory.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
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
            deserialized = self._deserialize('DataFlowListResponse', pipeline_response)
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
    list_by_factory.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/dataflows'}  # type: ignore
