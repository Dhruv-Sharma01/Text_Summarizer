# Text_Summarizer

# Text Summarizer

This is a simple Python application that performs extractive text summarization. It uses the NLTK library to tokenize the input text, calculate word frequencies, score sentences, and generate a summary based on the most important sentences.

## How it Works

1. **Tokenization:**
   - The input text is broken down into words and sentences using NLTK tokenization.

2. **Frequency Calculation:**
   - Stop words are removed, and a frequency table is created to store word frequencies.

3. **Scoring Sentences:**
   - Sentences are scored based on the sum of frequencies of words they contain.

4. **Determining Threshold:**
   - An average score is calculated, and a threshold is set to include sentences with scores above 1.2 times the average.

5. **Generating Summary:**
   - Sentences with scores above the threshold are included in the summary.

## How to Use

1. Make sure you have Python and NLTK installed on your system.
2. Clone this repository: `git clone <repository-url>`
3. Install the required libraries: `pip install nltk`
4. Run the script: `python text_summarizer.py`

