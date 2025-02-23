# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.ticker_input import TickerInput  # noqa: F401
from openapi_server.models.ticker_output import TickerOutput  # noqa: F401
from openapi_server.models.tickers_delete200_response import TickersDelete200Response  # noqa: F401
from openapi_server.models.tickers_list_get200_response import TickersListGet200Response  # noqa: F401


def test_tickers_delete(client: TestClient):
    """Test case for tickers_delete

    티커 삭제
    """
    params = [("ticker", 'AAPL')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/tickers",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tickers_get(client: TestClient):
    """Test case for tickers_get

    티커 조회
    """
    params = [("ticker", 'AAPL')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tickers",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tickers_list_get(client: TestClient):
    """Test case for tickers_list_get

    티커 목록 조회
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tickers/list",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tickers_post(client: TestClient):
    """Test case for tickers_post

    티커 추가
    """
    ticker_input = {"created_at":"2023-01-01T00:00:00Z","ticker":"AAPL","modified_at":"2023-01-01T00:00:00Z","name":"Apple Inc.","description":"Apple Inc. 주식"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/tickers",
    #    headers=headers,
    #    json=ticker_input,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tickers_put(client: TestClient):
    """Test case for tickers_put

    티커 수정
    """
    ticker_input = {"created_at":"2023-01-01T00:00:00Z","ticker":"AAPL","modified_at":"2023-01-01T00:00:00Z","name":"Apple Inc.","description":"Apple Inc. 주식"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/tickers",
    #    headers=headers,
    #    json=ticker_input,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

