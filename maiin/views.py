from django.shortcuts import render
from myapp.models import PemainBola, Klub

def home(request):
    template_name = 'halaman/about.html'
    data_pemainbola = PemainBola.objects.all()
    print(data_pemainbola)
    context = {
        'title': 'Rifqi Dzakwan Manchester United',
        'data_pemainbola': data_pemainbola,
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title': 'selamat datang di halaman about',
        'description': 'web portfolio saya',
        'body': 'Halaman about'
    }
    return render(request, template_name, context)