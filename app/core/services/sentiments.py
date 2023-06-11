# -*- coding: utf-8 -*-
from app.core.logging import logger

try:
    import torch
except ImportError:
    torch = None
    logger.warning("Unable to import torch. Some functionality may be unavailable.")

from transformers import AutoModelForSequenceClassification, AutoTokenizer


def calculate_sentiment(text: str):
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

    inputs = tokenizer.encode_plus(
        text,
        None,
        add_special_tokens=True,
        max_length=512,
        padding="max_length",
        return_token_type_ids=False,
        return_attention_mask=True,
        truncation=True,
        return_tensors="pt",
    )

    output = model(**inputs)
    logits = output.logits.detach().numpy()

    sentiment = torch.argmax(output.logits)
    score = torch.softmax(output.logits, dim=1).detach().numpy()[0][sentiment]

    if sentiment == 0:
        sentiment = "negative"
    elif sentiment == 1:
        sentiment = "neutral"
    else:
        sentiment = "positive"

    # If the sentiment is neutral and score > 0.8, return bad article
    if sentiment == "neutral" and score > 0.8:
        return "Bad article, not in context"

    return sentiment, score
