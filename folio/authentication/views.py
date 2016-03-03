from django.shortcuts import render_to_response, RequestContext
from .models import NewsLetter
from django.http import HttpResponse
import json
# Create your views here.

def index(request):

    return render_to_response('comingsoon.html')


def test(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        obj = NewsLetter(email=email)
        obj.save()
        return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json")
    return render_to_response('index.html', context_instance=RequestContext(request))

