# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

# coverd ops:
#   management_locks: /16
#   authorization_operations: 1/1

import unittest

import azure.mgmt.resource
import azure.mgmt.resource.resources.v2019_07_01
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtResourceLocksTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtResourceLocksTest, self).setUp()
        self.locks_client = self.create_mgmt_client(
            azure.mgmt.resource.ManagementLockClient
        )

        self.resource_client_v07 = self.create_mgmt_client(
            azure.mgmt.resource.resources.v2019_07_01.ResourceManagementClient
        )

    @unittest.skip("Forbidden")
    def test_locks_at_subscription_level(self):
        pass

    @unittest.skip("Forbidden")
    def test_locks_by_scope(self):
        pass

    @unittest.skip("Forbidden")
    @ResourceGroupPreparer()
    def test_locks_at_resource_level(self, resource_group, location):
        lock_name = 'pylockrg'
        resource_name = self.get_resource_name("pytestavset")

        # create resource
        create_result = self.resource_client_v07.resources.begin_create_or_update(
            resource_group_name=resource_group.name,
            resource_provider_namespace="Microsoft.Compute",
            parent_resource_path="",
            resource_type="availabilitySets",
            resource_name=resource_name,
            parameters={'location': self.region},
            # api_version="2019-07-01"
        )

        lock = self.locks_client.management_locks.create_or_update_at_resource_level(
            resource_group_name=resource_group.name,
            resource_provider_namespace="Microsoft.Compute",
            parent_resource_path="",
            resource_type="availabilitySets",
            resource_name=resource_name,
            lock_name=lock_name,
            parameters={
                'level': 'CanNotDelete'
            }
        )
        self.assertIsNotNone(lock)

        self.locks_client.management_locks.get_at_resource_group_level(
            resource_group_name=resource_group.name,
            resource_provider_namespace="Microsoft.Compute",
            parent_resource_path="",
            resource_type="availabilitySets",
            resource_name=resource_name,
            lock_name=lock_name,
        )

        locks = list(self.locks_client.management_locks.list_at_resource_group_level(
            resource_group_name=resource_group.name,
            resource_provider_namespace="Microsoft.Compute",
            parent_resource_path="",
            resource_type="availabilitySets",
            resource_name=resource_name,
        ))
        self.assertEqual(len(locks), 1)

        lock = self.locks_client.management_locks.delete_at_resource_group_level(
            resource_group_name=resource_group.name,
            resource_provider_namespace="Microsoft.Compute",
            parent_resource_path="",
            resource_type="availabilitySets",
            resource_name=resource_name,
            lock_name=lock_name,
        )

        # delete resource
        async_delete = self.resource_client_v07.resource_groups.begin_delete(
            resource_group.name
        )
        async_delete.wait()


    @unittest.skip("Forbidden")
    @ResourceGroupPreparer()
    def test_locks_at_resource_group_level(self, resource_group, location):
        lock_name = 'pylockrg'

        lock = self.locks_client.management_locks.create_or_update_at_resource_group_level(
            resource_group.name,
            lock_name,
            {
                'level': 'CanNotDelete'
            }
        )
        self.assertIsNotNone(lock)

        self.locks_client.management_locks.get_at_resource_group_level(
            resource_group.name,
            lock_name
        )

        locks = list(self.locks_client.management_locks.list_at_resource_group_level(
            resource_group.name
        ))
        self.assertEqual(len(locks), 1)

        lock = self.locks_client.management_locks.delete_at_resource_group_level(
            resource_group.name,
            lock_name
        )

    def test_operations(self):
        self.locks_client.authorization_operations.list()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
