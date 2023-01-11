from django.shortcuts import (HttpResponse)

# Create your views here.
def index(request):
    print("index")
    return HttpResponse("ok")