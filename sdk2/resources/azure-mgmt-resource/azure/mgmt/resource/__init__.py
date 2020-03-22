# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from .features.v2015_12_01 import FeatureClient
from .locks.v2016_09_01 import ManagementLockClient
from .policy.v2019_09_01 import PolicyClient
from .resources.v2019_10_01 import ResourceManagementClient
from .subscriptions.v2019_11_01 import SubscriptionClient
from .links.v2016_09_01 import ManagementLinkClient
from .managedapplications import ApplicationClient

from .version import VERSION

__version__ = VERSION
__all__ = [
    'FeatureClient',
    'ManagementLockClient',
    'PolicyClient',
    'ResourceManagementClient',
    'SubscriptionClient',
    'ManagementLinkClient',
    'ApplicationClient',
]
