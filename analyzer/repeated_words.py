from collections import Counter
from dataclasses import dataclass

import spacy

from analyzer.class_utils import JSON

# Initialize spacy 'en' model, keeping only tagger component needed for lemmatization
# Install with `python -m spacy download en_core_web_trf`
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])


@dataclass
class RepeatedWords(JSON):
    counter: "Counter[str]"
    lemmas: "dict[str, list[str]]"


def get_repeated_word_map(text: str):
    """Get repeated words that are not stop words"""

    doc = nlp(text)

    repeated_words_counter: Counter[str] = Counter()
    lemmas: "dict[str, list[str]]" = {}

    for token in doc:
        if token.is_punct or token.is_stop:
            continue

        word = token.text.lower()
        lemma = token.lemma_.lower()
        repeated_words_counter[lemma] += 1
        if lemma in lemmas:
            lemmas[lemma].append(word)
        else:
            lemmas[lemma] = [word]

    return RepeatedWords(counter=repeated_words_counter, lemmas=lemmas)
