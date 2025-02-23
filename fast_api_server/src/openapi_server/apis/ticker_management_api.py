# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.ticker_management_api_base import BaseTickerManagementApi
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
from openapi_server.models.ticker_input import TickerInput
from openapi_server.models.ticker_output import TickerOutput


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/tickers",
    responses={
        200: {"model": TickerOutput, "description": "성공적으로 티커가 삭제되었습니다."},
    },
    tags=["Ticker Management"],
    summary="티커 삭제",
    response_model_by_alias=True,
)
async def tickers_delete(
    ticker: Annotated[StrictStr, Field(description="삭제할 티커 코드")] = Query(None, description="삭제할 티커 코드", alias="ticker"),
) -> TickerOutput:
    """지정된 티커를 삭제합니다."""
    if not BaseTickerManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTickerManagementApi.subclasses[0]().tickers_delete(ticker)


@router.get(
    "/tickers",
    responses={
        200: {"model": TickerOutput, "description": "성공적으로 티커 정보를 조회했습니다."},
    },
    tags=["Ticker Management"],
    summary="티커 조회",
    response_model_by_alias=True,
)
async def tickers_get(
    ticker: Annotated[StrictStr, Field(description="조회할 티커 코드")] = Query(None, description="조회할 티커 코드", alias="ticker"),
) -> TickerOutput:
    """지정된 티커 정보를 조회합니다."""
    if not BaseTickerManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTickerManagementApi.subclasses[0]().tickers_get(ticker)


@router.get(
    "/tickers/list",
    responses={
        200: {"model": List[TickerOutput], "description": "성공적으로 티커 목록을 조회했습니다."},
    },
    tags=["Ticker Management"],
    summary="티커 목록 조회",
    response_model_by_alias=True,
)
async def tickers_list_get(
) -> List[TickerOutput]:
    """모든 티커 목록을 조회합니다."""
    if not BaseTickerManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTickerManagementApi.subclasses[0]().tickers_list_get()


@router.post(
    "/tickers",
    responses={
        200: {"model": TickerOutput, "description": "성공적으로 티커가 추가되었습니다."},
    },
    tags=["Ticker Management"],
    summary="티커 추가",
    response_model_by_alias=True,
)
async def tickers_post(
    ticker_input: TickerInput = Body(None, description=""),
) -> TickerOutput:
    """새로운 티커를 추가합니다."""
    if not BaseTickerManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTickerManagementApi.subclasses[0]().tickers_post(ticker_input)


@router.put(
    "/tickers",
    responses={
        200: {"model": TickerOutput, "description": "성공적으로 티커가 수정되었습니다."},
    },
    tags=["Ticker Management"],
    summary="티커 수정",
    response_model_by_alias=True,
)
async def tickers_put(
    ticker_input: TickerInput = Body(None, description=""),
) -> TickerOutput:
    """기존 티커 정보를 수정합니다."""
    if not BaseTickerManagementApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTickerManagementApi.subclasses[0]().tickers_put(ticker_input)
