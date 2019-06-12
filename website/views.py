from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.utils import timezone
from models.models import *
import random
import string
import hashlib
# Create your views here.

data = {"sitename":"Fdirect"}
#home page
def home(request):
    context = {"data":data}
    return render(request, 'website/index.html', context) 

#login is modal window so just post from modal window to auth
def login(request):
    pass

def auth(request):
    pass
