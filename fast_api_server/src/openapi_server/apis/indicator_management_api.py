# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.indicator_management_api_base import BaseIndicatorManagementApi
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
from pydantic import Field, StrictStr
from typing import List
from typing_extensions import Annotated
from openapi_server.models.indicator_input import IndicatorInput
from openapi_server.models.indicator_output import IndicatorOutput


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/indicators",
    responses={
        200: {"model": IndicatorOutput, "description": "성공적으로 인디케이터가 삭제되었습니다."},
    },
    tags=["Indicator Management"],
    summary="인디케이터 삭제",
    response_model_by_alias=True,
)
async def indicators_delete(
    indicator_code: Annotated[StrictStr, Field(description="삭제할 인디케이터 코드")] = Query(None, description="삭제할 인디케이터 코드", alias="indicatorCode"),
) -> IndicatorOutput:
    """지정된 인디케이터를 삭제합니다."""
    if not BaseIndicatorManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndicatorManagementApi.subclasses[0]().indicators_delete(indicator_code)


@router.get(
    "/indicators",
    responses={
        200: {"model": IndicatorOutput, "description": "성공적으로 인디케이터 정보를 조회했습니다."},
    },
    tags=["Indicator Management"],
    summary="인디케이터 조회",
    response_model_by_alias=True,
)
async def indicators_get(
    indicator_code: Annotated[StrictStr, Field(description="조회할 인디케이터 코드")] = Query(None, description="조회할 인디케이터 코드", alias="indicatorCode"),
) -> IndicatorOutput:
    """지정된 인디케이터 정보를 조회합니다."""
    if not BaseIndicatorManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndicatorManagementApi.subclasses[0]().indicators_get(indicator_code)


@router.get(
    "/indicators/list",
    responses={
        200: {"model": List[IndicatorOutput], "description": "성공적으로 인디케이터 목록을 조회했습니다."},
    },
    tags=["Indicator Management"],
    summary="인디케이터 목록 조회",
    response_model_by_alias=True,
)
async def indicators_list_get(
) -> List[IndicatorOutput]:
    """모든 인디케이터 목록을 조회합니다."""
    if not BaseIndicatorManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndicatorManagementApi.subclasses[0]().indicators_list_get()


@router.post(
    "/indicators",
    responses={
        200: {"model": IndicatorOutput, "description": "성공적으로 인디케이터가 추가되었습니다."},
    },
    tags=["Indicator Management"],
    summary="인디케이터 추가",
    response_model_by_alias=True,
)
async def indicators_post(
    indicator_input: IndicatorInput = Body(None, description=""),
) -> IndicatorOutput:
    """새로운 인디케이터를 추가합니다."""
    if not BaseIndicatorManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndicatorManagementApi.subclasses[0]().indicators_post(indicator_input)


@router.put(
    "/indicators",
    responses={
        200: {"model": IndicatorOutput, "description": "성공적으로 인디케이터가 수정되었습니다."},
    },
    tags=["Indicator Management"],
    summary="인디케이터 수정",
    response_model_by_alias=True,
)
async def indicators_put(
    indicator_input: IndicatorInput = Body(None, description=""),
) -> IndicatorOutput:
    """기존 인디케이터 정보를 수정합니다."""
    if not BaseIndicatorManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIndicatorManagementApi.subclasses[0]().indicators_put(indicator_input)
