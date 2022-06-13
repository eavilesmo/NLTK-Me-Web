# -----------------------------------------------------------------------------
# Description of the file
# -----------------------------------------------------------------------------

# The Text_Processing_Tools file hosts all the functions needed for the views
# file.

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


# Class Error for handling errors of the application
class ErrorCode:
    UNICODE_ERROR = 1
    VALUE_ERROR = 2
    PATH_ERROR = 3
    EMPTY_FILE_ERROR = 4
    NO_ERROR = 5

# -----------------------------------------------------------------------------
# Lists
# -----------------------------------------------------------------------------


stopword_symbols = ["¡", "!", ",", ".", ";", "-", "_", "¿", "?", "(", ")",
                    "/", "\\", "@", "#", ":", "'", "’"]

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


def tokenize_text(get_file_text, filename_path):
    """Text tokenizer - Divides a text into sentences"""
    try:
        tokenized_text = sent_tokenize(get_file_text)
        if len(tokenized_text) <= 0:
            return ErrorCode.EMPTY_FILE_ERROR
        else:
            with open(filename_path, "w") as result_text:
                for line in tokenized_text:
                    result_text.write(line)
                    result_text.write("\n")
            return ErrorCode.NO_ERROR
    except FileNotFoundError:
        return ErrorCode.PATH_ERROR
    except UnicodeDecodeError:
        return ErrorCode.UNICODE_ERROR


def tokenize_sentence(get_file_sentence, filename_path):
    """Sentence tokenizer - Divides one or more sentences into words"""
    try:
        tokenized_sentence = word_tokenize(get_file_sentence)
        if len(tokenized_sentence) <= 0:
            return ErrorCode.EMPTY_FILE_ERROR
        else:
            with open(filename_path, "w") as result_sentence:
                for word in tokenized_sentence:
                    result_sentence.write(word)
                    result_sentence.write("\n")
            return ErrorCode.NO_ERROR
    except FileNotFoundError:
        return ErrorCode.PATH_ERROR
    except UnicodeDecodeError:
        return ErrorCode.UNICODE_ERROR


def stopwords_remover(get_file_stopwords, filename_path, stopwords_language):
    """Stopwords remover - Removes the stopwords from a text"""
    try:
        stop_words = set(stopwords.words(stopwords_language))
        tokenized_file = word_tokenize(get_file_stopwords)
        if len(tokenized_file) <= 0:
            return ErrorCode.EMPTY_FILE_ERROR
        with open(filename_path, "w") as result_stopwords:
            for word in tokenized_file:
                word = word.lower()
                if word not in stop_words and word not in stopword_symbols:
                    result_stopwords.write(" " + word)
        return ErrorCode.NO_ERROR
    except FileNotFoundError:
        return ErrorCode.PATH_ERROR
    except UnicodeDecodeError:
        return ErrorCode.UNICODE_ERROR


def total_words_count(get_file_twords):
    """Total words - Shows how many words are in the text"""
    try:
        if len(get_file_twords) <= 0:
            data_from_twords = 0
            return ErrorCode.EMPTY_FILE_ERROR, data_from_twords
        tokenized_sentence = word_tokenize(get_file_twords)
        data_from_twords = len(tokenized_sentence)
        return ErrorCode.NO_ERROR, data_from_twords
    except FileNotFoundError:
        data_from_twords = 0
        return ErrorCode.PATH_ERROR, data_from_twords
    except UnicodeDecodeError:
        data_from_twords = 0
        return ErrorCode.UNICODE_ERROR, data_from_twords


# Frequency Distribution functions
def freqdist_count(get_file_fdist_count, get_data_count):
    """
    FreqDist Count - Count how many times a certain word appears in the text
    """
    try:
        get_file_fdist_count = get_file_fdist_count.lower()
        tokenizer = TreebankWordTokenizer()
        fdist_count_tokenized = tokenizer.tokenize(get_file_fdist_count)
        if len(fdist_count_tokenized) <= 0:
            data_from_count = 0
            return ErrorCode.EMPTY_FILE_ERROR, data_from_count
        fdist_count = FreqDist(fdist_count_tokenized)
        get_data_count = get_data_count.lower()
        data_from_count = fdist_count[get_data_count]
        return ErrorCode.NO_ERROR, data_from_count
    except FileNotFoundError:
        data_from_count = 0
        return ErrorCode.PATH_ERROR, data_from_count
    except UnicodeDecodeError:
        data_from_count = 0
        return ErrorCode.UNICODE_ERROR, data_from_count


def freqdist_max(get_file_fdist_max):
    """FreqDist Max - Shows most repeated word"""
    try:
        tokenizer = TreebankWordTokenizer()
        fdist_max_tokenized = tokenizer.tokenize(get_file_fdist_max)
        if len(fdist_max_tokenized) <= 0:
            data_from_max = 0
            return ErrorCode.EMPTY_FILE_ERROR, data_from_max
        fdist_max = FreqDist(fdist_max_tokenized)
        data_from_max = fdist_max.max()
        return ErrorCode.NO_ERROR, data_from_max
    except FileNotFoundError:
        data_from_max = 0
        return ErrorCode.PATH_ERROR, data_from_max
    except UnicodeDecodeError:
        data_from_max = 0
        return ErrorCode.UNICODE_ERROR, data_from_max


def freqdist_plot(get_file_fdist_plot):
    """FreqDist Plot - Shows a graph with words frequency"""
    try:
        tokenizer = TreebankWordTokenizer()
        fdist_plot_tokenized = tokenizer.tokenize(get_file_fdist_plot)
        if len(fdist_plot_tokenized) <= 0:
            data_from_plot = 0
            return ErrorCode.EMPTY_FILE_ERROR, data_from_plot
        fdist_plot = FreqDist(fdist_plot_tokenized)
        data_from_plot = fdist_plot.plot()
        return ErrorCode.NO_ERROR, data_from_plot
    except FileNotFoundError:
        data_from_plot = 0
        return ErrorCode.PATH_ERROR, data_from_plot
    except UnicodeDecodeError:
        data_from_plot = 0
        return ErrorCode.UNICODE_ERROR, data_from_plot
