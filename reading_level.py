import nltk, string, sys, unicodedata
from big_phoney import BigPhoney
phoney = BigPhoney()

text ="""Hillary Clinton wrote a letter to an 8-year-old girl who lost an election for class president, telling the young student that she knows "too well, it's not easy" to run for "a role that's only been sought by boys."

"While I know you may have been disappointed that you did not win President, I am so proud of you for deciding to run in the first place," Clinton wrote in her letter to Martha Kennedy Morales, a third grader at a Maryland private school.
"As I know too well, it's not easy when you stand up and put yourself in contention for a role that's only been sought by boys," Clinton wrote.
The Washington Post was the first to report on the letter, which Clinton spokesman Nick Merrill confirmed to CNN is authentic.
Clinton wrote that she heard about Martha's experience running for class president through her father's posts on Facebook about the election.
Martha told CNN in a phone interview on Sunday that she was "really excited" to receive Clinton's letter, dated December 6.
"It was really touching to know that Hillary Clinton herself sent me a letter," Martha told CNN. "That doesn't happen every day."
Martha had decided to run for class president, but lost by one vote to a male classmate in an election that took place two weeks ago. Martha did, however, become vice president.
"It's disappointing to figure out that you lost something that you fought for really hard and you put a lot of effort into it," she said in an interview alongside her father, Albert Morales, Sunday on "CNN Newsroom."
But she said she's happy being vice president: "I'm happy I get to be the tie-breaker when the House and the Senate can't agree on something."

In her letter to Martha, Clinton wrote, "The most important thing is that you fought for what you believed in, and that is always worth it."
"As you continue to learn and grow in the years ahead, never stop standing up for what is right and seeking opportunities to be a leader, and know that I am cheering you on for a future of great success," she added. Clinton also congratulated Martha on being elected vice president.
Martha, who said Clinton "really inspires" her, told CNN that she wrote Clinton back to thank her. She also said she might consider inviting the former Democratic presidential nominee to visit her school in Maryland and meet their class government.
In the "CNN Newsroom" interview, Albert Morales said he and his wife were "thrilled" about Clinton's letter.
"As a father, my wife and I are thrilled because she does look up to the secretary," he said. "We try to encourage her to learn as much about public figures as possible. It's just been really nice to see someone like the secretary take the time to actually write a little girl who lost an election by one vote, but got back up."
Martha said she intends to run for class president again if given the opportunity."""


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

# FKRA = (0.39 x ASL) + (11.8 x ASW) - 15.59 