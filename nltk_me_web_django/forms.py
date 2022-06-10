from django import forms

radio_bt = [("button_tok_text", "Tokenize a text"),
    ("button_tok_sent", "Tokenize a sentence"),
    ("button_stopwords", "Remove the stopwords"),
    ("button_total_words", "Count total words in a text"),
    ("button_count", "Count frequency of words in a text"),
    ("button_max", "Show the most frequent word in a text"),
    ("button_plot", "Show a graph with the frequency of words")]

class Action(forms.Form):
    # file = forms.FileField()
    action = forms.CharField(label="Please select an option:", 
                             widget=forms.RadioSelect(choices=radio_bt))

class OptionalInput(forms.Form):
    text_input = forms.CharField(label="Please select the word you want to count: ")

class SendButton(forms.Form):
    send_button = forms.FileField(label="Select a file")