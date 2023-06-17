from spacy.tokens import Doc


def get_num_sentences(doc: Doc):
    return len(list(doc.sents))


def get_num_words(doc: Doc):
    word_count = 0
    for token in doc:
        if not token.is_space and not token.is_punct:
            # TODO: hyphenated words are counted as one word
            word_count += len(token.text.split())
    return word_count


def get_num_syllables(doc: Doc, min_syllables: int = 1):
    syllables_count = 0
    for token in doc:
        if token._.syllables_count:
            syllables_count += token._.syllables_count
    return syllables_count
