# Templat Proyek Django untuk Railway

Repositori ini berisi sebuah templat untuk membuat proyek Django yang siap di-*deploy* ke [Railway](https://railway.app/).

## Daftar Isi

- [Daftar Isi](#daftar-isi)
- [Instruksi Penggunaan](#instruksi-penggunaan)
- [Lisensi](#lisensi)
- [Referensi](#referensi)

## Instruksi Penggunaan

### Pengembangan Lokal

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi, ikuti langkah-langkah berikut.

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.

2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (*filesystem*) komputermu.

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```

3. Masuk ke dalam repositori yang sudah di-*clone* dan jalankan perintah berikut
   untuk menyalakan *virtual environment*.

   ```shell
   python -m venv env
   ```

4. Nyalakan *virtual environment* dengan perintah berikut.

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

5. Instal *dependencies* yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut.

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara lokal.

   ```shell
   python manage.py runserver
   ```

7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

### Pengembangan di Railway

1. Buka situs web [Railway](https://railway.app/) dan klik tombol `Start a New Project`.

2. Klik pilihan `Deploy from GitHub repo`.

3. Klik tombol `Login With GitHub` dan masuklah ke dalam akun GitHub kamu.

4. Kamu akan kembali ke halaman pembuatan proyek baru. Klik pilihan `Deploy from GitHub repo` dan klik `Configure GitHub App`.

5. Pilih tempat kamu menyimpan repositori program ini dan klik `Install & Authorize`.

6. Kamu akan kembali ke halaman pembuatan proyek baru. Klik pilihan `Deploy from GitHub repo` dan pilih repositori program ini.

7. Klik `Add variables` dan buat variabel baru dengan nama `APP_NAME` dan isikan nama aplikasi kamu yang akan dibuat menjadi URL aplikasi.

8. Klik menu `Settings` dan ubahlah URL yang ada pada bagian `Domains` sesuai dengan `APP_NAME` yang telah dispesifikasikan sebelumnya.

9. Tekan Control + K atau Command + K dan pilih `New Service -> Database -> Add PostgreSQL` untuk menginisiasi basis data PostgreSQL sebagai basis data yang digunakan.

## Lisensi

Templat ini didistribusikan dengan lisensi [MIT](LICENSE).

## Referensi

- [django-template-heroku](https://github.com/laymonage/django-template-heroku)
- [Templat Proyek Django PBP](https://github.com/pbp-fasilkom-ui/django-pbp-template)
- [Pindah dari Heroku ke Railway](https://determinedguy.github.io/cecoret/heroku-to-railway/)

TUGAS README
------------
------------
link menuju aplikasi Railway yang sudah di-deploy
https://study-tracker.up.railway.app/study-tracker/

------------
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

https://compfest.link/Bagan-Req-Client 

------------
Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Berikut beberapa alasan mengapa menggunakan environment serta tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment

Mencegah Konflik: Virtual environment memungkinkan kita untuk mengisolasi dependensi (package) dan konfigurasi dari satu proyek ke proyek lain, sehingga mencegah terjadinya konflik dalam penggunaan package, dan memungkinkan pengembang untuk mengelola proyek dengan mudah.

Reproduksi yang Konsisten: Virtual environment memungkinkan pengembang untuk memastikan bahwa proyek yang sama dapat di-reproduksi dengan konsisten pada mesin yang berbeda, karena dependensi yang digunakan sama dan versinya dapat dikendalikan.

Versi Python yang Berbeda: Dalam beberapa kasus, mungkin diperlukan untuk menggunakan beberapa versi Python dalam satu mesin. Dengan virtual environment, pengembang dapat membuat lingkungan pengembangan yang terpisah untuk setiap versi Python yang dibutuhkan.

------------
Penjelasan bagaimana cara mengimplementasikan poin 1 sampai dengan 4 di atas.

- Melakukan git pull dari github "https://github.com/determinedguy/django-railway-template"

- Instal dependencies yang diperlukan untuk menjalankan proyek Django dengan perintah perintah pip install -r requirements.txt.

yang berisi:

asgiref==3.6.0
certifi==2022.12.7
charset-normalizer==3.0.1
dj-database-url==1.2.0
Django==4.1.7
gunicorn==20.1.0
idna==3.4
psycopg2-binary==2.9.5
pytz==2022.7.1
requests==2.28.2
six==1.16.0
sqlparse==0.4.3
typed-ast==1.5.4
tzdata==2022.7
urllib3==1.26.14
whitenoise==6.3.0
wrapt==1.14.1

- Membuat sebuah aplikasi baru pada proyek tersebut bernama study_tracker
Membuat sebuah proyek Django baru bernama django_project dengan perintah django-admin startproject study_tracker .

- Membuka settings.py di folder django_project dan menambahkan aplikasi study_tracker ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah dibuat kedalam proyek django.

menjadi seperti ini

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'study_tracker'
]

- Membuat model pada aplikasi study_tracker yang bernama Assignment dan memiliki atribut

menjadi seperti ini

from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    date = models.DateTimeField()
    progress = models.IntegerField()
    description = models.TextField()

- melakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

- menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

- Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model yang telah dibuat sebelumnya dan dikembalikan ke dalam sebuah HTML.

menjadi seperti ini

from django.shortcuts import render
from .models import Assignment

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignment_list.html', {'assignments': assignments})

- Sebelum kita mengimplemetasikan views, kita perlu membuat suatu skeleton yang berfungsi sebagai kerangka views dari situs web kita.

dengan menambahkan file template pada root folder 

berisi:

{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  {% block meta %}
  {% endblock meta %}
</head>
<body>
  {% block content %}
    <h1>Daftar Tugas</h1>
    <table>
      <thead>
        <tr>
          <th>Nama Tugas</th>
          <th>Mata Kuliah</th>
          <th>Tenggat Waktu</th>
          <th>Progress</th>
        </tr>
      </thead>
      <tbody>
        {% for assignment in assignments %}
        <tr>
          <td>{{ assignment.name }}</td>
          <td>{{ assignment.subject }}</td>
          <td>{{ assignment.date }}</td>
          <td>{{ assignment.progress }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  {% endblock content %}
</body>
</html>

- Menambahkan path pada urls.py

berisi:

from django.urls import path
from . import views

app_name = 'study_tracker'

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
]

- Dapat menjalankan proyek Django dengan perintah python manage.py runserver dan =membuka http://localhost:8000/study-tracker/ 