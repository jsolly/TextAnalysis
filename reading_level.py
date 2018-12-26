import nltk, string, sys, unicodedata, re, contractions, heapq, pickle, heapq
from collections import defaultdict
from big_phoney import BigPhoney
phoney = BigPhoney()

punctuation_regex = re.compile(r'[-.?!,":;()|0-9]')
extra_spaces_regex = re.compile(r'\s\s+')
possessives_regex = re.compile(r'(\'s)')
stopwords = nltk.corpus.stopwords.words('english')

def get_word_frequncies(tokenized_word_list, stopwords) -> dict:
    tokenized_words_cleaned = [word.lower() for word in tokenized_word_list if word not in stopwords]

    word_frequencies_dict = defaultdict(int) # This could be cleaned up
    for word in tokenized_words_cleaned:  
        word_frequencies_dict[word] += 1

    return word_frequencies_dict

def get_sentence_score_dict(sentence_list, cleaned_sentences_list, word_frequencies) -> dict:
    
    sentence_score_dict = defaultdict(int)

    for index, sentence in enumerate(cleaned_sentences_list): 
        if len(sentence.split(' ')) < 30: 
            for word in nltk.word_tokenize(sentence):
                sentence_score_dict[sentence_list[index]] += word_frequencies[word]
    return sentence_score_dict

def get_clean_text(text) -> str:
    no_extra_spaces_text = extra_spaces_regex.sub(" ", text) # Remove extra spaces
    no_contractions_text = contractions.fix(no_extra_spaces_text) # Remove contractions
    return no_contractions_text

def get_super_clean_text(clean_text) -> str:
    no_punctuation_text = punctuation_regex.sub("", clean_text) # Remove punctuation
    no_possessives_text = possessives_regex.sub("", no_punctuation_text) # Remove posessives
    return no_possessives_text

def get_text_stats(text):
    text_stats = {}
    text_stats["clean_text"] = get_clean_text(text)
    text_stats["super_clean_text"] = get_super_clean_text(text_stats["clean_text"]) # No punctuation!
    text_stats["tokenized_word_list"] = nltk.word_tokenize(text_stats["super_clean_text"])
    text_stats["number_of_words"] = len(text_stats["tokenized_word_list"]) # You still want all the punctuation to detect sentences!
    text_stats["sentences_list"] = nltk.sent_tokenize(text_stats["clean_text"])
    text_stats["cleaned_sentences"] = [get_super_clean_text(get_clean_text(sentence)) for sentence in text_stats["sentences_list"]]
    text_stats["number_of_sentences"] = len(text_stats["sentences_list"])
    text_stats["avg_sentence_length"] = text_stats["number_of_words"] / text_stats["number_of_sentences"]
    text_stats["syllables"] = phoney.count_syllables(text_stats["super_clean_text"])
    text_stats["avg_syllables_per_word"] = text_stats["syllables"] / text_stats["number_of_words"]
    text_stats["word_frequencies"] = get_word_frequncies(text_stats["tokenized_word_list"], stopwords)
    text_stats["maximum_word_frequency"] = max(text_stats["word_frequencies"].values())
    text_stats["weighted_word_frequencies"] = {word: text_stats["word_frequencies"][word]/text_stats["maximum_word_frequency"] for word in text_stats["word_frequencies"].keys()}
    text_stats["Flesch-Kincaid-reading-level"] = get_reading_level(text_stats["avg_sentence_length"], text_stats["avg_syllables_per_word"])
    text_stats["sentence_scores"] = get_sentence_score_dict(text_stats["sentences_list"],text_stats["cleaned_sentences"], text_stats["word_frequencies"])
    text_stats["summary"] = get_summary(text_stats["sentence_scores"])
    
    return text_stats


def get_reading_level(avg_sentence_length, avg_syllables_per_word):
    # Flesch-Kincaid
    return (0.39 * avg_sentence_length) + (11.8 * avg_syllables_per_word) - 15.99

def get_summary(sentence_scores):
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)  

def save_text_stats(text_stats):
    with open('text_stats.p', 'wb') as handle:
        pickle.dump(text_stats, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_text_stats(text_stats):
    with open('text_stats.p', 'rb') as handle:
        text_stats = pickle.load(handle)

if __name__ == "__main__":
    with open ("text_file.txt", "r") as reader_obj:
        text_stats = get_text_stats(reader_obj.read())
        print (text_stats)
        save_text_stats(text_stats)

