# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 5
# Methods Covered : 3
# Examples Total  : 3
# Examples Tested : 3
# Coverage %      : 60
# ----------------------

import unittest

import azure.mgmt.resource.subscriptions
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtSubscriptionClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtSubscriptionClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.resource.subscriptions.SubscriptionClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_resource(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Get locations with a subscription id[get]
        result = self.mgmt_client.subscriptions.list_locations()

        # Get all subscriptions.[get]
        result = self.mgmt_client.subscriptions.list()

        # Get a single subscription.[get]
        result = self.mgmt_client.subscriptions.get()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
