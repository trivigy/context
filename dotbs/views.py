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
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1')]
    response = opener.open(url)
    raw_html = response.read().encode('utf-8', 'ignore').decode('ascii', 'ignore')

    cleaner = Cleaner(kill_tags = ['style', 'script', 'head'], allow_tags = [''], remove_unknown_tags = False)
    raw_text = cleaner.clean_html(raw_html)
    ptn = re.compile('<div>|</div>')
    raw_text = re.sub(ptn, '', raw_text)
    ptn = re.compile('\s+')
    raw_text = re.sub(ptn, ' ', raw_text)
    raw_text = raw_text.strip().lower()
    prd, score = MLearn.predict(raw_text)
    donut = score * 100
    results = MLearn.predict_other(raw_text)
    related_headline = results[0][2]
    related_verdict = results[0][0]
    related_score = results[0][1] * 100

    context = {
    	'url': url,
    	'verdict': prd,
    	'score': donut,
    	'related_headline': related_headline,
    	'related_verdict': related_verdict,
    	'related_score': related_score,
    	'results': results,
    }

    return render(request, 'results.html', context)
