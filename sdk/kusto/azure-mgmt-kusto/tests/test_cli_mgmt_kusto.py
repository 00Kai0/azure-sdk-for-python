# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 48
# Methods Covered : 48
# Examples Total  : 48
# Examples Tested : 48
# Coverage %      : 100
# ----------------------

# current methods coverage:
#   attached_database_configurations: 1/4
#   cluster_principal_assignments: 2/5
#   clusters: 16/17
#   data_connections: 6/7
#   database_principal_assignments: 2/5
#   databases: 8/9
#   operations: 1/1

import unittest

import azure.mgmt.kusto as az_kusto
from devtools_testutils import AzureMgmtTestCase, RandomNameResourceGroupPreparer

AZURE_LOCATION = 'westus'

class MgmtKustoTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtKustoTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            az_kusto.KustoManagementClient
        )
        if self.is_live:
            import azure.mgmt.eventhub
            import azure.mgmt.storage
            self.storage_client = self.create_mgmt_client(
                azure.mgmt.storage.StorageManagementClient
            )
            self.eventhub_client = self.create_mgmt_client(
                azure.mgmt.eventhub.EventHubManagementClient
            )

    def create_eventhub(self, group_name, azure_location, storage_account_name, namespace_name, eventhub_name, consumergroup_name):
        import azure.mgmt.storage
        import azure.mgmt.storage.models
        params_create = azure.mgmt.storage.models.StorageAccountCreateParameters(
            sku=azure.mgmt.storage.models.Sku(name=azure.mgmt.storage.models.SkuName.standard_lrs),
            kind=azure.mgmt.storage.models.Kind.storage,
            location=azure_location
        )
        result_create = self.storage_client.storage_accounts.begin_create(
            group_name,
            storage_account_name,
            params_create,
        )
        result_create.result()

        SUBSCRIPTION_ID = self.settings.SUBSCRIPTION_ID

        # NamespaceCreate[put]
        BODY = {
          "sku": {
            "name": "Standard",
            "tier": "Standard"
          },
          "location": azure_location,
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.eventhub_client.namespaces.begin_create_or_update(group_name, namespace_name, BODY)
        result = result.result()

        # EventHubCreate[put]
        BODY = {
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
              "storage_account_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + group_name + "/providers/Microsoft.Storage/storageAccounts/" + storage_account_name + "",
              "blob_container": "container",
              "archive_name_format": "{Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}"
            }
          }
        }
        result = self.eventhub_client.event_hubs.create_or_update(group_name, namespace_name, eventhub_name, BODY)

        # ConsumerGroupCreate[put]
        BODY = {
          "user_metadata": "New consumergroup"
        }
        result = self.eventhub_client.consumer_groups.create_or_update(group_name, namespace_name, eventhub_name, consumergroup_name, BODY)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    def test_kusto(self, resource_group):

        UNIQUE = resource_group.name[-4:]
        SUBSCRIPTION_ID = self.settings.SUBSCRIPTION_ID
        TENANT_ID = self.settings.TENANT_ID
        RESOURCE_GROUP = resource_group.name
        CLUSTER_NAME = "myCluster" + UNIQUE
        PRINCIPAL_ASSIGNMENT_NAME = "myPrincipalAssignment" + UNIQUE
        DATABASE_NAME = "myDatabase" + UNIQUE
        ATTACHED_DATABASE_CONFIGURATION_NAME = "myAttachedDatabaseConfiguration"
        DATA_CONNECTION_NAME = "myDataConnection" + UNIQUE
        STORAGE_ACCOUNT_NAME = "myaccount" + UNIQUE
        NAMESPACE_NAME = "mynamespace" + UNIQUE
        EVENTHUB_NAME = "myEventhub" + UNIQUE
        CONSUMERGROUP_NAME = "testConsumerGroup1"

        if self.is_live:
            self.create_eventhub(RESOURCE_GROUP, AZURE_LOCATION, STORAGE_ACCOUNT_NAME, NAMESPACE_NAME, EVENTHUB_NAME, CONSUMERGROUP_NAME)
#--------------------------------------------------------------------------
        # /Clusters/put/KustoClustersCreateOrUpdate[put]
#--------------------------------------------------------------------------
        BODY = {
          "location": AZURE_LOCATION,
          "sku": {
            "name": "Standard_L8s",
            "capacity": "2",
            "tier": "Standard"
          },
          "identity": {
            "type": "SystemAssigned"
          },
          "enable_streaming_ingest": True,
        #   "enable_purge": True,
        #   "key_vault_properties": {
        #     "key_vault_uri": "https://dummy.keyvault.com",
        #     "key_name": "keyName",
        #     "key_version": "keyVersion"
        #   }
        }
        result = self.mgmt_client.clusters.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /Databases/put/KustoDatabasesCreateOrUpdate[put]
#--------------------------------------------------------------------------
        BODY = {
          "location": AZURE_LOCATION,
          "soft_delete_period": "P1D",
          "kind": "ReadWrite"
        }
        result = self.mgmt_client.databases.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/put/KustoClusterPrincipalAssignmentsCreateOrUpdate[put]
#--------------------------------------------------------------------------
        # BODY = {
        # #   "role": "Admin",
        #   "role": "AllDatabasesAdmin",
        #   "principal_id": "87654321-1234-1234-1234-123456789123",
        #   "principal_type": "App",
        #   "tenant_id": TENANT_ID
        # }
        # result = self.mgmt_client.cluster_principal_assignments.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME, parameters=BODY)
        # result = result.result()
#--------------------------------------------------------------------------
        # /DataConnections/put/KustoDataConnectionsCreateOrUpdate[put]
#--------------------------------------------------------------------------
        BODY = {
          "location": AZURE_LOCATION,
          "kind": "EventHub",
          "event_hub_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME,
          "consumer_group": CONSUMERGROUP_NAME
        }
        result = self.mgmt_client.data_connections.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=DATA_CONNECTION_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /AttachedDatabaseConfigurations/put/AttachedDatabaseConfigurationsCreateOrUpdate[put]
#--------------------------------------------------------------------------
        # BODY = {
        #   "location": AZURE_LOCATION,
        #   "cluster_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Kusto/Clusters/" + CLUSTER_NAME,
        #   "database_name": "db1",
        #   "database_name": DATABASE_NAME,
        #   "default_principals_modification_kind": "Union"
        # }
        # result = self.mgmt_client.attached_database_configurations.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, attached_database_configuration_name=ATTACHED_DATABASE_CONFIGURATION_NAME, parameters=BODY)
        # result = result.result()
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/put/KustoDatabasePrincipalAssignmentsCreateOrUpdate[put]
#--------------------------------------------------------------------------
        # BODY = {
        #   "role": "AllDatabasesAdmin",
        #   "principal_id": "87654321-1234-1234-1234-123456789123",
        #   "principal_id": self.settings.CLIENT_ID,
        #   "principal_type": "App",
        #   "tenant_id": self.settings.TENANT_ID
        # }
        # result = self.mgmt_client.database_principal_assignments.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME, parameters=BODY)
        # result = result.result()
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/get/KustoDatabasePrincipalAssignmentsGet[get]
#--------------------------------------------------------------------------
        # result = self.mgmt_client.database_principal_assignments.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME)
#--------------------------------------------------------------------------
        # /AttachedDatabaseConfigurations/get/AttachedDatabaseConfigurationsGet[get]
#--------------------------------------------------------------------------
        # result = self.mgmt_client.attached_database_configurations.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, attached_database_configuration_name=ATTACHED_DATABASE_CONFIGURATION_NAME)
#--------------------------------------------------------------------------
        # /DataConnections/get/KustoDataConnectionsGet[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.data_connections.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=DATA_CONNECTION_NAME)
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/get/KustoClusterPrincipalAssignmentsGet[get]
#--------------------------------------------------------------------------
        # result = self.mgmt_client.cluster_principal_assignments.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME)
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/get/KustoPrincipalAssignmentsList[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.database_principal_assignments.list(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME)
#--------------------------------------------------------------------------
        # /DataConnections/get/KustoDatabasesListByCluster[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.data_connections.list_by_database(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME)
#--------------------------------------------------------------------------
        # /AttachedDatabaseConfigurations/get/KustoAttachedDatabaseConfigurationsListByCluster[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.attached_database_configurations.list_by_cluster(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
#--------------------------------------------------------------------------
        # /Databases/get/KustoDatabasesGet[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.databases.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME)
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/get/KustoPrincipalAssignmentsList[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.cluster_principal_assignments.list(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
#--------------------------------------------------------------------------
        # /Databases/get/KustoDatabasesListByCluster[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.databases.list_by_cluster(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
#--------------------------------------------------------------------------
        # /Clusters/get/KustoClustersListResourceSkus[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.list_skus_by_resource(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
#--------------------------------------------------------------------------
        # /Clusters/get/KustoClustersGet[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
#--------------------------------------------------------------------------
        # /Clusters/get/KustoClustersListByResourceGroup[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.list_by_resource_group(resource_group_name=RESOURCE_GROUP)
#--------------------------------------------------------------------------
        # /Clusters/get/KustoClustersList[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.list()
#--------------------------------------------------------------------------
        # /Clusters/get/KustoClustersListSkus[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.list_skus()
#--------------------------------------------------------------------------
        # /Operations/get/KustoOperationsList[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.operations.list()
#--------------------------------------------------------------------------
        # /DataConnections/patch/KustoDataConnectionsUpdate[patch]
#--------------------------------------------------------------------------
        BODY = {
          "location": AZURE_LOCATION,
          "kind": "EventHub",
          "event_hub_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME,
          "consumer_group": "testConsumerGroup1"
        }
        result = self.mgmt_client.data_connections.begin_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=DATA_CONNECTION_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/post/KustoDatabaseCheckNameAvailability[post]
#--------------------------------------------------------------------------
        BODY = {
          "name": "kustoprincipal1",
          "type": "Microsoft.Kusto/clusters/databases/principalAssignments"
        }
        result = self.mgmt_client.database_principal_assignments.check_name_availability(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, principal_assignment_name=BODY)
#--------------------------------------------------------------------------
        # /DataConnections/post/KustoDataConnectionValidation[post]
#--------------------------------------------------------------------------
        # BODY = {
        #   "data_connection_name": "DataConnections8",
        #   "properties": {
        #     "kind": "EventHub",
        #     "event_hub_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME,
        #     "consumer_group": "testConsumerGroup1"
        #   }
        # }
        # result = self.mgmt_client.data_connections.data_connection_validation(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, parameters=BODY)
#--------------------------------------------------------------------------
        # /DataConnections/post/KustoDataConnectionsCheckNameAvailability[post]
#--------------------------------------------------------------------------
        BODY = {
          "name": "DataConnections8",
          "type": "Microsoft.Kusto/clusters/databases/dataConnections"
        }
        result = self.mgmt_client.data_connections.check_name_availability(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=BODY)
#--------------------------------------------------------------------------
        # /Databases/post/KustoDatabaseRemovePrincipals[post]
#--------------------------------------------------------------------------
        BODY = {
          "value": [
            {
              "name": "Some User",
              "role": "Admin",
              "type": "User",
              "fqn": "aaduser=some_guid",
              "email": "user@microsoft.com",
              "app_id": ""
            },
            {
              "name": "Kusto",
              "role": "Viewer",
              "type": "Group",
              "fqn": "aadgroup=some_guid",
              "email": "kusto@microsoft.com",
              "app_id": ""
            },
            {
              "name": "SomeApp",
              "role": "Admin",
              "type": "App",
              "fqn": "aadapp=some_guid_app_id",
              "email": "",
              "app_id": "some_guid_app_id"
            }
          ]
        }
        result = self.mgmt_client.databases.remove_principals(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, database_principals_to_remove=BODY)
#--------------------------------------------------------------------------
        # /Databases/post/KustoDatabaseListPrincipals[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.databases.list_principals(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME)
#--------------------------------------------------------------------------
        # /Databases/post/KustoDatabaseAddPrincipals[post]
#--------------------------------------------------------------------------
        # BODY = {
        #   "value": [
        #     {
        #       "name": "Some User",
        #       "role": "Admin",
        #       "type": "User",
        #       "email": "user@microsoft.com",
        #       "app_id": self.settings.CLIENT_ID
        #     },
        #     {
        #       "name": "Kusto",
        #       "role": "Viewer",
        #       "type": "Group",
        #       "fqn": "aadgroup=some_guid",
        #       "email": "kusto@microsoft.com",
        #       "app_id": ""
        #     },
        #     {
        #       "name": "SomeApp",
        #       "role": "Admin",
        #       "type": "App",
        #       "fqn": "aadapp=some_guid_app_id",
        #       "email": "",
        #       "app_id": "some_guid_app_id"
        #     }
        #   ]
        # }
        # result = self.mgmt_client.databases.add_principals(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, database_principals_to_add=BODY)
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/post/KustoClusterPrincipalAssignmentsCheckNameAvailability[post]
#--------------------------------------------------------------------------
        BODY = {
          "name": "kustoprincipal1",
          "type": "Microsoft.Kusto/clusters/principalAssignments"
        }
        result = self.mgmt_client.cluster_principal_assignments.check_name_availability(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, principal_assignment_name=BODY)
#--------------------------------------------------------------------------
        # /Databases/patch/KustoDatabasesUpdate[patch]
#--------------------------------------------------------------------------
        BODY = {
          "soft_delete_period": "P1D",
          "kind": "ReadWrite"
        }
        result = self.mgmt_client.databases.begin_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterRemoveLanguageExtensions[post]
#--------------------------------------------------------------------------
        BODY = {
          "value": [
            {
              "language_extension_name": "PYTHON"
            },
            {
              "language_extension_name": "R"
            }
          ]
        }
        result = self.mgmt_client.clusters.begin_remove_language_extensions(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, language_extensions_to_remove=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterDetachFollowerDatabases[post]
#--------------------------------------------------------------------------
        # BODY = {
        #   "cluster_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Kusto/clusters/" + CLUSTER_NAME,
        #   "attached_database_configuration_name": "myAttachedDatabaseConfiguration"
        # }
        # result = self.mgmt_client.clusters.begin_detach_follower_databases(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, follower_database_to_remove=BODY)
        # result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterDiagnoseVirtualNetwork[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.begin_diagnose_virtual_network(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterListLanguageExtensions[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.list_language_extensions(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterAddLanguageExtensions[post]
#--------------------------------------------------------------------------
        BODY = {
          "value": [
            {
              "language_extension_name": "PYTHON"
            },
            {
              "language_extension_name": "R"
            }
          ]
        }
        result = self.mgmt_client.clusters.begin_add_language_extensions(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, language_extensions_to_add=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterListFollowerDatabases[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.list_follower_databases(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
#--------------------------------------------------------------------------
        # /Databases/post/KustoDatabaseCheckNameAvailability[post]
#--------------------------------------------------------------------------
        BODY = {
          "name": "kustoresourcename1",
          "type": "Microsoft.Kusto/clusters/databases"
        }
        result = self.mgmt_client.databases.check_name_availability(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, resource_name=BODY)
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClustersStart[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.begin_start(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/patch/KustoClustersUpdate[patch]
#--------------------------------------------------------------------------
        BODY = {
          "location": AZURE_LOCATION
        }
        result = self.mgmt_client.clusters.begin_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClustersStop[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.begin_stop(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClustersCheckNameAvailability[post]
#--------------------------------------------------------------------------
        # BODY = {
        #   "name": "kuskusprod",
        #   "type": "Microsoft.Kusto/clusters"
        # }
        # result = self.mgmt_client.clusters.check_name_availability(location=AZURE_LOCATION, cluster_name=BODY)
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/delete/KustoDatabasePrincipalAssignmentsDelete[delete]
#--------------------------------------------------------------------------
        # result = self.mgmt_client.database_principal_assignments.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME)
        # result = result.result()
#--------------------------------------------------------------------------
        # /AttachedDatabaseConfigurations/delete/AttachedDatabaseConfigurationsDelete[delete]
#--------------------------------------------------------------------------
        # result = self.mgmt_client.attached_database_configurations.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, attached_database_configuration_name=ATTACHED_DATABASE_CONFIGURATION_NAME)
        # result = result.result()
#--------------------------------------------------------------------------
        # /DataConnections/delete/KustoDataConnectionsDelete[delete]
#--------------------------------------------------------------------------
        result = self.mgmt_client.data_connections.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=DATA_CONNECTION_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/delete/KustoClusterPrincipalAssignmentsDelete[delete]
#--------------------------------------------------------------------------
        # result = self.mgmt_client.cluster_principal_assignments.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME)
        # result = result.result()
#--------------------------------------------------------------------------
        # /Databases/delete/KustoDatabasesDelete[delete]
#--------------------------------------------------------------------------
        result = self.mgmt_client.databases.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/delete/KustoClustersDelete[delete]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
