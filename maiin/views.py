from django.shortcuts import render


def home(request):
    template_name = 'home.html'
    context = {
        'title': 'Portfolio Muhammad Rifqi Dzakwan',
        'description': 'web portfolio saya',
        'body': 'Halaman home'
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