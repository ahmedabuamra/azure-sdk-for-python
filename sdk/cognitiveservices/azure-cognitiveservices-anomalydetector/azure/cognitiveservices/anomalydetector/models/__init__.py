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

try:
    from .api_error_py3 import APIError, APIErrorException
    from .point_py3 import Point
    from .request_py3 import Request
    from .entire_detect_response_py3 import EntireDetectResponse
    from .last_detect_response_py3 import LastDetectResponse
    from .time_series_py3 import TimeSeries
    from .time_series_create_request_py3 import TimeSeriesCreateRequest
    from .time_series_list_py3 import TimeSeriesList
    from .time_series_group_py3 import TimeSeriesGroup
    from .time_series_group_create_request_py3 import TimeSeriesGroupCreateRequest
    from .time_series_group_list_py3 import TimeSeriesGroupList
    from .inconsistency_detect_request_py3 import InconsistencyDetectRequest
    from .inconsistency_py3 import Inconsistency
    from .inconsistency_query_request_py3 import InconsistencyQueryRequest
    from .change_point_detect_request_py3 import ChangePointDetectRequest
    from .change_point_detect_response_py3 import ChangePointDetectResponse
    from .change_point_detect_in_time_range_request_py3 import ChangePointDetectInTimeRangeRequest
    from .change_point_detect_in_time_range_response_py3 import ChangePointDetectInTimeRangeResponse
    from .time_series_query_request_py3 import TimeSeriesQueryRequest
    from .time_series_query_response_py3 import TimeSeriesQueryResponse
    from .anomaly_detect_in_time_range_request_py3 import AnomalyDetectInTimeRangeRequest
    from .anomaly_detect_in_time_range_response_py3 import AnomalyDetectInTimeRangeResponse
    from .label_request_py3 import LabelRequest
except (SyntaxError, ImportError):
    from .api_error import APIError, APIErrorException
    from .point import Point
    from .request import Request
    from .entire_detect_response import EntireDetectResponse
    from .last_detect_response import LastDetectResponse
    from .time_series import TimeSeries
    from .time_series_create_request import TimeSeriesCreateRequest
    from .time_series_list import TimeSeriesList
    from .time_series_group import TimeSeriesGroup
    from .time_series_group_create_request import TimeSeriesGroupCreateRequest
    from .time_series_group_list import TimeSeriesGroupList
    from .inconsistency_detect_request import InconsistencyDetectRequest
    from .inconsistency import Inconsistency
    from .inconsistency_query_request import InconsistencyQueryRequest
    from .change_point_detect_request import ChangePointDetectRequest
    from .change_point_detect_response import ChangePointDetectResponse
    from .change_point_detect_in_time_range_request import ChangePointDetectInTimeRangeRequest
    from .change_point_detect_in_time_range_response import ChangePointDetectInTimeRangeResponse
    from .time_series_query_request import TimeSeriesQueryRequest
    from .time_series_query_response import TimeSeriesQueryResponse
    from .anomaly_detect_in_time_range_request import AnomalyDetectInTimeRangeRequest
    from .anomaly_detect_in_time_range_response import AnomalyDetectInTimeRangeResponse
    from .label_request import LabelRequest
from .anomaly_detector_client_enums import (
    Granularity,
    TimeSeriesField,
    LabelType,
    LabelValue,
)

__all__ = [
    'APIError', 'APIErrorException',
    'Point',
    'Request',
    'EntireDetectResponse',
    'LastDetectResponse',
    'TimeSeries',
    'TimeSeriesCreateRequest',
    'TimeSeriesList',
    'TimeSeriesGroup',
    'TimeSeriesGroupCreateRequest',
    'TimeSeriesGroupList',
    'InconsistencyDetectRequest',
    'Inconsistency',
    'InconsistencyQueryRequest',
    'ChangePointDetectRequest',
    'ChangePointDetectResponse',
    'ChangePointDetectInTimeRangeRequest',
    'ChangePointDetectInTimeRangeResponse',
    'TimeSeriesQueryRequest',
    'TimeSeriesQueryResponse',
    'AnomalyDetectInTimeRangeRequest',
    'AnomalyDetectInTimeRangeResponse',
    'LabelRequest',
    'Granularity',
    'TimeSeriesField',
    'LabelType',
    'LabelValue',
]
