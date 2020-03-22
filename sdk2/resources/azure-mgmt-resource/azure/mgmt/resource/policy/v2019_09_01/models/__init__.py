# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CloudError
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import Identity
    from ._models_py3 import ParameterDefinitionsValue
    from ._models_py3 import ParameterDefinitionsValueMetadata
    from ._models_py3 import ParameterValuesValue
    from ._models_py3 import PolicyAssignment
    from ._models_py3 import PolicyAssignmentListResult
    from ._models_py3 import PolicyDefinition
    from ._models_py3 import PolicyDefinitionGroup
    from ._models_py3 import PolicyDefinitionListResult
    from ._models_py3 import PolicyDefinitionReference
    from ._models_py3 import PolicySetDefinition
    from ._models_py3 import PolicySetDefinitionListResult
    from ._models_py3 import PolicySku
except (SyntaxError, ImportError):
    from ._models import CloudError  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import ParameterDefinitionsValue  # type: ignore
    from ._models import ParameterDefinitionsValueMetadata  # type: ignore
    from ._models import ParameterValuesValue  # type: ignore
    from ._models import PolicyAssignment  # type: ignore
    from ._models import PolicyAssignmentListResult  # type: ignore
    from ._models import PolicyDefinition  # type: ignore
    from ._models import PolicyDefinitionGroup  # type: ignore
    from ._models import PolicyDefinitionListResult  # type: ignore
    from ._models import PolicyDefinitionReference  # type: ignore
    from ._models import PolicySetDefinition  # type: ignore
    from ._models import PolicySetDefinitionListResult  # type: ignore
    from ._models import PolicySku  # type: ignore

from ._policy_client_enums import (
    EnforcementMode,
    ParameterType,
    PolicyType,
    ResourceIdentityType,
)

__all__ = [
    'CloudError',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'Identity',
    'ParameterDefinitionsValue',
    'ParameterDefinitionsValueMetadata',
    'ParameterValuesValue',
    'PolicyAssignment',
    'PolicyAssignmentListResult',
    'PolicyDefinition',
    'PolicyDefinitionGroup',
    'PolicyDefinitionListResult',
    'PolicyDefinitionReference',
    'PolicySetDefinition',
    'PolicySetDefinitionListResult',
    'PolicySku',
    'EnforcementMode',
    'ParameterType',
    'PolicyType',
    'ResourceIdentityType',
]
