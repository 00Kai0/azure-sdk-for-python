# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 21
# Methods Covered : 21
# Examples Total  : 21
# Examples Tested : 21
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.network
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtNetworkTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtNetworkTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.network.NetworkManagementClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_network(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Create Bastion Host[put]
        BODY = {
          "properties": {
            "ip_configurations": [
              {
                "name": "bastionHostIpConfiguration",
                "properties": {
                  "subnet": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                  },
                  "public_ip_address": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/publicIPAddresses/" + PUBLIC_IP_ADDRESS_NAME + ""
                  }
                }
              }
            ]
          }
        }
        result = self.mgmt_client.bastion_hosts.create_or_update(resource_group.name, BASTION_HOST_NAME, BODY)
        result = result.result()

        # Create DDoS custom policy[put]
        BODY = {
          "location": "centraluseuap",
          "properties": {
            "protocol_custom_settings": [
              {
                "protocol": "Tcp"
              }
            ]
          }
        }
        result = self.mgmt_client.ddos_custom_policies.create_or_update(resource_group.name, DDOS_CUSTOM_POLICY_NAME, BODY)
        result = result.result()

        # Create DDoS protection plan[put]
        BODY = {
          "location": "westus"
        }
        result = self.mgmt_client.ddos_protection_plans.create_or_update(resource_group.name, DDOS_PROTECTION_PLAN_NAME, BODY)
        result = result.result()

        # Get DDoS protection plan[get]
        result = self.mgmt_client.ddos_protection_plans.get(resource_group.name, DDOS_PROTECTION_PLAN_NAME)

        # Get DDoS custom policy[get]
        result = self.mgmt_client.ddos_custom_policies.get(resource_group.name, DDOS_CUSTOM_POLICY_NAME)

        # Get Bastion Host[get]
        result = self.mgmt_client.bastion_hosts.get(resource_group.name, BASTION_HOST_NAME)

        # List DDoS protection plans in resource group[get]
        result = self.mgmt_client.ddos_protection_plans.list_by_resource_group(resource_group.name)

        # Check Dns Name Availability[get]
        result = self.mgmt_client..check_dns_name_availability(LOCATION_NAME)

        # List all Bastion Hosts for a given resource group[get]
        result = self.mgmt_client.bastion_hosts.list_by_resource_group(resource_group.name)

        # List all DDoS protection plans[get]
        result = self.mgmt_client.ddos_protection_plans.list()

        # List all Bastion Hosts for a given subscription[get]
        result = self.mgmt_client.bastion_hosts.list()

        # Deletes the specified active session[post]
        result = self.mgmt_client..disconnect_active_sessions(resource_group.name, BASTION_HOST_NAME)

        # Create Bastion Shareable Links for the request VMs[post]
        BODY = {
          "vms": [
            {
              "vm": {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
              }
            },
            {
              "vm": {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
              }
            }
          ]
        }
        result = self.mgmt_client..put_bastion_shareable_link(resource_group.name, BASTION_HOST_NAME, BODY)
        result = result.result()

        # Delete Bastion Shareable Links for the request VMs[post]
        BODY = {
          "vms": [
            {
              "vm": {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
              }
            },
            {
              "vm": {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
              }
            }
          ]
        }
        result = self.mgmt_client..delete_bastion_shareable_link(resource_group.name, BASTION_HOST_NAME, BODY)
        result = result.result()

        # Returns the Bastion Shareable Links for the request VMs[post]
        BODY = {
          "vms": [
            {
              "vm": {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
              }
            },
            {
              "vm": {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
              }
            }
          ]
        }
        result = self.mgmt_client..get_bastion_shareable_link(resource_group.name, BASTION_HOST_NAME, BODY)

        # Returns a list of currently active sessions on the Bastion[post]
        result = self.mgmt_client..get_active_sessions(resource_group.name, BASTION_HOST_NAME)
        result = result.result()

        # DDoS protection plan Update tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.ddos_protection_plans.update_tags(resource_group.name, DDOS_PROTECTION_PLAN_NAME, BODY)

        # DDoS Custom policy Update tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.ddos_custom_policies.update_tags(resource_group.name, DDOS_CUSTOM_POLICY_NAME, BODY)

        # Delete DDoS protection plan[delete]
        result = self.mgmt_client.ddos_protection_plans.delete(resource_group.name, DDOS_PROTECTION_PLAN_NAME)
        result = result.result()

        # Delete DDoS custom policy[delete]
        result = self.mgmt_client.ddos_custom_policies.delete(resource_group.name, DDOS_CUSTOM_POLICY_NAME)
        result = result.result()

        # Delete Bastion Host[delete]
        result = self.mgmt_client.bastion_hosts.delete(resource_group.name, BASTION_HOST_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
