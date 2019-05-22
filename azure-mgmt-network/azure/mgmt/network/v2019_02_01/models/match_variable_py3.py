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


class MatchVariable(Model):
    """Define match variables.

    All required parameters must be populated in order to send to Azure.

    :param variable_name: Required. Match Variable. Possible values include:
     'RemoteAddr', 'RequestMethod', 'QueryString', 'PostArgs', 'RequestUri',
     'RequestHeaders', 'RequestBody', 'RequestCookies'
    :type variable_name: str or
     ~azure.mgmt.network.v2019_02_01.models.WebApplicationFirewallMatchVariable
    :param selector: Describes field of the matchVariable collection
    :type selector: str
    """

    _validation = {
        'variable_name': {'required': True},
    }

    _attribute_map = {
        'variable_name': {'key': 'variableName', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
    }

    def __init__(self, *, variable_name, selector: str=None, **kwargs) -> None:
        super(MatchVariable, self).__init__(**kwargs)
        self.variable_name = variable_name
        self.selector = selector