from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def history(request):
    return render(request, 'history.html', {})

def wines(request):
    return render(request, 'wines.html', {})



