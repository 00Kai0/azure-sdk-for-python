# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 17
# Methods Covered : 6
# Examples Total  : 6
# Examples Tested : 6
# Coverage %      : 35.294117647058826
# ----------------------

import unittest

import azure.mgmt.resource.managedapplications
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtApplicationClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtApplicationClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.resource.managedapplications.ApplicationClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_resource(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Create or update managed application[put]
        BODY = {
          "properties": {
            "managed_application_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Solutions/applicationDefinitions/" + APPLICATION_DEFINITION_NAME + "",
            "managed_resource_group_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + ""
          },
          "name": "myManagedApplication",
          "location": "East US 2",
          "kind": "ServiceCatalog"
        }
        result = self.mgmt_client.applications.create_or_update(resource_group.name, APPLICATION_NAME, BODY)
        result = result.result()

        # Create or update managed application definition[put]
        BODY = {
          "properties": {
            "lock_level": "None",
            "display_name": "myManagedApplicationDef",
            "description": "myManagedApplicationDef description",
            "authorizations": [
              {
                "principal_id": "validprincipalguid",
                "role_definition_id": "validroleguid"
              }
            ],
            "package_file_uri": "https://path/to/packagezipfile"
          },
          "location": "East US 2"
        }
        result = self.mgmt_client.application_definitions.create_or_update(resource_group.name, APPLICATION_DEFINITION_NAME, BODY)
        result = result.result()

        # Get managed application definition[get]
        result = self.mgmt_client.application_definitions.get(resource_group.name, APPLICATION_DEFINITION_NAME)

        # Get a managed application[get]
        result = self.mgmt_client.applications.get(resource_group.name, APPLICATION_NAME)

        # List managed application definitions[get]
        result = self.mgmt_client.application_definitions.list_by_resource_group(resource_group.name)

        # Lists applications[get]
        result = self.mgmt_client.applications.list_by_resource_group(resource_group.name)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
