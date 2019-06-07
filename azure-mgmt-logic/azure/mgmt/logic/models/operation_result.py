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

from .operation_result_properties import OperationResultProperties


class OperationResult(OperationResultProperties):
    """The operation result definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param start_time: The start time of the workflow scope repetition.
    :type start_time: datetime
    :param end_time: The end time of the workflow scope repetition.
    :type end_time: datetime
    :param correlation: The correlation properties.
    :type correlation: ~azure.mgmt.logic.models.RunActionCorrelation
    :param status: The status of the workflow scope repetition. Possible
     values include: 'NotSpecified', 'Paused', 'Running', 'Waiting',
     'Succeeded', 'Skipped', 'Suspended', 'Cancelled', 'Failed', 'Faulted',
     'TimedOut', 'Aborted', 'Ignored'
    :type status: str or ~azure.mgmt.logic.models.WorkflowStatus
    :param code: The workflow scope repetition code.
    :type code: str
    :param error:
    :type error: object
    :ivar tracking_id: Gets the tracking id.
    :vartype tracking_id: str
    :ivar inputs: Gets the inputs.
    :vartype inputs: object
    :ivar inputs_link: Gets the link to inputs.
    :vartype inputs_link: ~azure.mgmt.logic.models.ContentLink
    :ivar outputs: Gets the outputs.
    :vartype outputs: object
    :ivar outputs_link: Gets the link to outputs.
    :vartype outputs_link: ~azure.mgmt.logic.models.ContentLink
    :ivar tracked_properties: Gets the tracked properties.
    :vartype tracked_properties: object
    :param retry_history: Gets the retry histories.
    :type retry_history: list[~azure.mgmt.logic.models.RetryHistory]
    :param iteration_count:
    :type iteration_count: int
    """

    _validation = {
        'tracking_id': {'readonly': True},
        'inputs': {'readonly': True},
        'inputs_link': {'readonly': True},
        'outputs': {'readonly': True},
        'outputs_link': {'readonly': True},
        'tracked_properties': {'readonly': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'correlation': {'key': 'correlation', 'type': 'RunActionCorrelation'},
        'status': {'key': 'status', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'error': {'key': 'error', 'type': 'object'},
        'tracking_id': {'key': 'trackingId', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': 'object'},
        'inputs_link': {'key': 'inputsLink', 'type': 'ContentLink'},
        'outputs': {'key': 'outputs', 'type': 'object'},
        'outputs_link': {'key': 'outputsLink', 'type': 'ContentLink'},
        'tracked_properties': {'key': 'trackedProperties', 'type': 'object'},
        'retry_history': {'key': 'retryHistory', 'type': '[RetryHistory]'},
        'iteration_count': {'key': 'iterationCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(OperationResult, self).__init__(**kwargs)
        self.tracking_id = None
        self.inputs = None
        self.inputs_link = None
        self.outputs = None
        self.outputs_link = None
        self.tracked_properties = None
        self.retry_history = kwargs.get('retry_history', None)
        self.iteration_count = kwargs.get('iteration_count', None)