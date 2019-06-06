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


class FabricError(Model):
    """The REST API operations for Service Fabric return standard HTTP status
    codes. This type defines the additional information returned from the
    Service Fabric API operations that are not successful.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. Error object containing error code and error
     message.
    :type error: ~azure.servicefabric.models.FabricErrorError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'Error', 'type': 'FabricErrorError'},
    }

    def __init__(self, **kwargs):
        super(FabricError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class FabricErrorException(HttpOperationError):
    """Server responsed with exception of type: 'FabricError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(FabricErrorException, self).__init__(deserialize, response, 'FabricError', *args)