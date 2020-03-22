# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class CloudError(msrest.serialization.Model):
    """An error response from a policy operation.

    :param error: The resource management error response.
    :type error: ~azure.mgmt.resource.policy.v2019_09_01.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CloudError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


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


class ErrorResponse(msrest.serialization.Model):
    """The resource management error response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.resource.policy.v2019_09_01.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.resource.policy.v2019_09_01.models.ErrorAdditionalInfo]
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
        'details': {'key': 'details', 'type': '[ErrorResponse]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class Identity(msrest.serialization.Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of the resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the resource identity.
    :vartype tenant_id: str
    :param type: The identity type. This is the only required field when adding a system assigned
     identity to a resource. Possible values include: 'SystemAssigned', 'None'.
    :type type: str or ~azure.mgmt.resource.policy.v2019_09_01.models.ResourceIdentityType
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
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class ParameterDefinitionsValue(msrest.serialization.Model):
    """The definition of a parameter that can be provided to the policy.

    :param type: The data type of the parameter. Possible values include: 'String', 'Array',
     'Object', 'Boolean', 'Integer', 'Float', 'DateTime'.
    :type type: str or ~azure.mgmt.resource.policy.v2019_09_01.models.ParameterType
    :param allowed_values: The allowed values for the parameter.
    :type allowed_values: list[object]
    :param default_value: The default value for the parameter if no value is provided.
    :type default_value: object
    :param metadata: General metadata for the parameter.
    :type metadata:
     ~azure.mgmt.resource.policy.v2019_09_01.models.ParameterDefinitionsValueMetadata
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'allowed_values': {'key': 'allowedValues', 'type': '[object]'},
        'default_value': {'key': 'defaultValue', 'type': 'object'},
        'metadata': {'key': 'metadata', 'type': 'ParameterDefinitionsValueMetadata'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ParameterDefinitionsValue, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.allowed_values = kwargs.get('allowed_values', None)
        self.default_value = kwargs.get('default_value', None)
        self.metadata = kwargs.get('metadata', None)


class ParameterDefinitionsValueMetadata(msrest.serialization.Model):
    """General metadata for the parameter.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param display_name: The display name for the parameter.
    :type display_name: str
    :param description: The description of the parameter.
    :type description: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ParameterDefinitionsValueMetadata, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)


class ParameterValuesValue(msrest.serialization.Model):
    """The value of a parameter.

    :param value: The value of the parameter.
    :type value: object
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ParameterValuesValue, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class PolicyAssignment(msrest.serialization.Model):
    """The policy assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy assignment.
    :vartype id: str
    :ivar type: The type of the policy assignment.
    :vartype type: str
    :ivar name: The name of the policy assignment.
    :vartype name: str
    :param sku: The policy sku. This property is optional, obsolete, and will be ignored.
    :type sku: ~azure.mgmt.resource.policy.v2019_09_01.models.PolicySku
    :param location: The location of the policy assignment. Only required when utilizing managed
     identity.
    :type location: str
    :param identity: The managed identity associated with the policy assignment.
    :type identity: ~azure.mgmt.resource.policy.v2019_09_01.models.Identity
    :param display_name: The display name of the policy assignment.
    :type display_name: str
    :param policy_definition_id: The ID of the policy definition or policy set definition being
     assigned.
    :type policy_definition_id: str
    :param scope: The scope for the policy assignment.
    :type scope: str
    :param not_scopes: The policy's excluded scopes.
    :type not_scopes: list[str]
    :param parameters: The parameter values for the assigned policy rule. The keys are the
     parameter names.
    :type parameters: dict[str,
     ~azure.mgmt.resource.policy.v2019_09_01.models.ParameterValuesValue]
    :param description: This message will be part of response in case of policy violation.
    :type description: str
    :param metadata: The policy assignment metadata. Metadata is an open ended object and is
     typically a collection of key value pairs.
    :type metadata: object
    :param enforcement_mode: The policy assignment enforcement mode. Possible values are Default
     and DoNotEnforce. Possible values include: 'Default', 'DoNotEnforce'.
    :type enforcement_mode: str or ~azure.mgmt.resource.policy.v2019_09_01.models.EnforcementMode
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'PolicySku'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'not_scopes': {'key': 'properties.notScopes', 'type': '[str]'},
        'parameters': {'key': 'properties.parameters', 'type': '{ParameterValuesValue}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'enforcement_mode': {'key': 'properties.enforcementMode', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicyAssignment, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.sku = kwargs.get('sku', None)
        self.location = kwargs.get('location', None)
        self.identity = kwargs.get('identity', None)
        self.display_name = kwargs.get('display_name', None)
        self.policy_definition_id = kwargs.get('policy_definition_id', None)
        self.scope = kwargs.get('scope', None)
        self.not_scopes = kwargs.get('not_scopes', None)
        self.parameters = kwargs.get('parameters', None)
        self.description = kwargs.get('description', None)
        self.metadata = kwargs.get('metadata', None)
        self.enforcement_mode = kwargs.get('enforcement_mode', None)


class PolicyAssignmentListResult(msrest.serialization.Model):
    """List of policy assignments.

    :param value: An array of policy assignments.
    :type value: list[~azure.mgmt.resource.policy.v2019_09_01.models.PolicyAssignment]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicyAssignmentListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class PolicyDefinition(msrest.serialization.Model):
    """The policy definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy definition.
    :vartype id: str
    :ivar name: The name of the policy definition.
    :vartype name: str
    :ivar type: The type of the resource (Microsoft.Authorization/policyDefinitions).
    :vartype type: str
    :param policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
     Custom, and Static. Possible values include: 'NotSpecified', 'BuiltIn', 'Custom', 'Static'.
    :type policy_type: str or ~azure.mgmt.resource.policy.v2019_09_01.models.PolicyType
    :param mode: The policy definition mode. Some examples are All, Indexed,
     Microsoft.KeyVault.Data.
    :type mode: str
    :param display_name: The display name of the policy definition.
    :type display_name: str
    :param description: The policy definition description.
    :type description: str
    :param policy_rule: The policy rule.
    :type policy_rule: object
    :param metadata: The policy definition metadata.  Metadata is an open ended object and is
     typically a collection of key value pairs.
    :type metadata: object
    :param parameters: The parameter definitions for parameters used in the policy rule. The keys
     are the parameter names.
    :type parameters: dict[str,
     ~azure.mgmt.resource.policy.v2019_09_01.models.ParameterDefinitionsValue]
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
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'policy_rule': {'key': 'properties.policyRule', 'type': 'object'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': '{ParameterDefinitionsValue}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicyDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.policy_type = kwargs.get('policy_type', None)
        self.mode = kwargs.get('mode', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.policy_rule = kwargs.get('policy_rule', None)
        self.metadata = kwargs.get('metadata', None)
        self.parameters = kwargs.get('parameters', None)


class PolicyDefinitionGroup(msrest.serialization.Model):
    """The policy definition group.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the group.
    :type name: str
    :param display_name: The group's display name.
    :type display_name: str
    :param category: The group's category.
    :type category: str
    :param description: The group's description.
    :type description: str
    :param additional_metadata_id: A resource ID of a resource that contains additional metadata
     about the group.
    :type additional_metadata_id: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'additional_metadata_id': {'key': 'additionalMetadataId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicyDefinitionGroup, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.category = kwargs.get('category', None)
        self.description = kwargs.get('description', None)
        self.additional_metadata_id = kwargs.get('additional_metadata_id', None)


class PolicyDefinitionListResult(msrest.serialization.Model):
    """List of policy definitions.

    :param value: An array of policy definitions.
    :type value: list[~azure.mgmt.resource.policy.v2019_09_01.models.PolicyDefinition]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicyDefinitionListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class PolicyDefinitionReference(msrest.serialization.Model):
    """The policy definition reference.

    All required parameters must be populated in order to send to Azure.

    :param policy_definition_id: Required. The ID of the policy definition or policy set
     definition.
    :type policy_definition_id: str
    :param parameters: The parameter values for the referenced policy rule. The keys are the
     parameter names.
    :type parameters: dict[str,
     ~azure.mgmt.resource.policy.v2019_09_01.models.ParameterValuesValue]
    :param policy_definition_reference_id: A unique id (within the policy set definition) for this
     policy definition reference.
    :type policy_definition_reference_id: str
    :param group_names: The name of the groups that this policy definition reference belongs to.
    :type group_names: list[str]
    """

    _validation = {
        'policy_definition_id': {'required': True},
    }

    _attribute_map = {
        'policy_definition_id': {'key': 'policyDefinitionId', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterValuesValue}'},
        'policy_definition_reference_id': {'key': 'policyDefinitionReferenceId', 'type': 'str'},
        'group_names': {'key': 'groupNames', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicyDefinitionReference, self).__init__(**kwargs)
        self.policy_definition_id = kwargs.get('policy_definition_id', None)
        self.parameters = kwargs.get('parameters', None)
        self.policy_definition_reference_id = kwargs.get('policy_definition_reference_id', None)
        self.group_names = kwargs.get('group_names', None)


class PolicySetDefinition(msrest.serialization.Model):
    """The policy set definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy set definition.
    :vartype id: str
    :ivar name: The name of the policy set definition.
    :vartype name: str
    :ivar type: The type of the resource (Microsoft.Authorization/policySetDefinitions).
    :vartype type: str
    :param policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
     Custom, and Static. Possible values include: 'NotSpecified', 'BuiltIn', 'Custom', 'Static'.
    :type policy_type: str or ~azure.mgmt.resource.policy.v2019_09_01.models.PolicyType
    :param display_name: The display name of the policy set definition.
    :type display_name: str
    :param description: The policy set definition description.
    :type description: str
    :param metadata: The policy set definition metadata.  Metadata is an open ended object and is
     typically a collection of key value pairs.
    :type metadata: object
    :param parameters: The policy set definition parameters that can be used in policy definition
     references.
    :type parameters: dict[str,
     ~azure.mgmt.resource.policy.v2019_09_01.models.ParameterDefinitionsValue]
    :param policy_definitions: An array of policy definition references.
    :type policy_definitions:
     list[~azure.mgmt.resource.policy.v2019_09_01.models.PolicyDefinitionReference]
    :param policy_definition_groups: The metadata describing groups of policy definition references
     within the policy set definition.
    :type policy_definition_groups:
     list[~azure.mgmt.resource.policy.v2019_09_01.models.PolicyDefinitionGroup]
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
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': '{ParameterDefinitionsValue}'},
        'policy_definitions': {'key': 'properties.policyDefinitions', 'type': '[PolicyDefinitionReference]'},
        'policy_definition_groups': {'key': 'properties.policyDefinitionGroups', 'type': '[PolicyDefinitionGroup]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicySetDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.policy_type = kwargs.get('policy_type', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.metadata = kwargs.get('metadata', None)
        self.parameters = kwargs.get('parameters', None)
        self.policy_definitions = kwargs.get('policy_definitions', None)
        self.policy_definition_groups = kwargs.get('policy_definition_groups', None)


class PolicySetDefinitionListResult(msrest.serialization.Model):
    """List of policy set definitions.

    :param value: An array of policy set definitions.
    :type value: list[~azure.mgmt.resource.policy.v2019_09_01.models.PolicySetDefinition]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicySetDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicySetDefinitionListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class PolicySku(msrest.serialization.Model):
    """The policy sku. This property is optional, obsolete, and will be ignored.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the policy sku. Possible values are A0 and A1.
    :type name: str
    :param tier: The policy sku tier. Possible values are Free and Standard.
    :type tier: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PolicySku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)
