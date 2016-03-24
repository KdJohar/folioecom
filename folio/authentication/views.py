from django.shortcuts import render_to_response, RequestContext
from .models import NewsLetter

# Create your views here.

def index(request):

    return render_to_response('index.html', context_instance=RequestContext(request))


def demo(request):
    return render_to_response('ecommerce/index2.html')

def bookdetail(request):
    return render_to_response('ecommerce/bookdetail.html')