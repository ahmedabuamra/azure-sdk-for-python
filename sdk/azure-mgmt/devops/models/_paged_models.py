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

from msrest.paging import Paged


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <microsoft.devops.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class PipelineTemplateDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PipelineTemplateDefinition <microsoft.devops.models.PipelineTemplateDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PipelineTemplateDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(PipelineTemplateDefinitionPaged, self).__init__(*args, **kwargs)
class PipelinePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Pipeline <microsoft.devops.models.Pipeline>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Pipeline]'}
    }

    def __init__(self, *args, **kwargs):

        super(PipelinePaged, self).__init__(*args, **kwargs)
