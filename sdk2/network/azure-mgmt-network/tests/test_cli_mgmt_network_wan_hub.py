# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 68
# Methods Covered : 68
# Examples Total  : 68
# Examples Tested : 68
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

        # VpnSiteCreate[put]
        BODY = {
          "tags": {
            "key1": "value1"
          },
          "location": "West US",
          "properties": {
            "virtual_wan": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualWANs/" + VIRTUAL_WAN_NAME + ""
            },
            "address_space": {
              "address_prefixes": [
                "10.0.0.0/16"
              ]
            },
            "is_security_site": False,
            "vpn_site_links": [
              {
                "name": "vpnSiteLink1",
                "properties": {
                  "ip_address": "50.50.50.56",
                  "link_properties": {
                    "link_provider_name": "vendor1",
                    "link_speed_in_mbps": "0"
                  },
                  "bgp_properties": {
                    "bgp_peering_address": "192.168.0.0",
                    "asn": "1234"
                  }
                }
              }
            ]
          }
        }
        result = self.mgmt_client.vpn_sites.create_or_update(resource_group.name, VPN_SITE_NAME, BODY)
        result = result.result()

        # VpnGatewayPut[put]
        BODY = {
          "location": "westcentralus",
          "tags": {
            "key1": "value1"
          },
          "properties": {
            "virtual_hub": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualHubs/" + VIRTUAL_HUB_NAME + ""
            },
            "connections": [
              {
                "name": "vpnConnection1",
                "properties": {
                  "remote_vpn_site": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/vpnSites/" + VPN_SITE_NAME + ""
                  },
                  "vpn_link_connections": [
                    {
                      "name": "Connection-Link1",
                      "properties": {
                        "vpn_site_link": {
                          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/vpnSites/" + VPN_SITE_NAME + "/vpnSiteLinks/" + VPN_SITE_LINK_NAME + ""
                        },
                        "connection_bandwidth": "200",
                        "vpn_connection_protocol_type": "IKEv2",
                        "shared_key": "key"
                      }
                    }
                  ]
                }
              }
            ],
            "bgp_settings": {
              "asn": "65515",
              "peer_weight": "0"
            }
          }
        }
        result = self.mgmt_client.vpn_gateways.create_or_update(resource_group.name, VPN_GATEWAY_NAME, BODY)
        result = result.result()

        # VirtualWANCreate[put]
        BODY = {
          "location": "West US",
          "tags": {
            "key1": "value1"
          },
          "properties": {
            "disable_vpn_encryption": False,
            "type": "Basic"
          }
        }
        result = self.mgmt_client.virtual_wans.create_or_update(resource_group.name, VIRTUAL_WAN_NAME, BODY)
        result = result.result()

        # VirtualHubPut[put]
        BODY = {
          "location": "West US",
          "tags": {
            "key1": "value1"
          },
          "properties": {
            "virtual_wan": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualWans/" + VIRTUAL_WAN_NAME + ""
            },
            "address_prefix": "10.168.0.0/24",
            "sku": "Basic"
          }
        }
        result = self.mgmt_client.virtual_hubs.create_or_update(resource_group.name, VIRTUAL_HUB_NAME, BODY)
        result = result.result()

        # Create VirtualRouter[put]
        BODY = {
          "tags": {
            "key1": "value1"
          },
          "location": "West US",
          "properties": {
            "hosted_gateway": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworkGateways/" + VIRTUAL_NETWORK_GATEWAY_NAME + ""
            }
          }
        }
        result = self.mgmt_client.virtual_routers.create_or_update(resource_group.name, VIRTUAL_ROUTER_NAME, BODY)
        result = result.result()

        # P2SVpnGatewayPut[put]
        BODY = {
          "location": "West US",
          "tags": {
            "key1": "value1"
          },
          "properties": {
            "virtual_hub": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualHubs/" + VIRTUAL_HUB_NAME + ""
            },
            "vpn_server_configuration": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/vpnServerConfigurations/" + VPN_SERVER_CONFIGURATION_NAME + ""
            },
            "p2sconnection_configurations": [
              {
                "name": "P2SConnectionConfig1",
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/p2sVpnGateways/" + P2S_VPN_GATEWAY_NAME + "/p2sConnectionConfigurations/" + P2S_CONNECTION_CONFIGURATION_NAME + "",
                "properties": {
                  "vpn_client_address_pool": {
                    "address_prefixes": [
                      "101.3.0.0/16"
                    ]
                  }
                }
              }
            ],
            "vpn_gateway_scale_unit": "1"
          }
        }
        result = self.mgmt_client.p2s_vpn_gateways.create_or_update(resource_group.name, P2SVPN_GATEWAY_NAME, BODY)
        result = result.result()

        # VpnServerConfigurationCreate[put]
        BODY = {
          "tags": {
            "key1": "value1"
          },
          "location": "West US",
          "properties": {
            "vpn_protocols": [
              "IkeV2"
            ],
            "vpn_client_ipsec_policies": [
              {
                "sa_life_time_seconds": "86472",
                "sa_data_size_kilobytes": "429497",
                "ipsec_encryption": "AES256",
                "ipsec_integrity": "SHA256",
                "ike_encryption": "AES256",
                "ike_integrity": "SHA384",
                "dh_group": "DHGroup14",
                "pfs_group": "PFS14"
              }
            ],
            "vpn_client_root_certificates": [
              {
                "name": "vpnServerConfigVpnClientRootCert1",
                "public_cert_data": "MIIC5zCCAc+gAwIBAgIQErQ0Hk4aDJxIA+Q5RagB+jANBgkqhkiG9w0BAQsFADAWMRQwEgYDVQQDDAtQMlNSb290Q2VydDAeFw0xNzEyMTQyMTA3MzhaFw0xODEyMTQyMTI3MzhaMBYxFDASBgNVBAMMC1AyU1Jvb3RDZXJ0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArP7/NQXmW7cQ/ZR1mv3Y3I29Lt7HTOqzo/1KUOoVH3NItbQIRAQbwKy3UWrOFz4eGNX2GWtNRMdCyWsKeqy9Ltsdfcm1IbKXkl84DFeU/ZacXu4Dl3xX3gV5du4TLZjEowJELyur11Ea2YcjPRQ/FzAF9/hGuboS1HZQEPLx4FdUs9OxCYOtc0MxBCwLfVTTRqarb0Ne+arNYd4kCzIhAke1nOyKAJBda5ZL+VHy3S5S8qGlD46jm8HXugmAkUygS4oIIXOmj/1O9sNAi3LN60zufSzCmP8Rm/iUGX+DHAGGiXxwZOKQLEDaZXKqoHjMPP0XudmSWwOIbyeQVrLhkwIDAQABozEwLzAOBgNVHQ8BAf8EBAMCAgQwHQYDVR0OBBYEFEfeNU2trYxNLF9ONmuJUsT13pKDMA0GCSqGSIb3DQEBCwUAA4IBAQBmM6RJzsGGipxyMhimHKN2xlkejhVsgBoTAhOU0llW9aUSwINJ9zFUGgI8IzUFy1VG776fchHp0LMRmPSIUYk5btEPxbsrPtumPuMH8EQGrS+Rt4pD+78c8H1fEPkq5CmDl/PKu4JoFGv+aFcE+Od0hlILstIF10Qysf++QXDolKfzJa/56bgMeYKFiju73loiRM57ns8ddXpfLl792UVpRkFU62LNns6Y1LKTwapmUF4IvIuAIzd6LZNOQng64LAKXtKnViJ1JQiXwf4CEzhgvAti3/ejpb3U90hsrUcyZi6wBv9bZLcAJRWpz61JNYliM1d1grSwQDKGXNQE4xuN"
              }
            ],
            "vpn_client_revoked_certificates": [
              {
                "name": "vpnServerConfigVpnClientRevokedCert1",
                "thumbprint": "83FFBFC8848B5A5836C94D0112367E16148A286F"
              }
            ],
            "radius_server_address": "8.9.9.9",
            "radius_server_secret": "123_abc",
            "radius_server_root_certificates": [
              {
                "name": "vpnServerConfigRadiusServerRootCer1",
                "public_cert_data": "MIIC5zCCAc+gAwIBAgIQErQ0Hk4aDJxIA+Q5RagB+jANBgkqhkiG9w0BAQsFADAWMRQwEgYDVQQDDAtQMlNSb290Q2VydDAeFw0xNzEyMTQyMTA3MzhaFw0xODEyMTQyMTI3MzhaMBYxFDASBgNVBAMMC1AyU1Jvb3RDZXJ0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArP7/NQXmW7cQ/ZR1mv3Y3I29Lt7HTOqzo/1KUOoVH3NItbQIRAQbwKy3UWrOFz4eGNX2GWtNRMdCyWsKeqy9Ltsdfcm1IbKXkl84DFeU/ZacXu4Dl3xX3gV5du4TLZjEowJELyur11Ea2YcjPRQ/FzAF9/hGuboS1HZQEPLx4FdUs9OxCYOtc0MxBCwLfVTTRqarb0Ne+arNYd4kCzIhAke1nOyKAJBda5ZL+VHy3S5S8qGlD46jm8HXugmAkUygS4oIIXOmj/1O9sNAi3LN60zufSzCmP8Rm/iUGX+DHAGGiXxwZOKQLEDaZXKqoHjMPP0XudmSWwOIbyeQVrLhkwIDAQABozEwLzAOBgNVHQ8BAf8EBAMCAgQwHQYDVR0OBBYEFEfeNU2trYxNLF9ONmuJUsT13pKDMA0GCSqGSIb3DQEBCwUAA4IBAQBmM6RJzsGGipxyMhimHKN2xlkejhVsgBoTAhOU0llW9aUSwINJ9zFUGgI8IzUFy1VG776fchHp0LMRmPSIUYk5btEPxbsrPtumPuMH8EQGrS+Rt4pD+78c8H1fEPkq5CmDl/PKu4JoFGv+aFcE+Od0hlILstIF10Qysf++QXDolKfzJa/56bgMeYKFiju73loiRM57ns8ddXpfLl792UVpRkFU62LNns6Y1LKTwapmUF4IvIuAIzd6LZNOQng64LAKXtKnViJ1JQiXwf4CEzhgvAti3/ejpb3U90hsrUcyZi6wBv9bZLcAJRWpz61JNYliM1d1grSwQDKGXNQE4xuM"
              }
            ],
            "radius_client_root_certificates": [
              {
                "name": "vpnServerConfigRadiusClientRootCert1",
                "thumbprint": "83FFBFC8848B5A5836C94D0112367E16148A286F"
              }
            ]
          }
        }
        result = self.mgmt_client.vpn_server_configurations.create_or_update(resource_group.name, VPN_SERVER_CONFIGURATION_NAME, BODY)
        result = result.result()

        # Create Virtual Router Peering[put]
        BODY = {
          "properties": {
            "peer_ip": "192.168.1.5",
            "peer_asn": "20000"
          }
        }
        result = self.mgmt_client.virtual_router_peerings.create_or_update(resource_group.name, VIRTUAL_ROUTER_NAME, PEERING_NAME, BODY)
        result = result.result()

        # VirtualHubRouteTableV2Put[put]
        BODY = {
          "properties": {
            "routes": [
              {
                "destination_type": "CIDR",
                "destinations": [
                  "20.10.0.0/16",
                  "20.20.0.0/16"
                ],
                "next_hop_type": "IPAddress",
                "next_hops": [
                  "10.0.0.68"
                ]
              },
              {
                "destination_type": "CIDR",
                "destinations": [
                  "0.0.0.0/0"
                ],
                "next_hop_type": "IPAddress",
                "next_hops": [
                  "10.0.0.68"
                ]
              }
            ],
            "attached_connections": [
              "All_Vnets"
            ]
          }
        }
        result = self.mgmt_client.virtual_hub_route_table_v2s.create_or_update(resource_group.name, VIRTUAL_HUB_NAME, ROUTE_TABLE_NAME, BODY)
        result = result.result()

        # VpnConnectionPut[put]
        BODY = {
          "properties": {
            "remote_vpn_site": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/vpnSites/" + VPN_SITE_NAME + ""
            },
            "vpn_link_connections": [
              {
                "name": "Connection-Link1",
                "properties": {
                  "vpn_site_link": {
                    "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/vpnSites/" + VPN_SITE_NAME + "/vpnSiteLinks/" + VPN_SITE_LINK_NAME + ""
                  },
                  "connection_bandwidth": "200",
                  "vpn_connection_protocol_type": "IKEv2",
                  "shared_key": "key"
                }
              }
            ]
          }
        }
        result = self.mgmt_client.vpn_connections.create_or_update(resource_group.name, VPN_GATEWAY_NAME, VPN_CONNECTION_NAME, BODY)
        result = result.result()

        # VpnSiteLinkConnectionGet[get]
        result = self.mgmt_client.vpn_site_link_connections.get(resource_group.name, VPN_GATEWAY_NAME, VPN_CONNECTION_NAME, VPN_LINK_CONNECTION_NAME)

        # HubVirtualNetworkConnectionGet[get]
        result = self.mgmt_client.hub_virtual_network_connections.get(resource_group.name, VIRTUAL_HUB_NAME, HUB_VIRTUAL_NETWORK_CONNECTION_NAME)

        # VpnSiteLinkConnectionList[get]
        result = self.mgmt_client.vpn_link_connections.list_by_vpn_connection(resource_group.name, VPN_GATEWAY_NAME, VPN_CONNECTION_NAME)

        # VpnConnectionGet[get]
        result = self.mgmt_client.vpn_connections.get(resource_group.name, VPN_GATEWAY_NAME, VPN_CONNECTION_NAME)

        # VirtualHubVirtualHubRouteTableV2Get[get]
        result = self.mgmt_client.virtual_hub_route_table_v2s.get(resource_group.name, VIRTUAL_HUB_NAME, ROUTE_TABLE_NAME)

        # Get Virtual Router Peering[get]
        result = self.mgmt_client.virtual_router_peerings.get(resource_group.name, VIRTUAL_ROUTER_NAME, PEERING_NAME)

        # VpnSiteGet[get]
        result = self.mgmt_client.vpn_site_links.get(resource_group.name, VPN_SITE_NAME, VPN_SITE_LINK_NAME)

        # HubVirtualNetworkConnectionList[get]
        result = self.mgmt_client.hub_virtual_network_connections.list(resource_group.name, VIRTUAL_HUB_NAME)

        # supportedSecurityProviders[get]
        result = self.mgmt_client..supported_security_providers(resource_group.name, VIRTUAL_WAN_NAME)

        # VpnServerConfigurationGet[get]
        result = self.mgmt_client.vpn_server_configurations.get(resource_group.name, VPN_SERVER_CONFIGURATION_NAME)

        # List all Virtual Router Peerings for a given Virtual Router[get]
        result = self.mgmt_client.virtual_router_peerings.list(resource_group.name, VIRTUAL_ROUTER_NAME)

        # VpnConnectionList[get]
        result = self.mgmt_client.vpn_connections.list_by_vpn_gateway(resource_group.name, VPN_GATEWAY_NAME)

        # VirtualHubRouteTableV2List[get]
        result = self.mgmt_client.virtual_hub_route_table_v2s.list(resource_group.name, VIRTUAL_HUB_NAME)

        # VpnSiteLinkListByVpnSite[get]
        result = self.mgmt_client.vpn_site_links.list_by_vpn_site(resource_group.name, VPN_SITE_NAME)

        # Get VirtualRouter[get]
        result = self.mgmt_client.virtual_routers.get(resource_group.name, VIRTUAL_ROUTER_NAME)

        # P2SVpnGatewayGet[get]
        result = self.mgmt_client.p2s_vpn_gateways.get(resource_group.name, P2SVPN_GATEWAY_NAME)

        # VirtualHubGet[get]
        result = self.mgmt_client.virtual_hubs.get(resource_group.name, VIRTUAL_HUB_NAME)

        # VpnGatewayGet[get]
        result = self.mgmt_client.vpn_gateways.get(resource_group.name, VPN_GATEWAY_NAME)

        # VirtualWANGet[get]
        result = self.mgmt_client.virtual_wans.get(resource_group.name, VIRTUAL_WAN_NAME)

        # VpnSiteGet[get]
        result = self.mgmt_client.vpn_site_links.get(resource_group.name, VPN_SITE_NAME, VPN_SITE_LINK_NAME)

        # VpnServerConfigurationListByResourceGroup[get]
        result = self.mgmt_client.vpn_server_configurations.list_by_resource_group(resource_group.name)

        # P2SVpnGatewayListByResourceGroup[get]
        result = self.mgmt_client.p2s_vpn_gateways.list_by_resource_group(resource_group.name)

        # List all Virtual Router for a given resource group[get]
        result = self.mgmt_client.virtual_routers.list_by_resource_group(resource_group.name)

        # VpnGatewayListByResourceGroup[get]
        result = self.mgmt_client.vpn_gateways.list_by_resource_group(resource_group.name)

        # VirtualHubListByResourceGroup[get]
        result = self.mgmt_client.virtual_hubs.list_by_resource_group(resource_group.name)

        # VirtualWANListByResourceGroup[get]
        result = self.mgmt_client.virtual_wans.list_by_resource_group(resource_group.name)

        # VpnSiteListByResourceGroup[get]
        result = self.mgmt_client.vpn_sites.list_by_resource_group(resource_group.name)

        # VpnServerConfigurationList[get]
        result = self.mgmt_client.vpn_server_configurations.list()

        # P2SVpnGatewayListBySubscription[get]
        result = self.mgmt_client.p2s_vpn_gateways.list()

        # List all Virtual Routers for a given subscription[get]
        result = self.mgmt_client.virtual_routers.list()

        # VirtualHubList[get]
        result = self.mgmt_client.virtual_hubs.list()

        # VpnGatewayListBySubscription[get]
        result = self.mgmt_client.vpn_gateways.list()

        # VirtualWANList[get]
        result = self.mgmt_client.virtual_wans.list()

        # VpnSiteList[get]
        result = self.mgmt_client.vpn_sites.list()

        # P2SVpnGatewayGetConnectionHealthDetailed[post]
        BODY = {
          "vpn_user_names_filter": [
            "vpnUser1",
            "vpnUser2"
          ],
          "output_blob_sas_url": "https://blobcortextesturl.blob.core.windows.net/folderforconfig/p2sconnectionhealths?sp=rw&se=2018-01-10T03%3A42%3A04Z&sv=2017-04-17&sig=WvXrT5bDmDFfgHs%2Brz%2BjAu123eRCNE9BO0eQYcPDT7pY%3D&sr=b"
        }
        result = self.mgmt_client.p2s_vpn_gateways.get_p2s_vpn_connection_health_detailed(resource_group.name, P2SVPN_GATEWAY_NAME, BODY)
        result = result.result()

        # Disconnect VpnConnections from P2sVpn Gateway[post]
        BODY = {
          "vpn_connection_ids": [
            "vpnconnId1",
            "vpnconnId2"
          ]
        }
        result = self.mgmt_client.p2s_vpn_gateways.disconnect_p2s_vpn_connections(resource_group.name, P2SVPN_GATEWAY_NAME, BODY)
        result = result.result()

        # P2SVpnGatewayGetConnectionHealth[post]
        result = self.mgmt_client.p2s_vpn_gateways.get_p2s_vpn_connection_health(resource_group.name, P2SVPN_GATEWAY_NAME)
        result = result.result()

        # VpnServerConfigurationUpdate[patch]
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          }
        }
        result = self.mgmt_client.vpn_server_configurations.update_tags(resource_group.name, VPN_SERVER_CONFIGURATION_NAME, BODY)

        # GenerateP2SVpnGatewayVPNProfile[post]
        BODY = {
          "authentication_method": "EAPTLS"
        }
        result = self.mgmt_client.p2s_vpn_gateways.generate_vpn_profile(resource_group.name, P2SVPN_GATEWAY_NAME, BODY)
        result = result.result()

        # GetVirtualWanVpnServerConfigurations[post]
        result = self.mgmt_client.vpn_server_configurations_associated_with_virtual_wan.list(resource_group.name, VIRTUAL_WAN_NAME)
        result = result.result()

        # GenerateVirtualWanVpnServerConfigurationVpnProfile[post]
        BODY = {
          "vpn_server_configuration_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/vpnServerConfigurations/" + VPN_SERVER_CONFIGURATION_NAME + "",
          "authentication_method": "EAPTLS"
        }
        result = self.mgmt_client..generatevirtualwanvpnserverconfigurationvpnprofile(resource_group.name, VIRTUAL_WAN_NAME, BODY)
        result = result.result()

        # VpnSitesConfigurationDownload[post]
        BODY = {
          "vpn_sites": [
            "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/vpnSites/abc"
          ],
          "output_blob_sas_url": "https://blobcortextesturl.blob.core.windows.net/folderforconfig/vpnFile?sp=rw&se=2018-01-10T03%3A42%3A04Z&sv=2017-04-17&sig=WvXrT5bDmDFfgHs%2Brz%2BjAu123eRCNE9BO0eQYcPDT7pY%3D&sr=b"
        }
        result = self.mgmt_client.vpn_sites_configuration.download(resource_group.name, VIRTUAL_WAN_NAME, BODY)
        result = result.result()

        # ResetVpnGateway[post]
        result = self.mgmt_client.vpn_gateways.reset(resource_group.name, VPN_GATEWAY_NAME)
        result = result.result()

        # P2SVpnGatewayUpdate[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.p2s_vpn_gateways.update_tags(resource_group.name, P2SVPN_GATEWAY_NAME, BODY)

        # VirtualHubUpdate[patch]
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          }
        }
        result = self.mgmt_client.virtual_hubs.update_tags(resource_group.name, VIRTUAL_HUB_NAME, BODY)

        # VirtualWANUpdate[patch]
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          }
        }
        result = self.mgmt_client.virtual_wans.update_tags(resource_group.name, VIRTUAL_WAN_NAME, BODY)

        # VpnGatewayUpdate[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.vpn_gateways.update_tags(resource_group.name, VPN_GATEWAY_NAME, BODY)

        # VpnSiteUpdate[patch]
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          }
        }
        result = self.mgmt_client.vpn_sites.update_tags(resource_group.name, VPN_SITE_NAME, BODY)

        # VpnConnectionDelete[delete]
        result = self.mgmt_client.vpn_connections.delete(resource_group.name, VPN_GATEWAY_NAME, VPN_CONNECTION_NAME)
        result = result.result()

        # VirtualHubRouteTableV2Delete[delete]
        result = self.mgmt_client.virtual_hub_route_table_v2s.delete(resource_group.name, VIRTUAL_HUB_NAME, ROUTE_TABLE_NAME)
        result = result.result()

        # Delete VirtualRouterPeering[delete]
        result = self.mgmt_client.virtual_router_peerings.delete(resource_group.name, VIRTUAL_ROUTER_NAME, PEERING_NAME)
        result = result.result()

        # VpnServerConfigurationDelete[delete]
        result = self.mgmt_client.vpn_server_configurations.delete(resource_group.name, VPN_SERVER_CONFIGURATION_NAME)
        result = result.result()

        # Delete VirtualRouter[delete]
        result = self.mgmt_client.virtual_routers.delete(resource_group.name, VIRTUAL_ROUTER_NAME)
        result = result.result()

        # P2SVpnGatewayDelete[delete]
        result = self.mgmt_client.p2s_vpn_gateways.delete(resource_group.name, P2SVPN_GATEWAY_NAME)
        result = result.result()

        # VpnGatewayDelete[delete]
        result = self.mgmt_client.vpn_gateways.delete(resource_group.name, VPN_GATEWAY_NAME)
        result = result.result()

        # VirtualHubDelete[delete]
        result = self.mgmt_client.virtual_hubs.delete(resource_group.name, VIRTUAL_HUB_NAME)
        result = result.result()

        # VirtualWANDelete[delete]
        result = self.mgmt_client.virtual_wans.delete(resource_group.name, VIRTUAL_WAN_NAME)
        result = result.result()

        # VpnSiteDelete[delete]
        result = self.mgmt_client.vpn_sites.delete(resource_group.name, VPN_SITE_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
