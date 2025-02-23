# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from openapi_server.models.indicator_input import IndicatorInput
from openapi_server.models.indicator_output import IndicatorOutput
from openapi_server.models.indicators_list_get200_response import IndicatorsListGet200Response
from openapi_server.models.tickers_delete200_response import TickersDelete200Response


class BaseIndicatorManagementApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseIndicatorManagementApi.subclasses = BaseIndicatorManagementApi.subclasses + (cls,)
    async def indicators_delete(
        self,
        indicator_code: Annotated[StrictStr, Field(description="삭제할 인디케이터 코드")],
    ) -> TickersDelete200Response:
        """지정된 인디케이터를 삭제합니다."""
        ...


    async def indicators_get(
        self,
        indicator_code: Annotated[StrictStr, Field(description="조회할 인디케이터 코드")],
    ) -> IndicatorOutput:
        """지정된 인디케이터 정보를 조회합니다."""
        ...


    async def indicators_list_get(
        self,
    ) -> IndicatorsListGet200Response:
        """모든 인디케이터 목록을 조회합니다."""
        ...


    async def indicators_post(
        self,
        indicator_input: IndicatorInput,
    ) -> IndicatorOutput:
        """새로운 인디케이터를 추가합니다."""
        ...


    async def indicators_put(
        self,
        indicator_input: IndicatorInput,
    ) -> IndicatorOutput:
        """기존 인디케이터 정보를 수정합니다."""
        ...
