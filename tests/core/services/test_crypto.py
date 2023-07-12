# -*- coding: utf-8 -*-
import pytest
from app.config import Settings
from app.core.services import make_api_request
from app.core.services.crypto import CryptoSymbol, get_historical_price_full_crypto, get_all_crypto

settings =Settings()

FMP_API_KEY = settings.FMP_API_KEY
BASE_URL_FMP = settings.BASE_URL_FMP


def test_get_all_crypto():
    """
    Test that get_all_crypto returns a list of CryptoSymbol
    """
    result = get_all_crypto()

    # Check that the function returns a list
    assert isinstance(result, list)

    # Check that the first item in the list is a CryptoSymbol
    assert isinstance(result[0], CryptoSymbol)

