from django.shortcuts import render
from django.views.static import serve
import os


def homepage(request):
    return render(request, template_name='river_simulation.html')


def river(request):
    filepath = os.getcwd() + '/river_simulation/river_sim.py'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

