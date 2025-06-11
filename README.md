# ✨ Project Django
## 🖼️ Deskripsinya
Website ini adalah web Tentang Manchester United, sebelumnya perkenalkan nama saya Muhammad Rifqi Dzakwan bisa dipanggil Rifqi, dan saya adalah mahasiswa UMKT Samarinda jurusan S1 TEKNIK INFORTMATIKA. Untuk tambahannya saya membuat Django app bernama **myapp** untuk modelnya **pemainbola** ⚽ **CRUD CUSTOM** ⭐
## 📱cara menjalankannya
1. untuk yang pertama kita harus hapus folder project lama **(bukan yang berisi .gitignore dan README.md).**
lalu jalankan perintahnya di cmd ya yaitu dengan cara
```shell
git clone https://github.com/RifqiDzakwan22/2311102441017_MUHAMMAD-RIFQI-DZAKWAN_DJANGO.git
```
```
git init          # inisialisasi repo Git di folder lokal
git clone <url>   # clone repo GitHub ke lokal
git add .         # add semua file ke staging area
git commit -m "pesan commit"   # buat commit
git push          # push ke GitHub
git pull          # ambil update terbaru dari GitHub
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

5. commit dan push yaitu dengan cara

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

6. untuk membuat start apps
```shell
python manage.py startapp "nama app mu bebas aja"
```

7. untuk membuat migration
```shell
python manage.py makemigrations "nama app yang kamu buat tadi ;)"
```
