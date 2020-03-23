# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 17
# Methods Covered : 17
# Examples Total  : 18
# Examples Tested : 18
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.keyvault
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtKeyVaultTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtKeyVaultTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.keyvault.KeyVault
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_keyvault(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Create a new vault or update an existing vault[put]
        BODY = {
          "location": "westus",
          "properties": {
            "tenant_id": "00000000-0000-0000-0000-000000000000",
            "sku": {
              "family": "A",
              "name": "standard"
            },
            "access_policies": [
              {
                "tenant_id": "00000000-0000-0000-0000-000000000000",
                "object_id": "00000000-0000-0000-0000-000000000000",
                "permissions": {
                  "keys": [
                    "encrypt",
                    "decrypt",
                    "wrapKey",
                    "unwrapKey",
                    "sign",
                    "verify",
                    "get",
                    "list",
                    "create",
                    "update",
                    "import",
                    "delete",
                    "backup",
                    "restore",
                    "recover",
                    "purge"
                  ],
                  "secrets": [
                    "get",
                    "list",
                    "set",
                    "delete",
                    "backup",
                    "restore",
                    "recover",
                    "purge"
                  ],
                  "certificates": [
                    "get",
                    "list",
                    "delete",
                    "create",
                    "import",
                    "update",
                    "managecontacts",
                    "getissuers",
                    "listissuers",
                    "setissuers",
                    "deleteissuers",
                    "manageissuers",
                    "recover",
                    "purge"
                  ]
                }
              }
            ],
            "enabled_for_deployment": True,
            "enabled_for_disk_encryption": True,
            "enabled_for_template_deployment": True
          }
        }
        result = self.mgmt_client.vaults.create_or_update(resource_group.name, VAULT_NAME, BODY)
        result = result.result()

        # Create or update a vault with network acls[put]
        BODY = {
          "location": "westus",
          "properties": {
            "tenant_id": "00000000-0000-0000-0000-000000000000",
            "sku": {
              "family": "A",
              "name": "standard"
            },
            "network_acls": {
              "default_action": "Deny",
              "bypass": "AzureServices",
              "ip_rules": [
                {
                  "value": "124.56.78.91"
                },
                {
                  "value": "'10.91.4.0/24'"
                }
              ],
              "virtual_network_rules": [
                {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                }
              ]
            },
            "enabled_for_deployment": True,
            "enabled_for_disk_encryption": True,
            "enabled_for_template_deployment": True
          }
        }
        result = self.mgmt_client.vaults.create_or_update(resource_group.name, VAULT_NAME, BODY)
        result = result.result()

        # Add an access policy, or update an access policy with new permissions[put]
        BODY = {
          "properties": {
            "access_policies": [
              {
                "tenant_id": "00000000-0000-0000-0000-000000000000",
                "object_id": "00000000-0000-0000-0000-000000000000",
                "permissions": {
                  "keys": [
                    "encrypt"
                  ],
                  "secrets": [
                    "get"
                  ],
                  "certificates": [
                    "get"
                  ]
                }
              }
            ]
          }
        }
        result = self.mgmt_client.vaults.update_access_policy(resource_group.name, VAULT_NAME, ACCESS_POLICY_NAME, BODY)

        # KeyVaultPutPrivateEndpointConnection[put]
        BODY = {
          "properties": {
            "private_link_service_connection_state": {
              "status": "Approved",
              "description": "My name is Joe and I'm approving this."
            }
          }
        }
        result = self.mgmt_client.private_endpoint_connections.put(resource_group.name, VAULT_NAME, PRIVATE_ENDPOINT_CONNECTION_NAME, BODY)

        # KeyVaultGetPrivateEndpointConnection[get]
        result = self.mgmt_client.private_endpoint_connections.get(resource_group.name, VAULT_NAME, PRIVATE_ENDPOINT_CONNECTION_NAME)

        # KeyVaultListPrivateLinkResources[get]
        result = self.mgmt_client.private_link_resources.list_by_vault(resource_group.name, VAULT_NAME)

        # Retrieve a deleted vault[get]
        result = self.mgmt_client.vaults.get_deleted(LOCATION_NAME, DELETED_VAULT_NAME)

        # Retrieve a vault[get]
        result = self.mgmt_client.vaults.get(resource_group.name, VAULT_NAME)

        # List vaults in the specified resource group[get]
        result = self.mgmt_client.vaults.list_by_resource_group(resource_group.name)

        # List deleted vaults in the specified subscription[get]
        result = self.mgmt_client.vaults.list_deleted()

        # List vaults in the specified subscription[get]
        result = self.mgmt_client.vaults.list_by_subscription()

        # List vaults in the specified subscription[get]
        result = self.mgmt_client.vaults.list_by_subscription()

        # Lists available Rest API operations.[get]
        result = self.mgmt_client.operations.list()

        # Purge a deleted vault[post]
        result = self.mgmt_client.vaults.purge_deleted(LOCATION_NAME, DELETED_VAULT_NAME)
        result = result.result()

        # Update an existing vault[patch]
        BODY = {
          "properties": {
            "tenant_id": "00000000-0000-0000-0000-000000000000",
            "sku": {
              "family": "A",
              "name": "standard"
            },
            "access_policies": [
              {
                "tenant_id": "00000000-0000-0000-0000-000000000000",
                "object_id": "00000000-0000-0000-0000-000000000000",
                "permissions": {
                  "keys": [
                    "encrypt",
                    "decrypt",
                    "wrapKey",
                    "unwrapKey",
                    "sign",
                    "verify",
                    "get",
                    "list",
                    "create",
                    "update",
                    "import",
                    "delete",
                    "backup",
                    "restore",
                    "recover",
                    "purge"
                  ],
                  "secrets": [
                    "get",
                    "list",
                    "set",
                    "delete",
                    "backup",
                    "restore",
                    "recover",
                    "purge"
                  ],
                  "certificates": [
                    "get",
                    "list",
                    "delete",
                    "create",
                    "import",
                    "update",
                    "managecontacts",
                    "getissuers",
                    "listissuers",
                    "setissuers",
                    "deleteissuers",
                    "manageissuers",
                    "recover",
                    "purge"
                  ]
                }
              }
            ],
            "enabled_for_deployment": True,
            "enabled_for_disk_encryption": True,
            "enabled_for_template_deployment": True
          }
        }
        result = self.mgmt_client.vaults.update(resource_group.name, VAULT_NAME, BODY)

        # Validate a vault name[post]
        BODY = {
          "name": "sample-vault",
          "type": "Microsoft.KeyVault/vaults"
        }
        result = self.mgmt_client.vaults.check_name_availability(BODY)

        # KeyVaultDeletePrivateEndpointConnection[delete]
        result = self.mgmt_client.private_endpoint_connections.delete(resource_group.name, VAULT_NAME, PRIVATE_ENDPOINT_CONNECTION_NAME)
        result = result.result()

        # Delete a vault[delete]
        result = self.mgmt_client.vaults.delete(resource_group.name, VAULT_NAME)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
