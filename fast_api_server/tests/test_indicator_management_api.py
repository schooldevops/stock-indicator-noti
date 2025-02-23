# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.indicator_input import IndicatorInput  # noqa: F401
from openapi_server.models.indicator_output import IndicatorOutput  # noqa: F401
from openapi_server.models.indicators_list_get200_response import IndicatorsListGet200Response  # noqa: F401
from openapi_server.models.tickers_delete200_response import TickersDelete200Response  # noqa: F401


def test_indicators_delete(client: TestClient):
    """Test case for indicators_delete

    인디케이터 삭제
    """
    params = [("indicator_code", 'MACD')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/indicators",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_indicators_get(client: TestClient):
    """Test case for indicators_get

    인디케이터 조회
    """
    params = [("indicator_code", 'MACD')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/indicators",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_indicators_list_get(client: TestClient):
    """Test case for indicators_list_get

    인디케이터 목록 조회
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/indicators/list",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_indicators_post(client: TestClient):
    """Test case for indicators_post

    인디케이터 추가
    """
    indicator_input = {"created_at":"2023-01-01T00:00:00Z","indicator_name":"MACD","modified_at":"2023-01-01T00:00:00Z","indicator_code":"MACD","description":"이동 평균 수렴 발산"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/indicators",
    #    headers=headers,
    #    json=indicator_input,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_indicators_put(client: TestClient):
    """Test case for indicators_put

    인디케이터 수정
    """
    indicator_input = {"created_at":"2023-01-01T00:00:00Z","indicator_name":"MACD","modified_at":"2023-01-01T00:00:00Z","indicator_code":"MACD","description":"이동 평균 수렴 발산"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/indicators",
    #    headers=headers,
    #    json=indicator_input,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

