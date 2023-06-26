import httpx
import logging
from app.config import Settings
from app.core.logging import Logger

logger = Logger(logging.INFO).get_logger()
settings = Settings()


        

async def send_message(self, content: str):
    client = httpx.AsyncClient()
    discord_webhook_url = settings.discord_webhook_url
    payload = {"content": content}
    try:
        response = await client.post(discord_webhook_url, json=payload)
        if response.status_code == 204:
            logger.info("Message sent successfully")
        else:
            logger.error("Failed to send message")
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")

    finally:
        client.close()

