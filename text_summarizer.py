# Importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Input text - to summarize
input_text = """In the bustling city of New York, where skyscrapers touch the sky and yellow taxis zoom through the streets, there is an air of endless possibilities. People from all walks of life come together in this melting pot of cultures, creating a vibrant tapestry of diversity. Amidst the chaos, Central Park stands as an oasis of tranquility, a lush green expanse where urban dwellers find solace in the midst of the concrete jungle. The city never sleeps, and neither do the dreams of those who call it home. From Broadway theaters to world-class museums, every corner of New York tells a story. It's a city that inspires, a city that challenges, and a city that never fails to leave a lasting impression on anyone who visits. """

# Tokenizing the input text
stop_words = set(stopwords.words("english"))
words = word_tokenize(input_text)

# Creating a frequency table to keep the score of each word
word_freq_table = dict()
for word in words:
    word = word.lower()
    if word in stop_words:
        continue
    if word in word_freq_table:
        word_freq_table[word] += 1
    else:
        word_freq_table[word] = 1

# Creating a dictionary to keep the score of each sentence
sentences = sent_tokenize(input_text)
sentence_value = dict()

for sentence in sentences:
    for word, freq in word_freq_table.items():
        if word in sentence.lower():
            if sentence in sentence_value:
                sentence_value[sentence] += freq
            else:
                sentence_value[sentence] = freq

sum_values = 0
for sentence in sentence_value:
    sum_values += sentence_value[sentence]

# Average value of a sentence from the original text
average_score = int(sum_values / len(sentence_value))

# Storing sentences into our summary
summary = ''
for sentence in sentences:
    if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average_score)):
        summary += " " + sentence

print(summary)
