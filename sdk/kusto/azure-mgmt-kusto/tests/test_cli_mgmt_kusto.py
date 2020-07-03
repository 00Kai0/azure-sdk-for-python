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

import unittest

import azure.mgmt.kusto
from devtools_testutils import AzureMgmtTestCase, RandomNameResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtKustoTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtKustoTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.kusto.KustoManagementClient
        )
    
    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    def test_kusto(self, resource_group):

        UNIQUE = resource_group.name[-4:]
        SUBSCRIPTION_ID = self.settings.SUBSCRIPTION_ID
        TENANT_ID = self.settings.TENANT_ID
        RESOURCE_GROUP = resource_group.name
        RESOURCE_GROUP = "myResourceGroup"
        CLUSTER_NAME = "myCluster" + UNIQUE
        PRINCIPAL_ASSIGNMENT_NAME = "myPrincipalAssignment" + UNIQUE
        DATABASE_NAME = "myDatabase" + UNIQUE
        ATTACHED_DATABASE_CONFIGURATION_NAME = "myAttachedDatabaseConfiguration"
        DATA_CONNECTION_NAME = "myDataConnection" + UNIQUE
        NAMESPACE_NAME = "my"
        EVENTHUB_NAME = "myEventhub"
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
        PROPERTIES = {
          "soft_delete_period": "P1D"
        }
        result = self.mgmt_client.databases.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, location=AZURE_LOCATION, properties=PROPERTIES, kind="ReadWrite")
        result = result.result()
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/put/KustoClusterPrincipalAssignmentsCreateOrUpdate[put]
#--------------------------------------------------------------------------
        BODY = {
          "role": "Admin",
          "principal_id": "87654321-1234-1234-1234-123456789123",
          "principal_type": "App",
          "tenant_id": TENANT_ID
        }
        result = self.mgmt_client.cluster_principal_assignments.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /DataConnections/put/KustoDataConnectionsCreateOrUpdate[put]
#--------------------------------------------------------------------------
        PROPERTIES = {
          "event_hub_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME,
          "consumer_group": "testConsumerGroup1"
        }
        result = self.mgmt_client.data_connections.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=DATA_CONNECTION_NAME, location=AZURE_LOCATION, kind="EventHub", properties=PROPERTIES)
        result = result.result()
#--------------------------------------------------------------------------
        # /AttachedDatabaseConfigurations/put/AttachedDatabaseConfigurationsCreateOrUpdate[put]
#--------------------------------------------------------------------------
        BODY = {
          "location": AZURE_LOCATION,
          "cluster_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Kusto/Clusters/" + CLUSTER_NAME,
          "database_name": "db1",
          "default_principals_modification_kind": "Union"
        }
        result = self.mgmt_client.attached_database_configurations.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, attached_database_configuration_name=ATTACHED_DATABASE_CONFIGURATION_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/put/KustoDatabasePrincipalAssignmentsCreateOrUpdate[put]
#--------------------------------------------------------------------------
        BODY = {
          "role": "Admin",
          "principal_id": "87654321-1234-1234-1234-123456789123",
          "principal_type": "App",
          "tenant_id": TENANT_ID
        }
        result = self.mgmt_client.database_principal_assignments.begin_create_or_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME, parameters=BODY)
        result = result.result()
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/get/KustoDatabasePrincipalAssignmentsGet[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.database_principal_assignments.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME)
#--------------------------------------------------------------------------
        # /AttachedDatabaseConfigurations/get/AttachedDatabaseConfigurationsGet[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.attached_database_configurations.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, attached_database_configuration_name=ATTACHED_DATABASE_CONFIGURATION_NAME)
#--------------------------------------------------------------------------
        # /DataConnections/get/KustoDataConnectionsGet[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.data_connections.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=DATA_CONNECTION_NAME)
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/get/KustoClusterPrincipalAssignmentsGet[get]
#--------------------------------------------------------------------------
        result = self.mgmt_client.cluster_principal_assignments.get(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME)
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
        PROPERTIES = {
          "event_hub_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME,
          "consumer_group": "testConsumerGroup1"
        }
        result = self.mgmt_client.data_connections.begin_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=DATA_CONNECTION_NAME, location=AZURE_LOCATION, kind="EventHub", properties=PROPERTIES)
        result = result.result()
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/post/KustoDatabaseCheckNameAvailability[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.database_principal_assignments.check_name_availability(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, name="kustoprincipal1", type="Microsoft.Kusto/clusters/databases/principalAssignments")
#--------------------------------------------------------------------------
        # /DataConnections/post/KustoDataConnectionValidation[post]
#--------------------------------------------------------------------------
        PROPERTIES = {
          "kind": "EventHub",
          "event_hub_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME,
          "consumer_group": "testConsumerGroup1"
        }
        result = self.mgmt_client.data_connections.data_connection_validation_method(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name="DataConnections8", properties=PROPERTIES)
#--------------------------------------------------------------------------
        # /DataConnections/post/KustoDataConnectionsCheckNameAvailability[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.data_connections.check_name_availability(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, name="DataConnections8", type="Microsoft.Kusto/clusters/databases/dataConnections")
#--------------------------------------------------------------------------
        # /Databases/post/KustoDatabaseRemovePrincipals[post]
#--------------------------------------------------------------------------
        [
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
        result = self.mgmt_client.databases.remove_principals(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, value=VALUE)
#--------------------------------------------------------------------------
        # /Databases/post/KustoDatabaseListPrincipals[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.databases.list_principals(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME)
#--------------------------------------------------------------------------
        # /Databases/post/KustoDatabaseAddPrincipals[post]
#--------------------------------------------------------------------------
        [
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
        result = self.mgmt_client.databases.add_principals(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, value=VALUE)
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/post/KustoClusterPrincipalAssignmentsCheckNameAvailability[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.cluster_principal_assignments.check_name_availability(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, name="kustoprincipal1", type="Microsoft.Kusto/clusters/principalAssignments")
#--------------------------------------------------------------------------
        # /Databases/patch/KustoDatabasesUpdate[patch]
#--------------------------------------------------------------------------
        PROPERTIES = {
          "soft_delete_period": "P1D"
        }
        result = self.mgmt_client.databases.begin_update(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, properties=PROPERTIES, kind="ReadWrite")
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterRemoveLanguageExtensions[post]
#--------------------------------------------------------------------------
        [
          {
            "language_extension_name": "PYTHON"
          },
          {
            "language_extension_name": "R"
          }
        ]
        result = self.mgmt_client.clusters.begin_remove_language_extensions(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, value=VALUE)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterDetachFollowerDatabases[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.begin_detach_follower_databases(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, cluster_resource_id="/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Kusto/clusters/" + CLUSTER_NAME, attached_database_configuration_name="myAttachedDatabaseConfiguration")
        result = result.result()
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
        [
          {
            "language_extension_name": "PYTHON"
          },
          {
            "language_extension_name": "R"
          }
        ]
        result = self.mgmt_client.clusters.begin_add_language_extensions(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, value=VALUE)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClusterListFollowerDatabases[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.list_follower_databases(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
#--------------------------------------------------------------------------
        # /Databases/post/KustoDatabaseCheckNameAvailability[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.databases.check_name_availability(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, name="kustoresourcename1", type="Microsoft.Kusto/clusters/databases")
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClustersStart[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.begin_start(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /Clusters/post/KustoClustersStop[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.begin_stop(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME)
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
        # /Clusters/post/KustoClustersCheckNameAvailability[post]
#--------------------------------------------------------------------------
        result = self.mgmt_client.clusters.check_name_availability(azure_location=AZURE_LOCATION, name="kuskusprod", type="Microsoft.Kusto/clusters")
#--------------------------------------------------------------------------
        # /DatabasePrincipalAssignments/delete/KustoDatabasePrincipalAssignmentsDelete[delete]
#--------------------------------------------------------------------------
        result = self.mgmt_client.database_principal_assignments.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /AttachedDatabaseConfigurations/delete/AttachedDatabaseConfigurationsDelete[delete]
#--------------------------------------------------------------------------
        result = self.mgmt_client.attached_database_configurations.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, attached_database_configuration_name=ATTACHED_DATABASE_CONFIGURATION_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /DataConnections/delete/KustoDataConnectionsDelete[delete]
#--------------------------------------------------------------------------
        result = self.mgmt_client.data_connections.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, database_name=DATABASE_NAME, data_connection_name=DATA_CONNECTION_NAME)
        result = result.result()
#--------------------------------------------------------------------------
        # /ClusterPrincipalAssignments/delete/KustoClusterPrincipalAssignmentsDelete[delete]
#--------------------------------------------------------------------------
        result = self.mgmt_client.cluster_principal_assignments.begin_delete(resource_group_name=RESOURCE_GROUP, cluster_name=CLUSTER_NAME, principal_assignment_name=PRINCIPAL_ASSIGNMENT_NAME)
        result = result.result()
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
