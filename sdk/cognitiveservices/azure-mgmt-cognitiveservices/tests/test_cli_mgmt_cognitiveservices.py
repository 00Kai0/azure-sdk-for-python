# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 14
# Methods Covered : 14
# Examples Total  : 14
# Examples Tested : 14
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.cognitiveservices
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtCognitiveServicesTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtCognitiveServicesTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.cognitiveservices.CognitiveServicesManagementClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_cognitiveservices(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Create Account[put]
        BODY = {
          "location": "West US",
          "kind": "Emotion",
          "sku": {
            "name": "S0"
          },
          "properties": {
            "encryption": {
              "key_vault_properties": {
                "key_name": "KeyName",
                "key_version": "891CF236-D241-4738-9462-D506AF493DFA",
                "key_vault_uri": "https://pltfrmscrts-use-pc-dev.vault.azure.net/"
              },
              "key_source": "Microsoft.KeyVault"
            },
            "user_owned_storage": [
              {
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
              }
            ]
          },
          "identity": {
            "type": "SystemAssigned"
          }
        }
        result = self.mgmt_client.accounts.create(resource_group.name, ACCOUNT_NAME, BODY)

        # Get Usages[get]
        result = self.mgmt_client.accounts.get_usages(resource_group.name, ACCOUNT_NAME)

        # List SKUs[get]
        result = self.mgmt_client.accounts.list_skus(resource_group.name, ACCOUNT_NAME)

        # Get Account[get]
        result = self.mgmt_client.accounts.get_properties(resource_group.name, ACCOUNT_NAME)

        # List Accounts by Resource Group[get]
        result = self.mgmt_client.accounts.list_by_resource_group(resource_group.name)

        # List Accounts by Subscription[get]
        result = self.mgmt_client.accounts.list()

        # Regenerate Keys[get]
        result = self.mgmt_client.resource_skus.list()

        # Get Operations[get]
        result = self.mgmt_client.operations.list()

        # Regenerate Keys[get]
        result = self.mgmt_client.resource_skus.list()

        # List Keys[post]
        result = self.mgmt_client.accounts.list_keys(resource_group.name, ACCOUNT_NAME)

        # Update Account[patch]
        BODY = {
          "sku": {
            "name": "S2"
          }
        }
        result = self.mgmt_client.accounts.update(resource_group.name, ACCOUNT_NAME, BODY)

        # Check SKU Availability[post]
        BODY = {
          "skus": [
            "S0"
          ],
          "kind": "Face",
          "type": "Microsoft.CognitiveServices/accounts"
        }
        result = self.mgmt_client..check_sku_availability(LOCATION_NAME, BODY)

        # Check SKU Availability[post]
        BODY = {
          "skus": [
            "S0"
          ],
          "kind": "Face",
          "type": "Microsoft.CognitiveServices/accounts"
        }
        result = self.mgmt_client..check_sku_availability(LOCATION_NAME, BODY)

        # Delete Account[delete]
        result = self.mgmt_client.accounts.delete(resource_group.name, ACCOUNT_NAME)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
