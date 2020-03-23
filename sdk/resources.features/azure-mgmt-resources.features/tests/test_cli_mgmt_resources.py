# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 5
# Methods Covered : 5
# Examples Total  : 5
# Examples Tested : 5
# Coverage %      : 100
# ----------------------

import unittest

import azure.mgmt.resources.features
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtFeatureClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtFeatureClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.resources.features.FeatureClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_resources(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"

        # Get feature[get]
        result = self.mgmt_client.features.get(FEATURE_NAME)

        # List provider Features[get]
        result = self.mgmt_client.features.list()

        # List subscription Features[get]
        result = self.mgmt_client.features.list_all()

        # List Features operations[get]
        result = self.mgmt_client..list_operations()

        # Register feature[post]
        result = self.mgmt_client.features.register(FEATURE_NAME)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
