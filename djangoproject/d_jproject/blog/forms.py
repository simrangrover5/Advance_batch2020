from django import forms

class Blog(forms.Form):
    title = forms.CharField(max_length=200)
    post = forms.CharField(widget=forms.Textarea)