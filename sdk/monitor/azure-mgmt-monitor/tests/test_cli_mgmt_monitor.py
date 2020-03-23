# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 63
# Methods Covered : 63
# Examples Total  : 87
# Examples Tested : 87
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.monitor
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtMonitorClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtMonitorClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.monitor.MonitorClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_monitor(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Creates or Updates the diagnostic setting[put]
        BODY = {
          "properties": {
            "storage_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
            "workspace_id": "",
            "event_hub_authorization_rule_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.eventhub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME + "/authorizationrules/" + AUTHORIZATIONRULE_NAME + "",
            "event_hub_name": "myeventhub",
            "metrics": [
              {
                "category": "WorkflowMetrics",
                "enabled": True,
                "retention_policy": {
                  "enabled": False,
                  "days": "0"
                }
              }
            ],
            "logs": [
              {
                "category": "WorkflowRuntime",
                "enabled": True,
                "retention_policy": {
                  "enabled": False,
                  "days": "0"
                }
              }
            ],
            "log_analytics_destination_type": "Dedicated"
          }
        }
        result = self.mgmt_client.diagnostic_settings.create_or_update({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME, BODY)

        # Create or update a log profile[put]
        BODY = {
          "location": "",
          "properties": {
            "locations": [
              "global"
            ],
            "categories": [
              "Write",
              "Delete",
              "Action"
            ],
            "retention_policy": {
              "enabled": True,
              "days": "3"
            },
            "storage_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
            "service_bus_rule_id": ""
          }
        }
        result = self.mgmt_client.log_profiles.create_or_update(LOGPROFILE_NAME, BODY)

        # Create or update an alert rule[put]
        BODY = {
          "location": "West US",
          "properties": {
            "name": "chiricutin",
            "description": "Pura Vida",
            "is_enabled": True,
            "condition": {
              "odata.type": "Microsoft.Azure.Management.Insights.Models.ThresholdRuleCondition",
              "data_source": {
                "odata.type": "Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource",
                "resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Web/sites/" + SITE_NAME + "",
                "metric_name": "Requests"
              },
              "operator": "GreaterThan",
              "threshold": "3",
              "window_size": "PT5M",
              "time_aggregation": "Total"
            },
            "last_updated_time": "2016-11-23T21:23:52.0221265Z",
            "actions": []
          }
        }
        result = self.mgmt_client.alert_rules.create_or_update(resource_group.name, ALERTRULE_NAME, BODY)

        # Create or update an alert rule on Resource group(s)[put]
        BODY = {
          "location": "global",
          "properties": {
            "description": "This is the description of the rule1",
            "severity": "3",
            "enabled": True,
            "scopes": [
              "/subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest1",
              "/subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest2"
            ],
            "evaluation_frequency": "PT1M",
            "window_size": "PT15M",
            "target_resource_type": "Microsoft.Compute/virtualMachines",
            "target_resource_region": "southcentralus",
            "criteria": {
              "odata.type": "Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria",
              "all_of": [
                {
                  "criterion_type": "StaticThresholdCriterion",
                  "name": "High_CPU_80",
                  "metric_name": "Percentage CPU",
                  "metric_namespace": "microsoft.compute/virtualmachines",
                  "dimensions": [],
                  "operator": "GreaterThan",
                  "threshold": "80.5",
                  "time_aggregation": "Average"
                }
              ]
            },
            "auto_mitigate": False,
            "actions": [
              {
                "action_group_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/notificationgroups/" + NOTIFICATIONGROUP_NAME + "",
                "web_hook_properties": {
                  "key11": "value11",
                  "key12": "value12"
                }
              }
            ]
          }
        }
        result = self.mgmt_client.metric_alerts.create_or_update(resource_group.name, METRIC_ALERT_NAME, BODY)

        # Create or update an alert rule for Single Resource[put]
        BODY = {
          "location": "global",
          "properties": {
            "description": "This is the description of the rule1",
            "severity": "3",
            "enabled": True,
            "scopes": [
              "/subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme"
            ],
            "evaluation_frequency": "Pt1m",
            "window_size": "Pt15m",
            "criteria": {
              "odata.type": "Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria",
              "all_of": [
                {
                  "criterion_type": "StaticThresholdCriterion",
                  "name": "High_CPU_80",
                  "metric_name": "\\Processor(_Total)\\% Processor Time",
                  "dimensions": [],
                  "operator": "GreaterThan",
                  "threshold": "80.5",
                  "time_aggregation": "Average"
                }
              ]
            },
            "auto_mitigate": False,
            "actions": [
              {
                "action_group_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/notificationgroups/" + NOTIFICATIONGROUP_NAME + "",
                "web_hook_properties": {
                  "key11": "value11",
                  "key12": "value12"
                }
              }
            ]
          }
        }
        result = self.mgmt_client.metric_alerts.create_or_update(resource_group.name, METRIC_ALERT_NAME, BODY)

        # Create or update an alert rule for Multiple Resource[put]
        BODY = {
          "location": "global",
          "properties": {
            "description": "This is the description of the rule1",
            "severity": "3",
            "enabled": True,
            "scopes": [
              "/subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme1",
              "/subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme2"
            ],
            "evaluation_frequency": "PT1M",
            "window_size": "PT15M",
            "target_resource_type": "Microsoft.Compute/virtualMachines",
            "target_resource_region": "southcentralus",
            "criteria": {
              "odata.type": "Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria",
              "all_of": [
                {
                  "criterion_type": "StaticThresholdCriterion",
                  "name": "High_CPU_80",
                  "metric_name": "Percentage CPU",
                  "metric_namespace": "microsoft.compute/virtualmachines",
                  "dimensions": [],
                  "operator": "GreaterThan",
                  "threshold": "80.5",
                  "time_aggregation": "Average"
                }
              ]
            },
            "auto_mitigate": False,
            "actions": [
              {
                "action_group_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/notificationgroups/" + NOTIFICATIONGROUP_NAME + "",
                "web_hook_properties": {
                  "key11": "value11",
                  "key12": "value12"
                }
              }
            ]
          }
        }
        result = self.mgmt_client.metric_alerts.create_or_update(resource_group.name, METRIC_ALERT_NAME, BODY)

        # Create or update an action group[put]
        BODY = {
          "location": "Global",
          "properties": {
            "group_short_name": "sample",
            "enabled": True,
            "email_receivers": [
              {
                "name": "John Doe's email",
                "email_address": "johndoe@email.com",
                "use_common_alert_schema": False
              },
              {
                "name": "Jane Smith's email",
                "email_address": "janesmith@email.com",
                "use_common_alert_schema": True
              }
            ],
            "sms_receivers": [
              {
                "name": "John Doe's mobile",
                "country_code": "1",
                "phone_number": "1234567890"
              },
              {
                "name": "Jane Smith's mobile",
                "country_code": "1",
                "phone_number": "0987654321"
              }
            ],
            "webhook_receivers": [
              {
                "name": "Sample webhook 1",
                "service_uri": "http://www.example.com/webhook1",
                "use_common_alert_schema": True
              },
              {
                "name": "Sample webhook 2",
                "service_uri": "http://www.example.com/webhook2",
                "use_common_alert_schema": True,
                "use_aad_auth": True,
                "object_id": "d3bb868c-fe44-452c-aa26-769a6538c808",
                "identifier_uri": "http://someidentifier/d7811ba3-7996-4a93-99b6-6b2f3f355f8a",
                "tenant_id": "68a4459a-ccb8-493c-b9da-dd30457d1b84"
              }
            ],
            "itsm_receivers": [
              {
                "name": "Sample itsm",
                "workspace_id": "5def922a-3ed4-49c1-b9fd-05ec533819a3|55dfd1f8-7e59-4f89-bf56-4c82f5ace23c",
                "connection_id": "a3b9076c-ce8e-434e-85b4-aff10cb3c8f1",
                "ticket_configuration": "{\"PayloadRevision\":0,\"WorkItemType\":\"Incident\",\"UseTemplate\":false,\"WorkItemData\":\"{}\",\"CreateOneWIPerCI\":false}",
                "region": "westcentralus"
              }
            ],
            "azure_app_push_receivers": [
              {
                "name": "Sample azureAppPush",
                "email_address": "johndoe@email.com"
              }
            ],
            "automation_runbook_receivers": [
              {
                "automation_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Automation/automationAccounts/" + AUTOMATION_ACCOUNT_NAME + "",
                "runbook_name": "Sample runbook",
                "webhook_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Automation/automationAccounts/" + AUTOMATION_ACCOUNT_NAME + "/webhooks/" + WEBHOOK_NAME + "",
                "is_global_runbook": False,
                "name": "testRunbook",
                "service_uri": "https://s13events.azure-automation.net/webhooks?token=iimE%2fD19Eg%2bvDy22yUMecIZY6Uiz%2bHfuQ67r8r1wY%2fI%3d",
                "use_common_alert_schema": True
              }
            ],
            "voice_receivers": [
              {
                "name": "Sample voice",
                "country_code": "1",
                "phone_number": "1234567890"
              }
            ],
            "logic_app_receivers": [
              {
                "name": "Sample logicApp",
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Logic/workflows/" + WORKFLOW_NAME + "",
                "callback_url": "https://prod-27.northcentralus.logic.azure.com/workflows/68e572e818e5457ba898763b7db90877/triggers/manual/paths/invoke/azns/test?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=Abpsb72UYJxPPvmDo937uzofupO5r_vIeWEx7KVHo7w",
                "use_common_alert_schema": False
              }
            ],
            "azure_function_receivers": [
              {
                "name": "Sample azureFunction",
                "function_app_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Web/sites/" + SITE_NAME + "",
                "function_name": "HttpTriggerCSharp1",
                "http_trigger_url": "https://testfunctionapp.azurewebsites.net/api/HttpTriggerCSharp1?code=4CopFfiXqUQC8dvIM7F53J7tIU3Gy9QQIG/vKAXMe2avhHqK3/jVYw==",
                "use_common_alert_schema": True
              }
            ],
            "arm_role_receivers": [
              {
                "name": "Sample armRole",
                "role_id": "8e3af657-a8ff-443c-a75c-2fe8c4bcb635",
                "use_common_alert_schema": True
              }
            ]
          }
        }
        result = self.mgmt_client.action_groups.create_or_update(resource_group.name, ACTION_GROUP_NAME, BODY)

        # Create or update a dynamic alert rule for Single Resource[put]
        BODY = {
          "location": "global",
          "properties": {
            "description": "This is the description of the rule1",
            "severity": "3",
            "enabled": True,
            "scopes": [
              "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme"
            ],
            "evaluation_frequency": "PT1M",
            "window_size": "PT15M",
            "target_resource_type": "Microsoft.Compute/virtualMachines",
            "target_resource_region": "southcentralus",
            "criteria": {
              "odata.type": "Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria",
              "all_of": [
                {
                  "criterion_type": "DynamicThresholdCriterion",
                  "name": "High_CPU_80",
                  "metric_name": "Percentage CPU",
                  "metric_namespace": "microsoft.compute/virtualmachines",
                  "operator": "GreaterOrLessThan",
                  "time_aggregation": "Average",
                  "dimensions": [],
                  "alert_sensitivity": "Medium",
                  "failing_periods": {
                    "number_of_evaluation_periods": "4",
                    "min_failing_periods_to_alert": "4"
                  },
                  "ignore_data_before": "2019-04-04T21:00:00Z"
                }
              ]
            },
            "auto_mitigate": False,
            "actions": [
              {
                "action_group_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/notificationgroups/" + NOTIFICATIONGROUP_NAME + "",
                "web_hook_properties": {
                  "key11": "value11",
                  "key12": "value12"
                }
              }
            ]
          }
        }
        result = self.mgmt_client.metric_alerts.create_or_update(resource_group.name, METRIC_ALERT_NAME, BODY)

        # Create or update a dynamic alert rule for Multiple Resources[put]
        BODY = {
          "location": "global",
          "properties": {
            "description": "This is the description of the rule1",
            "severity": "3",
            "enabled": True,
            "scopes": [
              "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme1",
              "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/gigtest/providers/Microsoft.Compute/virtualMachines/gigwadme2"
            ],
            "evaluation_frequency": "PT1M",
            "window_size": "PT15M",
            "target_resource_type": "Microsoft.Compute/virtualMachines",
            "target_resource_region": "southcentralus",
            "criteria": {
              "odata.type": "Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria",
              "all_of": [
                {
                  "criterion_type": "DynamicThresholdCriterion",
                  "name": "High_CPU_80",
                  "metric_name": "Percentage CPU",
                  "metric_namespace": "microsoft.compute/virtualmachines",
                  "operator": "GreaterOrLessThan",
                  "time_aggregation": "Average",
                  "dimensions": [],
                  "alert_sensitivity": "Medium",
                  "failing_periods": {
                    "number_of_evaluation_periods": "4",
                    "min_failing_periods_to_alert": "4"
                  }
                }
              ]
            },
            "auto_mitigate": False,
            "actions": [
              {
                "action_group_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/notificationgroups/" + NOTIFICATIONGROUP_NAME + "",
                "web_hook_properties": {
                  "key11": "value11",
                  "key12": "value12"
                }
              }
            ]
          }
        }
        result = self.mgmt_client.metric_alerts.create_or_update(resource_group.name, METRIC_ALERT_NAME, BODY)

        # Create or update a web test alert rule[put]
        BODY = {
          "location": "global",
          "tags": {
            "hidden-link:/subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/components/webtest-name-example": "Resource",
            "hidden-link:/subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/webtests/component-example": "Resource"
          },
          "properties": {
            "description": "Automatically created alert rule for availability test \"component-example\" a",
            "enabled": True,
            "severity": "4",
            "window_size": "PT15M",
            "evaluation_frequency": "PT1M",
            "criteria": {
              "failed_location_count": "2",
              "web_test_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/webtests/" + WEBTEST_NAME + "",
              "component_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/components/" + COMPONENT_NAME + "",
              "odata.type": "Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria"
            },
            "actions": [],
            "scopes": [
              "/subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/webtests/component-example",
              "/subscriptions/12345678-1234-1234-1234-123456789101/resourcegroups/rg-example/providers/microsoft.insights/components/webtest-name-example"
            ]
          }
        }
        result = self.mgmt_client.metric_alerts.create_or_update(resource_group.name, METRIC_ALERT_NAME, BODY)

        # Create or update an alert rule on Subscription [put]
        BODY = {
          "location": "global",
          "properties": {
            "description": "This is the description of the rule1",
            "severity": "3",
            "enabled": True,
            "scopes": [
              "/subscriptions/14ddf0c5-77c5-4b53-84f6-e1fa43ad68f7"
            ],
            "evaluation_frequency": "PT1M",
            "window_size": "PT15M",
            "target_resource_type": "Microsoft.Compute/virtualMachines",
            "target_resource_region": "southcentralus",
            "criteria": {
              "odata.type": "Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria",
              "all_of": [
                {
                  "criterion_type": "StaticThresholdCriterion",
                  "name": "High_CPU_80",
                  "metric_name": "Percentage CPU",
                  "metric_namespace": "microsoft.compute/virtualmachines",
                  "dimensions": [],
                  "operator": "GreaterThan",
                  "threshold": "80.5",
                  "time_aggregation": "Average"
                }
              ]
            },
            "auto_mitigate": False,
            "actions": [
              {
                "action_group_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/notificationgroups/" + NOTIFICATIONGROUP_NAME + "",
                "web_hook_properties": {
                  "key11": "value11",
                  "key12": "value12"
                }
              }
            ]
          }
        }
        result = self.mgmt_client.metric_alerts.create_or_update(resource_group.name, METRIC_ALERT_NAME, BODY)

        # Create or update an autoscale setting[put]
        BODY = {
          "location": "West US",
          "properties": {
            "profiles": [
              {
                "name": "adios",
                "capacity": {
                  "minimum": "1",
                  "maximum": "10",
                  "default": "1"
                },
                "rules": [
                  {
                    "metric_trigger": {
                      "metric_name": "Percentage CPU",
                      "metric_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
                      "time_grain": "PT1M",
                      "statistic": "Average",
                      "time_window": "PT5M",
                      "time_aggregation": "Average",
                      "operator": "GreaterThan",
                      "threshold": "10"
                    },
                    "scale_action": {
                      "direction": "Increase",
                      "type": "ChangeCount",
                      "value": "1",
                      "cooldown": "PT5M"
                    }
                  },
                  {
                    "metric_trigger": {
                      "metric_name": "Percentage CPU",
                      "metric_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
                      "time_grain": "PT2M",
                      "statistic": "Average",
                      "time_window": "PT5M",
                      "time_aggregation": "Average",
                      "operator": "GreaterThan",
                      "threshold": "15"
                    },
                    "scale_action": {
                      "direction": "Decrease",
                      "type": "ChangeCount",
                      "value": "2",
                      "cooldown": "PT6M"
                    }
                  }
                ],
                "fixed_date": {
                  "time_zone": "UTC",
                  "start": "2015-03-05T14:00:00Z",
                  "end": "2015-03-05T14:30:00Z"
                }
              },
              {
                "name": "saludos",
                "capacity": {
                  "minimum": "1",
                  "maximum": "10",
                  "default": "1"
                },
                "rules": [
                  {
                    "metric_trigger": {
                      "metric_name": "Percentage CPU",
                      "metric_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
                      "time_grain": "PT1M",
                      "statistic": "Average",
                      "time_window": "PT5M",
                      "time_aggregation": "Average",
                      "operator": "GreaterThan",
                      "threshold": "10"
                    },
                    "scale_action": {
                      "direction": "Increase",
                      "type": "ChangeCount",
                      "value": "1",
                      "cooldown": "PT5M"
                    }
                  },
                  {
                    "metric_trigger": {
                      "metric_name": "Percentage CPU",
                      "metric_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
                      "time_grain": "PT2M",
                      "statistic": "Average",
                      "time_window": "PT5M",
                      "time_aggregation": "Average",
                      "operator": "GreaterThan",
                      "threshold": "15"
                    },
                    "scale_action": {
                      "direction": "Decrease",
                      "type": "ChangeCount",
                      "value": "2",
                      "cooldown": "PT6M"
                    }
                  }
                ],
                "recurrence": {
                  "frequency": "Week",
                  "schedule": {
                    "time_zone": "UTC",
                    "days": [
                      "1"
                    ],
                    "hours": [
                      "5"
                    ],
                    "minutes": [
                      "15"
                    ]
                  }
                }
              }
            ],
            "enabled": True,
            "target_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
            "notifications": [
              {
                "operation": "Scale",
                "email": {
                  "send_to_subscription_administrator": True,
                  "send_to_subscription_co_administrators": True,
                  "custom_emails": [
                    "gu@ms.com",
                    "ge@ns.net"
                  ]
                },
                "webhooks": [
                  {
                    "service_uri": "http://myservice.com"
                  }
                ]
              }
            ]
          }
        }
        result = self.mgmt_client.autoscale_settings.create_or_update(resource_group.name, AUTOSCALESETTING_NAME, BODY)

        # Create or update an activity log alert[put]
        BODY = {
          "location": "Global",
          "properties": {
            "scopes": [
              "subscriptions/187f412d-1758-44d9-b052-169e2564721d"
            ],
            "enabled": True,
            "condition": {
              "all_of": [
                {
                  "field": "Category",
                  "equals": "Administrative"
                },
                {
                  "field": "Level",
                  "equals": "Error"
                }
              ]
            },
            "actions": {
              "action_groups": [
                {
                  "action_group_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/actionGroups/" + ACTION_GROUP_NAME + "",
                  "webhook_properties": {
                    "sample_webhook_property": "samplePropertyValue"
                  }
                }
              ]
            },
            "description": "Sample activity log alert description"
          }
        }
        result = self.mgmt_client.activity_log_alerts.create_or_update(resource_group.name, ACTIVITY_LOG_ALERT_NAME, BODY)

        # Create or Update rule - AlertingAction[put]
        BODY = {
          "location": "eastus",
          "properties": {
            "description": "log alert description",
            "enabled": "true",
            "last_updated_time": "2017-06-23T21:23:52.0221265Z",
            "provisioning_state": "Succeeded",
            "source": {
              "query": "Heartbeat | summarize AggregatedValue = count() by bin(TimeGenerated, 5m)",
              "data_source_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.OperationalInsights/workspaces/" + WORKSPACE_NAME + "",
              "query_type": "ResultCount"
            },
            "schedule": {
              "frequency_in_minutes": "15",
              "time_window_in_minutes": "15"
            },
            "action": {
              "odata.type": "Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction",
              "severity": "1",
              "azns_action": {
                "action_group": [],
                "email_subject": "Email Header",
                "custom_webhook_payload": "{}"
              },
              "trigger": {
                "threshold_operator": "GreaterThan",
                "threshold": "3",
                "metric_trigger": {
                  "threshold_operator": "GreaterThan",
                  "threshold": "5",
                  "metric_trigger_type": "Consecutive",
                  "metric_column": "Computer"
                }
              }
            }
          }
        }
        result = self.mgmt_client.scheduled_query_rules.create_or_update(resource_group.name, SCHEDULED_QUERY_RULE_NAME, BODY)

        # Create or Update rule - LogToMetricAction[put]
        BODY = {
          "location": "West Europe",
          "properties": {
            "description": "log to metric description",
            "enabled": "true",
            "source": {
              "data_source_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.OperationalInsights/workspaces/" + WORKSPACE_NAME + ""
            },
            "action": {
              "criteria": [
                {
                  "metric_name": "Average_% Idle Time",
                  "dimensions": []
                }
              ],
              "odata.type": "Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.LogToMetricAction"
            }
          }
        }
        result = self.mgmt_client.scheduled_query_rules.create_or_update(resource_group.name, SCHEDULED_QUERY_RULE_NAME, BODY)

        # Create or Update rule - AlertingAction with Cross-Resource[put]
        BODY = {
          "location": "eastus",
          "properties": {
            "description": "Sample Cross Resource alert",
            "enabled": "true",
            "source": {
              "query": "union requests, workspace(\"sampleWorkspace\").Update",
              "authorized_resources": [
                "/subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/Rac46PostSwapRG/providers/Microsoft.OperationalInsights/workspaces/sampleWorkspace",
                "/subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/Rac46PostSwapRG/providers/microsoft.insights/components/sampleAI"
              ],
              "data_source_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/microsoft.insights/components/" + COMPONENT_NAME + "",
              "query_type": "ResultCount"
            },
            "schedule": {
              "frequency_in_minutes": "60",
              "time_window_in_minutes": "60"
            },
            "action": {
              "severity": "3",
              "azns_action": {
                "action_group": [
                  "/subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/Rac46PostSwapRG/providers/microsoft.insights/actiongroups/test-ag"
                ],
                "email_subject": "Cross Resource Mail!!"
              },
              "trigger": {
                "threshold_operator": "GreaterThan",
                "threshold": "5000"
              },
              "odata.type": "Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction"
            }
          }
        }
        result = self.mgmt_client.scheduled_query_rules.create_or_update(resource_group.name, SCHEDULED_QUERY_RULE_NAME, BODY)

        # Get a single alert rule incident[get]
        result = self.mgmt_client.alert_rule_incidents.get(resource_group.name, ALERTRULE_NAME, INCIDENT_NAME)

        # Get an alert rule status[get]
        result = self.mgmt_client.metric_alerts_status.list_by_name(resource_group.name, METRIC_ALERT_NAME, STATUS_NAME)

        # Get rule[get]
        result = self.mgmt_client.scheduled_query_rules.get(resource_group.name, SCHEDULED_QUERY_RULE_NAME)

        # Get an activity log alert[get]
        result = self.mgmt_client.activity_log_alerts.get(resource_group.name, ACTIVITY_LOG_ALERT_NAME)

        # Get an autoscale setting[get]
        result = self.mgmt_client.autoscale_settings.get(resource_group.name, AUTOSCALESETTING_NAME)

        # Get an alert rule status[get]
        result = self.mgmt_client.metric_alerts_status.list_by_name(resource_group.name, METRIC_ALERT_NAME, STATUS_NAME)

        # List alert rule incidents[get]
        result = self.mgmt_client.alert_rule_incidents.list_by_alert_rule(resource_group.name, ALERTRULE_NAME)

        # Get a dynamic alert rule for multiple resources[get]
        result = self.mgmt_client.metric_alerts.get(resource_group.name, METRIC_ALERT_NAME)

        # Get an alert rule for single resource[get]
        result = self.mgmt_client.metric_alerts.get(resource_group.name, METRIC_ALERT_NAME)

        # Get an alert rule on resource group(s)[get]
        result = self.mgmt_client.metric_alerts.get(resource_group.name, METRIC_ALERT_NAME)

        # Get an alert rule for multiple resources[get]
        result = self.mgmt_client.metric_alerts.get(resource_group.name, METRIC_ALERT_NAME)

        # Get an alert rule on subscription[get]
        result = self.mgmt_client.metric_alerts.get(resource_group.name, METRIC_ALERT_NAME)

        # Get a dynamic alert rule for single resource[get]
        result = self.mgmt_client.metric_alerts.get(resource_group.name, METRIC_ALERT_NAME)

        # Get an action group[get]
        result = self.mgmt_client.action_groups.get(resource_group.name, ACTION_GROUP_NAME)

        # Get a web test alert rule[get]
        result = self.mgmt_client.metric_alerts.get(resource_group.name, METRIC_ALERT_NAME)

        # Get an alert rule[get]
        result = self.mgmt_client.alert_rules.get(resource_group.name, ALERTRULE_NAME)

        # List rules[get]
        result = self.mgmt_client.scheduled_query_rules.list_by_resource_group(resource_group.name)

        # List autoscale settings[get]
        result = self.mgmt_client.autoscale_settings.list_by_resource_group(resource_group.name)

        # List activity log alerts[get]
        result = self.mgmt_client.activity_log_alerts.list_by_resource_group(resource_group.name)

        # List metric alert rules[get]
        result = self.mgmt_client.metric_alerts.list_by_resource_group(resource_group.name)

        # List action groups[get]
        result = self.mgmt_client.action_groups.list_by_resource_group(resource_group.name)

        # List alert rules[get]
        result = self.mgmt_client.alert_rules.list_by_resource_group(resource_group.name)

        # Get Activity Logs with filter and select[get]
        result = self.mgmt_client.activity_logs.list(EVENTTYPE_NAME)

        # Get Activity Logs with filter[get]
        result = self.mgmt_client.activity_logs.list(EVENTTYPE_NAME)

        # Get Metric for data[get]
        result = self.mgmt_client.metric_baseline.get({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get Metric for metadata[get]
        result = self.mgmt_client.metric_baseline.get({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get log profile[get]
        result = self.mgmt_client.log_profiles.get(LOGPROFILE_NAME)

        # Get status for a subscription that has at least one VM that is actively reporting data[get]
        result = self.mgmt_client.vminsights.get_onboarding_status({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get status for a resource group that has at least one VM that is actively reporting data[get]
        result = self.mgmt_client.vminsights.get_onboarding_status({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get status for a VM scale set that is actively reporting data[get]
        result = self.mgmt_client.vminsights.get_onboarding_status({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get status for a VM that is actively reporting data[get]
        result = self.mgmt_client.vminsights.get_onboarding_status({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get status for a VM that has not yet reported data[get]
        result = self.mgmt_client.vminsights.get_onboarding_status({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Gets the diagnostic setting[get]
        result = self.mgmt_client.diagnostic_settings.get({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Gets the diagnostic setting[get]
        result = self.mgmt_client.diagnostic_settings.get({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Gets the diagnostic setting[get]
        result = self.mgmt_client.diagnostic_settings.get({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get Metric for data[get]
        result = self.mgmt_client.metric_baseline.get({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get Metric Namespaces without filter[get]
        result = self.mgmt_client.metric_namespaces.list({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get Metric Definitions without filter[get]
        result = self.mgmt_client.metric_definitions.list({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Gets the diagnostic setting[get]
        result = self.mgmt_client.diagnostic_settings.get({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get metric baselines[get]
        result = self.mgmt_client.baselines.list({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # Get Metric for metadata[get]
        result = self.mgmt_client.metric_baseline.get({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)

        # List rules[get]
        result = self.mgmt_client.scheduled_query_rules.list_by_resource_group(resource_group.name)

        # List activity log alerts[get]
        result = self.mgmt_client.activity_log_alerts.list_by_resource_group(resource_group.name)

        # List autoscale settings[get]
        result = self.mgmt_client.autoscale_settings.list_by_resource_group(resource_group.name)

        # List metric alert rules[get]
        result = self.mgmt_client.metric_alerts.list_by_resource_group(resource_group.name)

        # List action groups[get]
        result = self.mgmt_client.action_groups.list_by_resource_group(resource_group.name)

        # List log profiles[get]
        result = self.mgmt_client.log_profiles.list()

        # List alert rules[get]
        result = self.mgmt_client.alert_rules.list_by_resource_group(resource_group.name)

        # Get Tenant Activity Logs with filter[get]
        result = self.mgmt_client.tenant_activity_logs.list(EVENTTYPE_NAME)

        # Get Tenant Activity Logs with select[get]
        result = self.mgmt_client.tenant_activity_logs.list(EVENTTYPE_NAME)

        # Get Tenant Activity Logs with filter and select[get]
        result = self.mgmt_client.tenant_activity_logs.list(EVENTTYPE_NAME)

        # Get Tenant Activity Logs without filter or select[get]
        result = self.mgmt_client.tenant_activity_logs.list(EVENTTYPE_NAME)

        # Get event categories[get]
        result = self.mgmt_client.event_categories.list()

        # Get a list of operations for a resource provider[get]
        result = self.mgmt_client.operations.list()

        # Patch Log Search Rule[patch]
        BODY = {
          "properties": {
            "enabled": "true"
          }
        }
        result = self.mgmt_client.scheduled_query_rules.update(resource_group.name, SCHEDULED_QUERY_RULE_NAME, BODY)

        # Patch an activity log alert[patch]
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          },
          "properties": {
            "enabled": False
          }
        }
        result = self.mgmt_client.activity_log_alerts.update(resource_group.name, ACTIVITY_LOG_ALERT_NAME, BODY)

        # Enable the receiver[post]
        BODY = {
          "receiver_name": "John Doe's mobile"
        }
        result = self.mgmt_client.action_groups.enable_receiver(resource_group.name, ACTION_GROUP_NAME, BODY)

        # Patch an autoscale setting[patch]
        BODY = {
          "tags": {
            "$type": "Microsoft.WindowsAzure.Management.Common.Storage.CasePreservedDictionary"
          },
          "properties": {
            "profiles": [
              {
                "name": "adios",
                "capacity": {
                  "minimum": "1",
                  "maximum": "10",
                  "default": "1"
                },
                "rules": [
                  {
                    "metric_trigger": {
                      "metric_name": "Percentage CPU",
                      "metric_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
                      "time_grain": "PT1M",
                      "statistic": "Average",
                      "time_window": "PT5M",
                      "time_aggregation": "Average",
                      "operator": "GreaterThan",
                      "threshold": "10"
                    },
                    "scale_action": {
                      "direction": "Increase",
                      "type": "ChangeCount",
                      "value": "1",
                      "cooldown": "PT5M"
                    }
                  },
                  {
                    "metric_trigger": {
                      "metric_name": "Percentage CPU",
                      "metric_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
                      "time_grain": "PT2M",
                      "statistic": "Average",
                      "time_window": "PT5M",
                      "time_aggregation": "Average",
                      "operator": "GreaterThan",
                      "threshold": "15"
                    },
                    "scale_action": {
                      "direction": "Decrease",
                      "type": "ChangeCount",
                      "value": "2",
                      "cooldown": "PT6M"
                    }
                  }
                ],
                "fixed_date": {
                  "time_zone": "UTC",
                  "start": "2015-03-05T14:00:00Z",
                  "end": "2015-03-05T14:30:00Z"
                }
              },
              {
                "name": "saludos",
                "capacity": {
                  "minimum": "1",
                  "maximum": "10",
                  "default": "1"
                },
                "rules": [
                  {
                    "metric_trigger": {
                      "metric_name": "Percentage CPU",
                      "metric_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
                      "time_grain": "PT1M",
                      "statistic": "Average",
                      "time_window": "PT5M",
                      "time_aggregation": "Average",
                      "operator": "GreaterThan",
                      "threshold": "10"
                    },
                    "scale_action": {
                      "direction": "Increase",
                      "type": "ChangeCount",
                      "value": "1",
                      "cooldown": "PT5M"
                    }
                  },
                  {
                    "metric_trigger": {
                      "metric_name": "Percentage CPU",
                      "metric_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
                      "time_grain": "PT2M",
                      "statistic": "Average",
                      "time_window": "PT5M",
                      "time_aggregation": "Average",
                      "operator": "GreaterThan",
                      "threshold": "15"
                    },
                    "scale_action": {
                      "direction": "Decrease",
                      "type": "ChangeCount",
                      "value": "2",
                      "cooldown": "PT6M"
                    }
                  }
                ],
                "recurrence": {
                  "frequency": "Week",
                  "schedule": {
                    "time_zone": "UTC",
                    "days": [
                      "1"
                    ],
                    "hours": [
                      "5"
                    ],
                    "minutes": [
                      "15"
                    ]
                  }
                }
              }
            ],
            "enabled": True,
            "target_resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/virtualMachineScaleSets/" + VIRTUAL_MACHINE_SCALE_SET_NAME + "",
            "notifications": [
              {
                "operation": "Scale",
                "email": {
                  "send_to_subscription_administrator": True,
                  "send_to_subscription_co_administrators": True,
                  "custom_emails": [
                    "gu@ms.com",
                    "ge@ns.net"
                  ]
                },
                "webhooks": [
                  {
                    "service_uri": "http://myservice.com"
                  }
                ]
              }
            ]
          }
        }
        result = self.mgmt_client.autoscale_settings.update(resource_group.name, AUTOSCALESETTING_NAME, BODY)

        # Patch an action group[patch]
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          },
          "properties": {
            "enabled": False
          }
        }
        result = self.mgmt_client.action_groups.update(resource_group.name, ACTION_GROUP_NAME, BODY)

        # Create or update an alert rule[put]
        BODY = {
          "location": "West US",
          "properties": {
            "name": "chiricutin",
            "description": "Pura Vida",
            "is_enabled": True,
            "condition": {
              "odata.type": "Microsoft.Azure.Management.Insights.Models.ThresholdRuleCondition",
              "data_source": {
                "odata.type": "Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource",
                "resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Web/sites/" + SITE_NAME + "",
                "metric_name": "Requests"
              },
              "operator": "GreaterThan",
              "threshold": "3",
              "window_size": "PT5M",
              "time_aggregation": "Total"
            },
            "last_updated_time": "2016-11-23T21:23:52.0221265Z",
            "actions": []
          }
        }
        result = self.mgmt_client.alert_rules.create_or_update(resource_group.name, ALERTRULE_NAME, BODY)

        # Patch an alert rule[patch]
        BODY = {
          "tags": {
            "$type": "Microsoft.WindowsAzure.Management.Common.Storage.CasePreservedDictionary"
          },
          "properties": {
            "name": "chiricutin",
            "description": "Pura Vida",
            "is_enabled": True,
            "condition": {
              "odata.type": "Microsoft.Azure.Management.Insights.Models.ThresholdRuleCondition",
              "data_source": {
                "odata.type": "Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource",
                "resource_uri": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Web/sites/" + SITE_NAME + "",
                "metric_name": "Requests"
              },
              "operator": "GreaterThan",
              "threshold": "3",
              "window_size": "PT5M",
              "time_aggregation": "Total"
            },
            "last_updated_time": "2016-11-23T21:23:52.0221265Z",
            "actions": []
          }
        }
        result = self.mgmt_client.alert_rules.update(resource_group.name, ALERTRULE_NAME, BODY)

        # Patch a log profile[patch]
        BODY = {
          "tags": {
            "key1": "value1"
          },
          "properties": {
            "locations": [
              "global"
            ],
            "categories": [
              "Write",
              "Delete",
              "Action"
            ],
            "retention_policy": {
              "enabled": True,
              "days": "3"
            },
            "storage_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
            "service_bus_rule_id": ""
          }
        }
        result = self.mgmt_client.log_profiles.update(LOGPROFILE_NAME, BODY)

        # Calculate baseline[post]
        BODY = {
          "sensitivities": [
            "Low",
            "Medium"
          ],
          "values": [
            "61",
            "62"
          ]
        }
        result = self.mgmt_client.metric_baseline.calculate_baseline({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME, BODY)

        # Delete rule[delete]
        result = self.mgmt_client.scheduled_query_rules.delete(resource_group.name, SCHEDULED_QUERY_RULE_NAME)

        # Delete an activity log alert[delete]
        result = self.mgmt_client.activity_log_alerts.delete(resource_group.name, ACTIVITY_LOG_ALERT_NAME)

        # Delete an autoscale setting[delete]
        result = self.mgmt_client.autoscale_settings.delete(resource_group.name, AUTOSCALESETTING_NAME)

        # Delete an alert rule[delete]
        result = self.mgmt_client.metric_alerts.delete(resource_group.name, METRIC_ALERT_NAME)

        # Delete an action group[delete]
        result = self.mgmt_client.action_groups.delete(resource_group.name, ACTION_GROUP_NAME)

        # Delete an alert rule[delete]
        result = self.mgmt_client.metric_alerts.delete(resource_group.name, METRIC_ALERT_NAME)

        # Delete log profile[delete]
        result = self.mgmt_client.log_profiles.delete(LOGPROFILE_NAME)

        # Deletes the diagnostic setting[delete]
        result = self.mgmt_client.diagnostic_settings.delete({RESOURCE_URI}_NAME, MICROSOFT.INSIGHT_NAME)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
