import nltk, string, sys, unicodedata
from big_phoney import BigPhoney
phoney = BigPhoney()

def get_reading_level(text):
    # Investigate why tokenized_word_list and clean_text.split(" ") lengths are different
    remove_punct_map = dict.fromkeys(i for i in range(sys.maxunicode)
                                    if unicodedata.category(chr(i)).startswith('P'))

    clean_text = text.translate(remove_punct_map)
    tokenized_word_list = nltk.word_tokenize(clean_text) 
    number_of_words = len(tokenized_word_list)
    sentences = nltk.sent_tokenize(text) # You still want all the punctuation to detect sentences!
    number_of_sentences = len(sentences)
    avg_sentence_length = number_of_words / number_of_sentences
    syllables = phoney.count_syllables(' '.join(tokenized_word_list))
    avg_syllables_per_word = syllables / number_of_words

    reading_level = (0.39 * avg_sentence_length) + (11.8 * avg_syllables_per_word) - 15.99
    print (f"The reading level at the US grade leve of {reading_level}")
    # FKRA = (0.39 x ASL) + (11.8 x ASW) - 15.59 

if __name__ == "__main__":
    with open ("text_file.txt", "r") as text:
        get_reading_level(text.read())

