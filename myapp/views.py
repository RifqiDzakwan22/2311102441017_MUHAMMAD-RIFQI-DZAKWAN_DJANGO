from django.shortcuts import render, redirect
from myapp.models import PemainBola, Klub
from myapp.forms import KlubForm

# Create your views here.
def dashboard(request):
    
    template_name = "dashboard/index.html"
    context = {
        'title': 'halaman dashboard'
    }
    return render(request, template_name, context)

def pemainbola_list(request):

    template_name = "dashboard/devil/pemainbola_list.html"
    pemainbola = PemainBola.objects.all()
    print(pemainbola)
    context = {
        'title': 'halaman PemainBola',
        'pemainbola': pemainbola
    }
    return render(request, template_name, context)

def pemainbola_add(request):
    template_name = "dashboard/devil/pemainbola_add.html"
    if request.method == "POST":
        nama_input = request.POST.get('nama_pemainbola')
        pemain_id = request.POST.get('id')
        domisili = request.POST.get('domisili')
        tanggalLahir = request.POST.get('tanggalLahir')

        PemainBola.objects.create(
                nama = nama_input,
                id=pemain_id,
                domisili=domisili,
                tanggalLahir=tanggalLahir

            )
        return redirect(pemainbola_list)
        
    contex = {
        'title':'Tambah Pemainbola'
    }
    return render(request, template_name, contex)

def pemainbola_update(request, id_pemain):
    template_name = "dashboard/devil/pemainbola_update.html"
    try:
        pemainbola = PemainBola.objects.get(id=id_pemain)
    except:
        return redirect(pemainbola_list)

    if request.method == "POST":
        pemainbola.nama = request.POST.get('nama_pemainbola')
        pemainbola.domisili = request.POST.get('domisili')
        pemainbola.tanggalLahir = request.POST.get('tanggalLahir')
        pemainbola.save()
        return redirect(pemainbola_list)

    context = {
        'title': 'Tambah Pemainbola',
        'pemainbola': pemainbola
    }
    return render(request, template_name, context)

def pemainbola_delete(request, id_pemain):
    try:
        pemainbola = PemainBola.objects.get(id=id_pemain)
        pemainbola.delete()
    except:
        pass
    return redirect(pemainbola_list)


def klub_list(request):
    template_name = "dashboard/devil/klub_list.html"
    klub = Klub.objects.all()
    print(klub)
    context = {
        'title':'daftar klub',
        'klub': klub
    }
    return render(request, template_name, context)

def klub_add(request):
    template_name = "dashboard/devil/klub_forms.html"
    if request.method == "POST":
        forms = KlubForm(request.POST)
        if forms.is_valid():
            pup = forms.save(commit=False)
            pup.author = request.user
            pup.save()
            return redirect('klub_list')
        
        else:
            print(forms.errors)

    else:
        forms = KlubForm()

    context = {
        'title':'tambah klub',
        'forms':forms
    }
    return render(request, template_name, context)

def klub_detail(request, id_klub):
    template_name = "dashboard/devil/klub_detail.html"
    klub = Klub.objects.get(id=id_klub)
    context = {
        'title': klub.nama,
        'klub':klub
    }
    return render(request, template_name, context)

def klub_update(request, id_klub):
    template_name = "dashboard/devil/klub_forms.html"
    klub = Klub.objects.get(id=id_klub)
    if request.method == "POST":
        forms = KlubForm(request.POST, instance=klub)
        if forms.is_valid():
            pup = forms.save(commit=False)
            pup.author = request.user
            pup.save()
            return redirect(klub_list)


    forms = KlubForm(instance=klub)
    context = {
        'title':'tambah klub',
        'forms':forms
    }
    return render(request, template_name, context)

def klub_delete(request, id_klub):
    try:
        Klub.objects.get(id= id_klub).delete()
    except:pass
    return redirect(klub_list)