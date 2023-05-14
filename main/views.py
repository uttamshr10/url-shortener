from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from main import models

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def generate(request):
    if request.method == 'POST':
        url = request.POST['url']
        ids = str(uuid.uuid4())[:4]
        new_url = models.Link(url=url, uuid=ids)
        new_url.save()
        return HttpResponse(ids)
