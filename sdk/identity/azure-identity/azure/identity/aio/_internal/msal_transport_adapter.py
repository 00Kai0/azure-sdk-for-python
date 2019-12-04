# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Adapter to substitute an async azure-core pipeline for Requests in MSAL application token acquisition methods."""

import asyncio
from typing import TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import AsyncPipeline
from azure.core.pipeline.policies import (
    AsyncRetryPolicy,
    DistributedTracingPolicy,
    HttpLoggingPolicy,
    NetworkTraceLoggingPolicy,
    ProxyPolicy,
)
from azure.core.pipeline.transport import AioHttpTransport, HttpRequest

from azure.identity._internal import MsalTransportResponse

if TYPE_CHECKING:
    # pylint:disable=unused-import
    from typing import Any, Dict, Iterable, Optional
    from azure.core.pipeline.policies import AsyncHTTPPolicy
    from azure.core.pipeline.transport import AsyncHttpTransport


class MsalTransportAdapter:
    """Wraps an async azure-core pipeline with the shape of a (synchronous) Requests Session"""

    def __init__(
        self,
        config: "Optional[Configuration]" = None,
        policies: "Optional[Iterable[AsyncHTTPPolicy]]" = None,
        transport: "Optional[AsyncHttpTransport]" = None,
        **kwargs: "Any"
    ) -> None:

        config = config or self._create_config(**kwargs)
        policies = policies or [
            config.proxy_policy,
            config.retry_policy,
            config.logging_policy,
            DistributedTracingPolicy(**kwargs),
            HttpLoggingPolicy(**kwargs),
        ]
        self._transport = transport or AioHttpTransport(configuration=config)
        self._pipeline = AsyncPipeline(transport=self._transport, policies=policies)

    def get(
        self,
        url: str,
        loop: "asyncio.AbstractEventLoop",
        headers: "Optional[Dict[str, str]]" = None,
        params: "Optional[Dict[str, str]]" = None,
        timeout: "Optional[float]" = None,
        verify: "Optional[bool]" = None,
        **kwargs: "Any"
    ) -> MsalTransportResponse:

        request = HttpRequest("GET", url, headers=headers)
        if params:
            request.format_parameters(params)

        future = asyncio.run_coroutine_threadsafe(  # type: ignore
            self._send_request(request, connection_timeout=timeout, connection_verify=verify, **kwargs), loop
        )
        response = future.result(timeout=timeout)

        return MsalTransportResponse(response)

    def post(
        self,
        url: str,
        loop: "asyncio.AbstractEventLoop",
        data: "Any" = None,
        headers: "Optional[Dict[str, str]]" = None,
        params: "Optional[Dict[str, str]]" = None,
        timeout: "Optional[float]" = None,
        verify: "Optional[bool]" = None,
        **kwargs: "Any"
    ) -> MsalTransportResponse:

        request = HttpRequest("POST", url, headers=headers)
        if params:
            request.format_parameters(params)
        if data:
            request.headers["Content-Type"] = "application/x-www-form-urlencoded"
            request.set_formdata_body(data)

        future = asyncio.run_coroutine_threadsafe(  # type: ignore
            self._send_request(request, connection_timeout=timeout, connection_verify=verify, **kwargs), loop
        )
        response = future.result(timeout=timeout)

        return MsalTransportResponse(response)

    @staticmethod
    def _create_config(**kwargs: "Any") -> Configuration:
        config = Configuration(**kwargs)
        config.proxy_policy = ProxyPolicy(**kwargs)
        config.logging_policy = NetworkTraceLoggingPolicy(**kwargs)
        config.retry_policy = AsyncRetryPolicy(**kwargs)
        return config

    async def _send_request(self, *args, **kwargs):
        async with self._pipeline:
            return await self._pipeline.run(*args, **kwargs)
