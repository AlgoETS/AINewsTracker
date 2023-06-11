from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

def analyze_sentiment(text):
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        truncation=True,
        max_length=512,
        padding="longest",
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(
            inputs["input_ids"],
            token_type_ids=inputs["token_type_ids"],
            attention_mask=inputs["attention_mask"]
        )

    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1).tolist()[0]
    sentiment_scores = {
        "positive": probabilities[2],
        "negative": probabilities[0],
        "neutral": probabilities[1]
    }

    return  sentiment_scores    


