from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# from .models import Item

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def our_work(request):
    return render(request, 'our_work.html', {})

def about(request):
    return render(request, 'about.html', {})

def the_blackout_block_party(request):
    return render(request, 'the_blackout_block_party.html', {})

def quicksip(request):
    return render(request, 'quicksip.html', {})

def aaphdcs(request):
    return render(request, 'aaphdcs.html', {})
