# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional

import msrest.serialization


class ClassicAdministrator(msrest.serialization.Model):
    """Classic Administrators.

    :param id: The ID of the administrator.
    :type id: str
    :param name: The name of the administrator.
    :type name: str
    :param type: The type of the administrator.
    :type type: str
    :param email_address: The email address of the administrator.
    :type email_address: str
    :param role: The role of the administrator.
    :type role: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'email_address': {'key': 'properties.emailAddress', 'type': 'str'},
        'role': {'key': 'properties.role', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        email_address: Optional[str] = None,
        role: Optional[str] = None,
        **kwargs
    ):
        super(ClassicAdministrator, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.email_address = email_address
        self.role = role


class ClassicAdministratorListResult(msrest.serialization.Model):
    """ClassicAdministrator list result information.

    :param value: An array of administrators.
    :type value: list[~azure.mgmt.authorization.v2015_06_01.models.ClassicAdministrator]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ClassicAdministrator]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ClassicAdministrator"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ClassicAdministratorListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
