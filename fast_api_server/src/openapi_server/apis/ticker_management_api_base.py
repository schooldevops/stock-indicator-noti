# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from openapi_server.models.ticker_input import TickerInput
from openapi_server.models.ticker_output import TickerOutput
from openapi_server.models.tickers_delete200_response import TickersDelete200Response
from openapi_server.models.tickers_list_get200_response import TickersListGet200Response


class BaseTickerManagementApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTickerManagementApi.subclasses = BaseTickerManagementApi.subclasses + (cls,)
    async def tickers_delete(
        self,
        ticker: Annotated[StrictStr, Field(description="삭제할 티커 코드")],
    ) -> TickersDelete200Response:
        """지정된 티커를 삭제합니다."""
        ...


    async def tickers_get(
        self,
        ticker: Annotated[StrictStr, Field(description="조회할 티커 코드")],
    ) -> TickerOutput:
        """지정된 티커 정보를 조회합니다."""
        ...


    async def tickers_list_get(
        self,
    ) -> TickersListGet200Response:
        """모든 티커 목록을 조회합니다."""
        ...


    async def tickers_post(
        self,
        ticker_input: TickerInput,
    ) -> TickerOutput:
        """새로운 티커를 추가합니다."""
        ...


    async def tickers_put(
        self,
        ticker_input: TickerInput,
    ) -> TickerOutput:
        """기존 티커 정보를 수정합니다."""
        ...
