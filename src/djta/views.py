
from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    rmd = random.randint(0,1000000000)
    context = {
              "title_here":"godspeed's color picker",
              "red":random.randint(0,255),
              "green":random.randint(0,255),
              "blue":random.randint(0,255),
              }
    return render(request , "base.html" , context)
