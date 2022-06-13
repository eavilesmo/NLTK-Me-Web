from django import forms

class SendButton(forms.Form):
    send_button = forms.FileField(label="Select a file", required=True)