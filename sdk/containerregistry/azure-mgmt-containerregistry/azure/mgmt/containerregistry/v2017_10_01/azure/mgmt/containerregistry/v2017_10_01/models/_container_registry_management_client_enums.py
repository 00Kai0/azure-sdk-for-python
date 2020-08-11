# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6272, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Action(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The action of virtual network rule.
    """

    ALLOW = "Allow"

class DefaultAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The default action of allow or deny when no other rules match.
    """

    ALLOW = "Allow"
    DENY = "Deny"

class ImportMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """When Force, any existing target tags will be overwritten. When NoForce, any existing target
    tags will fail the operation before any copying begins.
    """

    NO_FORCE = "NoForce"
    FORCE = "Force"

class PasswordName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The password name.
    """

    PASSWORD = "password"
    PASSWORD2 = "password2"

class PolicyStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The value that indicates whether the policy is enabled or not.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the container registry at the time the operation was called.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class RegistryUsageUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of measurement.
    """

    COUNT = "Count"
    BYTES = "Bytes"

class SkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The SKU name of the container registry. Required for registry creation.
    """

    CLASSIC = "Classic"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class SkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The SKU tier based on the SKU name.
    """

    CLASSIC = "Classic"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class TrustPolicyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of trust policy.
    """

    NOTARY = "Notary"

class WebhookAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PUSH = "push"
    DELETE = "delete"
    QUARANTINE = "quarantine"
    CHART_PUSH = "chart_push"
    CHART_DELETE = "chart_delete"

class WebhookStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the webhook at the time the operation was called.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"
