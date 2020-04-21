# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 57
# Methods Covered : 57
# Examples Total  : 59
# Examples Tested : 59
# Coverage %      : 100
# ----------------------

# covered ops:
#   express_route_circuit_authorizations: 4/4
#   express_route_circuit_connections: 4/4
#   express_route_circuit_peerings: 4/4
#   express_route_circuits: 11/11
#   express_route_connections: 4/4
#   express_route_cross_connection_peerings: 4/4
#   express_route_cross_connections: 8/8
#   express_route_gateways: 5/5
#   express_route_links: 2/2
#   express_route_ports_locations: 2/2
#   express_route_ports: 6/6
#   express_route_service_providers: 1/1
#   peer_express_route_circuit_connections: 2/2

import unittest

import azure.mgmt.network.v2019_12_01
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtNetworkTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtNetworkTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.network.v2019_12_01.NetworkManagementClient
        )

    def create_virtual_hub(
        self,
        group_name,
        virtual_wan_name,
        virtual_hub_name
    ):
        result = self.mgmt_client.virtual_wans.begin_create_or_update(
            group_name,
            virtual_wan_name,
            {
              "location": "West US",
              "tags": {
                "key1": "value1"
              },
              "disable_vpn_encryption": False,
              "type": "Basic"
            }
        )
        wan = result.result()

        result = self.mgmt_client.virtual_hubs.begin_create_or_update(
            group_name,
            virtual_hub_name,
            {
              "location": "West US",
              "tags": {
                "key1": "value1"
              },
              "virtual_wan": {
                # "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualWans/virtualWan1"
                "id": wan.id
              },
              "address_prefix": "10.168.0.0/24",
              "sku": "Basic"
            }
        )
        return result.result()
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_network(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"
        SUBSCRIPTION_ID = self.settings.SUBSCRIPTION_ID
        RESOURCE_GROUP = resource_group.name
        PEERING_NAME = "peeringname"
        ROUTE_TABLE_NAME = "routetable"
        ARP_TABLE_NAME = "arptable"
        VIRTUAL_WAN_NAME = "virtualwan"
        VIRTUAL_HUB_NAME = "virtualhub"
        EXPRESS_ROUTE_PORT_NAME = "expressrouteport"
        EXPRESS_ROUTE_CIRCUIT_NAME = "expressroutecircuit"
        ROUTE_TABLES_SUMMARY_NAME = "routetablessummary"
        EXPRESS_ROUTE_CROSS_CONNECTION_NAME = "expressroutecrossconnectionname"
        EXPRESS_ROUTE_GATEWAY_NAME = "expressroutegateway"
        AUTHORIZATION_NAME = "authorizationname"
        EXPRESS_ROUTE_CONNECTION_NAME = "expressrouteconnection"

        vhub = self.create_virtual_hub(RESOURCE_GROUP, VIRTUAL_WAN_NAME, VIRTUAL_HUB_NAME)

        # ExpressRoutePortCreate[put]
        BODY = {
          "location": "westus",
          "peering_location": "peeringLocationName",
          "bandwidth_in_gbps": "100",
          "encapsulation": "QinQ"
        }
        result = self.mgmt_client.express_route_ports.begin_create_or_update(resource_group.name, EXPRESS_ROUTE_PORT_NAME, BODY)
        result = result.result()

        # Create ExpressRouteCircuit[put]
        BODY = {
          "sku": {
            "name": "Standard_MeteredData",
            "tier": "Standard",
            "family": "MeteredData"
          },
          "authorizations": [],
          "peerings": [],
          "allow_classic_operations": False,
          "service_provider_properties": {
            "service_provider_name": "Equinix",
            "peering_location": "Silicon Valley",
            "bandwidth_in_mbps": "200"
          },
          "location": "Brazil South"
        }
        result = self.mgmt_client.express_route_circuits.begin_create_or_update(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, BODY)
        result = result.result()

        # ExpressRouteGatewayCreate[put]
        BODY = {
          "location": "westus",
          "virtual_hub": {
            # "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualHubs/" + VIRTUAL_HUB_NAME + ""
            "id": vhub.id
          },
          "auto_scale_configuration": {
            "bounds": {
            "min": "3"
            }
          }
        }
        result = self.mgmt_client.express_route_gateways.begin_create_create_or_update(resource_group.name, EXPRESS_ROUTE_GATEWAY_NAME, BODY)
        result = result.result()

        """
        # Create ExpressRouteCircuit on ExpressRoutePort[put]
        BODY = {
          "location": "westus",
          "sku": {
            "name": "Premium_MeteredData",
            "tier": "Premium",
            "family": "MeteredData"
          },
        "express_route_port": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/expressRoutePorts/" + EXPRESS_ROUTE_PORT_NAME + ""
        },
        "bandwidth_in_gbps": "10"
        }
        result = self.mgmt_client.express_route_circuits.create_or_update(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, BODY)
        result = result.result()
        """

        # UpdateExpressRouteCrossConnection[put]
        BODY = {
          "service_provider_provisioning_state": "NotProvisioned"
        }
        result = self.mgmt_client.express_route_cross_connections.begin_create_or_update(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME, BODY)
        result = result.result()

        # Create ExpressRouteCircuit Peerings[put]
        BODY = {
          "peer_asn": "200",
          "primary_peer_address_prefix": "192.168.16.252/30",
          "secondary_peer_address_prefix": "192.168.18.252/30",
          "vlan_id": "200"
        }
        result = self.mgmt_client.express_route_circuit_peerings.begin_create_or_update(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, BODY)
        result = result.result()

        # Create ExpressRouteCircuit Authorization[put]
        BODY = {}
        result = self.mgmt_client.express_route_circuit_authorizations.begin_create_or_update(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, AUTHORIZATION_NAME, BODY)
        result = result.result()

        # ExpressRouteCrossConnectionBgpPeeringCreate[put]
        BODY = {
          "peer_asn": "200",
          "primary_peer_address_prefix": "192.168.16.252/30",
          "secondary_peer_address_prefix": "192.168.18.252/30",
          "vlan_id": "200",
          "ipv6peering_config": {
            "primary_peer_address_prefix": "3FFE:FFFF:0:CD30::/126",
            "secondary_peer_address_prefix": "3FFE:FFFF:0:CD30::4/126"
          }
        }
        result = self.mgmt_client.express_route_cross_connection_peerings.begin_create_or_update(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME, PEERING_NAME, BODY)
        result = result.result()

        # ExpressRouteConnectionCreate[put]
        BODY = {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/expressRouteGateways/" + EXPRESS_ROUTE_GATEWAY_NAME + "/expressRouteConnections/" + EXPRESS_ROUTE_CONNECTION_NAME + "",
          "name": "connectionName",
          "routing_weight": "2",
          "authorization_key": "authorizationKey",
          "express_route_circuit_peering": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/expressRouteCircuits/" + EXPRESS_ROUTE_CIRCUIT_NAME + "/peerings/" + PEERING_NAME + ""
          }
        }
        result = self.mgmt_client.express_route_connections.begin_create_or_update(resource_group.name, EXPRESS_ROUTE_GATEWAY_NAME, EXPRESS_ROUTE_CONNECTION_NAME, BODY)
        result = result.result()

        # ExpressRouteCircuitConnectionCreate[put]
        BODY = {
          "express_route_circuit_peering": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/expressRouteCircuits/" + EXPRESS_ROUTE_CIRCUIT_NAME + "/peerings/" + PEERING_NAME + ""
          },
          "peer_express_route_circuit_peering": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/expressRouteCircuits/" + EXPRESS_ROUTE_CIRCUIT_NAME + "/peerings/" + PEERING_NAME + ""
          },
          "authorization_key": "946a1918-b7a2-4917-b43c-8c4cdaee006a",
          "address_prefix": "10.0.0.0/29"
        }
        result = self.mgmt_client.express_route_circuit_connections.create_or_update(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, CONNECTION_NAME, BODY)
        result = result.result()

        # List Peer ExpressRouteCircuit Connection[get]
        result = self.mgmt_client.peer_express_route_circuit_connections.list(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME)

        # PeerExpressRouteCircuitConnectionGet[get]
        # result = self.mgmt_client.peer_express_route_circuit_connections.get(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, PEER_CONNECTION_NAME)

        # ExpressRouteCircuitConnectionGet[get]
        result = self.mgmt_client.express_route_circuit_connections.get(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, CONNECTION_NAME)

        # ExpressRouteConnectionGet[get]
        result = self.mgmt_client.express_route_connections.get(resource_group.name, EXPRESS_ROUTE_GATEWAY_NAME, EXPRESS_ROUTE_CONNECTION_NAME)

        # GetExpressRouteCrossConnectionBgpPeering[get]
        result = self.mgmt_client.express_route_cross_connection_peerings.get(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME, PEERING_NAME)

        # Get ExpressRouteCircuit Authorization[get]
        result = self.mgmt_client.express_route_circuit_authorizations.get(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, AUTHORIZATION_NAME)

        # List ExpressRouteCircuit Connection[get]
        result = self.mgmt_client.express_route_circuit_connections.list(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME)

        # Get ExpressRoute Circuit Peering Traffic Stats[get]
        result = self.mgmt_client.express_route_circuits.get_peering_stats(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME)

        # Get ExpressRouteCircuit Peering[get]
        result = self.mgmt_client.express_route_circuit_peerings.get(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME)

        # ExpressRouteCrossConnectionBgpPeeringList[get]
        result = self.mgmt_client.express_route_cross_connection_peerings.list(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME)

        # ExpressRouteConnectionList[get]
        result = self.mgmt_client.express_route_connections.list(resource_group.name, EXPRESS_ROUTE_GATEWAY_NAME)

        # GetExpressRouteCrossConnection[get]
        result = self.mgmt_client.express_route_cross_connections.get(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME)

        # ExpressRouteLinkGet[get]
        result = self.mgmt_client.express_route_links.get(resource_group.name, EXPRESS_ROUTE_PORT_NAME, LINK_NAME)

        # List ExpressRouteCircuit Authorization[get]
        result = self.mgmt_client.express_route_circuit_authorizations.list(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME)

        # List ExpressRouteCircuit Peerings[get]
        result = self.mgmt_client.express_route_circuit_peerings.list(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME)

        # Get ExpressRoute Circuit Traffic Stats[get]
        result = self.mgmt_client.express_route_circuits.get_stats(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME)

        # ExpressRouteLinkGet[get]
        result = self.mgmt_client.express_route_links.get(resource_group.name, EXPRESS_ROUTE_PORT_NAME, LINK_NAME)

        # Get ExpressRouteCircuit[get]
        result = self.mgmt_client.express_route_circuits.get(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME)

        # ExpressRouteGatewayGet[get]
        result = self.mgmt_client.express_route_gateways.get(resource_group.name, EXPRESS_ROUTE_GATEWAY_NAME)

        # ExpressRoutePortGet[get]
        result = self.mgmt_client.express_route_ports.get(resource_group.name, EXPRESS_ROUTE_PORT_NAME)

        # ExpressRoutePortsLocationGet[get]
        result = self.mgmt_client.express_route_ports_locations.get(EXPRESS_ROUTE_PORTS_LOCATION_NAME)

        # ExpressRouteCrossConnectionListByResourceGroup[get]
        result = self.mgmt_client.express_route_cross_connections.list_by_resource_group(resource_group.name)

        # ExpressRouteGatewayListByResourceGroup[get]
        result = self.mgmt_client.express_route_gateways.list_by_resource_group(resource_group.name)

        # List ExpressRouteCircuits in a resource group[get]
        result = self.mgmt_client.express_route_circuits.list(resource_group.name)

        # ExpressRoutePortListByResourceGroup[get]
        result = self.mgmt_client.express_route_ports.list_by_resource_group(resource_group.name)

        # ExpressRouteCrossConnectionList[get]
        result = self.mgmt_client.express_route_cross_connections.list()

        # List ExpressRoute providers[get]
        result = self.mgmt_client.express_route_service_providers.list()

        # ExpressRoutePortsLocationList[get]
        result = self.mgmt_client.express_route_ports_locations.list()

        # List ExpressRouteCircuits in a subscription[get]
        result = self.mgmt_client.express_route_circuits.list_all()

        # ExpressRouteGatewayListBySubscription[get]
        result = self.mgmt_client.express_route_gateways.list_by_subscription()

        # ExpressRoutePortList[get]
        result = self.mgmt_client.express_route_ports.list()

        # GetExpressRouteCrossConnectionsRouteTableSummary[post]
        result = self.mgmt_client.express_route_cross_connections.begin_list_routes_table_summary(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME, PEERING_NAME, ROUTE_TABLES_SUMMARY_NAME)
        result = result.result()

        # GetExpressRouteCrossConnectionsRouteTable[post]
        result = self.mgmt_client.express_route_cross_connections.begin_list_routes_table(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME, PEERING_NAME, ROUTE_TABLE_NAME)
        result = result.result()

        # List Route Table Summary[post]
        result = self.mgmt_client.express_route_circuits.list_routes_table_summary(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, ROUTE_TABLES_SUMMARY_NAME)
        result = result.result()

        # GetExpressRouteCrossConnectionsArpTable[post]
        result = self.mgmt_client.express_route_cross_connections.begin_list_arp_table(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME, PEERING_NAME, ARP_TABLE_NAME)
        result = result.result()

        # List Route Tables[post]
        result = self.mgmt_client.express_route_circuits.list_routes_table(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, ROUTE_TABLE_NAME)
        result = result.result()

        # List ARP Table[post]
        result = self.mgmt_client.express_route_circuits.list_arp_table(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, ARP_TABLE_NAME)
        result = result.result()

        # UpdateExpressRouteCrossConnectionTags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.express_route_cross_connections.update_tags(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME, BODY["tags"])

        # Update Express Route Circuit Tags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.express_route_circuits.update_tags(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, BODY)

        # ExpressRoutePortUpdateTags[patch]
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        result = self.mgmt_client.express_route_ports.update_tags(resource_group.name, EXPRESS_ROUTE_PORT_NAME, BODY)

        # Delete ExpressRouteCircuitConnection[delete]
        result = self.mgmt_client.express_route_circuit_connections.delete(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, CONNECTION_NAME)
        result = result.result()

        # ExpressRouteConnectionDelete[delete]
        result = self.mgmt_client.express_route_connections.delete(resource_group.name, EXPRESS_ROUTE_GATEWAY_NAME, EXPRESS_ROUTE_CONNECTION_NAME)
        result = result.result()

        # DeleteExpressRouteCrossConnectionBgpPeering[delete]
        result = self.mgmt_client.express_route_cross_connection_peerings.begin_delete(resource_group.name, EXPRESS_ROUTE_CROSS_CONNECTION_NAME, PEERING_NAME)
        result = result.result()

        # Delete ExpressRouteCircuit Authorization[delete]
        result = self.mgmt_client.express_route_circuit_authorizations.begin_delete(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, AUTHORIZATION_NAME)
        result = result.result()

        # Delete ExpressRouteCircuit Peerings[delete]
        result = self.mgmt_client.express_route_circuit_peerings.begin_delete(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME)
        result = result.result()

        # ExpressRouteGatewayDelete[delete]
        result = self.mgmt_client.express_route_gateways.begin_delete(resource_group.name, EXPRESS_ROUTE_GATEWAY_NAME)
        result = result.result()

        # Delete ExpressRouteCircuit[delete] TODO: swagger need change
        # result = self.mgmt_client.express_route_circuit_connections.delete(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME, PEERING_NAME, CONNECTION_NAME)
        # result = result.result()

        # DeleteExpressRouteCircuits[delete] TODO: need example
        result = self.mgmt_client.express_route_circuits.begin_delete(resource_group.name, EXPRESS_ROUTE_CIRCUIT_NAME)

        # ExpressRoutePortDelete[delete]
        result = self.mgmt_client.express_route_ports.begin_delete(resource_group.name, EXPRESS_ROUTE_PORT_NAME)
        result = result.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
