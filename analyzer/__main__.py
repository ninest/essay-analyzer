from .readability import get_readability
from .repeated_words import get_repeated_word_map


def main():
    essay = """This is the first paragraph.

This has been paragraphed second.

Here is the third one for good measure."""  # input("Enter essay: ")
    essay = essay.replace("\n", "")
    repeated = get_repeated_word_map(essay)
    readability = get_readability(essay)

    print("Repeated words: \n", repeated)
    print("\nReadability: \n", readability)


if __name__ == "__main__":
    main()
