# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
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


class AddRemove(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enum indicating if user is adding or removing a favorite lab
    """

    ADD = "Add"  #: Indicates that a user is adding a favorite lab.
    REMOVE = "Remove"  #: Indicates that a user is removing a favorite lab.

class ConfigurationState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the user's progress in configuring their environment setting
    """

    NOT_APPLICABLE = "NotApplicable"  #: User either hasn't started configuring their template
or they haven't started the configuration process.
    COMPLETED = "Completed"  #: User is finished modifying the template.

class LabUserAccessMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Lab user access mode (open to all vs. restricted to those listed on the lab).
    """

    RESTRICTED = "Restricted"  #: Only users registered with the lab can access VMs.
    OPEN = "Open"  #: Any user can register with the lab and access its VMs.

class ManagedLabVmSize(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The size category
    """

    BASIC = "Basic"  #: The base VM size.
    STANDARD = "Standard"  #: The standard or default VM size.
    PERFORMANCE = "Performance"  #: The most performant VM size.

class PublishingState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the readiness of this environment setting
    """

    DRAFT = "Draft"  #: Initial state of an environment setting.
    PUBLISHING = "Publishing"  #: Currently provisioning resources.
    PUBLISHED = "Published"  #: All resources are currently provisioned.
    PUBLISH_FAILED = "PublishFailed"  #: Failed to provision all the necessary resources.
    SCALING = "Scaling"  #: Currently provisioning resources without recreating VM image.
