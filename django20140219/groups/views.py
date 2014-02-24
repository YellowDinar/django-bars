from django.http import HttpResponse
from django.shortcuts import render
from groups.models import Group

def index(request):
    groups = Group.objects.all()
    return render(request,'groups/index.html', {'groups' : groups})

def details(request, id):
    group = Group.objects.get(id = id)
    return render(request,'groups/details.html', {'group' : group})