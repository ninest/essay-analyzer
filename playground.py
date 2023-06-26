import spacy

# instantiate pipeline with any model of your choosing
nlp = spacy.load("en_core_web_sm")

# words = "Those quickest and brownest foxes jumped over the laziest ones."
words = "He leveraged the resources. She is also leveraging them. How must we best leverage them?"

# only enable the needed pipeline components to speed up processing
# with nlp.select_pipes(enable=["tok2vec", "tagger", "attribute_ruler", "lemmatizer"]):
doc = nlp(words)

lemma_mapping = dict(
    [(token.text, token.lemma_) for token in doc if token.is_punct == False]
)

print(lemma_mapping)
