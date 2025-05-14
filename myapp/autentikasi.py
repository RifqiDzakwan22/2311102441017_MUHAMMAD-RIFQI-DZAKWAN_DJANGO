from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def akun_login(request):
    if request.user.is_authenticated:
        return request('/')

    template_name = "halaman/login.html"
    pesan = ''
    if request.method == "POST":
       username = request.POST.get("username")
       password = request.POST.get("password")

       user = authenticate(request, username=username, password=password)
       if user:
            login(request, user)
            return redirect('/')
       else:
           pesan = "gagal login"
    
    context = {
        'pesan': pesan
    }
    return render (request, template_name, context)