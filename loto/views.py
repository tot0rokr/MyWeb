# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import loto
import re

def index(request):
    seed = request.GET.get('seed_date')
    if (seed is not None and seed != ""):
        seed = re.sub("-", "", seed)
        print(seed)
        seed = int(seed)
    numbers = loto.lotos(seed)
    template = loader.get_template('loto/index.html')
    context = {
        'numbers': numbers,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(numbers)

# Create your views here.
