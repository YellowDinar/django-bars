from django.http import HttpResponse
def index(request):
    return HttpResponse("CAR")

def new(request, a):
    return HttpResponse(a)