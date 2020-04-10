# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ActionGroupList
    from ._models_py3 import ActionGroupPatchBody
    from ._models_py3 import ActionGroupResource
    from ._models_py3 import ArmRoleReceiver
    from ._models_py3 import AutomationRunbookReceiver
    from ._models_py3 import AzureAppPushReceiver
    from ._models_py3 import AzureFunctionReceiver
    from ._models_py3 import EmailReceiver
    from ._models_py3 import EnableRequest
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ItsmReceiver
    from ._models_py3 import LogicAppReceiver
    from ._models_py3 import Resource
    from ._models_py3 import SmsReceiver
    from ._models_py3 import VoiceReceiver
    from ._models_py3 import WebhookReceiver
except (SyntaxError, ImportError):
    from ._models import ActionGroupList  # type: ignore
    from ._models import ActionGroupPatchBody  # type: ignore
    from ._models import ActionGroupResource  # type: ignore
    from ._models import ArmRoleReceiver  # type: ignore
    from ._models import AutomationRunbookReceiver  # type: ignore
    from ._models import AzureAppPushReceiver  # type: ignore
    from ._models import AzureFunctionReceiver  # type: ignore
    from ._models import EmailReceiver  # type: ignore
    from ._models import EnableRequest  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ItsmReceiver  # type: ignore
    from ._models import LogicAppReceiver  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import SmsReceiver  # type: ignore
    from ._models import VoiceReceiver  # type: ignore
    from ._models import WebhookReceiver  # type: ignore

from ._monitor_management_client_enums import (
    ReceiverStatus,
)

__all__ = [
    'ActionGroupList',
    'ActionGroupPatchBody',
    'ActionGroupResource',
    'ArmRoleReceiver',
    'AutomationRunbookReceiver',
    'AzureAppPushReceiver',
    'AzureFunctionReceiver',
    'EmailReceiver',
    'EnableRequest',
    'ErrorResponse',
    'ItsmReceiver',
    'LogicAppReceiver',
    'Resource',
    'SmsReceiver',
    'VoiceReceiver',
    'WebhookReceiver',
    'ReceiverStatus',
]
