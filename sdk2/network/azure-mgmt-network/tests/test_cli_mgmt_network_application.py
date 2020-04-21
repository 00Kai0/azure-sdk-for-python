# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 23
# Methods Covered : 23
# Examples Total  : 23
# Examples Tested : 23
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

        # Create Application Gateway[put]
        BODY = {
          "identity": {
            "type": "UserAssigned",
            "user_assigned_identities": {}
          },
          "location": "eastus",
          "properties": {
            "sku": {
              "name": "Standard_v2",
              "tier": "Standard_v2",
              "capacity": "3"
            },
            "gateway_ipconfigurations": [
              {
                "name": "appgwipc",
                "properties": {
                  "subnet": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                  }
                }
              }
            ],
            "ssl_certificates": [
              {
                "name": "sslcert",
                "properties": {
                  "data": "****",
                  "password": "****"
                }
              },
              {
                "name": "sslcert2",
                "properties": {
                  "key_vault_secret_id": "https://kv/secret"
                }
              }
            ],
            "trusted_root_certificates": [
              {
                "name": "rootcert",
                "properties": {
                  "data": "****"
                }
              },
              {
                "name": "rootcert1",
                "properties": {
                  "key_vault_secret_id": "https://kv/secret"
                }
              }
            ],
            "frontend_ipconfigurations": [
              {
                "name": "appgwfip",
                "properties": {
                  "public_ip_address": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/publicIPAddresses/" + PUBLIC_IP_ADDRESS_NAME + ""
                  }
                }
              }
            ],
            "frontend_ports": [
              {
                "name": "appgwfp",
                "properties": {
                  "port": "443"
                }
              },
              {
                "name": "appgwfp80",
                "properties": {
                  "port": "80"
                }
              }
            ],
            "backend_address_pools": [
              {
                "name": "appgwpool",
                "properties": {
                  "backend_addresses": [
                    {
                      "ip_address": "10.0.1.1"
                    },
                    {
                      "ip_address": "10.0.1.2"
                    }
                  ]
                }
              }
            ],
            "backend_http_settings_collection": [
              {
                "name": "appgwbhs",
                "properties": {
                  "port": "80",
                  "protocol": "Http",
                  "cookie_based_affinity": "Disabled",
                  "request_timeout": "30"
                }
              }
            ],
            "http_listeners": [
              {
                "name": "appgwhl",
                "properties": {
                  "frontend_ipconfiguration": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/frontendIPConfigurations/" + FRONTEND_IPCONFIGURATION_NAME + ""
                  },
                  "frontend_port": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/frontendPorts/" + FRONTEND_PORT_NAME + ""
                  },
                  "protocol": "Https",
                  "ssl_certificate": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/sslCertificates/" + SSL_CERTIFICATE_NAME + ""
                  },
                  "require_server_name_indication": False
                }
              },
              {
                "name": "appgwhttplistener",
                "properties": {
                  "frontend_ipconfiguration": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/frontendIPConfigurations/" + FRONTEND_IPCONFIGURATION_NAME + ""
                  },
                  "frontend_port": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/frontendPorts/" + FRONTEND_PORT_NAME + ""
                  },
                  "protocol": "Http"
                }
              }
            ],
            "url_path_maps": [
              {
                "name": "pathMap1",
                "properties": {
                  "default_backend_address_pool": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/backendAddressPools/" + BACKEND_ADDRESS_POOL_NAME + ""
                  },
                  "default_backend_http_settings": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/backendHttpSettingsCollection/" + BACKEND_HTTP_SETTINGS_COLLECTION_NAME + ""
                  },
                  "default_rewrite_rule_set": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/rewriteRuleSets/" + REWRITE_RULE_SET_NAME + ""
                  },
                  "path_rules": [
                    {
                      "name": "apiPaths",
                      "properties": {
                        "paths": [
                          "/api",
                          "/v1/api"
                        ],
                        "backend_address_pool": {
                          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/backendAddressPools/" + BACKEND_ADDRESS_POOL_NAME + ""
                        },
                        "backend_http_settings": {
                          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/backendHttpSettingsCollection/" + BACKEND_HTTP_SETTINGS_COLLECTION_NAME + ""
                        },
                        "rewrite_rule_set": {
                          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/rewriteRuleSets/" + REWRITE_RULE_SET_NAME + ""
                        }
                      }
                    }
                  ]
                }
              }
            ],
            "request_routing_rules": [
              {
                "name": "appgwrule",
                "properties": {
                  "rule_type": "Basic",
                  "priority": "10",
                  "http_listener": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/httpListeners/" + HTTP_LISTENER_NAME + ""
                  },
                  "backend_address_pool": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/backendAddressPools/" + BACKEND_ADDRESS_POOL_NAME + ""
                  },
                  "backend_http_settings": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/backendHttpSettingsCollection/" + BACKEND_HTTP_SETTINGS_COLLECTION_NAME + ""
                  },
                  "rewrite_rule_set": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/rewriteRuleSets/" + REWRITE_RULE_SET_NAME + ""
                  }
                }
              },
              {
                "name": "appgwPathBasedRule",
                "properties": {
                  "rule_type": "PathBasedRouting",
                  "priority": "20",
                  "http_listener": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/httpListeners/" + HTTP_LISTENER_NAME + ""
                  },
                  "url_path_map": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/urlPathMaps/" + URL_PATH_MAP_NAME + ""
                  }
                }
              }
            ],
            "rewrite_rule_sets": [
              {
                "name": "rewriteRuleSet1",
                "properties": {
                  "rewrite_rules": [
                    {
                      "name": "Set X-Forwarded-For",
                      "rule_sequence": "102",
                      "conditions": [
                        {
                          "variable": "http_req_Authorization",
                          "pattern": "^Bearer",
                          "ignore_case": True,
                          "negate": False
                        }
                      ],
                      "action_set": {
                        "request_header_configurations": [
                          {
                            "header_name": "X-Forwarded-For",
                            "header_value": "{var_add_x_forwarded_for_proxy}"
                          }
                        ],
                        "response_header_configurations": [
                          {
                            "header_name": "Strict-Transport-Security",
                            "header_value": "max-age=31536000"
                          }
                        ],
                        "url_configuration": {
                          "modified_path": "/abc"
                        }
                      }
                    }
                  ]
                }
              }
            ]
          }
        }
        result = self.mgmt_client.application_gateways.create_or_update(resource_group.name, APPLICATION_GATEWAY_NAME, BODY)
        result = result.result()

        # Create application security group[put]
        BODY = {
          "location": "westus"
        }
        result = self.mgmt_client.application_security_groups.create_or_update(resource_group.name, APPLICATION_SECURITY_GROUP_NAME, BODY)
        result = result.result()

        # Get Available Ssl Predefined Policy by name[get]
        result = self.mgmt_client.application_gateways.get_ssl_predefined_policy(APPLICATION_GATEWAY_AVAILABLE_SSL_OPTION_NAME, PREDEFINED_POLICY_NAME)

        # Get Available Ssl Predefined Policies[get]
        result = self.mgmt_client.application_gateways.list_available_ssl_predefined_policies(APPLICATION_GATEWAY_AVAILABLE_SSL_OPTION_NAME)

        # Get application security group[get]
        result = self.mgmt_client.application_security_groups.get(resource_group.name, APPLICATION_SECURITY_GROUP_NAME)

        # Get Available Ssl Options[get]
        result = self.mgmt_client.application_gateways.list_available_ssl_options(APPLICATION_GATEWAY_AVAILABLE_SSL_OPTION_NAME)

        # Get ApplicationGateway[get]
        result = self.mgmt_client.application_gateways.get(resource_group.name, APPLICATION_GATEWAY_NAME)

        # List load balancers in resource group[get]
        result = self.mgmt_client.application_security_groups.list(resource_group.name)

        # Lists all application gateways in a resource group[get]
        result = self.mgmt_client.application_gateways.list(resource_group.name)

        # Get Available Server Variables[get]
        result = self.mgmt_client.application_gateways.list_available_server_variables()

        # Get Available Response Headers[get]
        result = self.mgmt_client.application_gateways.list_available_response_headers()

        # Get Available Request Headers[get]
        result = self.mgmt_client.application_gateways.list_available_request_headers()

        # Get Available Waf Rule Sets[get]
        result = self.mgmt_client.application_gateways.list_available_waf_rule_sets()

        # List all application security groups[get]
        result = self.mgmt_client.application_security_groups.list_all()

        # Lists all application gateways in a subscription[get]
        result = self.mgmt_client.application_gateways.list_all()

        # Test Backend Health[post]
        BODY = {
          "protocol": "Http",
          "pick_host_name_from_backend_http_settings": True,
          "path": "/",
          "timeout": "30",
          "backend_address_pool": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/backendaddressPools/" + BACKENDADDRESS_POOL_NAME + ""
          },
          "backend_http_settings": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/applicationGateways/" + APPLICATION_GATEWAY_NAME + "/backendHttpSettingsCollection/" + BACKEND_HTTP_SETTINGS_COLLECTION_NAME + ""
          }
        }
        result = self.mgmt_client.application_gateways.backend_health_on_demand(resource_group.name, APPLICATION_GATEWAY_NAME, BODY)
        result = result.result()

        # Get Backend Health[post]
        result = self.mgmt_client.application_gateways.backend_health(resource_group.name, APPLICATION_GATEWAY_NAME)
        result = result.result()

        # Update application security group tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.application_security_groups.update_tags(resource_group.name, APPLICATION_SECURITY_GROUP_NAME, BODY)

        # Start Application Gateway[post]
        result = self.mgmt_client.application_gateways.start(resource_group.name, APPLICATION_GATEWAY_NAME)
        result = result.result()

        # Stop Application Gateway[post]
        result = self.mgmt_client.application_gateways.stop(resource_group.name, APPLICATION_GATEWAY_NAME)
        result = result.result()

        # Update Application Gateway tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.application_gateways.update_tags(resource_group.name, APPLICATION_GATEWAY_NAME, BODY)

        # Delete application security group[delete]
        result = self.mgmt_client.application_security_groups.delete(resource_group.name, APPLICATION_SECURITY_GROUP_NAME)
        result = result.result()

        # Delete ApplicationGateway[delete]
        result = self.mgmt_client.application_gateways.delete(resource_group.name, APPLICATION_GATEWAY_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
