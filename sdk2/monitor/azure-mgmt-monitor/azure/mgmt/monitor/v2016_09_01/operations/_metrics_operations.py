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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class MetricsOperations(object):
    """MetricsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.monitor.v2016_09_01.models
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

    def list(
        self,
        resource_uri,  # type: str
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MetricCollection"
        """Lists the metric values for a resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param filter: Reduces the set of data collected.:code:`<br>`The filter is optional. If present
     it must contain a list of metric names to retrieve of the form: *(name.value eq 'metricName'
     [or name.value eq 'metricName' or ...])*. Optionally, the filter can contain conditions for the
     following attributes *aggregationType*\ , *startTime*\ , *endTime*\ , and *timeGrain* of the
     form *attributeName operator value*. Where operator is one of *ne*\ , *eq*\ , *gt*\ ,
     *lt*.:code:`<br>`Several conditions can be combined with parentheses and logical operators,
     e.g: *and*\ , *or*.:code:`<br>`Some example filter expressions are::code:`<br>`-
     $filter=(name.value eq 'RunsSucceeded') and aggregationType eq 'Total' and startTime eq
     2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1M',:code:`<br>`-
     $filter=(name.value eq 'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq
     'Average') and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq
     duration'PT1H',:code:`<br>`- $filter=(name.value eq 'ActionsCompleted' or name.value eq
     'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq 'Average') and startTime
     eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq
     duration'PT1M'.:code:`<br>`:code:`<br>`\ **NOTE**\ : When a metrics query comes in with
     multiple metrics, but with no aggregation types defined, the service will pick the Primary
     aggregation type of the first metrics to be used as the default aggregation type for all the
     metrics.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MetricCollection or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2016_09_01.models.MetricCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MetricCollection"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2016-09-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            if filter is not None:
                query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('MetricCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/metrics'}
