# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello")
    
def add(request, a, b):
    return HttpResponse(str(int(a) + int(b) ) )
    
def factorial(request, c):
    p = 1
    i = 2
    while i <= int(c):
            p = p * i
            i = i + 1
    return HttpResponse(str(p))
    
def factorization(request, d):
    m = 2
    s = ''
    while int(d) > 1:
            if int(d) % m == 0:
                    s = s + str(m) + ' '
                    d = int(d)/m
            else:
                    m = m +1
    return HttpResponse(str(s))
    