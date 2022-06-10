from django.http import HttpResponse
from django.shortcuts import render
from .forms import Action, OptionalInput, SendButton
from .Text_Processing_Tools import tokenize_text, tokenize_sentence, stopwords_remover, total_words_count, freqdist_count, freqdist_max, freqdist_plot
from .GUI_Constants import dict_EN

    # message = "This is a test for trying context in Django"
    # dict = {"message": message}
    # return render(request, "main.html", dict)

def welcome(request):
    return render(request, "welcome.html")

def home(request):
    return render(request, "home.html", {"dict_EN":dict_EN})

def tok_text(request):
    if request.method == "POST":
        form = SendButton(request.POST, request.FILES)
        if "send" in request.POST:
            print(request.FILES)
            print("This is working!")
            path = "C:/Users/Nxy_Kly/Desktop/result_tok_text.txt"
            content = decode_file(request.FILES["send_button"])
            tokenize_text(content, path)
            response = "Your text is tokenized!"
            print(response)
    else:
        form = SendButton()
    return render(request, "tok-text.html", {"form": form})


# def main(request):
#     if request.method == "POST":
#         form = Action(request.POST, request.FILES)
#         if form.is_valid():
#             if request.POST["action"] == "button_tok_text":
#                 path = "C:/Users/Nxy_Kly/Desktop/result_tok_text.txt"
#                 content = decode_file(request.FILES["file"])
#                 tokenize_text(content, path)
#                 response = "Your text is tokenized!"
#                 dict = {"response": response, "form":form}
#                 return render(request, "form_action.html", dict)
#             elif request.POST["action"] == "button_tok_sent":
#                 path = "C:/Users/Nxy_Kly/Desktop/result_tok_sent.txt"
#                 content = decode_file(request.FILES["file"])
#                 tokenize_sentence(content, path)
#                 response = "Your text is tokenized!"
#                 dict = {"response": response, "form":form}
#                 return render(request, "form_action.html", dict)
#             elif request.POST["action"] == "button_stopwords":
#                 path = "C:/Users/Nxy_Kly/Desktop/result_stopwords.txt"
#                 content = decode_file(request.FILES["file"])
#                 language = "english"
#                 stopwords_remover(content, path, language)
#                 response = "The stopwords were removed!"
#                 dict = {"response": response, "form":form}
#                 return render(request, "form_action.html", dict)
#             elif request.POST["action"] == "button_total_words":
#                 content = decode_file(request.FILES["file"])
#                 result = total_words_count(content)
#                 dict = {"result": result, "form":form}
#                 return render(request, "form_action.html", dict)
#             elif request.POST["action"] == "button_count":
#                 # if request.POST.get("text_input") == False:
#                 #     optional = OptionalInput()
#                 #     dict = {"form":form, "optional_input":optional}
#                 #     return render(request, "form_action.html", dict)
#                 # elif request.POST.get("text_input") == True:
#                 #     print("Yupiiiii, is workiiiing")
#                 # else:
#                 #     print("Wtf is going on here")
#                 pass                    
#             elif request.POST["action"] == "button_max":
#                 content = decode_file(request.FILES["file"])
#                 result = freqdist_max(content)
#                 dict = {"result": result, "form":form}
#                 return render(request, "form_action.html", dict)
#             elif request.POST["action"] == "button_plot":
#                 content = decode_file(request.FILES["file"])
#                 freqdist_plot(content)
#                 dict = {"form":form}
#                 return render(request, "form_action.html", dict)
#             else:
#                 pass
#     else:
#         form = Action()
#     return render(request, "form_action.html", {"form":form})

def decode_file(f):
    file = f.read()
    file_content = file.decode("UTF-8")
    return file_content