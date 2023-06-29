import httpx
import logging
from app.config import Settings
from app.core.logging import Logger

logger = Logger(logging.INFO).get_logger()
settings = Settings()



async def send_message(content: str):
    client = httpx.AsyncClient()
    discord_webhook_url = settings.DISCORD_WEBHOOK_URL
    message= f"""
✨📰 News Update:

📌 Headline: Tech Company Releases New AI Product
🗒️ Summary: ${content}.

📊  Sentiment Analysis:
Overall Sentiment: Positive

"""
    payload = {"content": message}
    try:
        response = await client.post(discord_webhook_url, json=payload)
        logger.info(f"Response status code: {response.status_code}")
        if response.status_code == 204:
            logger.info("Message sent successfully")
        else:
            logger.error("Failed to send message")
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")

    

