from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Adopt
from .forms import AdoptForm

def home(request):
    adopt = Adopt.objects.all()
    return render(request, 'adopt/home1.html', {'adopt':adopt})

def adopt_new(request):
    if request.method == 'POST':
        form = AdoptForm(request.POST, request.FILES)
        if form.is_valid():
            adopt = form.save(commit=False)
            #adopt.posted_by = request.user
            adopt.posted_by = User.objects.get(username='angelica')
            adopt.save()
            return redirect('/')

    else:
        form = AdoptForm()
    return render(request, 'adopt/adopt_edit.html', {'form':form})

def adopt_edit(request, pk):
    adopt = get_object_or_404(Adopt, pk=pk)
    if request.method == "POST":
        form = AdoptForm(request.POST, request.FILES,instance=adopt)
        if form.is_valid():
            adopt = form.save(commit=False)
            adopt.posted_by = User.objects.get(username='angelica')
            adopt.save()
            return redirect('/', pk=adopt.pk)
    else:
        form = AdoptForm(instance=adopt)
    return render(request, 'adopt/adopt_edit.html', {'form':form})
