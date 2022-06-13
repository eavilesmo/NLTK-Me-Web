from django.shortcuts import render
from .forms import SendButton
from .Text_Processing_Tools import tokenize_text, tokenize_sentence, stopwords_remover, total_words_count, freqdist_count, freqdist_max
from .GUI_Constants import dict_EN
import os


def welcome(request):
    return render(request, "welcome.html", {"dict_EN":dict_EN})

def home(request):
    return render(request, "home.html", {"dict_EN":dict_EN})

def tok_text(request):
    if request.method == "POST":
        form = SendButton(request.POST, request.FILES)
        if "send" in request.POST:
            filename = request.POST["save-file"]
            path = get_path(filename)
            content = decode_file(request.FILES["send_button"])
            output = tokenize_text(content, path)
            message = error_handling(output)
            if message == "Valid result":
                result = "Your text is tokenized! The file is in this path: {}".format(path)
            else:
                result = message
            dict = {"form": form, "dict_EN":dict_EN, "result":result}
            return render(request, "base-template.html", dict)
    else:
        form = SendButton()
        dict = {"form": form, "dict_EN":dict_EN}
        return render(request, "base-template.html", dict)

def tok_sent(request):
    if request.method == "POST":
        form = SendButton(request.POST, request.FILES)
        if "send" in request.POST:
            filename = request.POST["save-file"]
            path = get_path(filename)
            content = decode_file(request.FILES["send_button"])
            output = tokenize_sentence(content, path)
            message = error_handling(output)
            if message == "Valid result":
                result = "Your text is tokenized! The file is in this path: {}".format(path)
            else:
                result = message
            dict = {"form": form, "dict_EN":dict_EN, "result":result}
            return render(request, "tok-sent.html", dict)
    else:
        form = SendButton()
        dict = {"form": form, "dict_EN":dict_EN}
        return render(request, "tok-sent.html", dict)

def stopwords(request):
    if request.method == "POST":
        form = SendButton(request.POST, request.FILES)
        if "send" in request.POST:
            filename = request.POST["save-file"]
            path = get_path(filename)
            content = decode_file(request.FILES["send_button"])
            language = request.POST["select-language"]
            output = stopwords_remover(content, path, language)
            message = error_handling(output)
            if message == "Valid result":
                result = "The stopwords were removed! The file is in this path: {}".format(path)
            else:
                result = message
            dict = {"form": form, "dict_EN":dict_EN, "result":result}
            return render(request, "stopwords.html", dict)
    else: 
        form = SendButton()
        dict = {"form": form, "dict_EN":dict_EN}
        return render(request, "stopwords.html", dict)

def total_words(request):
    if request.method == "POST":
        form = SendButton(request.POST, request.FILES)
        if "send" in request.POST:
            content = decode_file(request.FILES["send_button"])
            output, words = total_words_count(content)
            message = error_handling(output)
            if message == "Valid result":
                result = "The text has {} words in total".format(words)
            else:
                result = message
            dict = {"form": form, "dict_EN":dict_EN, "result":result}
            return render(request, "count-total.html", dict)
    else: 
        form = SendButton()
        dict = {"form": form, "dict_EN":dict_EN}
        return render(request, "count-total.html", dict)

def count_one(request):
    if request.method == "POST":
        form = SendButton(request.POST, request.FILES)
        if "send" in request.POST:
            word_for_count = request.POST["word-for-count"]
            content = decode_file(request.FILES["send_button"])
            output, times = freqdist_count(content, word_for_count)
            message = error_handling(output)
            if message == "Valid result":
                result = "The word {} appears {} times in your text".format(word_for_count, times)
            else:
                result = message
            dict = {"form": form, "dict_EN":dict_EN, "result":result}
            return render(request, "count-one.html", dict)
    else: 
        form = SendButton()
        dict = {"form": form, "dict_EN":dict_EN}
        return render(request, "count-one.html", dict)

def count_max(request):
    if request.method == "POST":
        form = SendButton(request.POST, request.FILES)
        if "send" in request.POST:
            content = decode_file(request.FILES["send_button"])
            output, word = freqdist_max(content)
            message = error_handling(output)
            if message == "Valid result":
                result = "The most repeated word in your text is {}".format(word)
            else:
                result = message
            dict = {"form": form, "dict_EN":dict_EN, "result":result}
            return render(request, "count-max.html", dict)
    else:
        form = SendButton()
        dict = {"form": form, "dict_EN":dict_EN}
        return render(request, "count-max.html", dict)

def plot(request):
    form = SendButton()
    dict = {"form": form, "dict_EN":dict_EN}
    return render(request, "plot.html", dict)

def decode_file(f):
    file = f.read()
    file_content = file.decode("UTF-8")
    return file_content

def get_path(filename):
    path_desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    path_desktop.replace("\\", "/")
    final_path = path_desktop + "/" + str(filename) + ".txt"
    return final_path

def error_handling(error_result):
    if error_result == 1:
        return dict_EN["unicode_error"]
    elif error_result == 2:
        return dict_EN["value_error"]
    elif error_result == 3:
        return dict_EN["path_error"]
    elif error_result == 4:
        return dict_EN["empty_file_error"]
    elif error_result == 5:
        return "Valid result"
    else:
        return "Unexpected error"


