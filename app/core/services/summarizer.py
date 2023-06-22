# Import necessary libraries
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Define constants for model name and maximum token length
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
MAX_TOKENS = 1024

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Create summarization pipeline
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)


def summarize_text(text: str) -> str:
    """
    Function to summarize a given text using a pretrained DistilBART model.

    Args:
        text (str): Input text to summarize.

    Returns:
        summary (str): Summarized version of the input text.
    """
    # Tokenize the input text
    inputs = tokenizer(
        text,
        max_length=MAX_TOKENS, 
        truncation=True,
        return_tensors="pt"
    )
    
    # Generate summary ids
    summary_ids = model.generate(inputs["input_ids"])
    
    # Decode the summary ids and convert it into text
    summary = tokenizer.batch_decode(
        summary_ids, 
        skip_special_tokens=True, 
        clean_up_tokenization_spaces=False
    )
    
    return summary[0]
