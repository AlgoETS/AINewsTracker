# -*- coding: utf-8 -*-
import logging

from transformers import AutoModelForSequenceClassification, AutoTokenizer

try:
    import torch
except ImportError:
    logging.warning("Unable to import torch. Some functionality may be unavailable.")

try:
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
except Exception:
    logging.warning(
        "Unable to load finbert model. Some functionality may be unavailable."
    )


def analyze_sentiment(text):
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        truncation=True,
        max_length=512,
        padding="longest",
        return_tensors="pt",
    )
    try:
        with torch.no_grad():
            outputs = model(
                inputs["input_ids"],
                token_type_ids=inputs["token_type_ids"],
                attention_mask=inputs["attention_mask"],
            )

        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1).tolist()[0]
        return {
            "positive": probabilities[2],
            "negative": probabilities[0],
            "neutral": probabilities[1],
        }
    except Exception:
        probabilities = [0, 0, 0]
        return {
            "positive": probabilities[2],
            "negative": probabilities[0],
            "neutral": probabilities[1],
        }
