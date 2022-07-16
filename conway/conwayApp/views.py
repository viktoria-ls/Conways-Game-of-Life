from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def setSize(request):
    size = int(request.GET["size"])
    # Calls main.py stuff