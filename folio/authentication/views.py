from django.shortcuts import render_to_response, RequestContext
from .models import NewsLetter
# Create your views here.

def index(request):

    return render_to_response('comingsoon.html')


def test(request):

    return render_to_response('index.html')

