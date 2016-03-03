from django.shortcuts import render_to_response, RequestContext
from .models import NewsLetter
# Create your views here.

def index(request):
    if request.POST:
        email = request.POST.get('email')
        obj = NewsLetter.objects.create(email=email)
        obj.save()
    return render_to_response('comingsoon.html')

