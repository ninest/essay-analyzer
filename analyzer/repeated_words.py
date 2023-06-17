from collections import Counter

import spacy

# Initialize spacy 'en' model, keeping only tagger component needed for lemmatization
# Install with `python -m spacy download en_core_web_trf`
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

def get_repeated_word_map(text: str):
    doc = nlp(text)

    repeated_words_counter = Counter()

    for token in doc:
        if token.is_punct or token.is_stop:
            continue
        repeated_words_counter[token.lemma_.lower()] += 1
    
    print(repeated_words_counter)
    
