# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 30
# Methods Covered : 30
# Examples Total  : 38
# Examples Tested : 38
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.resources.policy
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtPolicyClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtPolicyClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.resources.policy.PolicyClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_resources(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Create or update policy assignment with a managed identity by ID[put]
        BODY = {
          "identity": {
            "type": "SystemAssigned"
          },
          "location": "eastus",
          "properties": {
            "display_name": "Enforce storage account SKU",
            "description": "Allow only storage accounts of SKU Standard_GRS or Standard_LRS to be created",
            "metadata": {
              "assigned_by": "Cheapskate Boss"
            },
            "policy_definition_id": "/providers/Microsoft.Authorization/policyDefinitions/7433c107-6db4-4ad1-b57a-a76dce0154a1",
            "parameters": {
              "list_of_allowed_skus": {
                "value": [
                  "Standard_GRS",
                  "Standard_LRS"
                ]
              }
            },
            "enforcement_mode": "Default"
          }
        }
        result = self.mgmt_client.policy_assignments.create_by_id(BODY)

        # Create or update policy assignment by ID[put]
        BODY = {
          "properties": {
            "display_name": "Enforce storage account SKU",
            "description": "Allow only storage accounts of SKU Standard_GRS or Standard_LRS to be created",
            "metadata": {
              "assigned_by": "Cheapskate Boss"
            },
            "policy_definition_id": "/providers/Microsoft.Authorization/policyDefinitions/7433c107-6db4-4ad1-b57a-a76dce0154a1",
            "parameters": {
              "list_of_allowed_skus": {
                "value": [
                  "Standard_GRS",
                  "Standard_LRS"
                ]
              }
            },
            "enforcement_mode": "Default"
          }
        }
        result = self.mgmt_client.policy_assignments.create_by_id(BODY)

        # Create or update a policy assignment with a managed identity[put]
        BODY = {
          "location": "eastus",
          "identity": {
            "type": "SystemAssigned"
          },
          "properties": {
            "display_name": "Enforce resource naming rules",
            "description": "Force resource names to begin with given DeptA and end with -LC",
            "metadata": {
              "assigned_by": "Foo Bar"
            },
            "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
            "parameters": {
              "prefix": {
                "value": "DeptA"
              },
              "suffix": {
                "value": "-LC"
              }
            },
            "enforcement_mode": "Default"
          }
        }
        result = self.mgmt_client.policy_assignments.create(POLICY_ASSIGNMENT_NAME, BODY)

        # Create or update a policy assignment[put]
        BODY = {
          "properties": {
            "display_name": "Enforce resource naming rules",
            "description": "Force resource names to begin with given DeptA and end with -LC",
            "metadata": {
              "assigned_by": "Special Someone"
            },
            "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
            "parameters": {
              "prefix": {
                "value": "DeptA"
              },
              "suffix": {
                "value": "-LC"
              }
            }
          }
        }
        result = self.mgmt_client.policy_assignments.create(POLICY_ASSIGNMENT_NAME, BODY)

        # Create or update a policy assignment without enforcing policy effect during resource creation or update.[put]
        BODY = {
          "properties": {
            "display_name": "Enforce resource naming rules",
            "description": "Force resource names to begin with given DeptA and end with -LC",
            "metadata": {
              "assigned_by": "Special Someone"
            },
            "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
            "parameters": {
              "prefix": {
                "value": "DeptA"
              },
              "suffix": {
                "value": "-LC"
              }
            },
            "enforcement_mode": "DoNotEnforce"
          }
        }
        result = self.mgmt_client.policy_assignments.create(POLICY_ASSIGNMENT_NAME, BODY)

        # Create or update a policy definition[put]
        BODY = {
          "properties": {
            "mode": "All",
            "display_name": "Enforce resource naming convention",
            "description": "Force resource names to begin with given 'prefix' and/or end with given 'suffix'",
            "metadata": {
              "category": "Naming"
            },
            "policy_rule": {
              "if": {
                "not": {
                  "field": "name",
                  "like": "[concat(parameters('prefix'), '*', parameters('suffix'))]"
                }
              },
              "then": {
                "effect": "deny"
              }
            },
            "parameters": {
              "prefix": {
                "type": "String",
                "metadata": {
                  "display_name": "Prefix",
                  "description": "Resource name prefix"
                }
              },
              "suffix": {
                "type": "String",
                "metadata": {
                  "display_name": "Suffix",
                  "description": "Resource name suffix"
                }
              }
            }
          }
        }
        result = self.mgmt_client.policy_definitions.create_or_update(POLICY_DEFINITION_NAME, BODY)

        # Create or update a policy definition with advanced parameters[put]
        BODY = {
          "properties": {
            "mode": "Indexed",
            "display_name": "Event Hubs should have diagnostic logging enabled",
            "description": "Audit enabling of logs and retain them up to a year. This enables recreation of activity trails for investigation purposes when a security incident occurs or your network is compromised",
            "metadata": {
              "category": "Event Hub"
            },
            "policy_rule": {
              "if": {
                "field": "type",
                "equals": "Microsoft.EventHub/namespaces"
              },
              "then": {
                "effect": "AuditIfNotExists",
                "details": {
                  "type": "Microsoft.Insights/diagnosticSettings",
                  "existence_condition": {
                    "all_of": [
                      {
                        "field": "Microsoft.Insights/diagnosticSettings/logs[*].retentionPolicy.enabled",
                        "equals": "true"
                      },
                      {
                        "field": "Microsoft.Insights/diagnosticSettings/logs[*].retentionPolicy.days",
                        "equals": "[parameters('requiredRetentionDays')]"
                      }
                    ]
                  }
                }
              }
            },
            "parameters": {
              "required_retention_days": {
                "type": "Integer",
                "default_value": "365",
                "allowed_values": [
                  "0",
                  "30",
                  "90",
                  "180",
                  "365"
                ],
                "metadata": {
                  "display_name": "Required retention (days)",
                  "description": "The required diagnostic logs retention in days"
                }
              }
            }
          }
        }
        result = self.mgmt_client.policy_definitions.create_or_update(POLICY_DEFINITION_NAME, BODY)

        # Create or update a policy set definition[put]
        BODY = {
          "properties": {
            "display_name": "Cost Management",
            "description": "Policies to enforce low cost storage SKUs",
            "metadata": {
              "category": "Cost Management"
            },
            "parameters": {
              "name_prefix": {
                "type": "String",
                "default_value": "myPrefix",
                "metadata": {
                  "display_name": "Prefix to enforce on resource names"
                }
              }
            },
            "policy_definitions": [
              {
                "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
                "policy_definition_reference_id": "Limit_Skus",
                "parameters": {
                  "list_of_allowed_skus": {
                    "value": [
                      "Standard_GRS",
                      "Standard_LRS"
                    ]
                  }
                }
              },
              {
                "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
                "policy_definition_reference_id": "Resource_Naming",
                "parameters": {
                  "prefix": {
                    "value": "[parameters('namePrefix')]"
                  },
                  "suffix": {
                    "value": "-LC"
                  }
                }
              }
            ]
          }
        }
        result = self.mgmt_client.policy_set_definitions.create_or_update(POLICY_SET_DEFINITION_NAME, BODY)

        # Create or update a policy set definition with groups[put]
        BODY = {
          "properties": {
            "display_name": "Cost Management",
            "description": "Policies to enforce low cost storage SKUs",
            "metadata": {
              "category": "Cost Management"
            },
            "policy_definition_groups": [
              {
                "name": "CostSaving",
                "display_name": "Cost Management Policies",
                "description": "Policies designed to control spend within a subscription."
              },
              {
                "name": "Organizational",
                "display_name": "Organizational Policies",
                "description": "Policies that help enforce resource organization standards within a subscription."
              }
            ],
            "policy_definitions": [
              {
                "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
                "policy_definition_reference_id": "Limit_Skus",
                "group_names": [
                  "CostSaving"
                ],
                "parameters": {
                  "list_of_allowed_skus": {
                    "value": [
                      "Standard_GRS",
                      "Standard_LRS"
                    ]
                  }
                }
              },
              {
                "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
                "policy_definition_reference_id": "Resource_Naming",
                "group_names": [
                  "Organizational"
                ],
                "parameters": {
                  "prefix": {
                    "value": "DeptA"
                  },
                  "suffix": {
                    "value": "-LC"
                  }
                }
              }
            ]
          }
        }
        result = self.mgmt_client.policy_set_definitions.create_or_update(POLICY_SET_DEFINITION_NAME, BODY)

        # Create or update a policy definition at management group level[put]
        BODY = {
          "properties": {
            "mode": "All",
            "display_name": "Enforce resource naming convention",
            "description": "Force resource names to begin with given 'prefix' and/or end with given 'suffix'",
            "metadata": {
              "category": "Naming"
            },
            "policy_rule": {
              "if": {
                "not": {
                  "field": "name",
                  "like": "[concat(parameters('prefix'), '*', parameters('suffix'))]"
                }
              },
              "then": {
                "effect": "deny"
              }
            },
            "parameters": {
              "prefix": {
                "type": "String",
                "metadata": {
                  "display_name": "Prefix",
                  "description": "Resource name prefix"
                }
              },
              "suffix": {
                "type": "String",
                "metadata": {
                  "display_name": "Suffix",
                  "description": "Resource name suffix"
                }
              }
            }
          }
        }
        result = self.mgmt_client.policy_definitions.create_or_update_at_management_group(MANAGEMENTGROUP_NAME, POLICY_DEFINITION_NAME, BODY)

        # Create or update a policy set definition with groups at management group level[put]
        BODY = {
          "properties": {
            "display_name": "Cost Management",
            "description": "Policies to enforce low cost storage SKUs",
            "metadata": {
              "category": "Cost Management"
            },
            "policy_definition_groups": [
              {
                "name": "CostSaving",
                "display_name": "Cost Management Policies",
                "description": "Policies designed to control spend within a subscription."
              },
              {
                "name": "Organizational",
                "display_name": "Organizational Policies",
                "description": "Policies that help enforce resource organization standards within a subscription."
              }
            ],
            "policy_definitions": [
              {
                "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
                "policy_definition_reference_id": "Limit_Skus",
                "group_names": [
                  "CostSaving"
                ],
                "parameters": {
                  "list_of_allowed_skus": {
                    "value": [
                      "Standard_GRS",
                      "Standard_LRS"
                    ]
                  }
                }
              },
              {
                "policy_definition_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.Authorization/policyDefinitions/" + POLICY_DEFINITION_NAME + "",
                "policy_definition_reference_id": "Resource_Naming",
                "group_names": [
                  "Organizational"
                ],
                "parameters": {
                  "prefix": {
                    "value": "DeptA"
                  },
                  "suffix": {
                    "value": "-LC"
                  }
                }
              }
            ]
          }
        }
        result = self.mgmt_client.policy_set_definitions.create_or_update_at_management_group(MANAGEMENTGROUP_NAME, POLICY_SET_DEFINITION_NAME, BODY)

        # Create or update a policy set definition at management group level[put]
        BODY = {
          "properties": {
            "display_name": "Cost Management",
            "description": "Policies to enforce low cost storage SKUs",
            "metadata": {
              "category": "Cost Management"
            },
            "policy_definitions": [
              {
                "policy_definition_id": "/providers/Microsoft.Management/managementgroups/MyManagementGroup/providers/Microsoft.Authorization/policyDefinitions/7433c107-6db4-4ad1-b57a-a76dce0154a1",
                "policy_definition_reference_id": "Limit_Skus",
                "parameters": {
                  "list_of_allowed_skus": {
                    "value": [
                      "Standard_GRS",
                      "Standard_LRS"
                    ]
                  }
                }
              },
              {
                "policy_definition_id": "/providers/Microsoft.Management/managementgroups/MyManagementGroup/providers/Microsoft.Authorization/policyDefinitions/ResourceNaming",
                "policy_definition_reference_id": "Resource_Naming",
                "parameters": {
                  "prefix": {
                    "value": "DeptA"
                  },
                  "suffix": {
                    "value": "-LC"
                  }
                }
              }
            ]
          }
        }
        result = self.mgmt_client.policy_set_definitions.create_or_update_at_management_group(MANAGEMENTGROUP_NAME, POLICY_SET_DEFINITION_NAME, BODY)

        # List all policy assignments that apply to a resource[get]
        result = self.mgmt_client.policy_assignments.list_for_resource(resource_group.name, {PARENT_RESOURCE_PATH}_NAME, {RESOURCE_NAME}_NAME, MICROSOFT.AUTHORIZATION_NAME)

        # Retrieve a policy set definition at management group level[get]
        result = self.mgmt_client.policy_set_definitions.get_at_management_group(MANAGEMENTGROUP_NAME, POLICY_SET_DEFINITION_NAME)

        # Retrieve a policy definition at management group level[get]
        result = self.mgmt_client.policy_definitions.get_at_management_group(MANAGEMENTGROUP_NAME, POLICY_DEFINITION_NAME)

        # List policy set definitions at management group level[get]
        result = self.mgmt_client.policy_set_definitions.list_by_management_group(MANAGEMENTGROUP_NAME)

        # List policy definitions by management group[get]
        result = self.mgmt_client.policy_definitions.list_by_management_group(MANAGEMENTGROUP_NAME)

        # List policy assignments that apply to a management group[get]
        result = self.mgmt_client.policy_assignments.list_for_management_group(MANAGEMENTGROUP_NAME)

        # Retrieve a policy set definition[get]
        result = self.mgmt_client.policy_set_definitions.get(POLICY_SET_DEFINITION_NAME)

        # List policy assignments that apply to a resource group[get]
        result = self.mgmt_client.policy_assignments.list_for_resource_group(resource_group.name)

        # Retrieve a policy definition[get]
        result = self.mgmt_client.policy_definitions.get(POLICY_DEFINITION_NAME)

        # List policy set definitions[get]
        result = self.mgmt_client.policy_set_definitions.list()

        # Retrieve a policy assignment with a managed identity[get]
        result = self.mgmt_client.policy_assignments.get(POLICY_ASSIGNMENT_NAME)

        # Retrieve a policy assignment[get]
        result = self.mgmt_client.policy_assignments.get(POLICY_ASSIGNMENT_NAME)

        # List policy assignments that apply to a subscription[get]
        result = self.mgmt_client.policy_assignments.list()

        # Retrieve a built-in policy set definition[get]
        result = self.mgmt_client.policy_set_definitions.get_built_in(POLICY_SET_DEFINITION_NAME)

        # List policy definitions by subscription[get]
        result = self.mgmt_client.policy_definitions.list()

        # Retrieve a built-in policy definition[get]
        result = self.mgmt_client.policy_definitions.get_built_in(POLICY_DEFINITION_NAME)

        # List built-in policy set definitions[get]
        result = self.mgmt_client.policy_set_definitions.list_built_in()

        # List built-in policy definitions[get]
        result = self.mgmt_client.policy_definitions.list_built_in()

        # Retrieve a policy assignment by ID[get]
        result = self.mgmt_client.policy_assignments.get_by_id()

        # Retrieve a policy assignment with a managed identity by ID[get]
        result = self.mgmt_client.policy_assignments.get_by_id()

        # Delete a policy set definition at management group level[delete]
        result = self.mgmt_client.policy_set_definitions.delete_at_management_group(MANAGEMENTGROUP_NAME, POLICY_SET_DEFINITION_NAME)

        # Delete a policy definition at management group level[delete]
        result = self.mgmt_client.policy_definitions.delete_at_management_group(MANAGEMENTGROUP_NAME, POLICY_DEFINITION_NAME)

        # Delete a policy set definition[delete]
        result = self.mgmt_client.policy_set_definitions.delete(POLICY_SET_DEFINITION_NAME)

        # Delete a policy definition[delete]
        result = self.mgmt_client.policy_definitions.delete(POLICY_DEFINITION_NAME)

        # Delete a policy assignment[delete]
        result = self.mgmt_client.policy_assignments.delete(POLICY_ASSIGNMENT_NAME)

        # Delete a policy assignment by ID[delete]
        result = self.mgmt_client.policy_assignments.delete_by_id()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
