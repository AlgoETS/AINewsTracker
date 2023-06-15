# -*- coding: utf-8 -*-
from unittest import mock

import httpx
import pytest

from app.core.logging import Logger
from app.core.services.__init__ import make_api_request

logger = Logger().get_logger()


@pytest.fixture
def api_details():
    url = "https://financialmodelingprep.com/api/v4/historical/social-sentiment"
    params = {"symbol": "AAPL", "page": "0", "apikey": "YOUR_API_KEY"}
    return url, params


@pytest.mark.parametrize(
    "status_code, response_data, expected",
    [(200, {"data": "test"}, {"data": "test"}), (404, None, "")],
)
@mock.patch("httpx.Client")
def test_make_api_request(
    mock_client, status_code, response_data, expected, api_details
):
    url, params = api_details

    # Mock the response from the API
    mock_response = mock.Mock()
    mock_response.status_code = status_code
    mock_response.json.return_value = response_data

    # Mock the client and its context manager behavior
    mock_client_instance = mock_client.return_value
    mock_client_instance.get.return_value = mock_response
    mock_client_instance.__enter__.return_value = mock_client_instance

    # Mock the behavior of raise_for_status
    if status_code != 200:
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "error", request=mock.Mock(), response=mock_response
        )
    else:
        mock_response.raise_for_status.return_value = None

    response = make_api_request(url, params)

    assert response == expected
