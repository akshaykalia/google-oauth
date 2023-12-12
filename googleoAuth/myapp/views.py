import os
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html', {"GOOGLE_CLIENT_ID": os.getenv("GOOGLE_CLIENT_ID")})
