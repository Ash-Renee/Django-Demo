from django.shortcuts import render, redirect
from time import strftime
import random, os

# Create your views here.
path = r"C:\Users\Ashley\Desktop\time_display\main_app\static\images"

def root(request):
    return redirect('/index')

def index(request):
    context = {
        "time" : strftime("%A %B %d %Y %H:%M"),
        "bg_img": 'static/images/' + random.choice(os.listdir(path))
    }
    return render(request, 'index.html', context)