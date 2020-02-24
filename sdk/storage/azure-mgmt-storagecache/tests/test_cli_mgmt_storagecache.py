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
# Examples Total  : 17
# Examples Tested : 17
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.network
import azure.mgmt.storagecache
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtStorageCacheTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtStorageCacheTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.storagecache.StorageCacheManagementClient
        )
        self.network_client = self.create_mgmt_client(
          azure.mgmt.network.NetworkManagementClient
        )

   
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_storagecache(self, resource_group):

        SUBSCRIPTION_ID = self.settings.SUBSCRIPTION_ID
        RESOURCE_GROUP = resource_group.name
        VIRTUAL_NETWORK_NAME = 'vnet1'
        SUBNET_NAME = 'subnet1'
        CACHE_NAME = 'testCache'
        STORAGE_TARGET_NAME = 'testStorageTarget'

        # # -- SET UP START --
        # # Create VNet
        # async_vnet_creation = self.network_client.virtual_networks.create_or_update(
        #     resource_group.name,
        #     VIRTUAL_NETWORK_NAME,
        #     {
        #         'location': AZURE_LOCATION,
        #         'address_space': {
        #             'address_prefixes': ['10.0.0.0/16']
        #         }
        #     }
        # )
        # async_vnet_creation.wait()

        # # Create Subnet
        # async_subnet_creation = self.network_client.subnets.create_or_update(
        #     resource_group.name,
        #     VIRTUAL_NETWORK_NAME,
        #     SUBNET_NAME,
        #     {'address_prefix': '10.0.0.0/24'}
        # )
        # subnet_info = async_subnet_creation.result()
        # # -- SET UP END --

        # Caches_CreateOrUpdate[put]
        BODY = {
          "tags": {
            "dept": "Initech"
          },
          "location": "eastus",

          # "properties": {

          # "type": "Microsoft.StorageCache",  # What i added
          "cache_size_gb": "3072",
          "subnet": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",
          # },

          "sku": {
            "name": "Standard_2G"
          }
        }
        result = self.mgmt_client.caches.create_or_update(resource_group.name, CACHE_NAME, BODY)
        result = result.result()

        # StorageTargets_CreateOrUpdate[put]
        BODY = {
          "properties": {
            "junctions": [
              {
                "namespace_path": "/path/on/cache",
                "target_path": "/path/on/exp1",
                "nfs_export": "exp1"
              },
              {
                "namespace_path": "/path2/on/cache",
                "target_path": "/path2/on/exp2",
                "nfs_export": "exp2"
              }
            ],
            "target_type": "nfs3",
            "nfs3": {
              "target": "10.0.44.44",
              "usage_model": "READ_HEAVY_INFREQ"
            }
          }
        }
        result = self.mgmt_client.storage_targets.create_or_update(resource_group.name, CACHE_NAME, STORAGE_TARGET_NAME, BODY)
        result = result.result()

        # StorageTargets_Get[get]
        result = self.mgmt_client.storage_targets.get(resource_group.name, CACHE_NAME, STORAGE_TARGET_NAME)

        # StorageTargets_List[get]
        result = self.mgmt_client.operations.list()

        # Caches_Get[get]
        result = self.mgmt_client.caches.get(resource_group.name, CACHE_NAME)

        # Caches_ListByResourceGroup[get]
        result = self.mgmt_client.caches.list_by_resource_group(resource_group.name)

        # UsageModels_List[get]
        result = self.mgmt_client.usage_models.list()

        # Caches_List[get]
        result = self.mgmt_client.caches.list()

        # Skus_List[get]
        result = self.mgmt_client.skus.list()

        # StorageTargets_List[get]
        result = self.mgmt_client.operations.list()

        # Caches_UpgradeFirmware[post]
        result = self.mgmt_client.caches.upgrade_firmware(resource_group.name, CACHE_NAME)
        result = result.result()

        # Caches_Flush[post]
        result = self.mgmt_client.caches.flush(resource_group.name, CACHE_NAME)
        result = result.result()

        # Caches_Start[post]
        result = self.mgmt_client.caches.start(resource_group.name, CACHE_NAME)
        result = result.result()

        # Caches_Stop[post]
        result = self.mgmt_client.caches.stop(resource_group.name, CACHE_NAME)
        result = result.result()

        # Caches_Update[patch]
        BODY = {
          "tags": {
            "dept": "Initech"
          },
          "location": "eastus",
          "properties": {
            "cache_size_gb": "3072",
            "subnet": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
          },
          "sku": {
            "name": "Standard_2G"
          }
        }
        result = self.mgmt_client.caches.update(resource_group.name, CACHE_NAME, BODY)

        # StorageTargets_Delete[delete]
        result = self.mgmt_client.storage_targets.delete(resource_group.name, CACHE_NAME, STORAGE_TARGET_NAME)
        result = result.result()

        # Caches_Delete[delete]
        result = self.mgmt_client.caches.delete(resource_group.name, CACHE_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
