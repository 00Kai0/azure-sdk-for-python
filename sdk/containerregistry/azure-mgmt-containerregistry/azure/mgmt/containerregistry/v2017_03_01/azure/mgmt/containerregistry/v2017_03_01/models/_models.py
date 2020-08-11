# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6272, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class OperationDefinition(msrest.serialization.Model):
    """The definition of a container registry operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The display information for the container registry operation.
    :type display: ~azure.mgmt.containerregistry.v2017_03_01.models.OperationDisplayDefinition
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplayDefinition'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDefinition, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationDisplayDefinition(msrest.serialization.Model):
    """The display information for a container registry operation.

    :param provider: The resource provider name: Microsoft.ContainerRegistry.
    :type provider: str
    :param resource: The resource on which the operation is performed.
    :type resource: str
    :param operation: The operation that users can perform.
    :type operation: str
    :param description: The description for the operation.
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
        super(OperationDisplayDefinition, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationListResult(msrest.serialization.Model):
    """The result of a request to list container registry operations.

    :param value: The list of container registry operations. Since this list may be incomplete, the
     nextLink field should be used to request the next list of operations.
    :type value: list[~azure.mgmt.containerregistry.v2017_03_01.models.OperationDefinition]
    :param next_link: The URI that can be used to request the next list of container registry
     operations.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class RegenerateCredentialParameters(msrest.serialization.Model):
    """The parameters used to regenerate the login credential.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Specifies name of the password which should be regenerated -- password
     or password2. Possible values include: "password", "password2".
    :type name: str or ~azure.mgmt.containerregistry.v2017_03_01.models.PasswordName
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RegenerateCredentialParameters, self).__init__(**kwargs)
        self.name = kwargs['name']


class Resource(msrest.serialization.Model):
    """An Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: Required. The location of the resource. This cannot be changed after the
     resource is created.
    :type location: str
    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
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
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs['location']
        self.tags = kwargs.get('tags', None)


class Registry(Resource):
    """An object that represents a container registry.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: Required. The location of the resource. This cannot be changed after the
     resource is created.
    :type location: str
    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    :param sku: Required. The SKU of the container registry.
    :type sku: ~azure.mgmt.containerregistry.v2017_03_01.models.Sku
    :ivar login_server: The URL that can be used to log into the container registry.
    :vartype login_server: str
    :ivar creation_date: The creation date of the container registry in ISO8601 format.
    :vartype creation_date: ~datetime.datetime
    :ivar provisioning_state: The provisioning state of the container registry at the time the
     operation was called. Possible values include: "Creating", "Succeeded".
    :vartype provisioning_state: str or
     ~azure.mgmt.containerregistry.v2017_03_01.models.ProvisioningState
    :param admin_user_enabled: The value that indicates whether the admin user is enabled.
    :type admin_user_enabled: bool
    :param storage_account: The properties of the storage account for the container registry.
    :type storage_account:
     ~azure.mgmt.containerregistry.v2017_03_01.models.StorageAccountProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
        'login_server': {'readonly': True},
        'creation_date': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'login_server': {'key': 'properties.loginServer', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'admin_user_enabled': {'key': 'properties.adminUserEnabled', 'type': 'bool'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'StorageAccountProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Registry, self).__init__(**kwargs)
        self.sku = kwargs['sku']
        self.login_server = None
        self.creation_date = None
        self.provisioning_state = None
        self.admin_user_enabled = kwargs.get('admin_user_enabled', False)
        self.storage_account = kwargs.get('storage_account', None)


class RegistryCreateParameters(msrest.serialization.Model):
    """The parameters for creating a container registry.

    All required parameters must be populated in order to send to Azure.

    :param tags: A set of tags. The tags for the container registry.
    :type tags: dict[str, str]
    :param location: Required. The location of the container registry. This cannot be changed after
     the resource is created.
    :type location: str
    :param sku: Required. The SKU of the container registry.
    :type sku: ~azure.mgmt.containerregistry.v2017_03_01.models.Sku
    :param admin_user_enabled: The value that indicates whether the admin user is enabled.
    :type admin_user_enabled: bool
    :param storage_account: The parameters of a storage account for the container registry. If
     specified, the storage account must be in the same physical location as the container registry.
    :type storage_account:
     ~azure.mgmt.containerregistry.v2017_03_01.models.StorageAccountParameters
    """

    _validation = {
        'location': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'admin_user_enabled': {'key': 'properties.adminUserEnabled', 'type': 'bool'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'StorageAccountParameters'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RegistryCreateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs['location']
        self.sku = kwargs['sku']
        self.admin_user_enabled = kwargs.get('admin_user_enabled', False)
        self.storage_account = kwargs.get('storage_account', None)


class RegistryListCredentialsResult(msrest.serialization.Model):
    """The response from the ListCredentials operation.

    :param username: The username for a container registry.
    :type username: str
    :param passwords: The list of passwords for a container registry.
    :type passwords: list[~azure.mgmt.containerregistry.v2017_03_01.models.RegistryPassword]
    """

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'passwords': {'key': 'passwords', 'type': '[RegistryPassword]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RegistryListCredentialsResult, self).__init__(**kwargs)
        self.username = kwargs.get('username', None)
        self.passwords = kwargs.get('passwords', None)


class RegistryListResult(msrest.serialization.Model):
    """The result of a request to list container registries.

    :param value: The list of container registries. Since this list may be incomplete, the nextLink
     field should be used to request the next list of container registries.
    :type value: list[~azure.mgmt.containerregistry.v2017_03_01.models.Registry]
    :param next_link: The URI that can be used to request the next list of container registries.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Registry]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RegistryListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class RegistryNameCheckRequest(msrest.serialization.Model):
    """A request to check whether a container registry name is available.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the container registry.
    :type name: str
    :ivar type: Required. The resource type of the container registry. This field must be set to
     'Microsoft.ContainerRegistry/registries'. Default value:
     "Microsoft.ContainerRegistry/registries".
    :vartype type: str
    """

    _validation = {
        'name': {'required': True, 'max_length': 50, 'min_length': 5, 'pattern': r'^[a-zA-Z0-9]*$'},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.ContainerRegistry/registries"

    def __init__(
        self,
        **kwargs
    ):
        super(RegistryNameCheckRequest, self).__init__(**kwargs)
        self.name = kwargs['name']


class RegistryNameStatus(msrest.serialization.Model):
    """The result of a request to check the availability of a container registry name.

    :param name_available: The value that indicates whether the name is available.
    :type name_available: bool
    :param reason: If any, the reason that the name is not available.
    :type reason: str
    :param message: If any, the error message that provides more detail for the reason that the
     name is not available.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RegistryNameStatus, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)


class RegistryPassword(msrest.serialization.Model):
    """The login password for the container registry.

    :param name: The password name. Possible values include: "password", "password2".
    :type name: str or ~azure.mgmt.containerregistry.v2017_03_01.models.PasswordName
    :param value: The password value.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RegistryPassword, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)


class RegistryUpdateParameters(msrest.serialization.Model):
    """The parameters for updating a container registry.

    :param tags: A set of tags. The tags for the container registry.
    :type tags: dict[str, str]
    :param admin_user_enabled: The value that indicates whether the admin user is enabled.
    :type admin_user_enabled: bool
    :param storage_account: The parameters of a storage account for the container registry. If
     specified, the storage account must be in the same physical location as the container registry.
    :type storage_account:
     ~azure.mgmt.containerregistry.v2017_03_01.models.StorageAccountParameters
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'admin_user_enabled': {'key': 'properties.adminUserEnabled', 'type': 'bool'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'StorageAccountParameters'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RegistryUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.admin_user_enabled = kwargs.get('admin_user_enabled', None)
        self.storage_account = kwargs.get('storage_account', None)


class Sku(msrest.serialization.Model):
    """The SKU of a container registry.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The SKU name of the container registry. Required for registry creation.
     Allowed value: Basic.
    :type name: str
    :ivar tier: The SKU tier based on the SKU name. Possible values include: "Basic".
    :vartype tier: str or ~azure.mgmt.containerregistry.v2017_03_01.models.SkuTier
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.tier = None


class StorageAccountParameters(msrest.serialization.Model):
    """The parameters of a storage account for a container registry.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the storage account.
    :type name: str
    :param access_key: Required. The access key to the storage account.
    :type access_key: str
    """

    _validation = {
        'name': {'required': True},
        'access_key': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'access_key': {'key': 'accessKey', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountParameters, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.access_key = kwargs['access_key']


class StorageAccountProperties(msrest.serialization.Model):
    """The properties of a storage account for a container registry.

    :param name: The name of the storage account.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountProperties, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
