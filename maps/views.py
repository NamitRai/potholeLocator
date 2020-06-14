from django.shortcuts import render
from .models import location
# Sample Co-ordinates
data = [[77.4908, 28.4628], [77.4999, 28.4615],
        [77.4826, 28.4745], [77.5883, 28.4634]]


def default_map(request):
    loc = location.objects
    return render(request, 'default.html', {"data": loc})


def about(request):

    return render(request, 'about.html', {})
