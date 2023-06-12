# -*- coding: utf-8 -*-
import httpx
from app.core.logging import Logger

logger = Logger().get_logger()

def make_api_request(url, params):
    with httpx.Client() as client:
        try:
            response = client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            logger.warning(f"Error: Failed to send GET request: {e}")
        except httpx.HTTPStatusError as e:
            logger.warning(f"Error: Received HTTP status {e.response.status_code} from the server")
    return ""