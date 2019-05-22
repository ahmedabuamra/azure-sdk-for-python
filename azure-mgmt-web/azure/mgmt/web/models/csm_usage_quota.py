# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CsmUsageQuota(Model):
    """Usage of the quota resource.

    :param unit: Units of measurement for the quota resource.
    :type unit: str
    :param next_reset_time: Next reset time for the resource counter.
    :type next_reset_time: datetime
    :param current_value: The current value of the resource counter.
    :type current_value: long
    :param limit: The resource limit.
    :type limit: long
    :param name: Quota name.
    :type name: ~azure.mgmt.web.models.LocalizableString
    """

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'next_reset_time': {'key': 'nextResetTime', 'type': 'iso-8601'},
        'current_value': {'key': 'currentValue', 'type': 'long'},
        'limit': {'key': 'limit', 'type': 'long'},
        'name': {'key': 'name', 'type': 'LocalizableString'},
    }

    def __init__(self, **kwargs):
        super(CsmUsageQuota, self).__init__(**kwargs)
        self.unit = kwargs.get('unit', None)
        self.next_reset_time = kwargs.get('next_reset_time', None)
        self.current_value = kwargs.get('current_value', None)
        self.limit = kwargs.get('limit', None)
        self.name = kwargs.get('name', None)