# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 6
# Methods Covered : 0
# Examples Total  : 0
# Examples Tested : 0
# Coverage %      : NaN
# ----------------------

import unittest

import azure.mgmt.resource.links
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtManagementLinkClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtManagementLinkClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.resource.links.ManagementLinkClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_resource(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
