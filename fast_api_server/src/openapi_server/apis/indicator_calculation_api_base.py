# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.calculate_indicator_post200_response import CalculateIndicatorPost200Response
from openapi_server.models.calculate_indicator_post_request import CalculateIndicatorPostRequest


class BaseIndicatorCalculationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseIndicatorCalculationApi.subclasses = BaseIndicatorCalculationApi.subclasses + (cls,)
    async def calculate_indicator_post(
        self,
        calculate_indicator_post_request: CalculateIndicatorPostRequest,
    ) -> CalculateIndicatorPost200Response:
        """지정된 인디케이터를 계산합니다."""
        ...
