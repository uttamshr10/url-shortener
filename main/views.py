from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from main import models

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def generate(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:4]
        new_url = models.Link(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def show(request, pk):
    details = models.Link.objects.get(uuid=pk)
    return redirect('https://'+details.link)
