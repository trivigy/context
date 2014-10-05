from django import forms

class ArticleInputForm(forms.Form):
	url = forms.CharField(label="URL")
