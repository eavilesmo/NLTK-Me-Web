# -----------------------------------------------------------------------------
# Description of the file
# -----------------------------------------------------------------------------

# A file for storing the descriptions and names of the buttons appearing in the website.

# -----------------------------------------------------------------------------

dict_EN = {
    # Descriptions
    "tok_text_description": "With Text Tokenizer, you can tokenize (split) "
                            "a text into sentences. The text is split based "
                            "on full stops.This option will create a file "
                            "with the result in your desktop. You can choose the "
                            "name for your output file.",
    "tok_sentence_description": "With Sentence Tokenizer, you can tokenize "
                                "(split) a sentence into words. The sentences "
                                "are split based on spaces.This option will "
                                "create a file with the result in your desktop. You can "
                                "choose the name for your output file.",
    "stopwords_rem_description": "This function removes the stopwords from a "
                                 "text. This means that all words with no "
                                 "meaning in the text (as articles, "
                                 "prepositions or punctuation marks) will be "
                                 "removed from the text.This option will "
                                 "create a file with the result in your desktop. You can "
                                 "choose the name for your output file.",
    "twords_description": "This function shows how many words in total are in the text."
                          "You can check the result below!",
    "count_one_description": "This function shows how many times a word appears "
                         "in the text.Please note this function isn't case "
                         "sensitive, which means that it differentiates between"
                         " capital or lower-case letters.You can check the result below!",
    "max_description": "This function shows the most common word in the text."
                       "It's recommended to first execute the function 'Remove "
                       "stopwords' in the file to avoid getting strange "
                       "results (for instance, getting articles, pronouns "
                       "or even punctuation marks as the most frequent word.)"
                       "You can check the result below!",
    "plot_description": "This function shows a graph with the most frequent "
                        "words in the text and the number of time they appear. "
                        "You can choose how many words will be displayed.\nA"
                        " new window will appear with the graph.\nIt's "
                        "recommended to first execute the function 'Remove "
                        "stopwords' in the file to avoid getting strange "
                        "results (for instance, getting articles, pronouns or "
                        "even punctuation marks as words in the graph.)",

    # Errors
    "unicode_error": "The program is not able to work with your file due "
                     "to its encoding.\nPlease change the encoding of your "
                     "file before trying again.",
    "value_error": "The introduced value is not correct. Please try again.",
    "path_error": "The path you introduced is not correct. Please try again.",
    "empty_file_error": "The file you introduced is empty! Please try again.",

    # Buttons
    "button_tok_text": "Tokenize a text",
    "button_tok_sent": "Tokenize a sentence",
    "button_stopwords": "Remove the stopwords",
    "button_total_words": "Count total words in a text",
    "button_count_one": "Count frequency of words in a text",
    "button_max": "Show the most frequent word in a text",
    "button_plot": "Show a graph with the frequency of words",

    # Web title
    "web_title": "NLTK-Me!",

    # Welcome page
    "welcome_text_1": "Welcome to",
    "welcome_text_2": "NLTK-Me!",
    "welcome_description": "An application based in the NLTK library for Python",
    "welcome_button": "Try Me!",

    # Home page
    "home_title": "Welcome to NLTK-Me!",
    "home_intro_1": "With NLTK-Me!, you can find the most repeated word in a text, split sentences into words, and much more!",
    "home_intro_2": "Explore the different options below!",
    "home_tok_text": "Split a text into sentences",
    "home_tok_sent": "Split a sentence into words",
    "home_stopwords": "Remove the stopwords from a text",
    "home_count_total": "Count the total words in a text",
    "home_count_one": "Count how many times a word appears in a text",
    "home_max": "Show the most frequent word in a text",
    "home_plot": "Show a graph with words's frequency",
    "home_send": "Go!",

    # Function pages
    "send_button_tok": "Tokenize!",
    "send_button_stopwords": "Go!",
    "send_button_count": "Count!",
    "send_button_show": "Show!",
    "select_file": "Please select the input file:",
    "name_file": "Please choose a name for the output file (with no extension):",
    "result_title": "Result",
    "information_title": "What does this function do?",
    "back_home": "Home",
    "word_for_count": "Please type the word you want to count:",
    "select_language": "Please select the language of your file:",
}

