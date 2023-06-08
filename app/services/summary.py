from transformers import pipeline

def summarizer(text: str):
    # Instantiate a pipeline for summarization
    summarization = pipeline("summarization")
    return summarization(text)[0]['summary_text']
