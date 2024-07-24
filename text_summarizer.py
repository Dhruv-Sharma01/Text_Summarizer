import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK resources (if not already installed)
nltk.download('punkt')
nltk.download('stopwords')

# Define the function to summarize text
def summarize_text(text):
    # Tokenizing the input text
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)

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
    sentences = sent_tokenize(text)
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

    return summary

# Streamlit app layout
st.title('Text Summarizer Using NLTK Corpus')
st.write('Enter text below to get a summary:')

# Text input
input_text = st.text_area("Input Text", height=200)

if st.button('Summarize'):
    if input_text:
        summary = summarize_text(input_text)
        st.subheader('Summary')
        st.write(summary)
    else:
        st.write('Please enter some text to summarize.')
