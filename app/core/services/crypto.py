

from app.config import BASE_URL_FMP, FMP_API_KEY
from app.core.services import make_api_request


def get_historical_price_full_crypto(symbol):
    api_endpoint = f"{BASE_URL_FMP}/historical-price-full/crypto/{symbol}"
    params = {"apikey": FMP_API_KEY}
    return make_api_request(api_endpoint, params)

def get_all_crypto():
    """
    All possible crypto symbols
    """
    return [
        "BTCUSD",
        "ETHUSD",
        "LTCUSD",
        "BCHUSD",
        "XRPUSD",
        "EOSUSD",
        "XLMUSD",
        "TRXUSD",
        "ETCUSD",
        "DASHUSD",
        "ZECUSD",
        "XTZUSD",
        "XMRUSD",
        "ADAUSD",
        "NEOUSD",
        "XEMUSD",
        "VETUSD",
        "DOGEUSD",
        "OMGUSD",
        "ZRXUSD",
        "BATUSD"
        "USDTUSD",
        "LINKUSD",
        "BTTUSD",
        "BNBUSD",
        "ONTUSD",
        "QTUMUSD",
        "ALGOUSD",
        "ZILUSD",
        "ICXUSD",
        "KNCUSD",
        "ZENUSD",
        "THETAUSD",
        "IOSTUSD",
        "ATOMUSD",
        "MKRUSD",
        "COMPUSD",
        "YFIUSD",
        "SUSHIUSD",
        "SNXUSD",
        "UMAUSD",
        "BALUSD",
        "AAVEUSD",
        "UNIUSD",
        "RENBTCUSD",
        "RENUSD",
        "CRVUSD",
        "SXPUSD",
        "KSMUSD",
        "OXTUSD",
        "DGBUSD",
        "LRCUSD",
        "WAVESUSD",
        "NMRUSD",
        "STORJUSD",
        "KAVAUSD",
        "RLCUSD",
        "BANDUSD",
        "SCUSD",
        "ENJUSD",
    ]