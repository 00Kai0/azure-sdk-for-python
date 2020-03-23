# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 17
# Methods Covered : 16
# Examples Total  : 19
# Examples Tested : 19
# Coverage %      : 94.11764705882352
# ----------------------

import unittest

import azure.mgmt.appconfiguration
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtAppConfigurationTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtAppConfigurationTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.appconfiguration.AppConfigurationManagementClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_appconfiguration(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # ConfigurationStores_Create[put]
        BODY = {
          "location": "westus",
          "sku": {
            "name": "Free"
          },
          "tags": {
            "my_tag": "myTagValue"
          }
        }
        result = self.mgmt_client.configuration_stores.create(resource_group.name, CONFIGURATION_STORE_NAME, BODY)
        result = result.result()

        # ConfigurationStores_Create_WithIdentity[put]
        BODY = {
          "location": "westus",
          "sku": {
            "name": "Free"
          },
          "tags": {
            "my_tag": "myTagValue"
          },
          "identity": {
            "type": "SystemAssigned, UserAssigned",
            "user_assigned_identities": {}
          }
        }
        result = self.mgmt_client.configuration_stores.create(resource_group.name, CONFIGURATION_STORE_NAME, BODY)
        result = result.result()

        # PrivateEndpointConnection_CreateOrUpdate[put]
        BODY = {
          "properties": {
            "private_link_service_connection_state": {
              "status": "Approved",
              "description": "Auto-Approved"
            }
          }
        }
        result = self.mgmt_client.private_endpoint_connections.create_or_update(resource_group.name, CONFIGURATION_STORE_NAME, PRIVATE_ENDPOINT_CONNECTION_NAME, BODY)
        result = result.result()

        # PrivateEndpointConnection_GetConnection[get]
        result = self.mgmt_client.private_endpoint_connections.get(resource_group.name, CONFIGURATION_STORE_NAME, PRIVATE_ENDPOINT_CONNECTION_NAME)

        # PrivateLinkResources_Get[get]
        result = self.mgmt_client.private_link_resources.get(resource_group.name, CONFIGURATION_STORE_NAME, PRIVATE_LINK_RESOURCE_NAME)

        # PrivateEndpointConnection_List[get]
        result = self.mgmt_client.private_endpoint_connections.list_by_configuration_store(resource_group.name, CONFIGURATION_STORE_NAME)

        # PrivateLinkResources_ListGroupIds[get]
        result = self.mgmt_client.private_link_resources.list_by_configuration_store(resource_group.name, CONFIGURATION_STORE_NAME)

        # ConfigurationStores_Get[get]
        result = self.mgmt_client.configuration_stores.get(resource_group.name, CONFIGURATION_STORE_NAME)

        # ConfigurationStores_ListByResourceGroup[get]
        result = self.mgmt_client.configuration_stores.list_by_resource_group(resource_group.name)

        # ConfigurationStores_List[get]
        result = self.mgmt_client.configuration_stores.list()

        # ConfigurationStores_RegenerateKey[post]
        BODY = {
          "id": "439AD01B4BE67DB1"
        }
        result = self.mgmt_client.configuration_stores.regenerate_key(resource_group.name, CONFIGURATION_STORE_NAME, BODY)

        # ConfigurationStores_ListKeyValue[post]
        BODY = {
          "key": "MaxRequests",
          "label": "dev"
        }
        result = self.mgmt_client.configuration_stores.list_key_value(resource_group.name, CONFIGURATION_STORE_NAME, BODY)

        # ConfigurationStores_ListKeys[post]
        result = self.mgmt_client.configuration_stores.list_keys(resource_group.name, CONFIGURATION_STORE_NAME)

        # ConfigurationStores_Update[patch]
        BODY = {
          "tags": {
            "category": "Marketing"
          },
          "sku": {
            "name": "Standard"
          }
        }
        result = self.mgmt_client.configuration_stores.update(resource_group.name, CONFIGURATION_STORE_NAME, BODY)
        result = result.result()

        # ConfigurationStores_Update_WithIdentity[patch]
        BODY = {
          "tags": {
            "category": "Marketing"
          },
          "sku": {
            "name": "Standard"
          },
          "identity": {
            "type": "SystemAssigned, UserAssigned",
            "user_assigned_identities": {}
          }
        }
        result = self.mgmt_client.configuration_stores.update(resource_group.name, CONFIGURATION_STORE_NAME, BODY)
        result = result.result()

        # ConfigurationStores_CheckNameNotAvailable[post]
        BODY = {
          "name": "contoso",
          "type": "Microsoft.AppConfiguration/configurationStores"
        }
        result = self.mgmt_client.operations.check_name_availability(BODY)

        # ConfigurationStores_CheckNameAvailable[post]
        BODY = {
          "name": "contoso",
          "type": "Microsoft.AppConfiguration/configurationStores"
        }
        result = self.mgmt_client.operations.check_name_availability(BODY)

        # PrivateEndpointConnections_Delete[delete]
        result = self.mgmt_client.private_endpoint_connections.delete(resource_group.name, CONFIGURATION_STORE_NAME, PRIVATE_ENDPOINT_CONNECTION_NAME)
        result = result.result()

        # ConfigurationStores_Delete[delete]
        result = self.mgmt_client.configuration_stores.delete(resource_group.name, CONFIGURATION_STORE_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
