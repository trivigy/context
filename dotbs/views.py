from django.http import HttpResponse
from django.shortcuts import render
from lxml.html.clean import Cleaner
import re

from .forms import ArticleInputForm
from dotbs.models import MLearn

def index(request):
    form = ArticleInputForm()
    return render(request, 'index.html', {'form': form})

def analyze(request):
    url = "http://www.bbc.com/news/world-asia-china-29489387"# request.GET['url']

    if MLearn.driver is None:
        raise AttributeError("Attempted to parse url without selenium driver")
    MLearn.driver.get(url)
    raw_html = MLearn.driver.page_source

    cleaner = Cleaner(kill_tags = ['style', 'script', 'head'], allow_tags = [''], remove_unknown_tags = False)
    raw_text = cleaner.clean_html(raw_html)
    ptn = re.compile('<div>|</div>')
    raw_text = re.sub(ptn, '', raw_text)
    ptn = re.compile('\s+')
    raw_text = re.sub(ptn, ' ', raw_text)
    raw_text = raw_text.strip().lower()
    result = MLearn.label(MLearn.predict(raw_text))

    return render(request, 'results.html', {'url': result})