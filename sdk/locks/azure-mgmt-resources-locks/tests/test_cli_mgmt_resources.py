# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------


# TEST SCENARIO COVERAGE
# ----------------------
# Methods Total   : 17
# Methods Covered : 0
# Examples Total  : 0
# Examples Tested : 0
# Coverage %      : NaN
# ----------------------

import unittest

import azure.mgmt.resources.locks
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtManagementLockClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtManagementLockClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.resources.locks.ManagementLockClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_resources(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
