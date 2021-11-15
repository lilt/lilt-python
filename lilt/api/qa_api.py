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


class QAApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def qa_check(self, target, trglang, **kwargs):  # noqa: E501
        """Perform QA check  # noqa: E501

        Perform QA checks on a target string. Optionally, you can specify a source string for additional bilingual checks, e.g. number consistency.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.qa_check(target, trglang, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str target: A target string to be checked. (required)
        :param str trglang: An ISO 639-1 language code. (required)
        :param str source: An optional source string.
        :param str srclang: An ISO 639-1 language code.
        :param int memory_id: Any custom rules defined for this Memory will also be applied as part of the QA check. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: QARuleMatches
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.qa_check_with_http_info(target, trglang, **kwargs)  # noqa: E501

    def qa_check_with_http_info(self, target, trglang, **kwargs):  # noqa: E501
        """Perform QA check  # noqa: E501

        Perform QA checks on a target string. Optionally, you can specify a source string for additional bilingual checks, e.g. number consistency.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.qa_check_with_http_info(target, trglang, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str target: A target string to be checked. (required)
        :param str trglang: An ISO 639-1 language code. (required)
        :param str source: An optional source string.
        :param str srclang: An ISO 639-1 language code.
        :param int memory_id: Any custom rules defined for this Memory will also be applied as part of the QA check. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(QARuleMatches, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'target',
            'trglang',
            'source',
            'srclang',
            'memory_id'
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
                    " to method qa_check" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'target' is set
        if self.api_client.client_side_validation and ('target' not in local_var_params or  # noqa: E501
                                                        local_var_params['target'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `target` when calling `qa_check`")  # noqa: E501
        # verify the required parameter 'trglang' is set
        if self.api_client.client_side_validation and ('trglang' not in local_var_params or  # noqa: E501
                                                        local_var_params['trglang'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `trglang` when calling `qa_check`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'target' in local_var_params and local_var_params['target'] is not None:  # noqa: E501
            query_params.append(('target', local_var_params['target']))  # noqa: E501
        if 'trglang' in local_var_params and local_var_params['trglang'] is not None:  # noqa: E501
            query_params.append(('trglang', local_var_params['trglang']))  # noqa: E501
        if 'source' in local_var_params and local_var_params['source'] is not None:  # noqa: E501
            query_params.append(('source', local_var_params['source']))  # noqa: E501
        if 'srclang' in local_var_params and local_var_params['srclang'] is not None:  # noqa: E501
            query_params.append(('srclang', local_var_params['srclang']))  # noqa: E501
        if 'memory_id' in local_var_params and local_var_params['memory_id'] is not None:  # noqa: E501
            query_params.append(('memory_id', local_var_params['memory_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/qa', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QARuleMatches',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
