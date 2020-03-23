# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DiagnosticSettingsOperations(object):
    """DiagnosticSettingsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.monitor.v2017_05_01_preview.models
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

    def get(
        self,
        resource_uri,  # type: str
        name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DiagnosticSettingsResource"
        """Gets the active diagnostic settings for the specified resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2017_05_01_preview.models.DiagnosticSettingsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DiagnosticSettingsResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-05-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
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
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DiagnosticSettingsResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/diagnosticSettings/{name}'}

    def create_or_update(
        self,
        resource_uri,  # type: str
        name,  # type: str
        parameters,  # type: "models.DiagnosticSettingsResource"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DiagnosticSettingsResource"
        """Creates or updates diagnostic settings for the specified resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :param parameters: Parameters supplied to the operation.
        :type parameters: ~azure.mgmt.monitor.v2017_05_01_preview.models.DiagnosticSettingsResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2017_05_01_preview.models.DiagnosticSettingsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DiagnosticSettingsResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-05-01-preview"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
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
        body_content = self._serialize.body(parameters, 'DiagnosticSettingsResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DiagnosticSettingsResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/diagnosticSettings/{name}'}

    def delete(
        self,
        resource_uri,  # type: str
        name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes existing diagnostic settings for the specified resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-05-01-preview"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/diagnosticSettings/{name}'}

    def list(
        self,
        resource_uri,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DiagnosticSettingsResourceCollection"
        """Gets the active diagnostic settings list for the specified resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DiagnosticSettingsResourceCollection or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2017_05_01_preview.models.DiagnosticSettingsResourceCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DiagnosticSettingsResourceCollection"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-05-01-preview"

        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
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
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DiagnosticSettingsResourceCollection', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/diagnosticSettings'}
