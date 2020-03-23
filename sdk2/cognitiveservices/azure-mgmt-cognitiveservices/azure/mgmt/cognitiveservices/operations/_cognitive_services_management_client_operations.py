# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class CognitiveServicesManagementClientOperationsMixin(object):

    def check_sku_availability(
        self,
        location,  # type: str
        skus,  # type: List[str]
        kind,  # type: str
        type,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.CheckSkuAvailabilityResultList"
        """Check available SKUs.

        :param location: Resource location.
        :type location: str
        :param skus: The SKU of the resource.
        :type skus: list[str]
        :param kind: The Kind of the resource.
        :type kind: str
        :param type: The Type of the resource.
        :type type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckSkuAvailabilityResultList or the result of cls(response)
        :rtype: ~azure.mgmt.cognitiveservices.models.CheckSkuAvailabilityResultList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CheckSkuAvailabilityResultList"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _parameters = models.CheckSkuAvailabilityParameter(skus=skus, kind=kind, type=type)
        api_version = "2017-04-18"

        # Construct URL
        url = self.check_sku_availability.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
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
        body_content = self._serialize.body(_parameters, 'CheckSkuAvailabilityParameter')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CheckSkuAvailabilityResultList', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    check_sku_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.CognitiveServices/locations/{location}/checkSkuAvailability'}

    def check_domain_availability(
        self,
        subdomain_name,  # type: str
        type,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.CheckDomainAvailabilityResult"
        """Check whether a domain is available.

        :param subdomain_name: The subdomain name to use.
        :type subdomain_name: str
        :param type: The Type of the resource.
        :type type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckDomainAvailabilityResult or the result of cls(response)
        :rtype: ~azure.mgmt.cognitiveservices.models.CheckDomainAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CheckDomainAvailabilityResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _parameters = models.CheckDomainAvailabilityParameter(subdomain_name=subdomain_name, type=type)
        api_version = "2017-04-18"

        # Construct URL
        url = self.check_domain_availability.metadata['url']
        path_format_arguments = {
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
        body_content = self._serialize.body(_parameters, 'CheckDomainAvailabilityParameter')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CheckDomainAvailabilityResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    check_domain_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.CognitiveServices/checkDomainAvailability'}
