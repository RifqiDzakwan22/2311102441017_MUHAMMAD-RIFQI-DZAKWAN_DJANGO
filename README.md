# ✨ Project Django
## 🖼️ Deskripsinya
Website ini adalah web portfolio saya yang sudah pasti isinya tentang diri saya, sebelumnya perkenalkan nama saya Muhammad Rifqi Dzakwan bisa dipanggil Rifqi, dan saya adalah mahasiswa UMKT Samarinda jurusan S1 TEKNIK INFORTMATIKA.
## 📱cara menjalankannya
1. untuk yang pertama kita harus hapus folder project lama **(bukan yang berisi .gitignore dan README.md).**
lalu jalankan perintahnya di cmd ya yaitu dengan cara
```shell
git clone https://github.com/RifqiDzakwan22/2311102441017_MUHAMMAD-RIFQI-DZAKWAN_DJANGO.git
```

2. Masuk kedalam mode virtual environment dengan cara

```shell
# Universal Python
python -m venv .venv
```

3. lalu di aktifkan modenya

```shell
# Windows
.venv\Scripts\activate
```

4. install Djangonya
```shell
pip install django
```

5. Tambahkan 1 fungsi views.py yaitu dengan cara

**menambahkan file views.py di folder project yang kita buat tadi**

nambahkan file views.py
```shell
type nul > views.py
```

isi code di views.py
```shell
from django.shortcuts import render


def home(request):
    template_name = 'portfolio/home.html'
    context = {
        'title': 'Muhamamd Rifqi Dzakwan',
        'description': 'web portfolio saya',
        'body': 'Halaman Utama'}

    return render(request, template_name, context)
```
6. Buat HTML

```shell
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Portfolio Muhammad Rifqi Dzakwan</title>
</head>
<body>
    <h1>Portfolio Muhammad Rifqi Dzakwan</h1>
    <p>HALOOO Selamat datang di halaman portfolio saya</p>
</body>
</html>
```

7. commit dan push yaitu dengan cara

masukin file ke commit
```shell
commit "git add ."
```
cek git nya biar tau status gitnya
```shell
git status
```
masukan commit pesan
```shell
git commit -m "kasi pesan yang wajar aja"
```
push gitnya
```shell
git push origin main
```


