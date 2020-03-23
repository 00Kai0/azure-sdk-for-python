# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 90
# Methods Covered : 11
# Examples Total  : 15
# Examples Tested : 15
# Coverage %      : 12.222222222222221
# ----------------------

import unittest

import azure.mgmt.resource.resources
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtResourceTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtResourceTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.resource.resources.ResourceManagementClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_resource(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Update tags on a subscription[put]
        BODY = {
          "properties": {
            "tags": {
              "tag_key1": "tagValue1",
              "tag_key2": "tagValue2"
            }
          }
        }
        result = self.mgmt_client.tags.create_or_update_at_scope(TAG_NAME, BODY)

        # Update tags on a resource[put]
        BODY = {
          "properties": {
            "tags": {
              "tag_key1": "tagValue1",
              "tag_key2": "tagValue2"
            }
          }
        }
        result = self.mgmt_client.tags.create_or_update_at_scope(TAG_NAME, BODY)

        # Create deployment at tenant scope.[put]
        BODY = {
          "location": "eastus",
          "properties": {
            "template_link": {
              "uri": "{templateUri}"
            },
            "mode": "Incremental"
          },
          "tags": {
            "tag_key1": "tagValue1",
            "tag_key2": "tagValue2"
          }
        }
        result = self.mgmt_client.deployments.create_or_update_at_tenant_scope(DEPLOYMENT_NAME, BODY)
        result = result.result()

        # Create deployment at a given scope.[put]
        BODY = {
          "location": "eastus",
          "properties": {
            "template_link": {
              "uri": "{templateUri}"
            },
            "mode": "Incremental"
          },
          "tags": {
            "tag_key1": "tagValue1",
            "tag_key2": "tagValue2"
          }
        }
        result = self.mgmt_client.deployments.create_or_update_at_scope(DEPLOYMENT_NAME, BODY)
        result = result.result()

        # Create or update a resource group[put]
        BODY = {
          "location": "eastus"
        }
        result = self.mgmt_client.resource_groups.create_or_update(resource_group.name, BODY)

        # Create a deployment that will redeploy the last successful deployment on failure[put]
        BODY = {
          "properties": {
            "template_link": {
              "uri": "{templateUri}"
            },
            "mode": "Complete",
            "on_error_deployment": {
              "type": "LastSuccessful"
            }
          }
        }
        result = self.mgmt_client.deployments.create_or_update(resource_group.name, DEPLOYMENT_NAME, BODY)
        result = result.result()

        # Create a deployment that will redeploy another deployment on failure[put]
        BODY = {
          "properties": {
            "template_link": {
              "uri": "{templateUri}"
            },
            "mode": "Complete",
            "on_error_deployment": {
              "type": "SpecificDeployment",
              "deployment_name": "{nameOfDeploymentToUse}"
            }
          }
        }
        result = self.mgmt_client.deployments.create_or_update(resource_group.name, DEPLOYMENT_NAME, BODY)
        result = result.result()

        # Create deployment at management group scope.[put]
        BODY = {
          "location": "eastus",
          "properties": {
            "template_link": {
              "uri": "{templateUri}"
            },
            "mode": "Incremental"
          }
        }
        result = self.mgmt_client.deployments.create_or_update_at_management_group_scope(MANAGEMENT_GROUP_NAME, DEPLOYMENT_NAME, BODY)
        result = result.result()

        # Get tags on a subscription[get]
        result = self.mgmt_client.tags.get_at_scope(TAG_NAME)

        # Get tags on a resource[get]
        result = self.mgmt_client.tags.get_at_scope(TAG_NAME)

        # Predict template changes at resource group scope[post]
        BODY = {
          "properties": {
            "template_link": "https://example.com/exampleTemplate.json",
            "mode": "Incremental"
          }
        }
        result = self.mgmt_client.deployments.what_if(resource_group.name, DEPLOYMENT_NAME, BODY)
        result = result.result()

        # Predict template changes at subscription scope[post]
        BODY = {
          "location": "westus",
          "properties": {
            "template_link": "https://example.com/exampleTemplate.json",
            "mode": "Incremental"
          }
        }
        result = self.mgmt_client.deployments.what_if_at_subscription_scope(DEPLOYMENT_NAME, BODY)
        result = result.result()

        # Export a resource group with filtering[post]
        BODY = {
          "resources": [
            "/subscriptions/eaee6a92-e973-4922-9471-3a0a6abf81cd/resourceGroups/myResourceGroup/providers/My.RP/myResourceType/myFirstResource"
          ],
          "options": "SkipResourceNameParameterization"
        }
        result = self.mgmt_client.resource_groups.export_template(resource_group.name, BODY)
        result = result.result()

        # Export a resource group[post]
        BODY = {
          "resources": [
            "*"
          ],
          "options": "IncludeParameterDefaultValue,IncludeComments"
        }
        result = self.mgmt_client.resource_groups.export_template(resource_group.name, BODY)
        result = result.result()

        # Calculate template hash[post]
        BODY = {
          "$schema": "http://schemas.management.azure.com/deploymentTemplate?api-version=2014-04-01-preview",
          "content_version": "1.0.0.0",
          "parameters": {
            "string": {
              "type": "string"
            }
          },
          "variables": {
            "string": "string",
            "int": "42",
            "bool": True,
            "array": [
              "1",
              "2",
              "3",
              "4"
            ],
            "object": {
              "object": {
                "vm_size": "Large",
                "location": "West US"
              }
            }
          },
          "resources": [],
          "outputs": {
            "string": {
              "type": "string",
              "value": "myvalue"
            }
          }
        }
        result = self.mgmt_client.deployments.calculate_template_hash(BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
