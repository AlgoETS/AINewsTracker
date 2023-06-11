from fastapi import FastAPI
import spacy

nlp = spacy.load('en_core_web_sm')


def classify_topic(text: str):
    doc = nlp(text)
    topics = set()
    for ent in doc.ents:
        if ent.label_ == 'ORG':  # Adjust the entity label as per your requirements
            topics.add(ent.text)
    return list(topics)

