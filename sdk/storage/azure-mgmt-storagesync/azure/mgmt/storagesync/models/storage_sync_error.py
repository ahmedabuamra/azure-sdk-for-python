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
from msrest.exceptions import HttpOperationError


class StorageSyncError(Model):
    """Error type.

    :param error: Error details of the given entry.
    :type error: ~azure.mgmt.storagesync.models.StorageSyncApiError
    :param innererror: Error details of the given entry.
    :type innererror: ~azure.mgmt.storagesync.models.StorageSyncApiError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'StorageSyncApiError'},
        'innererror': {'key': 'innererror', 'type': 'StorageSyncApiError'},
    }

    def __init__(self, **kwargs):
        super(StorageSyncError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)
        self.innererror = kwargs.get('innererror', None)


class StorageSyncErrorException(HttpOperationError):
    """Server responsed with exception of type: 'StorageSyncError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(StorageSyncErrorException, self).__init__(deserialize, response, 'StorageSyncError', *args)
