import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tags
from collections import Counter

# Sample text
text = "This is a sample sentence, showing off the stop words removal, tokenization, word frequency counting, and POS tagging."

# Tokenization
tokens = word_tokenize(text)

# Count word frequency
word_freq = Counter(tokens)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# POS tagging (on filtered tokens)
pos_tags = pos_tags(filtered_tokens)

# Print results
print("Original text:", text)
print("\nTokenization:")
print(tokens)
print("\nWord frequency:")
print(word_freq)
print("\nStop words removal:")
print(filtered_tokens)
print("\nPOS tagging (on filtered tokens):")
print(pos_tags)
