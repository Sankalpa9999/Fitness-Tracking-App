from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trainer
from .forms import TrainerCreationForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def trainer(request):
    trainers = Trainer.objects.all()
    context = {
        'trainers': trainers
    }
    return render(request, 'trainer/trainerhome.html', context)
