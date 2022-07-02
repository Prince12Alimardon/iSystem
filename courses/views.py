from django.shortcuts import render
from .models import Course, Contact
from .forms import ContactForm


def home(request):
    return render(request, 'index.html')


def courses(request):
    posts = Course.objects.filter().order_by('-id')
    ctx = {
        'posts': posts
    }
    return render(request, 'courses.html', ctx)


def about(request):
    return render(request, 'about.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    ctx = {
        'form': form
    }
    return render(request, 'contact.html', ctx)
