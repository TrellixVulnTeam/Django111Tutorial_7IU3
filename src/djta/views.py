
from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    rmd = random.randint(0,1000000000)
    return render(request , "base.html" , {
                                            "title_here":"godspeed's color picker",
                                            "rmd":rmd
                                          })
