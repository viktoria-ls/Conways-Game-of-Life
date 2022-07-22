from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import json

# from conway_grid import update_grid
from . import conway_grid

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def nextState(request):
    curr_grid = json.loads(request.GET.get('grid'))
    next_grid = conway_grid.update_grid(curr_grid)
    canUpdate = curr_grid != next_grid
    return JsonResponse({'grid': next_grid, 'canUpdate': canUpdate}, status=200)
    