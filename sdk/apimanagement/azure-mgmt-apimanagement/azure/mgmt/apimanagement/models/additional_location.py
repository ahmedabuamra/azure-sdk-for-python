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


class AdditionalLocation(Model):
    """Description of an additional API Management resource location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The location name of the additional region
     among Azure Data center regions.
    :type location: str
    :param sku: Required. SKU properties of the API Management service.
    :type sku:
     ~azure.mgmt.apimanagement.models.ApiManagementServiceSkuProperties
    :ivar public_ip_addresses: Public Static Load Balanced IP addresses of the
     API Management service in the additional location. Available only for
     Basic, Standard and Premium SKU.
    :vartype public_ip_addresses: list[str]
    :ivar private_ip_addresses: Private Static Load Balanced IP addresses of
     the API Management service which is deployed in an Internal Virtual
     Network in a particular additional location. Available only for Basic,
     Standard and Premium SKU.
    :vartype private_ip_addresses: list[str]
    :param virtual_network_configuration: Virtual network configuration for
     the location.
    :type virtual_network_configuration:
     ~azure.mgmt.apimanagement.models.VirtualNetworkConfiguration
    :ivar gateway_regional_url: Gateway URL of the API Management service in
     the Region.
    :vartype gateway_regional_url: str
    """

    _validation = {
        'location': {'required': True},
        'sku': {'required': True},
        'public_ip_addresses': {'readonly': True},
        'private_ip_addresses': {'readonly': True},
        'gateway_regional_url': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'ApiManagementServiceSkuProperties'},
        'public_ip_addresses': {'key': 'publicIPAddresses', 'type': '[str]'},
        'private_ip_addresses': {'key': 'privateIPAddresses', 'type': '[str]'},
        'virtual_network_configuration': {'key': 'virtualNetworkConfiguration', 'type': 'VirtualNetworkConfiguration'},
        'gateway_regional_url': {'key': 'gatewayRegionalUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdditionalLocation, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.sku = kwargs.get('sku', None)
        self.public_ip_addresses = None
        self.private_ip_addresses = None
        self.virtual_network_configuration = kwargs.get('virtual_network_configuration', None)
        self.gateway_regional_url = None