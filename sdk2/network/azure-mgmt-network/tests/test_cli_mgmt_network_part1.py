# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 60
# Methods Covered : 60
# Examples Total  : 63
# Examples Tested : 63
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

        # Create network watcher[put]
        BODY = {
          "location": "eastus"
        }
        result = self.mgmt_client.network_watchers.create_or_update(resource_group.name, NETWORK_WATCHER_NAME, BODY)

        # Create network profile defaults[put]
        BODY = {
          "location": "westus",
          "properties": {
            "container_network_interface_configurations": [
              {
                "name": "eth1",
                "properties": {
                  "ip_configurations": [
                    {
                      "name": "ipconfig1",
                      "properties": {
                        "subnet": {
                          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                        }
                      }
                    }
                  ]
                }
              }
            ]
          }
        }
        result = self.mgmt_client.network_profiles.create_or_update(resource_group.name, NETWORK_PROFILE_NAME, BODY)

        # Create network security group[put]
        BODY = {
          "location": "eastus"
        }
        result = self.mgmt_client.network_security_groups.create_or_update(resource_group.name, NETWORK_SECURITY_GROUP_NAME, BODY)
        result = result.result()

        # Create network security group with rule[put]
        BODY = {
          "properties": {
            "security_rules": [
              {
                "name": "rule1",
                "properties": {
                  "protocol": "*",
                  "source_address_prefix": "*",
                  "destination_address_prefix": "*",
                  "access": "Allow",
                  "destination_port_range": "80",
                  "source_port_range": "*",
                  "priority": "130",
                  "direction": "Inbound"
                }
              }
            ]
          },
          "location": "eastus"
        }
        result = self.mgmt_client.network_security_groups.create_or_update(resource_group.name, NETWORK_SECURITY_GROUP_NAME, BODY)
        result = result.result()

        # Create NetworkVirtualAppliance[put]
        BODY = {
          "tags": {
            "key1": "value1"
          },
          "sku": {
            "vendor": "Cisco SDWAN",
            "bundled_scale_unit": "1",
            "market_place_version": "12.1"
          },
          "identity": {
            "type": "UserAssigned",
            "user_assigned_identities": {}
          },
          "location": "West US",
          "properties": {
            "virtual_hub": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualHubs/" + VIRTUAL_HUB_NAME + ""
            },
            "boot_strap_configuration_blob": [
              "https://csrncvhdstorage1.blob.core.windows.net/csrncvhdstoragecont/csrbootstrapconfig"
            ],
            "cloud_init_configuration_blob": [
              "https://csrncvhdstorage1.blob.core.windows.net/csrncvhdstoragecont/csrcloudinitconfig"
            ],
            "virtual_appliance_asn": "10000"
          }
        }
        result = self.mgmt_client.network_virtual_appliances.create_or_update(resource_group.name, NETWORK_VIRTUAL_APPLIANCE_NAME, BODY)
        result = result.result()

        # Create or update flow log[put]
        BODY = {
          "location": "centraluseuap",
          "properties": {
            "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/networkSecurityGroups/" + NETWORK_SECURITY_GROUP_NAME + "",
            "storage_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
            "enabled": True,
            "format": {
              "type": "JSON",
              "version": "1"
            }
          }
        }
        result = self.mgmt_client.flow_logs.create_or_update(resource_group.name, NETWORK_WATCHER_NAME, FLOW_LOG_NAME, BODY)
        result = result.result()

        # Create packet capture[put]
        BODY = {
          "properties": {
            "target": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + "",
            "bytes_to_capture_per_packet": "10000",
            "total_bytes_per_session": "100000",
            "time_limit_in_seconds": "100",
            "storage_location": {
              "storage_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
              "storage_path": "https://mytestaccountname.blob.core.windows.net/capture/pc1.cap",
              "file_path": "D:\\capture\\pc1.cap"
            },
            "filters": [
              {
                "protocol": "TCP",
                "local_ip_address": "10.0.0.4",
                "local_port": "80"
              }
            ]
          }
        }
        result = self.mgmt_client.packet_captures.create(resource_group.name, NETWORK_WATCHER_NAME, PACKET_CAPTURE_NAME, BODY)
        result = result.result()

        # Create connection monitor V2[put]
        BODY = {
          "properties": {
            "endpoints": [
              {
                "name": "vm1",
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
              },
              {
                "name": "CanaryWorkspaceVamshi",
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.OperationalInsights/workspaces/" + WORKSPACE_NAME + "",
                "filter": {
                  "type": "Include",
                  "items": [
                    {
                      "type": "AgentAddress",
                      "address": "npmuser"
                    }
                  ]
                }
              },
              {
                "name": "bing",
                "address": "bing.com"
              },
              {
                "name": "google",
                "address": "google.com"
              }
            ],
            "test_configurations": [
              {
                "name": "testConfig1",
                "test_frequency_sec": "60",
                "protocol": "Tcp",
                "tcp_configuration": {
                  "port": "80",
                  "disable_trace_route": False
                }
              }
            ],
            "test_groups": [
              {
                "name": "test1",
                "disable": False,
                "test_configurations": [
                  "testConfig1"
                ],
                "sources": [
                  "vm1",
                  "CanaryWorkspaceVamshi"
                ],
                "destinations": [
                  "bing",
                  "google"
                ]
              }
            ],
            "outputs": []
          }
        }
        result = self.mgmt_client.connection_monitors.create_or_update(resource_group.name, NETWORK_WATCHER_NAME, CONNECTION_MONITOR_NAME, BODY)
        result = result.result()

        # Create connection monitor V1[put]
        BODY = {
          "properties": {
            "source": {
              "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
            },
            "destination": {
              "address": "bing.com",
              "port": "80"
            },
            "monitoring_interval_in_seconds": "60"
          }
        }
        result = self.mgmt_client.connection_monitors.create_or_update(resource_group.name, NETWORK_WATCHER_NAME, CONNECTION_MONITOR_NAME, BODY)
        result = result.result()

        # Create security rule[put]
        BODY = {
          "properties": {
            "protocol": "*",
            "source_address_prefix": "10.0.0.0/8",
            "destination_address_prefix": "11.0.0.0/8",
            "access": "Deny",
            "destination_port_range": "8080",
            "source_port_range": "*",
            "priority": "100",
            "direction": "Outbound"
          }
        }
        result = self.mgmt_client.security_rules.create_or_update(resource_group.name, NETWORK_SECURITY_GROUP_NAME, SECURITY_RULE_NAME, BODY)
        result = result.result()

        # DefaultSecurityRuleGet[get]
        result = self.mgmt_client.default_security_rules.get(resource_group.name, NETWORK_SECURITY_GROUP_NAME, DEFAULT_SECURITY_RULE_NAME)

        # Get network security rule in network security group[get]
        result = self.mgmt_client.security_rules.get(resource_group.name, NETWORK_SECURITY_GROUP_NAME, SECURITY_RULE_NAME)

        # Get connection monitor[get]
        result = self.mgmt_client.connection_monitors.get(resource_group.name, NETWORK_WATCHER_NAME, CONNECTION_MONITOR_NAME)

        # Get packet capture[get]
        result = self.mgmt_client.packet_captures.get(resource_group.name, NETWORK_WATCHER_NAME, PACKET_CAPTURE_NAME)

        # DefaultSecurityRuleList[get]
        result = self.mgmt_client.default_security_rules.list(resource_group.name, NETWORK_SECURITY_GROUP_NAME)

        # Get flow log[get]
        result = self.mgmt_client.flow_logs.get(resource_group.name, NETWORK_WATCHER_NAME, FLOW_LOG_NAME)

        # List network security rules in network security group[get]
        result = self.mgmt_client.security_rules.list(resource_group.name, NETWORK_SECURITY_GROUP_NAME)

        # Get NetworkVirtualAppliance[get]
        result = self.mgmt_client.network_virtual_appliances.get(resource_group.name, NETWORK_VIRTUAL_APPLIANCE_NAME)

        # List connection monitors[get]
        result = self.mgmt_client.connection_monitors.list(resource_group.name, NETWORK_WATCHER_NAME)

        # List packet captures[get]
        result = self.mgmt_client.packet_captures.list(resource_group.name, NETWORK_WATCHER_NAME)

        # Get network security group[get]
        result = self.mgmt_client.network_security_groups.get(resource_group.name, NETWORK_SECURITY_GROUP_NAME)

        # List connection monitors[get]
        result = self.mgmt_client.connection_monitors.list(resource_group.name, NETWORK_WATCHER_NAME)

        # Get network profile[get]
        result = self.mgmt_client.network_profiles.get(resource_group.name, NETWORK_PROFILE_NAME)

        # Get network watcher[get]
        result = self.mgmt_client.network_watchers.get(resource_group.name, NETWORK_WATCHER_NAME)

        # Get network profile with container network interfaces[get]
        result = self.mgmt_client.network_profiles.get(resource_group.name, NETWORK_PROFILE_NAME)

        # List all Network Virtual Appliance for a given resource group[get]
        result = self.mgmt_client.network_virtual_appliances.list_by_resource_group(resource_group.name)

        # List network security groups in resource group[get]
        result = self.mgmt_client.network_security_groups.list(resource_group.name)

        # List network watchers[get]
        result = self.mgmt_client.network_watchers.list(resource_group.name)

        # List resource group network profiles[get]
        result = self.mgmt_client.network_profiles.list(resource_group.name)

        # List all Network Virtual Appliances for a given subscription[get]
        result = self.mgmt_client.network_virtual_appliances.list()

        # List all network security groups[get]
        result = self.mgmt_client.network_security_groups.list_all()

        # List all network watchers[get]
        result = self.mgmt_client.network_watchers.list_all()

        # List all network profiles[get]
        result = self.mgmt_client.network_profiles.list_all()

        # Query connection monitor[post]
        result = self.mgmt_client.connection_monitors.query(resource_group.name, NETWORK_WATCHER_NAME, CONNECTION_MONITOR_NAME)
        result = result.result()

        # Start connection monitor[post]
        result = self.mgmt_client.connection_monitors.start(resource_group.name, NETWORK_WATCHER_NAME, CONNECTION_MONITOR_NAME)
        result = result.result()

        # Stop connection monitor[post]
        result = self.mgmt_client.connection_monitors.stop(resource_group.name, NETWORK_WATCHER_NAME, CONNECTION_MONITOR_NAME)
        result = result.result()

        # Query packet capture status[post]
        result = self.mgmt_client.packet_captures.get_status(resource_group.name, NETWORK_WATCHER_NAME, PACKET_CAPTURE_NAME)
        result = result.result()

        # Update connection monitor tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.connection_monitors.update_tags(resource_group.name, NETWORK_WATCHER_NAME, CONNECTION_MONITOR_NAME, BODY)

        # Stop packet capture[post]
        result = self.mgmt_client.packet_captures.stop(resource_group.name, NETWORK_WATCHER_NAME, PACKET_CAPTURE_NAME)
        result = result.result()

        # Network configuration diagnostic[post]
        BODY = {
          "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + "",
          "profiles": [
            {
              "direction": "Inbound",
              "protocol": "TCP",
              "source": "10.1.0.4",
              "destination": "12.11.12.14",
              "destination_port": "12100"
            }
          ]
        }
        result = self.mgmt_client.network_watchers.get_network_configuration_diagnostic(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Get Azure Reachability Report[post]
        BODY = {
          "provider_location": {
            "country": "United States",
            "state": "washington"
          },
          "providers": [
            "Frontier Communications of America, Inc. - ASN 5650"
          ],
          "azure_locations": [
            "West US"
          ],
          "start_time": "2017-09-07T00:00:00Z",
          "end_time": "2017-09-10T00:00:00Z"
        }
        result = self.mgmt_client.network_watchers.get_azure_reachability_report(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Get troubleshoot result[post]
        BODY = {
          "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
        }
        result = self.mgmt_client.network_watchers.get_troubleshooting_result(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Get Available Providers List[post]
        BODY = {
          "azure_locations": [
            "West US"
          ],
          "country": "United States",
          "state": "washington",
          "city": "seattle"
        }
        result = self.mgmt_client.network_watchers.list_available_providers(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Update NetworkVirtualAppliance[patch]
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          }
        }
        result = self.mgmt_client.network_virtual_appliances.update_tags(resource_group.name, NETWORK_VIRTUAL_APPLIANCE_NAME, BODY)

        # Get flow log status[post]
        BODY = {
          "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/networkSecurityGroups/" + NETWORK_SECURITY_GROUP_NAME + ""
        }
        result = self.mgmt_client.network_watchers.get_flow_log_status(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Get security group view[post]
        BODY = {
          "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
        }
        result = self.mgmt_client.network_watchers.get_vmsecurity_rules(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Check connectivity[post]
        BODY = {
          "source": {
            "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + ""
          },
          "destination": {
            "address": "192.168.100.4",
            "port": "3389"
          },
          "preferred_ipversion": "IPv4"
        }
        result = self.mgmt_client.network_watchers.check_connectivity(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Configure flow log[post]
        BODY = {
          "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/networkSecurityGroups/" + NETWORK_SECURITY_GROUP_NAME + "",
          "properties": {
            "storage_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
            "enabled": True
          }
        }
        result = self.mgmt_client.network_watchers.set_flow_log_configuration(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Update network security group tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.network_security_groups.update_tags(resource_group.name, NETWORK_SECURITY_GROUP_NAME, BODY)

        # Get troubleshooting[post]
        BODY = {
          "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + "",
          "properties": {
            "storage_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
            "storage_path": "https://st1.blob.core.windows.net/cn1"
          }
        }
        result = self.mgmt_client.network_watchers.get_troubleshooting(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Ip flow verify[post]
        BODY = {
          "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + "",
          "direction": "Outbound",
          "protocol": "TCP",
          "local_port": "80",
          "remote_port": "80",
          "local_ip_address": "10.2.0.4",
          "remote_ip_address": "121.10.1.1"
        }
        result = self.mgmt_client.network_watchers.verify_ipflow(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Get Topology[post]
        BODY = {
          "target_resource_group_name": "rg2"
        }
        result = self.mgmt_client.network_watchers.get_topology(resource_group.name, NETWORK_WATCHER_NAME, BODY)

        # Get next hop[post]
        BODY = {
          "target_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachines/" + VIRTUAL_MACHINE_NAME + "",
          "source_ip_address": "10.0.0.5",
          "destination_ip_address": "10.0.0.10",
          "target_nic_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/networkInterfaces/" + NETWORK_INTERFACE_NAME + ""
        }
        result = self.mgmt_client.network_watchers.get_next_hop(resource_group.name, NETWORK_WATCHER_NAME, BODY)
        result = result.result()

        # Update network profile tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.network_profiles.update_tags(resource_group.name, NETWORK_PROFILE_NAME, BODY)

        # Update network watcher tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.network_watchers.update_tags(resource_group.name, NETWORK_WATCHER_NAME, BODY)

        # Delete network security rule from network security group[delete]
        result = self.mgmt_client.security_rules.delete(resource_group.name, NETWORK_SECURITY_GROUP_NAME, SECURITY_RULE_NAME)
        result = result.result()

        # Delete connection monitor[delete]
        result = self.mgmt_client.connection_monitors.delete(resource_group.name, NETWORK_WATCHER_NAME, CONNECTION_MONITOR_NAME)
        result = result.result()

        # Delete packet capture[delete]
        result = self.mgmt_client.packet_captures.delete(resource_group.name, NETWORK_WATCHER_NAME, PACKET_CAPTURE_NAME)
        result = result.result()

        # Delete flow log[delete]
        result = self.mgmt_client.flow_logs.delete(resource_group.name, NETWORK_WATCHER_NAME, FLOW_LOG_NAME)
        result = result.result()

        # Delete NetworkVirtualAppliance[delete]
        result = self.mgmt_client.network_virtual_appliances.delete(resource_group.name, NETWORK_VIRTUAL_APPLIANCE_NAME)
        result = result.result()

        # Delete network security group[delete]
        result = self.mgmt_client.network_security_groups.delete(resource_group.name, NETWORK_SECURITY_GROUP_NAME)
        result = result.result()

        # Delete network profile[delete]
        result = self.mgmt_client.network_profiles.delete(resource_group.name, NETWORK_PROFILE_NAME)
        result = result.result()

        # Delete network watcher[delete]
        result = self.mgmt_client.network_watchers.delete(resource_group.name, NETWORK_WATCHER_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
