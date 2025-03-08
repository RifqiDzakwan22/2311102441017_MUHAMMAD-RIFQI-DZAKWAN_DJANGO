from django.shortcuts import render


def home(request):
    template_name = 'portfolio/home.html'
    context = {
        'title': 'Muhamamd Rifqi Dzakwan',
        'description': 'web portfolio saya',
        'body': 'Halaman Utama'
    }
    return render(request, template_name, context)