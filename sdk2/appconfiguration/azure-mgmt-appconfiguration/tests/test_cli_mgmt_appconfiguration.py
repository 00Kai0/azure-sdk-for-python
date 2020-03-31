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

# covered ops:
#   configuration_stores: 8/9
#   operations: 2/2
#   private_endpoint_connections: 4/4
#   private_link_resources: 2/2

import time
import unittest

import azure.mgmt.appconfiguration
import azure.mgmt.network
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtAppConfigurationTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtAppConfigurationTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.appconfiguration.AppConfigurationManagementClient
        )

        self.network_client = self.create_mgmt_client(
          azure.mgmt.network.NetworkManagementClient
        )

    # TODO: update to track 2 version later
    def create_endpoint(self, group_name, vnet_name, sub_net, endpoint_name, conf_store_id):
        # Create VNet
        async_vnet_creation = self.network_client.virtual_networks.create_or_update(
            group_name,
            vnet_name,
            {
                'location': AZURE_LOCATION,
                'address_space': {
                    'address_prefixes': ['10.0.0.0/16']
                }
            }
        )
        async_vnet_creation.wait()

        # Create Subnet
        async_subnet_creation = self.network_client.subnets.create_or_update(
            group_name,
            vnet_name,
            sub_net,
            {
              'address_prefix': '10.0.0.0/24',
               'private_link_service_network_policies': 'disabled',
               'private_endpoint_network_policies': 'disabled'
            }
        )
        subnet_info = async_subnet_creation.result()

        # Create private endpoint
        BODY = {
          "location": "eastus",
          "properties": {
            "privateLinkServiceConnections": [
              # {
              #   "name": PRIVATE_LINK_SERVICES,  # TODO: This is needed, but was not showed in swagger.
              #   "private_link_service_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/privateLinkServices/" + PRIVATE_LINK_SERVICES,
              # },
              {
                "name": "myconnection",
                # "private_link_service_id": "/subscriptions/" + self.settings.SUBSCRIPTION_ID + "/resourceGroups/" + group_name + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
                "private_link_service_id": conf_store_id,
                "group_ids": ["configurationStores"]
              }
            ],
            "subnet": {
              "id": "/subscriptions/" + self.settings.SUBSCRIPTION_ID + "/resourceGroups/" + group_name + "/providers/Microsoft.Network/virtualNetworks/" + vnet_name + "/subnets/" + sub_net
            }
          }
        }
        result = self.network_client.private_endpoints.create_or_update(group_name, endpoint_name, BODY)

        return result.result()
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_appconfiguration(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"
        VNET_NAME = "vnetname"
        SUB_NET = "subnetname"
        ENDPOINT_NAME = "endpointxyz"
        CONFIGURATION_STORE_NAME = self.get_resource_name("configuration")
        PRIVATE_ENDPOINT_CONNECTION_NAME = self.get_resource_name("privateendpoint")

        # ConfigurationStores_Create[put]
        BODY = {
          "location": "westus",
          "sku": {
            "name": "Standard"  # Free can not use private endpoint
          },
          "tags": {
            "my_tag": "myTagValue"
          }
        }
        result = self.mgmt_client.configuration_stores.begin_create(resource_group.name, CONFIGURATION_STORE_NAME, BODY)
        conf_store = result.result()

        # create endpoint
        endpoint = self.create_endpoint(resource_group.name, VNET_NAME, SUB_NET, ENDPOINT_NAME, conf_store.id)

        # ConfigurationStores_Create_WithIdentity[put]
        # BODY = {
        #   "location": "westus",
        #   "sku": {
        #     "name": "Free"
        #   },
        #   "tags": {
        #     "my_tag": "myTagValue"
        #   },
        #   "identity": {
        #     "type": "SystemAssigned, UserAssigned",
        #     "user_assigned_identities": {}
        #   }
        # }
        # result = self.mgmt_client.configuration_stores.begin_create(resource_group.name, CONFIGURATION_STORE_NAME, BODY)
        # result = result.result()

        # ConfigurationStores_Get[get]
        conf_store = self.mgmt_client.configuration_stores.get(resource_group.name, CONFIGURATION_STORE_NAME)
        PRIVATE_ENDPOINT_CONNECTION_NAME = conf_store.private_endpoint_connections[0].name
        private_connection_id = conf_store.private_endpoint_connections[0].id

        # TODO: azure.core.exceptions.HttpResponseError: (InvalidProperty) Some of the properties of 'PrivateEndpointConnection' are invalid. Errors: 'Missing required property 'Id'.'
        # PrivateEndpointConnection_CreateOrUpdate[put]
        BODY = {
          # "id": "https://management.azure.com/subscriptions/" + self.settings.SUBSCRIPTION_ID + "/resourceGroups/" + resource_group.name + "/providers/Microsoft.AppConfiguration/configurationStores/" + CONFIGURATION_STORE_NAME + "/privateEndpointConnections/" + PRIVATE_ENDPOINT_CONNECTION_NAME,
          "id": private_connection_id,
          "private_endpoint": {
            "id": "/subscriptions/" + self.settings.SUBSCRIPTION_ID + "/resourceGroups/" + resource_group.name + "/providers/Microsoft.Network/privateEndpoints/" + ENDPOINT_NAME,
          },
          "private_link_service_connection_state": {
            "status": "Approved",
            "description": "Auto-Approved"
          }
        }
        result = self.mgmt_client.private_endpoint_connections.begin_create_or_update(
            resource_group.name,
            CONFIGURATION_STORE_NAME,
            PRIVATE_ENDPOINT_CONNECTION_NAME,
            BODY)
            # id=BODY["id"],
            # private_endpoint=BODY["private_endpoint"],
            # private_link_service_connection_state=BODY["private_link_service_connection_state"])
        result = result.result()
          
        # PrivateEndpointConnection_GetConnection[get]
        result = self.mgmt_client.private_endpoint_connections.get(resource_group.name, CONFIGURATION_STORE_NAME, PRIVATE_ENDPOINT_CONNECTION_NAME)

        # PrivateLinkResources_ListGroupIds[get]
        privatelinks = list(self.mgmt_client.private_link_resources.list_by_configuration_store(resource_group.name, CONFIGURATION_STORE_NAME))
        PRIVATE_LINK_RESOURCE_NAME = privatelinks[0].name

        # PrivateLinkResources_Get[get]
        result = self.mgmt_client.private_link_resources.get(resource_group.name, CONFIGURATION_STORE_NAME, PRIVATE_LINK_RESOURCE_NAME)

        # PrivateEndpointConnection_List[get]
        result = list(self.mgmt_client.private_endpoint_connections.list_by_configuration_store(resource_group.name, CONFIGURATION_STORE_NAME))

        # List the operations available
        result = self.mgmt_client.operations.list()

        # ConfigurationStores_ListByResourceGroup[get]
        result = self.mgmt_client.configuration_stores.list_by_resource_group(resource_group.name)

        # ConfigurationStores_List[get]
        result = self.mgmt_client.configuration_stores.list()

        # ConfigurationStores_ListKeys[post]
        keys = list(self.mgmt_client.configuration_stores.list_keys(resource_group.name, CONFIGURATION_STORE_NAME))

        # ConfigurationStores_RegenerateKey[post]
        BODY = {
          "id": keys[0].id
        }
        result = self.mgmt_client.configuration_stores.regenerate_key(resource_group.name, CONFIGURATION_STORE_NAME, BODY["id"])

        # TODO: azure.core.exceptions.HttpResponseError: (InternalServerError) Cannot serve the request. Please retry.
        # ConfigurationStores_ListKeyValue[post]
        # BODY = {
        #   "key": "MaxRequests",
        #   "label": "dev"
        # }
        # result = self.mgmt_client.configuration_stores.list_key_value(resource_group.name, CONFIGURATION_STORE_NAME, BODY["key"], BODY["label"])

        # ConfigurationStores_Update[patch]
        BODY = {
          "tags": {
            "category": "Marketing"
          },
          "sku": {
            "name": "Standard"
          }
        }
        result = self.mgmt_client.configuration_stores.begin_update(resource_group.name, CONFIGURATION_STORE_NAME, BODY)
        result = result.result()

        # ConfigurationStores_Update_WithIdentity[patch]
        # BODY = {
        #   "tags": {
        #     "category": "Marketing"
        #   },
        #   "sku": {
        #     "name": "Standard"
        #   },
        #   "identity": {
        #     "type": "SystemAssigned, UserAssigned",
        #     "user_assigned_identities": {}
        #   }
        # }
        # result = self.mgmt_client.configuration_stores.begin_update(resource_group.name, CONFIGURATION_STORE_NAME, BODY)
        # result = result.result()

        # ConfigurationStores_CheckNameNotAvailable[post]
        BODY = {
          "name": "contoso",
          "type": "Microsoft.AppConfiguration/configurationStores"
        }
        result = self.mgmt_client.operations.check_name_availability(BODY["name"])

        # ConfigurationStores_CheckNameAvailable[post]
        # BODY = {
        #   "name": "contoso",
        #   "type": "Microsoft.AppConfiguration/configurationStores"
        # }
        # result = self.mgmt_client.operations.check_name_availability(BODY["name"])

        # PrivateEndpointConnections_Delete[delete]
        result = self.mgmt_client.private_endpoint_connections.begin_delete(resource_group.name, CONFIGURATION_STORE_NAME, PRIVATE_ENDPOINT_CONNECTION_NAME)
        result = result.result()

        # ConfigurationStores_Delete[delete]
        result = self.mgmt_client.configuration_stores.begin_delete(resource_group.name, CONFIGURATION_STORE_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
