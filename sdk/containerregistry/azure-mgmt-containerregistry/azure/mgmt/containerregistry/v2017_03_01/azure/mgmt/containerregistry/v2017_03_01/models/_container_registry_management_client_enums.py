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


class PasswordName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The password name.
    """

    PASSWORD = "password"
    PASSWORD2 = "password2"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the container registry at the time the operation was called.
    """

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"

class SkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The SKU tier based on the SKU name.
    """

    BASIC = "Basic"
