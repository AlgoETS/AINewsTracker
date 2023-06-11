from transformers import pipeline

# Load the summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_article(article_text, max_length=130, min_length=30, do_sample=False):
    """
    Summarize a given article text.

    Args:
    article_text (str): The article text to summarize.
    max_length (int, optional): The maximum length of the summary. Defaults to 130.
    min_length (int, optional): The minimum length of the summary. Defaults to 30.
    do_sample (bool, optional): Whether to use sampling in the generation of the summary. Defaults to False.

    Returns:
    str: The summary of the article.
    """

    # Summarize the article
    summary = summarizer(article_text, max_length=max_length, min_length=min_length, do_sample=do_sample)

    return summary[0]['summary_text']


def summarizer(text: str):
    # Instantiate a pipeline for summarization
    summarization = pipeline("summarization")
    return summarization(text)[0]["summary_text"]