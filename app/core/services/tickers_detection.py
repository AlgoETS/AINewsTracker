from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Initializing the tokenizer and the model using the 'roberta-ticker' pretrained version
tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-ticker")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-ticker")

# Setting up a NER (Named Entity Recognition) pipeline using the above model and tokenizer
# 'aggregation_strategy' is set to "simple" to aggregate the scores of overlapping tokens 
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def process_text(text: str):
    """
    Process the given text using a Named Entity Recognition (NER) pipeline.
    The pipeline will identify and classify entities in the text based on their types.

    Args:
        text (str): The text to process.

    Returns:
        result: The result of the NER pipeline. This is a list of dictionary objects,
                where each dictionary represents a detected entity. Each dictionary
                contains information about the entity, such as its value, score,
                entity type, index, start and end positions in the text.
    """
    result = nlp(text)
    return result
