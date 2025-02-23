# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.calculate_indicator_post200_response import CalculateIndicatorPost200Response  # noqa: F401
from openapi_server.models.calculate_indicator_post_request import CalculateIndicatorPostRequest  # noqa: F401


def test_calculate_indicator_post(client: TestClient):
    """Test case for calculate_indicator_post

    인디케이터 계산
    """
    calculate_indicator_post_request = openapi_server.CalculateIndicatorPostRequest()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/calculate-indicator",
    #    headers=headers,
    #    json=calculate_indicator_post_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

