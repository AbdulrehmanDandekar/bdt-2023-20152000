# -*- coding: utf-8 -*-
"""Q7-bdt-PBA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aqxypm1kFRfHTukLqeCUQWVD_-nTQMD_
"""

documents = [
    ("D1", "the cat sat on the mat"),
    ("D2", "the dog sat on the log")
]

def map_function(document):
    doc_id, text = document
    words = text.split()
    word_document_pairs = [(word, doc_id) for word in words]
    return word_document_pairs

def reduce_function(word, doc_ids):
    sorted_doc_ids = sorted(doc_ids)
    return (word, sorted_doc_ids)

inverted_index = {}

for document in documents:
    word_document_pairs = map_function(document)
    for word, doc_id in word_document_pairs:
        if word not in inverted_index:
            inverted_index[word] = []
        inverted_index[word].append(doc_id)

inverted_index_result = []
for word, doc_ids in inverted_index.items():
    word_doc_pair = reduce_function(word, doc_ids)
    inverted_index_result.append(word_doc_pair)

for word, doc_ids in inverted_index_result:
    print(f"{word}: {', '.join(doc_ids)}")

from google.colab import drive
drive.mount('/content/drive')
import os
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import defaultdict
from operator import itemgetter

romeo_and_juliet_file = '/content/drive/My Drive/Datasets/RomeoandJuliet.txt'
king_lear_file = '/content/drive/My Drive/Datasets/KingLear.txt'

def preprocess_text(text):
    words = re.findall(r'[a-z\']+', text.lower())
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    return filtered_words

def create_inverted_index(documents):
    inverted_index = defaultdict(list)
    for doc_id, file_path in documents.items():
        with open(file_path, 'r') as file:
            text = file.read()
            words = preprocess_text(text)
            for word in words:
                inverted_index[word].append(doc_id)
    return inverted_index

documents = {
    'RomeoAndJuliet': romeo_and_juliet_file,
    'KingLear': king_lear_file
}

inverted_index = create_inverted_index(documents)

excerpt_words = list(inverted_index.keys())[:20]
for word in excerpt_words:
    doc_ids = inverted_index[word]
    print(f"{word}: {', '.join(doc_ids)}")

import os
import re
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
from operator import itemgetter

def preprocess_text(text):
    words = re.findall(r'[a-z\']+', text.lower())
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    return filtered_words

def create_expanded_inverted_index(documents):
    inverted_index = defaultdict(list)
    for doc_id, file_path in documents.items():
        with open(file_path, 'r') as file:
            text = file.read()
            lines = text.split('\n')
            position = 0
            for line in lines:
                words = preprocess_text(line)
                for word in words:
                    inverted_index[word].append((doc_id, position))
                    position += 1
    return inverted_index

romeo_and_juliet_file = '/content/drive/My Drive/Datasets/RomeoandJuliet.txt'
king_lear_file = '/content/drive/My Drive/Datasets/KingLear.txt'

documents = {
    'RomeoAndJuliet': romeo_and_juliet_file,
    'KingLear': king_lear_file
}

expanded_inverted_index = create_expanded_inverted_index(documents)

sorted_index = {word: sorted(entries, key=itemgetter(0, 1)) for word, entries in expanded_inverted_index.items()}

excerpt_words = list(sorted_index.keys())[:20]
for word in excerpt_words:
    entries = sorted_index[word]
    print(f"{word}: {entries}")