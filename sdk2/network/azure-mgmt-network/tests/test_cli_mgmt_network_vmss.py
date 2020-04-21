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
# Examples Total  : 8
# Examples Tested : 8
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

        # GetVMSSPublicIP[get]
        result = self.mgmt_client.public_ip_addresses.get_virtual_machine_scale_set_public_ip_address(resource_group.name, VIRTUAL_MACHINE_SCALE_SET_NAME, VIRTUAL_MACHINE_NAME, NETWORK_INTERFACE_NAME, IPCONFIGURATION_NAME, PUBLICIP_ADDRESS_NAME)

        # ListVMSSVMPublicIP[get]
        result = self.mgmt_client.public_ip_addresses.list_virtual_machine_scale_set_vmpublic_ip_addresses(resource_group.name, VIRTUAL_MACHINE_SCALE_SET_NAME, VIRTUAL_MACHINE_NAME, NETWORK_INTERFACE_NAME, IPCONFIGURATION_NAME)

        # Get virtual machine scale set network interface[get]
        result = self.mgmt_client.network_interfaces.get_virtual_machine_scale_set_ip_configuration(resource_group.name, VIRTUAL_MACHINE_SCALE_SET_NAME, VIRTUAL_MACHINE_NAME, NETWORK_INTERFACE_NAME, IP_CONFIGURATION_NAME)

        # List virtual machine scale set network interface ip configurations[get]
        result = self.mgmt_client.network_interfaces.list_virtual_machine_scale_set_ip_configurations(resource_group.name, VIRTUAL_MACHINE_SCALE_SET_NAME, VIRTUAL_MACHINE_NAME, NETWORK_INTERFACE_NAME)

        # Get virtual machine scale set network interface[get]
        result = self.mgmt_client.network_interfaces.get_virtual_machine_scale_set_ip_configuration(resource_group.name, VIRTUAL_MACHINE_SCALE_SET_NAME, VIRTUAL_MACHINE_NAME, NETWORK_INTERFACE_NAME, IP_CONFIGURATION_NAME)

        # List virtual machine scale set vm network interfaces[get]
        result = self.mgmt_client.network_interfaces.list_virtual_machine_scale_set_vmnetwork_interfaces(resource_group.name, VIRTUAL_MACHINE_SCALE_SET_NAME, VIRTUAL_MACHINE_NAME)

        # ListVMSSPublicIP[get]
        result = self.mgmt_client.public_ip_addresses.list_virtual_machine_scale_set_public_ip_addresses(resource_group.name, VIRTUAL_MACHINE_SCALE_SET_NAME)

        # List virtual machine scale set network interfaces[get]
        result = self.mgmt_client.network_interfaces.list_virtual_machine_scale_set_network_interfaces(resource_group.name, VIRTUAL_MACHINE_SCALE_SET_NAME)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
