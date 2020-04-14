# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class EncryptionScopesOperations:
    """EncryptionScopesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.storage.v2019_06_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def put(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: "models.EncryptionScope",
        **kwargs
    ) -> "models.EncryptionScope":
        """Synchronously creates or updates an encryption scope under the specified storage account. If an encryption scope is already created and a subsequent request is issued with different properties, the encryption scope properties will be updated per the specified request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and lower-
         case letters only.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the create or update.
        :type encryption_scope: ~azure.mgmt.storage.v2019_06_01.models.EncryptionScope
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.EncryptionScope or ~azure.mgmt.storage.v2019_06_01.models.EncryptionScope
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EncryptionScope"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-06-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.put.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'encryptionScopeName': self._serialize.url("encryption_scope_name", encryption_scope_name, 'str', max_length=63, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(encryption_scope, 'EncryptionScope')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('EncryptionScope', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('EncryptionScope', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    put.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}'}

    async def patch(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: "models.EncryptionScope",
        **kwargs
    ) -> "models.EncryptionScope":
        """Update encryption scope properties as specified in the request body. Update fails if the specified encryption scope does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and lower-
         case letters only.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the update.
        :type encryption_scope: ~azure.mgmt.storage.v2019_06_01.models.EncryptionScope
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.EncryptionScope
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EncryptionScope"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-06-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.patch.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'encryptionScopeName': self._serialize.url("encryption_scope_name", encryption_scope_name, 'str', max_length=63, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(encryption_scope, 'EncryptionScope')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EncryptionScope', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    patch.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}'}

    async def get(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        **kwargs
    ) -> "models.EncryptionScope":
        """Returns the properties for the specified encryption scope.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and lower-
         case letters only.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number.
        :type encryption_scope_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.EncryptionScope
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EncryptionScope"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-06-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'encryptionScopeName': self._serialize.url("encryption_scope_name", encryption_scope_name, 'str', max_length=63, min_length=3),
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EncryptionScope', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}'}

    def list(
        self,
        resource_group_name: str,
        account_name: str,
        **kwargs
    ) -> "models.EncryptionScopeListResult":
        """Lists all the encryption scopes available under the specified storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
     name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and lower-
     case letters only.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScopeListResult or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.EncryptionScopeListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EncryptionScopeListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-06-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('EncryptionScopeListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes'}
