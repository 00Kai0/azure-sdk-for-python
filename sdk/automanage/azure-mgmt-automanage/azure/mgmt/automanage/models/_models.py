# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
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
    """The resource model definition for an Azure Resource Manager tracked top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs['location']


class Account(TrackedResource):
    """Definition of the Automanage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param identity: The identity of the Automanage account.
    :type identity: ~automanage_client.models.AccountIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'AccountIdentity'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Account, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)


class AccountIdentity(msrest.serialization.Model):
    """Identity for the Automanage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal id of Automanage account identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant id associated with the Automanage account.
    :vartype tenant_id: str
    :param type: The type of identity used for the Automanage account. Currently, the only
     supported type is 'SystemAssigned', which implicitly creates an identity. Possible values
     include: "SystemAssigned", "None".
    :type type: str or ~automanage_client.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccountIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class AccountList(msrest.serialization.Model):
    """The response of the list Account operation.

    :param value: Result of the list Account operation.
    :type value: list[~automanage_client.models.Account]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Account]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccountList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class UpdateResource(msrest.serialization.Model):
    """Represents an update resource.

    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UpdateResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class AccountUpdate(UpdateResource):
    """Definition of the Automanage account.

    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    :param identity: The identity of the Automanage account.
    :type identity: ~automanage_client.models.AccountIdentity
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'AccountIdentity'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccountUpdate, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)


class ConfigurationProfileAssignment(Resource):
    """Configuration profile assignment is an association between a VM and automanage profile configuration.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param properties: Properties of the configuration profile assignment.
    :type properties: ~automanage_client.models.ConfigurationProfileAssignmentProperties
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
        'properties': {'key': 'properties', 'type': 'ConfigurationProfileAssignmentProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfileAssignment, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class ConfigurationProfileAssignmentCompliance(msrest.serialization.Model):
    """The compliance status for the configuration profile assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar update_status: The state of compliance, which only appears in the response. Possible
     values include: "Succeeded", "Failed", "Created".
    :vartype update_status: str or ~automanage_client.models.UpdateStatus
    """

    _validation = {
        'update_status': {'readonly': True},
    }

    _attribute_map = {
        'update_status': {'key': 'updateStatus', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfileAssignmentCompliance, self).__init__(**kwargs)
        self.update_status = None


class ConfigurationProfileAssignmentList(msrest.serialization.Model):
    """The response of the list configuration profile assignment operation.

    :param value: Result of the list configuration profile assignment operation.
    :type value: list[~automanage_client.models.ConfigurationProfileAssignment]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConfigurationProfileAssignment]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfileAssignmentList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ConfigurationProfileAssignmentProperties(msrest.serialization.Model):
    """Automanage configuration profile assignment properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param configuration_profile: A value indicating configuration profile. Possible values
     include: "Azure virtual machine best practices – Dev/Test", "Azure virtual machine best
     practices – Production".
    :type configuration_profile: str or ~automanage_client.models.ConfigurationProfile
    :param target_id: The target VM resource URI.
    :type target_id: str
    :param account_id: The Automanage account ARM Resource URI.
    :type account_id: str
    :param configuration_profile_preference_id: The configuration profile custom preferences ARM
     resource URI.
    :type configuration_profile_preference_id: str
    :ivar provisioning_state: The state of onboarding, which only appears in the response. Possible
     values include: "Succeeded", "Failed", "Created".
    :vartype provisioning_state: str or ~automanage_client.models.ProvisioningState
    :param compliance: The configuration setting for the configuration profile.
    :type compliance: ~automanage_client.models.ConfigurationProfileAssignmentCompliance
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'configuration_profile': {'key': 'configurationProfile', 'type': 'str'},
        'target_id': {'key': 'targetId', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
        'configuration_profile_preference_id': {'key': 'configurationProfilePreferenceId', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'compliance': {'key': 'compliance', 'type': 'ConfigurationProfileAssignmentCompliance'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfileAssignmentProperties, self).__init__(**kwargs)
        self.configuration_profile = kwargs.get('configuration_profile', None)
        self.target_id = kwargs.get('target_id', None)
        self.account_id = kwargs.get('account_id', None)
        self.configuration_profile_preference_id = kwargs.get('configuration_profile_preference_id', None)
        self.provisioning_state = None
        self.compliance = kwargs.get('compliance', None)


class ConfigurationProfilePreference(TrackedResource):
    """Definition of the configuration profile preference.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param properties: Properties of the configuration profile preference.
    :type properties: ~automanage_client.models.ConfigurationProfilePreferenceProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ConfigurationProfilePreferenceProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfilePreference, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class ConfigurationProfilePreferenceAntiMalware(msrest.serialization.Model):
    """Automanage configuration profile Antimalware preferences.

    :param enable_real_time_protection: Enables or disables Real Time Protection. Possible values
     include: "True", "False".
    :type enable_real_time_protection: str or ~automanage_client.models.EnableRealTimeProtection
    :param exclusions: Extensions, Paths and Processes that must be excluded from scan.
    :type exclusions: object
    :param run_scheduled_scan: Enables or disables a periodic scan for antimalware. Possible values
     include: "True", "False".
    :type run_scheduled_scan: str or ~automanage_client.models.RunScheduledScan
    :param scan_type: Type of scheduled scan. Possible values include: "Quick", "Full".
    :type scan_type: str or ~automanage_client.models.ScanType
    :param scan_day: Schedule scan settings day.
    :type scan_day: str
    :param scan_time_in_minutes: Schedule scan settings time.
    :type scan_time_in_minutes: str
    """

    _attribute_map = {
        'enable_real_time_protection': {'key': 'enableRealTimeProtection', 'type': 'str'},
        'exclusions': {'key': 'exclusions', 'type': 'object'},
        'run_scheduled_scan': {'key': 'runScheduledScan', 'type': 'str'},
        'scan_type': {'key': 'scanType', 'type': 'str'},
        'scan_day': {'key': 'scanDay', 'type': 'str'},
        'scan_time_in_minutes': {'key': 'scanTimeInMinutes', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceAntiMalware, self).__init__(**kwargs)
        self.enable_real_time_protection = kwargs.get('enable_real_time_protection', None)
        self.exclusions = kwargs.get('exclusions', None)
        self.run_scheduled_scan = kwargs.get('run_scheduled_scan', None)
        self.scan_type = kwargs.get('scan_type', None)
        self.scan_day = kwargs.get('scan_day', None)
        self.scan_time_in_minutes = kwargs.get('scan_time_in_minutes', None)


class ConfigurationProfilePreferenceList(msrest.serialization.Model):
    """The response of the list ConfigurationProfilePreference operation.

    :param value: Result of the list ConfigurationProfilePreference operation.
    :type value: list[~automanage_client.models.ConfigurationProfilePreference]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConfigurationProfilePreference]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ConfigurationProfilePreferenceProperties(msrest.serialization.Model):
    """Automanage configuration profile preference properties.

    :param vm_backup: The custom preferences for Azure VM Backup.
    :type vm_backup: ~automanage_client.models.ConfigurationProfilePreferenceVmBackup
    :param anti_malware: The custom preferences for Azure Antimalware.
    :type anti_malware: ~automanage_client.models.ConfigurationProfilePreferenceAntiMalware
    """

    _attribute_map = {
        'vm_backup': {'key': 'vmBackup', 'type': 'ConfigurationProfilePreferenceVmBackup'},
        'anti_malware': {'key': 'antiMalware', 'type': 'ConfigurationProfilePreferenceAntiMalware'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceProperties, self).__init__(**kwargs)
        self.vm_backup = kwargs.get('vm_backup', None)
        self.anti_malware = kwargs.get('anti_malware', None)


class ConfigurationProfilePreferenceUpdate(UpdateResource):
    """Definition of the configuration profile preference.

    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    :param properties: Properties of the configuration profile preference.
    :type properties: ~automanage_client.models.ConfigurationProfilePreferenceProperties
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'ConfigurationProfilePreferenceProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceUpdate, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class ConfigurationProfilePreferenceVmBackup(msrest.serialization.Model):
    """Automanage configuration profile VM Backup preferences.

    :param time_zone: TimeZone optional input as string. For example: Pacific Standard Time.
    :type time_zone: str
    :param instant_rp_retention_range_in_days: Instant RP retention policy range in days.
    :type instant_rp_retention_range_in_days: int
    :param retention_policy: Retention policy with the details on backup copy retention ranges.
    :type retention_policy: str
    :param schedule_policy: Backup schedule specified as part of backup policy.
    :type schedule_policy: str
    """

    _attribute_map = {
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'instant_rp_retention_range_in_days': {'key': 'instantRpRetentionRangeInDays', 'type': 'int'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'str'},
        'schedule_policy': {'key': 'schedulePolicy', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationProfilePreferenceVmBackup, self).__init__(**kwargs)
        self.time_zone = kwargs.get('time_zone', None)
        self.instant_rp_retention_range_in_days = kwargs.get('instant_rp_retention_range_in_days', None)
        self.retention_policy = kwargs.get('retention_policy', None)
        self.schedule_policy = kwargs.get('schedule_policy', None)


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~automanage_client.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~automanage_client.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :param error: The error object.
    :type error: ~automanage_client.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class Operation(msrest.serialization.Model):
    """Automanage REST API operation.

    :param name: Operation name: For ex.
     providers/Microsoft.Automanage/configurationProfileAssignments/write or read.
    :type name: str
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: str
    :param display: Provider, Resource, Operation and description values.
    :type display: ~automanage_client.models.OperationDisplay
    :param status_code: Service provider: Microsoft.Automanage.
    :type status_code: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'status_code': {'key': 'properties.statusCode', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_data_action = kwargs.get('is_data_action', None)
        self.display = kwargs.get('display', None)
        self.status_code = kwargs.get('status_code', None)


class OperationDisplay(msrest.serialization.Model):
    """Provider, Resource, Operation and description values.

    :param provider: Service provider: Microsoft.Automanage.
    :type provider: str
    :param resource: Resource on which the operation is performed:  For ex.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param description: Description about operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationList(msrest.serialization.Model):
    """The response model for the list of Automanage operations.

    :param value: List of Automanage operations supported by the Automanage resource provider.
    :type value: list[~automanage_client.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ProxyResource(Resource):
    """The resource model definition for an Azure Resource Manager proxy resource. It will have everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
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
        super(ProxyResource, self).__init__(**kwargs)
