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


class AlertRuleResourcePatch(Model):
    """The alert rule object for patch operations.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param name: Required. the name of the alert rule.
    :type name: str
    :param description: the description of the alert rule that will be
     included in the alert email.
    :type description: str
    :param is_enabled: Required. the flag that indicates whether the alert
     rule is enabled.
    :type is_enabled: bool
    :param condition: Required. the condition that results in the alert rule
     being activated.
    :type condition: ~azure.mgmt.monitor.models.RuleCondition
    :param actions: the array of actions that are performed when the alert
     rule becomes active, and when an alert condition is resolved.
    :type actions: list[~azure.mgmt.monitor.models.RuleAction]
    :ivar last_updated_time: Last time the rule was updated in ISO8601 format.
    :vartype last_updated_time: datetime
    """

    _validation = {
        'name': {'required': True},
        'is_enabled': {'required': True},
        'condition': {'required': True},
        'last_updated_time': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'name': {'key': 'properties.name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'is_enabled': {'key': 'properties.isEnabled', 'type': 'bool'},
        'condition': {'key': 'properties.condition', 'type': 'RuleCondition'},
        'actions': {'key': 'properties.actions', 'type': '[RuleAction]'},
        'last_updated_time': {'key': 'properties.lastUpdatedTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(AlertRuleResourcePatch, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.is_enabled = kwargs.get('is_enabled', None)
        self.condition = kwargs.get('condition', None)
        self.actions = kwargs.get('actions', None)
        self.last_updated_time = None