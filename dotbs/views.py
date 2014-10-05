from django.http import HttpResponse
from django.shortcuts import render
from lxml.html.clean import Cleaner
import re
import urllib2

from .forms import ArticleInputForm
from dotbs.models import MLearn

def index(request):
    form = ArticleInputForm()
    return render(request, 'index.html', {'form': form})

def analyze(request):
    url = request.GET['url']
    response = urllib2.urlopen(url)
    raw_html = response.read().encode('utf-8').decode('ascii')

    cleaner = Cleaner(kill_tags = ['style', 'script', 'head'], allow_tags = [''], remove_unknown_tags = False)
    raw_text = cleaner.clean_html(raw_html)
    ptn = re.compile('<div>|</div>')
    raw_text = re.sub(ptn, '', raw_text)
    ptn = re.compile('\s+')
    raw_text = re.sub(ptn, ' ', raw_text)
    raw_text = raw_text.strip().lower()
    result = MLearn.label(MLearn.predict(raw_text))

    return render(request, 'results.html', {'url': result})
