from django.shortcuts import render
from .models import Course, Contact, Isystem_in_numbers
from .forms import ContactForm


def home(request):
    isystem_nums = Isystem_in_numbers.objects.all().order_by('id').first()
    return render(request, 'index.html', {'isystem_nums': isystem_nums})


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
