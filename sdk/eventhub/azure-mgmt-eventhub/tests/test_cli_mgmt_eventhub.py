# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 43
# Methods Covered : 43
# Examples Total  : 44
# Examples Tested : 44
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.eventhub
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtEventHubTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtEventHubTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.eventhub.EventHubManagementClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_eventhub(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # NamespaceCreate[put]
        BODY = {
          "sku": {
            "name": "Standard",
            "tier": "Standard"
          },
          "location": "South Central US",
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.namespaces.create_or_update(resource_group.name, NAMESPACE_NAME, BODY)
        result = result.result()

        # EventHubCreate[put]
        BODY = {
          "properties": {
            "message_retention_in_days": "4",
            "partition_count": "4",
            "status": "Active",
            "capture_description": {
              "enabled": True,
              "encoding": "Avro",
              "interval_in_seconds": "120",
              "size_limit_in_bytes": "10485763",
              "destination": {
                "name": "EventHubArchive.AzureBlockBlob",
                "properties": {
                  "storage_account_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ClassicStorage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
                  "blob_container": "container",
                  "archive_name_format": "{Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}"
                }
              }
            }
          }
        }
        result = self.mgmt_client.event_hubs.create_or_update(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, BODY)

        # NameSpaceNetworkRuleSetCreate[put]
        BODY = {
          "properties": {
            "default_action": "Deny",
            "virtual_network_rules": [
              {
                "subnet": {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                },
                "ignore_missing_vnet_service_endpoint": True
              },
              {
                "subnet": {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                },
                "ignore_missing_vnet_service_endpoint": False
              },
              {
                "subnet": {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                },
                "ignore_missing_vnet_service_endpoint": False
              }
            ],
            "ip_rules": [
              {
                "ip_mask": "1.1.1.1",
                "action": "Allow"
              },
              {
                "ip_mask": "1.1.1.2",
                "action": "Allow"
              },
              {
                "ip_mask": "1.1.1.3",
                "action": "Allow"
              },
              {
                "ip_mask": "1.1.1.4",
                "action": "Allow"
              },
              {
                "ip_mask": "1.1.1.5",
                "action": "Allow"
              }
            ]
          }
        }
        result = self.mgmt_client.namespaces.create_or_update_network_rule_set(resource_group.name, NAMESPACE_NAME, NETWORK_RULE_SET_NAME, BODY)

        # NameSpaceAuthorizationRuleCreate[put]
        BODY = {
          "properties": {
            "rights": [
              "Listen",
              "Send"
            ]
          }
        }
        result = self.mgmt_client.namespaces.create_or_update_authorization_rule(resource_group.name, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, BODY)

        # EHAliasCreate[put]
        BODY = {
          "properties": {
            "partner_namespace": "sdk-Namespace-37"
          }
        }
        result = self.mgmt_client.disaster_recovery_configs.create_or_update(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)

        # ConsumerGroupCreate[put]
        BODY = {
          "properties": {
            "user_metadata": "New consumergroup"
          }
        }
        result = self.mgmt_client.consumer_groups.create_or_update(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, CONSUMERGROUP_NAME, BODY)

        # EventHubAuthorizationRuleCreate[put]
        BODY = {
          "properties": {
            "rights": [
              "Listen",
              "Send"
            ]
          }
        }
        result = self.mgmt_client.event_hubs.create_or_update_authorization_rule(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, AUTHORIZATION_RULE_NAME, BODY)

        # NameSpaceAuthorizationRuleGet[get]
        result = self.mgmt_client.disaster_recovery_configs.get_authorization_rule(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, AUTHORIZATION_RULE_NAME)

        # ListAuthorizationRules[get]
        result = self.mgmt_client.disaster_recovery_configs.list_authorization_rules(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME)

        # EventHubAuthorizationRuleGet[get]
        result = self.mgmt_client.event_hubs.get_authorization_rule(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, AUTHORIZATION_RULE_NAME)

        # ConsumerGroupGet[get]
        result = self.mgmt_client.consumer_groups.get(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, CONSUMERGROUP_NAME)

        # EHAliasGet[get]
        result = self.mgmt_client.disaster_recovery_configs.get(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME)

        # EventHubAuthorizationRuleListAll[get]
        result = self.mgmt_client.event_hubs.list_authorization_rules(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME)

        # NameSpaceAuthorizationRuleGet[get]
        result = self.mgmt_client.disaster_recovery_configs.get_authorization_rule(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, AUTHORIZATION_RULE_NAME)

        # ConsumerGroupsListAll[get]
        result = self.mgmt_client.consumer_groups.list_by_event_hub(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME)

        # NameSpaceNetworkRuleSetGet[get]
        result = self.mgmt_client.namespaces.get_network_rule_set(resource_group.name, NAMESPACE_NAME, NETWORK_RULE_SET_NAME)

        # EventHubGet[get]
        result = self.mgmt_client.event_hubs.get(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME)

        # EHAliasList[get]
        result = self.mgmt_client.disaster_recovery_configs.list(resource_group.name, NAMESPACE_NAME)

        # ListAuthorizationRules[get]
        result = self.mgmt_client.disaster_recovery_configs.list_authorization_rules(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME)

        # NameSpaceNetworkRuleSetList[get]
        result = self.mgmt_client.namespaces.list_network_rule_sets(resource_group.name, NAMESPACE_NAME)

        # GetNamespaceMessagingPlan[get]
        result = self.mgmt_client.namespaces.get_messaging_plan(resource_group.name, NAMESPACE_NAME)

        # EventHubsListAll[get]
        result = self.mgmt_client.event_hubs.list_by_namespace(resource_group.name, NAMESPACE_NAME)

        # NameSpaceGet[get]
        result = self.mgmt_client.namespaces.get(resource_group.name, NAMESPACE_NAME)

        # NamespaceListByResourceGroup[get]
        result = self.mgmt_client.namespaces.list_by_resource_group(resource_group.name)

        # RegionsListBySkuStandard[get]
        result = self.mgmt_client.regions.list_by_sku(SKU_NAME)

        # RegionsListBySkuBasic[get]
        result = self.mgmt_client.regions.list_by_sku(SKU_NAME)

        # NamespacesListBySubscription[get]
        result = self.mgmt_client.namespaces.list()

        # EHOperations_List[get]
        result = self.mgmt_client.operations.list()

        # NameSpaceAuthorizationRuleListKey[post]
        result = self.mgmt_client.disaster_recovery_configs.list_keys(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, AUTHORIZATION_RULE_NAME)

        # EventHubAuthorizationRuleRegenerateKey[post]
        BODY = {
          "key_type": "PrimaryKey"
        }
        result = self.mgmt_client.event_hubs.regenerate_keys(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, AUTHORIZATION_RULE_NAME, BODY)

        # EventHubAuthorizationRuleListKey[post]
        result = self.mgmt_client.event_hubs.list_keys(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, AUTHORIZATION_RULE_NAME)

        # EHAliasBreakPairing[post]
        result = self.mgmt_client.disaster_recovery_configs.break_pairing(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME)

        # EHAliasFailOver[post]
        result = self.mgmt_client.disaster_recovery_configs.fail_over(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME)

        # NameSpaceAuthorizationRuleRegenerateKey[post]
        BODY = {
          "key_type": "PrimaryKey"
        }
        result = self.mgmt_client.namespaces.regenerate_keys(resource_group.name, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, BODY)

        # NamespacesCheckNameAvailability[post]
        BODY = {
          "name": "sdk-DisasterRecovery-9474"
        }
        result = self.mgmt_client.disaster_recovery_configs.check_name_availability(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)

        # NameSpaceAuthorizationRuleListKey[post]
        result = self.mgmt_client.disaster_recovery_configs.list_keys(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, AUTHORIZATION_RULE_NAME)

        # NamespacesUpdate[patch]
        BODY = {
          "location": "South Central US",
          "tags": {
            "tag3": "value3",
            "tag4": "value4"
          }
        }
        result = self.mgmt_client.namespaces.update(resource_group.name, NAMESPACE_NAME, BODY)

        # NamespacesCheckNameAvailability[post]
        BODY = {
          "name": "sdk-DisasterRecovery-9474"
        }
        result = self.mgmt_client.disaster_recovery_configs.check_name_availability(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)

        # EventHubAuthorizationRuleDelete[delete]
        result = self.mgmt_client.event_hubs.delete_authorization_rule(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, AUTHORIZATION_RULE_NAME)

        # ConsumerGroupDelete[delete]
        result = self.mgmt_client.consumer_groups.delete(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME, CONSUMERGROUP_NAME)

        # EHAliasDelete[delete]
        result = self.mgmt_client.disaster_recovery_configs.delete(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME)

        # NameSpaceAuthorizationRuleDelete[delete]
        result = self.mgmt_client.namespaces.delete_authorization_rule(resource_group.name, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME)

        # EventHubDelete[delete]
        result = self.mgmt_client.event_hubs.delete(resource_group.name, NAMESPACE_NAME, EVENTHUB_NAME)

        # NameSpaceDelete[delete]
        result = self.mgmt_client.namespaces.delete(resource_group.name, NAMESPACE_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
