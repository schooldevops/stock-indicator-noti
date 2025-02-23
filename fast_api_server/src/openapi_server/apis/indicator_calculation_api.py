# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.indicator_calculation_api_base import BaseIndicatorCalculationApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.calculate_indicator_post200_response import CalculateIndicatorPost200Response
from openapi_server.models.calculate_indicator_post_request import CalculateIndicatorPostRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/calculate-indicator",
    responses={
        200: {"model": CalculateIndicatorPost200Response, "description": "성공적으로 인디케이터가 계산되었습니다."},
    },
    tags=["Indicator Calculation"],
    summary="인디케이터 계산",
    response_model_by_alias=True,
)
async def calculate_indicator_post(
    calculate_indicator_post_request: CalculateIndicatorPostRequest = Body(None, description=""),
) -> CalculateIndicatorPost200Response:
    """지정된 인디케이터를 계산합니다."""
    if not BaseIndicatorCalculationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndicatorCalculationApi.subclasses[0]().calculate_indicator_post(calculate_indicator_post_request)
