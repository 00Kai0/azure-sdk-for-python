# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import PolicyClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class PolicyClient(MultiApiClientMixin, _SDKClient):
    """To manage and control access to your resources, you can define customized policies and assign them at a scope.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2020-09-01'
    _PROFILE_TAG = "azure.mgmt.resource.PolicyClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "AsyncTokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = PolicyClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(PolicyClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-10-01-preview: :mod:`v2015_10_01_preview.models<azure.mgmt.resource.v2015_10_01_preview.models>`
           * 2016-04-01: :mod:`v2016_04_01.models<azure.mgmt.resource.v2016_04_01.models>`
           * 2016-12-01: :mod:`v2016_12_01.models<azure.mgmt.resource.v2016_12_01.models>`
           * 2017-06-01-preview: :mod:`v2017_06_01_preview.models<azure.mgmt.resource.v2017_06_01_preview.models>`
           * 2018-03-01: :mod:`v2018_03_01.models<azure.mgmt.resource.v2018_03_01.models>`
           * 2018-05-01: :mod:`v2018_05_01.models<azure.mgmt.resource.v2018_05_01.models>`
           * 2019-01-01: :mod:`v2019_01_01.models<azure.mgmt.resource.v2019_01_01.models>`
           * 2019-06-01: :mod:`v2019_06_01.models<azure.mgmt.resource.v2019_06_01.models>`
           * 2019-09-01: :mod:`v2019_09_01.models<azure.mgmt.resource.v2019_09_01.models>`
           * 2020-09-01: :mod:`v2020_09_01.models<azure.mgmt.resource.v2020_09_01.models>`
        """
        if api_version == '2015-10-01-preview':
            from ..v2015_10_01_preview import models
            return models
        elif api_version == '2016-04-01':
            from ..v2016_04_01 import models
            return models
        elif api_version == '2016-12-01':
            from ..v2016_12_01 import models
            return models
        elif api_version == '2017-06-01-preview':
            from ..v2017_06_01_preview import models
            return models
        elif api_version == '2018-03-01':
            from ..v2018_03_01 import models
            return models
        elif api_version == '2018-05-01':
            from ..v2018_05_01 import models
            return models
        elif api_version == '2019-01-01':
            from ..v2019_01_01 import models
            return models
        elif api_version == '2019-06-01':
            from ..v2019_06_01 import models
            return models
        elif api_version == '2019-09-01':
            from ..v2019_09_01 import models
            return models
        elif api_version == '2020-09-01':
            from ..v2020_09_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def data_policy_manifests(self):
        """Instance depends on the API version:

           * 2020-09-01: :class:`DataPolicyManifestsOperations<azure.mgmt.resource.v2020_09_01.aio.operations.DataPolicyManifestsOperations>`
        """
        api_version = self._get_api_version('data_policy_manifests')
        if api_version == '2020-09-01':
            from ..v2020_09_01.aio.operations import DataPolicyManifestsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'data_policy_manifests'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_assignments(self):
        """Instance depends on the API version:

           * 2015-10-01-preview: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2015_10_01_preview.aio.operations.PolicyAssignmentsOperations>`
           * 2016-04-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2016_04_01.aio.operations.PolicyAssignmentsOperations>`
           * 2016-12-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2016_12_01.aio.operations.PolicyAssignmentsOperations>`
           * 2017-06-01-preview: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2017_06_01_preview.aio.operations.PolicyAssignmentsOperations>`
           * 2018-03-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2018_03_01.aio.operations.PolicyAssignmentsOperations>`
           * 2018-05-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2018_05_01.aio.operations.PolicyAssignmentsOperations>`
           * 2019-01-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2019_01_01.aio.operations.PolicyAssignmentsOperations>`
           * 2019-06-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2019_06_01.aio.operations.PolicyAssignmentsOperations>`
           * 2019-09-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2019_09_01.aio.operations.PolicyAssignmentsOperations>`
           * 2020-09-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.v2020_09_01.aio.operations.PolicyAssignmentsOperations>`
        """
        api_version = self._get_api_version('policy_assignments')
        if api_version == '2015-10-01-preview':
            from ..v2015_10_01_preview.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2016-04-01':
            from ..v2016_04_01.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2016-12-01':
            from ..v2016_12_01.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2017-06-01-preview':
            from ..v2017_06_01_preview.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2018-03-01':
            from ..v2018_03_01.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2018-05-01':
            from ..v2018_05_01.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-01-01':
            from ..v2019_01_01.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2020-09-01':
            from ..v2020_09_01.aio.operations import PolicyAssignmentsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'policy_assignments'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_definitions(self):
        """Instance depends on the API version:

           * 2015-10-01-preview: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2015_10_01_preview.aio.operations.PolicyDefinitionsOperations>`
           * 2016-04-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2016_04_01.aio.operations.PolicyDefinitionsOperations>`
           * 2016-12-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2016_12_01.aio.operations.PolicyDefinitionsOperations>`
           * 2017-06-01-preview: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2017_06_01_preview.aio.operations.PolicyDefinitionsOperations>`
           * 2018-03-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2018_03_01.aio.operations.PolicyDefinitionsOperations>`
           * 2018-05-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2018_05_01.aio.operations.PolicyDefinitionsOperations>`
           * 2019-01-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2019_01_01.aio.operations.PolicyDefinitionsOperations>`
           * 2019-06-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2019_06_01.aio.operations.PolicyDefinitionsOperations>`
           * 2019-09-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2019_09_01.aio.operations.PolicyDefinitionsOperations>`
           * 2020-09-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.v2020_09_01.aio.operations.PolicyDefinitionsOperations>`
        """
        api_version = self._get_api_version('policy_definitions')
        if api_version == '2015-10-01-preview':
            from ..v2015_10_01_preview.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2016-04-01':
            from ..v2016_04_01.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2016-12-01':
            from ..v2016_12_01.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2017-06-01-preview':
            from ..v2017_06_01_preview.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2018-03-01':
            from ..v2018_03_01.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2018-05-01':
            from ..v2018_05_01.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-01-01':
            from ..v2019_01_01.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2020-09-01':
            from ..v2020_09_01.aio.operations import PolicyDefinitionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'policy_definitions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_exemptions(self):
        """Instance depends on the API version:

           * 2020-09-01: :class:`PolicyExemptionsOperations<azure.mgmt.resource.v2020_09_01.aio.operations.PolicyExemptionsOperations>`
        """
        api_version = self._get_api_version('policy_exemptions')
        if api_version == '2020-09-01':
            from ..v2020_09_01.aio.operations import PolicyExemptionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'policy_exemptions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_set_definitions(self):
        """Instance depends on the API version:

           * 2017-06-01-preview: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.v2017_06_01_preview.aio.operations.PolicySetDefinitionsOperations>`
           * 2018-03-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.v2018_03_01.aio.operations.PolicySetDefinitionsOperations>`
           * 2018-05-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.v2018_05_01.aio.operations.PolicySetDefinitionsOperations>`
           * 2019-01-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.v2019_01_01.aio.operations.PolicySetDefinitionsOperations>`
           * 2019-06-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.v2019_06_01.aio.operations.PolicySetDefinitionsOperations>`
           * 2019-09-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.v2019_09_01.aio.operations.PolicySetDefinitionsOperations>`
           * 2020-09-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.v2020_09_01.aio.operations.PolicySetDefinitionsOperations>`
        """
        api_version = self._get_api_version('policy_set_definitions')
        if api_version == '2017-06-01-preview':
            from ..v2017_06_01_preview.aio.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2018-03-01':
            from ..v2018_03_01.aio.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2018-05-01':
            from ..v2018_05_01.aio.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-01-01':
            from ..v2019_01_01.aio.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2020-09-01':
            from ..v2020_09_01.aio.operations import PolicySetDefinitionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'policy_set_definitions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
