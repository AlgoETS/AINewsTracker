from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-ticker")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-ticker")
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def process_text(text: str):
    result = nlp(text)
    return result
