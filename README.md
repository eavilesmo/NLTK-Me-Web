# NLTK-Me! Web Version

## Introduction

NLTK-Me! is an API based in the NLTK library for Python. It processes texts using different functions of NLTK, such as tokenizing texts, removing stopwords, or searching frequency of a specific word. In a previous project I created it under a graphical user interface, but this time I converted it into an API. You can check my previous project in https://github.com/eavilesmo/NLTK-Me.git

## Description of functions

- **Text tokenizer**: Tokenizes (splits) a text into sentences. The text is split based on full stops. The function will create a file with the results, the user can choose the name for the file. It will be saved in the user's Desktop.
- **Sentence tokenizer**: Tokenizes (splits) sentences into words. The sentences are split based on spaces. The function will create a file with the results, the user can choose the name for the file. It will be saved in the user's Desktop.
- **Stopwords remover**: Removes the stopwords from a text. The stopwords are words with no meaning in the text, such as articles, prepositions or punctuation marks. The function will create a file with the results, the user can choose the name for the file. It will be saved in the user's Desktop.
- **Count of total words**: Counts how many words are in the text. The result will appear in the Result section.
- **Frequency Distribution - Count**: Counts how many times a specific words appear in the text. The user can input the word to be counted. The result will appear in the Result section.
- **Frequency Distribution - Max**: Shows the most frequent word in a text. The result will appear in the Result section.

## How To Run

Go to Terminal
Introduce the following command: docker build -t exchange github.com/eavilesmo/CRM-API#main
Introduce the following command: docker run --publish 8000:5000 exchange
Introduce the following command: curl localhost:8000
Navigate to: http://127.0.0.1:8000

Note: step 2 and onwards must be executed from the terminal, possibly requiring root privileges

1) Install Docker \
  https://www.docker.com/products/docker-desktop/
2) Go to Terminal \
3) Introduce the following command:  \
    |docker build -t exchange github.com/eavilesmo/CRM-API#main| \
4) Introduce the following command: \
    |docker run --publish 8000:5000 exchange| \
4) Introduce the following command: \
    |curl localhost:8000| \
5) Navigate to: \
    |http://127.0.0.1:8000| \
6) Enjoy!

## Screenshots

Welcome Page

![Welcome Page] (https://raw.githubusercontent.com/eavilesmo/NLTK-Me-Web/main/welcome.png)

Home Page

![Home Page] (https://github.com/eavilesmo/NLTK-Me-Web/blob/main/home.jpg?raw=true)

Tokenize A Text Page

![Tokenize A Text Page] (https://github.com/eavilesmo/NLTK-Me-Web/blob/main/tok-text-screenshot.png)

Total Count of Words Page

![Total Count of Words Page] (https://github.com/eavilesmo/NLTK-Me-Web/blob/main/count-total-screenshot.jpg?raw=true)

## Next Steps
- Implement unit testing with Unittest or Pytest
- Activate GitHub Actions in order to perform unit tests automatically
- Make the website responsive for different browsers, as for now it has a fixed appearance.
- Include Spanish as a language for the API
- Include a dark mode
- Include a missing feature for showing a graph with the different word's frequency in the text. This feature was also present in the previous NLTK-Me! project.
- Add a Contact Me section
- Add an About NLTK section
