from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def our_work(request):
    return render(request, 'our_work.html', {})

def about(request):
    return render(request, 'about.html', {})
