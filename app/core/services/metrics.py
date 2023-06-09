# -*- coding: utf-8 -*-
import os
from typing import Dict, Any
import logging

from app.core.logging import Logger

logger = Logger(logging.INFO).get_logger()

try:
    import torch
    # os.environ["CUDA_VISIBLE_DEVICES"]=""
    # torch.set_default_tensor_type(torch.FloatTensor)
except ImportError as e:
    logger.warning(f"Error importing torch: {e}")

try:
    import spacy
except ImportError as e:
    logger.warning(f"Error importing spacy: {e}")

try:
    from transformers import (
        AutoModelForSeq2SeqLM,
        AutoModelForTokenClassification,
        AutoModelForSequenceClassification,
        AutoTokenizer,
        pipeline,
    )
except ImportError as e:
    logger.warning(f"Error importing transformers: {e}")

try:
    # Use CUDA if it's available
    device = "cuda" if torch.cuda.is_available() else "cpu"
except Exception as e:
    logger.warning(f"Error initializing CUDA: {e}")

def requires_cuda(func):
    """Decorator for methods that require CUDA."""
    def wrapper(self, *args, **kwargs):
        if device != "cuda":
            logger.warning(f"{func.__name__} requires CUDA but CUDA is unavailable.")
            return self.fake_value
        return func(self, *args, **kwargs)
    return wrapper


class TextMetrics:
    def __init__(self):
        # Set the fake value
        self.fake_value = "Sorry, could not process the request due to unavailability of CUDA."

        try:
            # Load Spacy model for topic classification
            self.nlp = spacy.load("en_core_web_sm")
        except Exception as e:
            logger.error(f"Error initializing Spacy: {e}")

        try:
            # Load model for ticker detection
            self.ticker_tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-ticker")
            self.ticker_model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-ticker").to(device)
            self.ticker_pipeline = pipeline("ner", model=self.ticker_model, tokenizer=self.ticker_tokenizer, aggregation_strategy="simple")
        except Exception as e:
            logger.error(f"Error initializing Ticker Detection Model: {e}")

        try:
            # Load model for text summarization
            self.summarizer_tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
            self.summarizer_model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6").to(device)
            self.summarizer = pipeline("summarization", model=self.summarizer_model, tokenizer=self.summarizer_tokenizer)
        except Exception as e:
            logger.error(f"Error initializing Text Summarization Model: {e}")

        try:
            # Load model for sentiment analysis
            self.sentiment_tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
            self.sentiment_model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert").to(device)
        except Exception as e:
            logger.error(f"Error initializing Sentiment Analysis Model: {e}")


    def classify_topic(self, text: str) -> Dict[str, Any]:
        doc = self.nlp(text)
        topics = {ent.text for ent in doc.ents if ent.label_ == "ORG"}
        return list(topics)

    def detect_ticker(self, text: str) -> Dict[str, Any]:
        return self.ticker_pipeline(text)

    def summarize_text(self, text: str) -> str:
        inputs = self.summarizer_tokenizer(
            text,
            max_length=1024,
            truncation=True,
            return_tensors="pt"
        ).to(device)
        summary_ids = self.summarizer_model.generate(inputs["input_ids"])
        summary = self.summarizer_tokenizer.batch_decode(
            summary_ids,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )
        return summary[0]

    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        inputs = self.sentiment_tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            truncation=True,
            max_length=512,
            padding="longest",
            return_tensors="pt",
        ).to(device)
        outputs = self.sentiment_model(
            inputs["input_ids"],
            token_type_ids=inputs["token_type_ids"],
            attention_mask=inputs["attention_mask"],
        )
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1).tolist()[0]
        logger.info(f"Probabilities: {probabilities}")
        return {
            "positive": probabilities[1],
            "negative": probabilities[0],
            "neutral": probabilities[2],
        }
