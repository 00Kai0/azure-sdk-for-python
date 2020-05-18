# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AvailableCluster(msrest.serialization.Model):
    """Pre-provisioned and readily available Event Hubs Cluster count per region.

    :param location: Location fo the Available Cluster.
    :type location: str
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AvailableCluster, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)


class AvailableClustersList(msrest.serialization.Model):
    """The response of the List Available Clusters operation.

    :param value: The count of readily available and pre-provisioned Event Hubs Clusters per
     region.
    :type value: list[~azure.mgmt.eventhub.v2018_01_01_preview.models.AvailableCluster]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[AvailableCluster]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AvailableClustersList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class Resource(msrest.serialization.Model):
    """The Resource definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """Definition of an Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class Cluster(TrackedResource):
    """Single Event Hubs Cluster resource in List or Get operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param sku: Properties of the cluster SKU.
    :type sku: ~azure.mgmt.eventhub.v2018_01_01_preview.models.ClusterSku
    :ivar created: The UTC time when the Event Hubs Cluster was created.
    :vartype created: str
    :ivar updated: The UTC time when the Event Hubs Cluster was last updated.
    :vartype updated: str
    :ivar metric_id: The metric ID of the cluster resource. Provided by the service and not
     modifiable by the user.
    :vartype metric_id: str
    :ivar status: Status of the Cluster resource.
    :vartype status: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created': {'readonly': True},
        'updated': {'readonly': True},
        'metric_id': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'ClusterSku'},
        'created': {'key': 'properties.created', 'type': 'str'},
        'updated': {'key': 'properties.updated', 'type': 'str'},
        'metric_id': {'key': 'properties.metricId', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Cluster, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.created = None
        self.updated = None
        self.metric_id = None
        self.status = None


class ClusterListResult(msrest.serialization.Model):
    """The response of the List Event Hubs Clusters operation.

    :param value: The Event Hubs Clusters present in the List Event Hubs operation results.
    :type value: list[~azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster]
    :param next_link: Link to the next set of results. Empty unless the value parameter contains an
     incomplete list of Event Hubs Clusters.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Cluster]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ClusterListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class ClusterQuotaConfigurationProperties(msrest.serialization.Model):
    """Contains all settings for the cluster.

    :param settings: All possible Cluster settings - a collection of key/value paired settings
     which apply to quotas and configurations imposed on the cluster.
    :type settings: dict[str, str]
    """

    _attribute_map = {
        'settings': {'key': 'settings', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ClusterQuotaConfigurationProperties, self).__init__(**kwargs)
        self.settings = kwargs.get('settings', None)


class ClusterSku(msrest.serialization.Model):
    """SKU parameters particular to a cluster instance.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of this SKU. Possible values include: 'Dedicated', 'Basic',
     'Standard'.
    :type name: str or ~azure.mgmt.eventhub.v2018_01_01_preview.models.SkuName
    :param capacity: The quantity of Event Hubs Cluster Capacity Units contained in this cluster.
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
        'capacity': {'maximum': 32, 'minimum': 1},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ClusterSku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.capacity = kwargs.get('capacity', None)


class EHNamespace(TrackedResource):
    """Single Namespace item in List or Get Operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param sku: Properties of sku resource.
    :type sku: ~azure.mgmt.eventhub.v2018_01_01_preview.models.Sku
    :ivar provisioning_state: Provisioning state of the Namespace.
    :vartype provisioning_state: str
    :ivar created_at: The time the Namespace was created.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: The time the Namespace was updated.
    :vartype updated_at: ~datetime.datetime
    :ivar service_bus_endpoint: Endpoint you can use to perform Service Bus operations.
    :vartype service_bus_endpoint: str
    :param cluster_arm_id: Cluster ARM ID of the Namespace.
    :type cluster_arm_id: str
    :ivar metric_id: Identifier for Azure Insights metrics.
    :vartype metric_id: str
    :param is_auto_inflate_enabled: Value that indicates whether AutoInflate is enabled for
     eventhub namespace.
    :type is_auto_inflate_enabled: bool
    :param maximum_throughput_units: Upper limit of throughput units when AutoInflate is enabled,
     value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true).
    :type maximum_throughput_units: int
    :param kafka_enabled: Value that indicates whether Kafka is enabled for eventhub namespace.
    :type kafka_enabled: bool
    :param zone_redundant: Enabling this property creates a Standard Event Hubs Namespace in
     regions supported availability zones.
    :type zone_redundant: bool
    :param identity: Properties of BYOK Identity description.
    :type identity: ~azure.mgmt.eventhub.v2018_01_01_preview.models.Identity
    :param encryption: Properties of BYOK Encryption description.
    :type encryption: ~azure.mgmt.eventhub.v2018_01_01_preview.models.Encryption
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'service_bus_endpoint': {'readonly': True},
        'metric_id': {'readonly': True},
        'maximum_throughput_units': {'maximum': 20, 'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'service_bus_endpoint': {'key': 'properties.serviceBusEndpoint', 'type': 'str'},
        'cluster_arm_id': {'key': 'properties.clusterArmId', 'type': 'str'},
        'metric_id': {'key': 'properties.metricId', 'type': 'str'},
        'is_auto_inflate_enabled': {'key': 'properties.isAutoInflateEnabled', 'type': 'bool'},
        'maximum_throughput_units': {'key': 'properties.maximumThroughputUnits', 'type': 'int'},
        'kafka_enabled': {'key': 'properties.kafkaEnabled', 'type': 'bool'},
        'zone_redundant': {'key': 'properties.zoneRedundant', 'type': 'bool'},
        'identity': {'key': 'properties.identity', 'type': 'Identity'},
        'encryption': {'key': 'properties.encryption', 'type': 'Encryption'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EHNamespace, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.provisioning_state = None
        self.created_at = None
        self.updated_at = None
        self.service_bus_endpoint = None
        self.cluster_arm_id = kwargs.get('cluster_arm_id', None)
        self.metric_id = None
        self.is_auto_inflate_enabled = kwargs.get('is_auto_inflate_enabled', None)
        self.maximum_throughput_units = kwargs.get('maximum_throughput_units', None)
        self.kafka_enabled = kwargs.get('kafka_enabled', None)
        self.zone_redundant = kwargs.get('zone_redundant', None)
        self.identity = kwargs.get('identity', None)
        self.encryption = kwargs.get('encryption', None)


class EHNamespaceIdContainer(msrest.serialization.Model):
    """The full ARM ID of an Event Hubs Namespace.

    :param id: id parameter.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EHNamespaceIdContainer, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class EHNamespaceIdListResult(msrest.serialization.Model):
    """The response of the List Namespace IDs operation.

    :param value: Result of the List Namespace IDs operation.
    :type value: list[~azure.mgmt.eventhub.v2018_01_01_preview.models.EHNamespaceIdContainer]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EHNamespaceIdContainer]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EHNamespaceIdListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class EHNamespaceListResult(msrest.serialization.Model):
    """The response of the List Namespace operation.

    :param value: Result of the List Namespace operation.
    :type value: list[~azure.mgmt.eventhub.v2018_01_01_preview.models.EHNamespace]
    :param next_link: Link to the next set of results. Not empty if Value contains incomplete list
     of namespaces.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EHNamespace]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EHNamespaceListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class Encryption(msrest.serialization.Model):
    """Properties to configure Encryption.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param key_vault_properties: Properties of KeyVault.
    :type key_vault_properties: ~azure.mgmt.eventhub.v2018_01_01_preview.models.KeyVaultProperties
    :ivar key_source: Enumerates the possible value of keySource for Encryption. Default value:
     "Microsoft.KeyVault".
    :vartype key_source: str
    """

    _validation = {
        'key_source': {'constant': True},
    }

    _attribute_map = {
        'key_vault_properties': {'key': 'keyVaultProperties', 'type': 'KeyVaultProperties'},
        'key_source': {'key': 'keySource', 'type': 'str'},
    }

    key_source = "Microsoft.KeyVault"

    def __init__(
        self,
        **kwargs
    ):
        super(Encryption, self).__init__(**kwargs)
        self.key_vault_properties = kwargs.get('key_vault_properties', None)


class ErrorResponse(msrest.serialization.Model):
    """Error response that indicates the service is not able to process the incoming request. The reason is provided in the error message.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class Identity(msrest.serialization.Model):
    """Properties to configure Identity for Bring your Own Keys.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param principal_id: ObjectId from the KeyVault.
    :type principal_id: str
    :param tenant_id: TenantId from the KeyVault.
    :type tenant_id: str
    :ivar type: Enumerates the possible value Identity type, which currently supports only
     'SystemAssigned'. Default value: "SystemAssigned".
    :vartype type: str
    """

    _validation = {
        'type': {'constant': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "SystemAssigned"

    def __init__(
        self,
        **kwargs
    ):
        super(Identity, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.tenant_id = kwargs.get('tenant_id', None)


class IpFilterRule(Resource):
    """Single item in a List or Get IpFilterRules operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param ip_mask: IP Mask.
    :type ip_mask: str
    :param action: The IP Filter Action. Possible values include: 'Accept', 'Reject'.
    :type action: str or ~azure.mgmt.eventhub.v2018_01_01_preview.models.IPAction
    :param filter_name: IP Filter name.
    :type filter_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'ip_mask': {'key': 'properties.ipMask', 'type': 'str'},
        'action': {'key': 'properties.action', 'type': 'str'},
        'filter_name': {'key': 'properties.filterName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(IpFilterRule, self).__init__(**kwargs)
        self.ip_mask = kwargs.get('ip_mask', None)
        self.action = kwargs.get('action', None)
        self.filter_name = kwargs.get('filter_name', None)


class IpFilterRuleListResult(msrest.serialization.Model):
    """The response from the List namespace operation.

    :param value: Result of the List IpFilter Rules operation.
    :type value: list[~azure.mgmt.eventhub.v2018_01_01_preview.models.IpFilterRule]
    :param next_link: Link to the next set of results. Not empty if Value contains an incomplete
     list of IpFilter Rules.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[IpFilterRule]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(IpFilterRuleListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class KeyVaultProperties(msrest.serialization.Model):
    """Properties to configure keyVault Properties.

    :param key_name: Name of the Key from KeyVault.
    :type key_name: str
    :param key_vault_uri: Uri of KeyVault.
    :type key_vault_uri: str
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
        'key_vault_uri': {'key': 'keyVaultUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyVaultProperties, self).__init__(**kwargs)
        self.key_name = kwargs.get('key_name', None)
        self.key_vault_uri = kwargs.get('key_vault_uri', None)


class NetworkRuleSet(Resource):
    """Description of topic resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param default_action: Default Action for Network Rule Set. Possible values include: 'Allow',
     'Deny'.
    :type default_action: str or ~azure.mgmt.eventhub.v2018_01_01_preview.models.DefaultAction
    :param virtual_network_rules: List VirtualNetwork Rules.
    :type virtual_network_rules:
     list[~azure.mgmt.eventhub.v2018_01_01_preview.models.NWRuleSetVirtualNetworkRules]
    :param ip_rules: List of IpRules.
    :type ip_rules: list[~azure.mgmt.eventhub.v2018_01_01_preview.models.NWRuleSetIpRules]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'default_action': {'key': 'properties.defaultAction', 'type': 'str'},
        'virtual_network_rules': {'key': 'properties.virtualNetworkRules', 'type': '[NWRuleSetVirtualNetworkRules]'},
        'ip_rules': {'key': 'properties.ipRules', 'type': '[NWRuleSetIpRules]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(NetworkRuleSet, self).__init__(**kwargs)
        self.default_action = kwargs.get('default_action', None)
        self.virtual_network_rules = kwargs.get('virtual_network_rules', None)
        self.ip_rules = kwargs.get('ip_rules', None)


class NWRuleSetIpRules(msrest.serialization.Model):
    """The response from the List namespace operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param ip_mask: IP Mask.
    :type ip_mask: str
    :ivar action: The IP Filter Action. Default value: "Allow".
    :vartype action: str
    """

    _validation = {
        'action': {'constant': True},
    }

    _attribute_map = {
        'ip_mask': {'key': 'ipMask', 'type': 'str'},
        'action': {'key': 'action', 'type': 'str'},
    }

    action = "Allow"

    def __init__(
        self,
        **kwargs
    ):
        super(NWRuleSetIpRules, self).__init__(**kwargs)
        self.ip_mask = kwargs.get('ip_mask', None)


class NWRuleSetVirtualNetworkRules(msrest.serialization.Model):
    """The response from the List namespace operation.

    :param subnet: Subnet properties.
    :type subnet: ~azure.mgmt.eventhub.v2018_01_01_preview.models.Subnet
    :param ignore_missing_vnet_service_endpoint: Value that indicates whether to ignore missing
     Vnet Service Endpoint.
    :type ignore_missing_vnet_service_endpoint: bool
    """

    _attribute_map = {
        'subnet': {'key': 'subnet', 'type': 'Subnet'},
        'ignore_missing_vnet_service_endpoint': {'key': 'ignoreMissingVnetServiceEndpoint', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(NWRuleSetVirtualNetworkRules, self).__init__(**kwargs)
        self.subnet = kwargs.get('subnet', None)
        self.ignore_missing_vnet_service_endpoint = kwargs.get('ignore_missing_vnet_service_endpoint', None)


class Operation(msrest.serialization.Model):
    """A Event Hub REST API operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.eventhub.v2018_01_01_preview.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = kwargs.get('display', None)


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: Service provider: Microsoft.EventHub.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed: Invoice, etc.
    :vartype resource: str
    :ivar operation: Operation type: Read, write, delete, etc.
    :vartype operation: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Event Hub operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Event Hub operations supported by the Microsoft.EventHub resource
     provider.
    :vartype value: list[~azure.mgmt.eventhub.v2018_01_01_preview.models.Operation]
    :ivar next_link: URL to get the next set of operation list results if there are any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class Sku(msrest.serialization.Model):
    """SKU parameters supplied to the create namespace operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of this SKU. Possible values include: 'Dedicated', 'Basic',
     'Standard'.
    :type name: str or ~azure.mgmt.eventhub.v2018_01_01_preview.models.SkuName
    :param tier: The billing tier of this particular SKU. Possible values include: 'Basic',
     'Standard'.
    :type tier: str or ~azure.mgmt.eventhub.v2018_01_01_preview.models.SkuTier
    :param capacity: The Event Hubs throughput units, value should be 0 to 20 throughput units.
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
        'capacity': {'maximum': 20, 'minimum': 0},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)
        self.capacity = kwargs.get('capacity', None)


class Subnet(msrest.serialization.Model):
    """Properties supplied for Subnet.

    :param id: Resource ID of Virtual Network Subnet.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Subnet, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class VirtualNetworkRule(Resource):
    """Single item in a List or Get VirtualNetworkRules operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param virtual_network_subnet_id: ARM ID of Virtual Network Subnet.
    :type virtual_network_subnet_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'virtual_network_subnet_id': {'key': 'properties.virtualNetworkSubnetId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(VirtualNetworkRule, self).__init__(**kwargs)
        self.virtual_network_subnet_id = kwargs.get('virtual_network_subnet_id', None)


class VirtualNetworkRuleListResult(msrest.serialization.Model):
    """The response from the List namespace operation.

    :param value: Result of the List VirtualNetwork Rules operation.
    :type value: list[~azure.mgmt.eventhub.v2018_01_01_preview.models.VirtualNetworkRule]
    :param next_link: Link to the next set of results. Not empty if Value contains an incomplete
     list of VirtualNetwork Rules.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[VirtualNetworkRule]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(VirtualNetworkRuleListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)
