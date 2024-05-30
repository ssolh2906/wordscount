# Imports
import heapq
import os
from collections import Counter


# Functions
def read_txt_files_from_dir():
    text_sources_dir = os.path.dirname(os.path.dirname(__file__))
    for _ in range(2):
        text_sources_dir = os.path.dirname(text_sources_dir)

    text_sources_dir = os.path.join(text_sources_dir, 'textsource')

    file_list = os.listdir(text_sources_dir)
    text_files = [file for file in file_list if file.endswith('.txt')]
    text_list = []
    for filename in text_files:
        text_list.append(read_txt(text_sources_dir, filename))
    return text_list


def read_txt(file_path, text_file):
    with open(os.path.join(file_path, text_file), 'r', encoding='utf-8') as file:
        text_list = file.readlines()
    return text_list

def pdf_to_txt(file_path):
    return


def count_word_frequency(text_list, top_n=None):
    word_counts = Counter()
    for text in text_list:
        for line in text:
            words = line.split()
            words = [word.lower() for word in words]  # Convert words to lower case
            word_counts.update(words)

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

    return sorted_word_counts


txt_list = read_txt_files_from_dir()
wc = count_word_frequency(txt_list)
print(wc)
