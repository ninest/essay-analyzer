from .repeated_words import get_repeated_word_map
from .readability import get_readability
from .utils import get_num_words
import spacy

def main():
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    # get_readability('Let\'s do it')
    words = get_num_words(nlp('say - no'))
    print(words)

if __name__=='__main__':
    main()