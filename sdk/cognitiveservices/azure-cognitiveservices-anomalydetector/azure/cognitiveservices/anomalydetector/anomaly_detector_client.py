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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from .operations.time_series_operations import TimeSeriesOperations
from .operations.time_series_group_operations import TimeSeriesGroupOperations
from . import models


class AnomalyDetectorClientConfiguration(Configuration):
    """Configuration for AnomalyDetectorClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus2.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = '{Endpoint}/anomalydetector/v1.0'

        super(AnomalyDetectorClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-anomalydetector/{}'.format(VERSION))

        self.endpoint = endpoint
        self.credentials = credentials


class AnomalyDetectorClient(SDKClient):
    """The Anomaly Detector API detects anomalies automatically in time series data. It supports two kinds of mode, one is for stateless using, another is for stateful using. In stateless mode, there are three functionalities. Entire Detect is for detecting the whole series with model trained by the time series, Last Detect is detecting last point with model trained by points before. ChangePoint Detect is for detecting trend changes in time series. In stateful mode, user can store time series, the stored time series will be used for detection anomalies. Under this mode, user can still use the above three functionalities by only giving a time range without preparing time series in client side. Besides the above three functionalities, stateful model also provide group based detection and labeling service. By leveraging labeling service user can provide labels for each detection result, these labels will be used for retuning or regenerating detection models. Inconsistency detection is a kind of group based detection, this detection will find inconsistency ones in a set of time series. By using anomaly detector service, business customers can discover incidents and establish a logic flow for root cause analysis.

    :ivar config: Configuration for client.
    :vartype config: AnomalyDetectorClientConfiguration

    :ivar time_series: TimeSeries operations
    :vartype time_series: azure.cognitiveservices.anomalydetector.operations.TimeSeriesOperations
    :ivar time_series_group: TimeSeriesGroup operations
    :vartype time_series_group: azure.cognitiveservices.anomalydetector.operations.TimeSeriesGroupOperations

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus2.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        self.config = AnomalyDetectorClientConfiguration(endpoint, credentials)
        super(AnomalyDetectorClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.time_series = TimeSeriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.time_series_group = TimeSeriesGroupOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def entire_detect(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Detect anomalies for the entire series in batch.

        This operation generates a model using an entire series, each point is
        detected with the same model. With this method, points before and after
        a certain point are used to determine whether it is an anomaly. The
        entire detection can give user an overall status of the time series.

        :param body: Time series points and period if needed. Advanced model
         parameters can also be set in the request.
        :type body: ~azure.cognitiveservices.anomalydetector.models.Request
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: EntireDetectResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.anomalydetector.models.EntireDetectResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.entire_detect.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'Request')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('EntireDetectResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    entire_detect.metadata = {'url': '/timeseries/entire/detect'}

    def last_detect(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Detect anomaly status of the latest point in time series.

        This operation generates a model using points before the latest one.
        With this method, only historical points are used to determine whether
        the target point is an anomaly. The latest point detecting operation
        matches the scenario of real-time monitoring of business metrics.

        :param body: Time series points and period if needed. Advanced model
         parameters can also be set in the request.
        :type body: ~azure.cognitiveservices.anomalydetector.models.Request
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LastDetectResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.anomalydetector.models.LastDetectResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.last_detect.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'Request')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LastDetectResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    last_detect.metadata = {'url': '/timeseries/last/detect'}

    def change_point_detect(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Detect change point for the entire series.

        Evaluate change point score of every series point.

        :param body: Time series points and granularity is needed. Advanced
         model parameters can also be set in the request if needed.
        :type body:
         ~azure.cognitiveservices.anomalydetector.models.ChangePointDetectRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ChangePointDetectResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.anomalydetector.models.ChangePointDetectResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.change_point_detect.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'ChangePointDetectRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ChangePointDetectResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    change_point_detect.metadata = {'url': '/timeseries/changepoint/detect'}
