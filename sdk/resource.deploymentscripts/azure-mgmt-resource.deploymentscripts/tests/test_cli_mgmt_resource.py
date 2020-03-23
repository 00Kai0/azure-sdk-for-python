# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 8
# Methods Covered : 8
# Examples Total  : 10
# Examples Tested : 10
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.resource.deploymentscripts
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtDeploymentScriptsClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtDeploymentScriptsClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.resource.deploymentscripts.DeploymentScriptsClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_resource(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # DeploymentScriptsCreate[put]
        BODY = {
          "kind": "AzurePowerShell",
          "location": "westus",
          "identity": {
            "type": "UserAssigned",
            "user_assigned_identities": {}
          },
          "properties": {
            "az_power_shell_version": "1.7.0",
            "script_content": "Param([string]$Location,[string]$Name) $deploymentScriptOutputs['test'] = 'value' Get-AzResourceGroup -Location $Location -Name $Name",
            "arguments": "-Location 'westus' -Name \"*rg2\"",
            "supporting_script_uris": [
              "https://uri1.to.supporting.script",
              "https://uri2.to.supporting.script"
            ],
            "retention_interval": "PT7D",
            "timeout": "PT1H",
            "cleanup_preference": "Always"
          }
        }
        result = self.mgmt_client.deployment_scripts.create(resource_group.name, DEPLOYMENT_SCRIPT_NAME, BODY)
        result = result.result()

        # DeploymentScriptsCreate_MinCreate[put]
        BODY = {
          "kind": "AzurePowerShell",
          "location": "westus",
          "identity": {
            "type": "UserAssigned",
            "user_assigned_identities": {}
          },
          "properties": {
            "az_power_shell_version": "1.7.0",
            "script_content": "Param([string]$Location,[string]$Name) $deploymentScriptOutputs['test'] = 'value' Get-AzResourceGroup -Location $Location -Name $Name",
            "arguments": "-Location 'westus' -Name \"*rg2\"",
            "retention_interval": "P7D"
          }
        }
        result = self.mgmt_client.deployment_scripts.create(resource_group.name, DEPLOYMENT_SCRIPT_NAME, BODY)
        result = result.result()

        # DeploymentScriptsGetLogsWithTail[get]
        result = self.mgmt_client.deployment_scripts.get_logs_default(resource_group.name, DEPLOYMENT_SCRIPT_NAME, LOG_NAME)

        # DeploymentScriptsGetLogs[get]
        result = self.mgmt_client.deployment_scripts.get_logs_default(resource_group.name, DEPLOYMENT_SCRIPT_NAME, LOG_NAME)

        # DeploymentScriptsGetLogs[get]
        result = self.mgmt_client.deployment_scripts.get_logs_default(resource_group.name, DEPLOYMENT_SCRIPT_NAME, LOG_NAME)

        # DeploymentScriptsGet[get]
        result = self.mgmt_client.deployment_scripts.get(resource_group.name, DEPLOYMENT_SCRIPT_NAME)

        # DeploymentScriptsList[get]
        result = self.mgmt_client.deployment_scripts.list_by_resource_group(resource_group.name)

        # DeploymentScriptsListBySubscription[get]
        result = self.mgmt_client.deployment_scripts.list_by_subscription()

        # DeploymentScriptsUpdate[patch]
        BODY = {}
        result = self.mgmt_client.deployment_scripts.update(resource_group.name, DEPLOYMENT_SCRIPT_NAME, BODY)

        # DeploymentScriptsDelete[delete]
        result = self.mgmt_client.deployment_scripts.delete(resource_group.name, DEPLOYMENT_SCRIPT_NAME)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
