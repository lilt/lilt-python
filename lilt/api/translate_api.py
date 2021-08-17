# coding: utf-8

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests. ## Authentication Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.   # noqa: E501

    The version of the OpenAPI document: v2.0
    Contact: support@lilt.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lilt.api_client import ApiClient
from lilt.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TranslateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_translate_file(self, file_id, memory_id, **kwargs):  # noqa: E501
        """Translate a File  # noqa: E501

        Start machine translation of one or more Files that have previously been uploaded.  The response will include an `id` parameter that can be used to monitor and download the translations in subsequent calls.  Example CURL: ``` curl --X --request POST 'https://lilt.com/2/translate/file?key=API_KEY&fileId=583&memoryId=2495&configId=123' ```    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_translate_file(file_id, memory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str file_id: List of File ids to be translated, comma separated. (required)
        :param str memory_id: Id of Memory to use in translation. (required)
        :param float config_id: An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TranslationInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.batch_translate_file_with_http_info(file_id, memory_id, **kwargs)  # noqa: E501

    def batch_translate_file_with_http_info(self, file_id, memory_id, **kwargs):  # noqa: E501
        """Translate a File  # noqa: E501

        Start machine translation of one or more Files that have previously been uploaded.  The response will include an `id` parameter that can be used to monitor and download the translations in subsequent calls.  Example CURL: ``` curl --X --request POST 'https://lilt.com/2/translate/file?key=API_KEY&fileId=583&memoryId=2495&configId=123' ```    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_translate_file_with_http_info(file_id, memory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str file_id: List of File ids to be translated, comma separated. (required)
        :param str memory_id: Id of Memory to use in translation. (required)
        :param float config_id: An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TranslationInfo, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'file_id',
            'memory_id',
            'config_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_translate_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'file_id' is set
        if self.api_client.client_side_validation and ('file_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['file_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file_id` when calling `batch_translate_file`")  # noqa: E501
        # verify the required parameter 'memory_id' is set
        if self.api_client.client_side_validation and ('memory_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['memory_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `memory_id` when calling `batch_translate_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_id' in local_var_params and local_var_params['file_id'] is not None:  # noqa: E501
            query_params.append(('fileId', local_var_params['file_id']))  # noqa: E501
        if 'memory_id' in local_var_params and local_var_params['memory_id'] is not None:  # noqa: E501
            query_params.append(('memoryId', local_var_params['memory_id']))  # noqa: E501
        if 'config_id' in local_var_params and local_var_params['config_id'] is not None:  # noqa: E501
            query_params.append(('configId', local_var_params['config_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/translate/file', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TranslationInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_file(self, id, **kwargs):  # noqa: E501
        """Download translated file  # noqa: E501

        Download a translated File.  Example CURL: ``` curl --X --request GET 'https://lilt.com/2/translate/files?key=API_KEY&id=1' ```    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A translation id. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.download_file_with_http_info(id, **kwargs)  # noqa: E501

    def download_file_with_http_info(self, id, **kwargs):  # noqa: E501
        """Download translated file  # noqa: E501

        Download a translated File.  Example CURL: ``` curl --X --request GET 'https://lilt.com/2/translate/files?key=API_KEY&id=1' ```    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: A translation id. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `download_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params and local_var_params['id'] is not None:  # noqa: E501
            query_params.append(('id', local_var_params['id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/translate/files', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def monitor_file_translation(self, **kwargs):  # noqa: E501
        """Monitor file translation  # noqa: E501

        Get information about the one or more Files that are being translated with machine translation. Query filters are optional but at least one must be provided.  Example CURL: ``` curl --X --request GET 'https://lilt.com/2/translate/file?key=API_KEY&translationIds=1,2&fromTime=1607966744&toTime=1707966744&status=InProgress' ```    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.monitor_file_translation(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str translation_ids: List of translation ids, comma separated
        :param str status: One of the translation statuses - `InProgress`, `Completed`, `Failed`, `ReadyForDownload`
        :param float from_time: Results after this time (inclusive) will be returned, specified as seconds since the Unix epoch.
        :param float to_time: Results before this time (exclusive) will be returned, specified as seconds since the Unix epoch.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TranslationInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.monitor_file_translation_with_http_info(**kwargs)  # noqa: E501

    def monitor_file_translation_with_http_info(self, **kwargs):  # noqa: E501
        """Monitor file translation  # noqa: E501

        Get information about the one or more Files that are being translated with machine translation. Query filters are optional but at least one must be provided.  Example CURL: ``` curl --X --request GET 'https://lilt.com/2/translate/file?key=API_KEY&translationIds=1,2&fromTime=1607966744&toTime=1707966744&status=InProgress' ```    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.monitor_file_translation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str translation_ids: List of translation ids, comma separated
        :param str status: One of the translation statuses - `InProgress`, `Completed`, `Failed`, `ReadyForDownload`
        :param float from_time: Results after this time (inclusive) will be returned, specified as seconds since the Unix epoch.
        :param float to_time: Results before this time (exclusive) will be returned, specified as seconds since the Unix epoch.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TranslationInfo, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'translation_ids',
            'status',
            'from_time',
            'to_time'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method monitor_file_translation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'translation_ids' in local_var_params and local_var_params['translation_ids'] is not None:  # noqa: E501
            query_params.append(('translationIds', local_var_params['translation_ids']))  # noqa: E501
        if 'status' in local_var_params and local_var_params['status'] is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'from_time' in local_var_params and local_var_params['from_time'] is not None:  # noqa: E501
            query_params.append(('fromTime', local_var_params['from_time']))  # noqa: E501
        if 'to_time' in local_var_params and local_var_params['to_time'] is not None:  # noqa: E501
            query_params.append(('toTime', local_var_params['to_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/translate/file', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TranslationInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_segment(self, source, srclang, trglang, **kwargs):  # noqa: E501
        """Register a segment  # noqa: E501

        Register a source string for interactive translation. The `source_hash` value that is returned by this request is required by the `prefix` parameter for the translation endpoint. The maximum source length is 5,000 characters. Usage charges apply to this endpoint for production REST API keys.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_segment(source, srclang, trglang, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str source: A source string to be registered. (required)
        :param str srclang: An ISO 639-1 language code. (required)
        :param str trglang: An ISO 639-1 language code. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TranslateRegisterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.register_segment_with_http_info(source, srclang, trglang, **kwargs)  # noqa: E501

    def register_segment_with_http_info(self, source, srclang, trglang, **kwargs):  # noqa: E501
        """Register a segment  # noqa: E501

        Register a source string for interactive translation. The `source_hash` value that is returned by this request is required by the `prefix` parameter for the translation endpoint. The maximum source length is 5,000 characters. Usage charges apply to this endpoint for production REST API keys.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_segment_with_http_info(source, srclang, trglang, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str source: A source string to be registered. (required)
        :param str srclang: An ISO 639-1 language code. (required)
        :param str trglang: An ISO 639-1 language code. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TranslateRegisterResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'source',
            'srclang',
            'trglang'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_segment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'source' is set
        if self.api_client.client_side_validation and ('source' not in local_var_params or  # noqa: E501
                                                        local_var_params['source'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `source` when calling `register_segment`")  # noqa: E501
        # verify the required parameter 'srclang' is set
        if self.api_client.client_side_validation and ('srclang' not in local_var_params or  # noqa: E501
                                                        local_var_params['srclang'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `srclang` when calling `register_segment`")  # noqa: E501
        # verify the required parameter 'trglang' is set
        if self.api_client.client_side_validation and ('trglang' not in local_var_params or  # noqa: E501
                                                        local_var_params['trglang'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `trglang` when calling `register_segment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source' in local_var_params and local_var_params['source'] is not None:  # noqa: E501
            query_params.append(('source', local_var_params['source']))  # noqa: E501
        if 'srclang' in local_var_params and local_var_params['srclang'] is not None:  # noqa: E501
            query_params.append(('srclang', local_var_params['srclang']))  # noqa: E501
        if 'trglang' in local_var_params and local_var_params['trglang'] is not None:  # noqa: E501
            query_params.append(('trglang', local_var_params['trglang']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/translate/register', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TranslateRegisterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def translate_segment(self, memory_id, **kwargs):  # noqa: E501
        """Translate a segment  # noqa: E501

        Translate a source string.  Setting the `rich` parameter to `true` will change the response format to include additional information about each translation including a model score, word alignments,  and formatting information. The rich format can be seen in the example response on this page.  By default, this endpoint also returns translation memory (TM) fuzzy matches, along with associated scores. Fuzzy matches always appear ahead of machine translation output in the response.  The maximum source length is 5,000 characters.  Usage charges apply to this endpoint for production REST API keys.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translate_segment(memory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int memory_id: A unique Memory identifier. (required)
        :param str source: The source text to be translated.
        :param int source_hash: A source hash code.
        :param str prefix: A target prefix.
        :param int n: Return top n translations (deprecated).
        :param bool rich: Returns rich translation information (e.g., with word alignments).
        :param bool tm_matches: Include translation memory fuzzy matches.
        :param bool project_tags: Project tags. Projects tags in source to target if set to true.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TranslationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.translate_segment_with_http_info(memory_id, **kwargs)  # noqa: E501

    def translate_segment_with_http_info(self, memory_id, **kwargs):  # noqa: E501
        """Translate a segment  # noqa: E501

        Translate a source string.  Setting the `rich` parameter to `true` will change the response format to include additional information about each translation including a model score, word alignments,  and formatting information. The rich format can be seen in the example response on this page.  By default, this endpoint also returns translation memory (TM) fuzzy matches, along with associated scores. Fuzzy matches always appear ahead of machine translation output in the response.  The maximum source length is 5,000 characters.  Usage charges apply to this endpoint for production REST API keys.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.translate_segment_with_http_info(memory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int memory_id: A unique Memory identifier. (required)
        :param str source: The source text to be translated.
        :param int source_hash: A source hash code.
        :param str prefix: A target prefix.
        :param int n: Return top n translations (deprecated).
        :param bool rich: Returns rich translation information (e.g., with word alignments).
        :param bool tm_matches: Include translation memory fuzzy matches.
        :param bool project_tags: Project tags. Projects tags in source to target if set to true.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TranslationList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'memory_id',
            'source',
            'source_hash',
            'prefix',
            'n',
            'rich',
            'tm_matches',
            'project_tags'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method translate_segment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'memory_id' is set
        if self.api_client.client_side_validation and ('memory_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['memory_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `memory_id` when calling `translate_segment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'memory_id' in local_var_params and local_var_params['memory_id'] is not None:  # noqa: E501
            query_params.append(('memory_id', local_var_params['memory_id']))  # noqa: E501
        if 'source' in local_var_params and local_var_params['source'] is not None:  # noqa: E501
            query_params.append(('source', local_var_params['source']))  # noqa: E501
        if 'source_hash' in local_var_params and local_var_params['source_hash'] is not None:  # noqa: E501
            query_params.append(('source_hash', local_var_params['source_hash']))  # noqa: E501
        if 'prefix' in local_var_params and local_var_params['prefix'] is not None:  # noqa: E501
            query_params.append(('prefix', local_var_params['prefix']))  # noqa: E501
        if 'n' in local_var_params and local_var_params['n'] is not None:  # noqa: E501
            query_params.append(('n', local_var_params['n']))  # noqa: E501
        if 'rich' in local_var_params and local_var_params['rich'] is not None:  # noqa: E501
            query_params.append(('rich', local_var_params['rich']))  # noqa: E501
        if 'tm_matches' in local_var_params and local_var_params['tm_matches'] is not None:  # noqa: E501
            query_params.append(('tm_matches', local_var_params['tm_matches']))  # noqa: E501
        if 'project_tags' in local_var_params and local_var_params['project_tags'] is not None:  # noqa: E501
            query_params.append(('project_tags', local_var_params['project_tags']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/translate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TranslationList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
