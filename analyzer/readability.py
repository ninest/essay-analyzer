import spacy
from spacy_syllables import SpacySyllables
from dataclasses import dataclass
from .utils import get_num_syllables, get_num_words, get_num_sentences

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("syllables", after="tagger")


@dataclass
class Readability:
    total_syllables: int
    total_words: int
    total_sentences: int

    average_syllables_per_word: float
    average_words_per_sentence: float

    flesch_reading_ease: float
    flesch_kincaid_grade_level: float


def get_readability(text: str):
    doc = nlp(text)

    no_syllables = get_num_syllables(doc)
    no_words = get_num_words(doc)
    no_sentences = get_num_sentences(doc)

    flesch_reading_ease = (
        206.835 - 1.015 * (no_words / no_sentences) - 84.6 * (no_syllables / no_words)
    )
    flesch_kincaid_grade_level = (
        0.39 * (no_words / no_sentences) + 11.8 * (no_syllables / no_words) - 15.59
    )

    return Readability(
        total_syllables=no_syllables,
        total_words=no_words,
        total_sentences=no_sentences,
        average_syllables_per_word=no_syllables / no_words,
        average_words_per_sentence=no_words / no_sentences,
        flesch_reading_ease=flesch_reading_ease,
        flesch_kincaid_grade_level=flesch_kincaid_grade_level,
    )
