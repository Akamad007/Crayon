# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from api.models import ApiFaviconUrl

@login_required
def home(request):    
    faviconObjects = ApiFaviconUrl.objects.all()
    return render(request,"home/home.html",{"faviconObjects":faviconObjects})




