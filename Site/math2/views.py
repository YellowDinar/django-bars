# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello")
    
def add(request, a, b):
    return HttpResponse(str(int(a) + int(b) ) )