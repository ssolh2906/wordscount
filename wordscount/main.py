# Imports
import heapq
import os
import re
from collections import Counter

from wordscount.config import CONVERTED_TEXTS_DIR, WORDS_TO_EXCLUDE


# Functions
def get_txt_list_from_dir():
    text_sources_dir = os.path.dirname(os.path.dirname(__file__))
    for _ in range(2):
        text_sources_dir = os.path.dirname(text_sources_dir)

    text_sources_dir = os.path.join(text_sources_dir, CONVERTED_TEXTS_DIR)

    file_list = os.listdir(text_sources_dir)
    text_files = [file for file in file_list if file.endswith('.txt')]
    text_list = []
    for filename in text_files:
        text_list.extend(read_txt(text_sources_dir, filename))
    return text_list


def get_words_to_exclude():
    source_dir = os.path.dirname(os.path.dirname(__file__))
    for _ in range(2):
        source_dir = os.path.dirname(source_dir)

    words_list = read_txt(source_dir, WORDS_TO_EXCLUDE)

    return words_list


def read_txt(file_path, file_name):
    """
    input : file path, file_name
    output : list of words in file
    """
    word_list = []
    pattern = r'[^a-zA-Z]'
    with open(os.path.join(file_path, file_name), 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        cleaned_line = re.sub(pattern, ' ', line)
        words = cleaned_line.split()
        filtered_words = [word.lower() for word in words if len(word) > 1]
        word_list.extend(filtered_words)
    return word_list


def count_word_frequency(words_list, top_n=None):
    word_counts = Counter()
    word_counts.update(words_list)

    # Convert the Counter to a list of tuples and use a heap to keep top N frequent words
    heap = []
    for word, count in word_counts.items():
        heapq.heappush(heap, (-count, word))  # Invert count for max-heap behavior

    # Extract top N words if specified
    if top_n:
        top_words = heapq.nlargest(top_n, heap)
    else:
        top_words = sorted(heap, reverse=False)  # Get all words sorted by frequency

    # Convert to (word, count) format for the final output
    sorted_word_counts = [(word, -count) for count, word in top_words]

    words_to_exclude = get_words_to_exclude()
    new_word_counts = {k: v for k, v in sorted_word_counts if k not in words_to_exclude}

    return new_word_counts


# Starts here
words_list = get_txt_list_from_dir()
wc = count_word_frequency(words_list)

print(wc)
