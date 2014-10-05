from django.http import HttpResponse
from django.shortcuts import render

from .forms import ArticleInputForm
from dotbs.models import MLearn

def index(request):
	form = ArticleInputForm()
	return render(request, 'index.html', {'form': form})

def analyze(request):
	url = request.GET['url']
	# magic
	# SOMESHIT.count = SOMESHIT.count + 1
	# countShit = SOMESHIT.count
	return render(request, 'results.html', {'url': url})
