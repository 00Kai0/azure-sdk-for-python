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

class VirtualMachineScaleSetExtensionsOperations(object):
    """VirtualMachineScaleSetExtensionsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2017_12_01.models
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

    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        vm_scale_set_name,  # type: str
        vmss_extension_name,  # type: str
        extension_parameters,  # type: "models.VirtualMachineScaleSetExtension"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.VirtualMachineScaleSetExtension"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.VirtualMachineScaleSetExtension"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-12-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'vmScaleSetName': self._serialize.url("vm_scale_set_name", vm_scale_set_name, 'str'),
            'vmssExtensionName': self._serialize.url("vmss_extension_name", vmss_extension_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
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
        body_content = self._serialize.body(extension_parameters, 'VirtualMachineScaleSetExtension')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}

    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        vm_scale_set_name,  # type: str
        vmss_extension_name,  # type: str
        extension_parameters,  # type: "models.VirtualMachineScaleSetExtension"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.VirtualMachineScaleSetExtension"
        """The operation to create or update an extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set where the extension should be create or
     updated.
        :type vm_scale_set_name: str
        :param vmss_extension_name: The name of the VM scale set extension.
        :type vmss_extension_name: str
        :param extension_parameters: Parameters supplied to the Create VM scale set Extension
     operation.
        :type extension_parameters: ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineScaleSetExtension
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns VirtualMachineScaleSetExtension
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.compute.v2017_12_01.models.VirtualMachineScaleSetExtension]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.VirtualMachineScaleSetExtension"]
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            vmss_extension_name=vmss_extension_name,
            extension_parameters=extension_parameters,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}

    def _delete_initial(
        self,
        resource_group_name,  # type: str
        vm_scale_set_name,  # type: str
        vmss_extension_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.OperationStatusResponse"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.OperationStatusResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-12-01"

        # Construct URL
        url = self._delete_initial.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'vmScaleSetName': self._serialize.url("vm_scale_set_name", vm_scale_set_name, 'str'),
            'vmssExtensionName': self._serialize.url("vmss_extension_name", vmss_extension_name, 'str'),
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
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('OperationStatusResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}

    def begin_delete(
        self,
        resource_group_name,  # type: str
        vm_scale_set_name,  # type: str
        vmss_extension_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.OperationStatusResponse"
        """The operation to delete the extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set where the extension should be deleted.
        :type vm_scale_set_name: str
        :param vmss_extension_name: The name of the VM scale set extension.
        :type vmss_extension_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns OperationStatusResponse
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.compute.v2017_12_01.models.OperationStatusResponse]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.OperationStatusResponse"]
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            vmss_extension_name=vmss_extension_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('OperationStatusResponse', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}

    def get(
        self,
        resource_group_name,  # type: str
        vm_scale_set_name,  # type: str
        vmss_extension_name,  # type: str
        expand=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.VirtualMachineScaleSetExtension"
        """The operation to get the extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set containing the extension.
        :type vm_scale_set_name: str
        :param vmss_extension_name: The name of the VM scale set extension.
        :type vmss_extension_name: str
        :param expand: The expand expression to apply on the operation.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineScaleSetExtension or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineScaleSetExtension
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.VirtualMachineScaleSetExtension"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-12-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'vmScaleSetName': self._serialize.url("vm_scale_set_name", vm_scale_set_name, 'str'),
            'vmssExtensionName': self._serialize.url("vmss_extension_name", vmss_extension_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
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

        deserialized = self._deserialize('VirtualMachineScaleSetExtension', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}'}

    def list(
        self,
        resource_group_name,  # type: str
        vm_scale_set_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.VirtualMachineScaleSetExtensionListResult"
        """Gets a list of all extensions in a VM scale set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set containing the extension.
        :type vm_scale_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineScaleSetExtensionListResult or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineScaleSetExtensionListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.VirtualMachineScaleSetExtensionListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-12-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'vmScaleSetName': self._serialize.url("vm_scale_set_name", vm_scale_set_name, 'str'),
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
            deserialized = self._deserialize('VirtualMachineScaleSetExtensionListResult', pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions'}
