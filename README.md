## TUGAS README

------------

### link menuju aplikasi Railway yang sudah di-deploy
- https://study-tracker.up.railway.app/study-tracker/XML 
- https://study-tracker.up.railway.app/study-tracker/json

------------

### Apakah kita dapat menginput data selain melalui form? Namun mengapa form dapat dikatakan lebih baik daripada menggunakan cara tersebut?

Ya, kita dapat menginput data selain melalui form Django, yaitu dengan menggunakan ORM (Object-Relational Mapping) Django. Dalam ORM, kita dapat membuat objek model dan menyimpannya ke dalam database dengan menggunakan metode save().

Ada beberapa alasan mengapa menggunakan form pada Django lebih baik dibandingkan dengan menginput data langsung ke database. Berikut adalah beberapa di antaranya:

Validasi data: Django menyediakan fitur validasi data yang memastikan data yang diinput sesuai dengan aturan yang telah ditetapkan. Hal ini dapat meminimalkan kesalahan input data dan membuat data yang tersimpan di database lebih akurat.

Keamanan: Form pada Django mengambil keuntungan dari keamanan yang telah diterapkan pada Django. Form memastikan bahwa data yang dimasukkan aman dari serangan seperti injeksi SQL, XSS, dan serangan keamanan lainnya.

Kemudahan: Form pada Django mempermudah proses input data karena kita tidak perlu menuliskan kode SQL atau melakukan query langsung ke database. Django menyediakan fitur ORM yang memungkinkan kita untuk memanipulasi data secara mudah menggunakan Python.

Kemudahan penggunaan: Form pada Django dirancang untuk digunakan oleh pengguna yang tidak terlalu mengerti tentang teknis programming. Oleh karena itu, pengguna yang tidak mengerti tentang coding tetap dapat memanfaatkan fitur-fitur Django seperti form untuk mengelola data.

------------

### Jelaskan perbedaan antara JSON, XML, dan HTML!

- JSON (JavaScript Object Notation):
JSON adalah format pertukaran data ringan yang digunakan untuk mentransmisikan data antara server dan aplikasi web. Ini didasarkan pada sintaks JavaScript dan sering digunakan dengan JavaScript untuk membuat halaman web yang dinamis. Data JSON direpresentasikan sebagai key-value pair, di mana kuncinya selalu string dan nilainya bisa dari berbagai jenis seperti string, angka, array, atau objek. JSON lebih ringkas daripada XML dan karena itu lebih cepat diurai, menjadikannya pilihan populer untuk aplikasi web yang membutuhkan kinerja tinggi.

- XML (Extensible Markup Language):
XML adalah bahasa markup yang digunakan untuk menyandikan dokumen dalam format yang dapat dibaca oleh manusia dan dapat dibaca oleh mesin. Ini banyak digunakan untuk bertukar data antara sistem yang berbeda. XML menggunakan tag untuk mendefinisikan elemen dan atribut untuk memberikan informasi tambahan tentang elemen tersebut. Ini juga mendukung struktur hierarkis, menjadikannya pilihan yang baik untuk merepresentasikan data yang kompleks. XML lebih bertele-tele dibandingkan dengan JSON, yang membuatnya lebih lambat untuk diuraikan, tetapi juga lebih fleksibel dan dapat diperluas.

- HTML (Hypertext Markup Language):
HTML adalah bahasa markup yang digunakan untuk membuat halaman web. Ini mendefinisikan struktur dan konten halaman web, termasuk teks, gambar, tautan, dan elemen lainnya. HTML menggunakan tag untuk mendefinisikan elemen dan atributnya. Tidak seperti JSON dan XML, HTML dirancang khusus untuk menampilkan konten di browser web, bukan untuk bertukar data antar sistem. HTML dapat digunakan untuk membuat halaman web yang dinamis, tetapi sering digunakan bersamaan dengan teknologi lain seperti JavaScript, CSS, dan bahasa skrip sisi server.

### Referensi: 
- JSON.org. (n.d.). JSON: The JavaScript Object Notation. Retrieved from https://www.json.org/json-en.html 
- W3C. (2008). Extensible Markup Language (XML) 1.0 (Fifth Edition). Retrieved from https://www.w3.org/TR/REC-xml/
- Mozilla. (n.d.). HTML Basics. Retrieved from https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics
- W3C. (2008). Extensible Markup Language (XML) 1.0 (Fifth Edition). Retrieved from https://www.w3.org/TR/REC-xml/
- JSON.org. (n.d.). JSON: The JavaScript Object Notation. Retrieved from https://www.json.org/json-en.html
- Mozilla. (n.d.). HTML Basics. Retrieved from https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics

------------

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform !

Pengiriman data adalah komponen penting dalam mengimplementasikan platform karena memungkinkan transfer informasi antara berbagai bagian platform dan penggunanya. Sistem pengiriman data memungkinkan pengiriman data secara efisien, aman, dan akurat, memastikan bahwa pengguna dapat mengakses informasi yang mereka butuhkan secara tepat waktu. Selain itu, sistem pengiriman data yang kuat dapat meningkatkan pengalaman pengguna dengan meningkatkan kecepatan, keandalan, dan kinerja platform secara keseluruhan.

Menurut laporan IBM, pengiriman data merupakan komponen penting dari platform modern, yang harus mendukung transfer data berkecepatan tinggi antara pengguna, perangkat, dan aplikasi. Laporan tersebut mencatat bahwa karena volume data yang dihasilkan oleh platform ini terus meningkat, ada kebutuhan yang meningkat akan sistem pengiriman data yang dapat diskalakan secara efektif untuk menangani data ini. Tanpa sistem pengiriman data yang andal, platform mungkin mengalami waktu muat yang lambat, kehilangan data, dan masalah kinerja lainnya yang dapat berdampak negatif pada pengalaman pengguna.

Demikian pula, dalam laporan oleh Akamai, penyedia jaringan pengiriman konten terkemuka, pengiriman data disorot sebagai komponen penting dalam memberikan pengalaman online yang cepat dan aman. Laporan tersebut mencatat bahwa sistem pengiriman data harus dirancang untuk mendukung berbagai jenis konten, termasuk teks, gambar, audio, dan video, dan harus dapat beradaptasi dengan perubahan kondisi jaringan untuk memastikan kinerja yang optimal.

Singkatnya, pengiriman data merupakan komponen penting dari setiap implementasi platform. Sistem pengiriman data yang kuat memungkinkan transfer data yang efisien, aman, dan akurat antara pengguna, perangkat, dan aplikasi, meningkatkan pengalaman pengguna dan memastikan bahwa platform dapat diskalakan secara efektif untuk menangani volume data yang terus bertambah.

### Referensi:
- IBM. (2018). IBM Cloud Pak for Data: Modernizing your data platform. Retrieved from https://www.ibm.com/downloads/cas/6GMRZVWY
- Akamai. (2019). State of the internet/security: A year in review. Retrieved from https://www.akamai.com/us/en/multimedia/documents/state-of-the-internet/state-of-the-internet-security-year-in-review-2019.pdf

------------

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuka models.py yang ada pada folder study_tracker yang sudah dibuat sebelumnya. 

menjadi seperti ini

```
from django.db import models

TYPE_CHOICES = [
    ('Tugas Harian', 'Tugas Harian'),
    ('Tugas Akhir', 'Tugas Akhir'),
    ('Ujian', 'Ujian'),
]

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    subject = models.CharField(max_length=100)
    date = models.DateTimeField()
    progress = models.IntegerField()
    description = models.TextField()
```

- Melakukan perintah python manage.py makemigrations study_tracker dan python manage.py migrate pada Terminal atau Command Prompt untuk mengaplikasikan perubahan model yang telah dilakukan pada langkah sebelumnya.

- Membuat file baru pada folder study_tracker dengan nama forms.py yang dapat menerima data jadwal baru 

menjadi seperti ini

```
from django import forms
from django.forms import ModelForm, NumberInput
from study_tracker.models import Assignment

class AssignmentForm(ModelForm):
 
    class Meta:
        model = Assignment
        fields = ['name', 'type', 'subject', 'date', 'progress', 'description']
        
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
```

- Membuka file views.py pada folder study_tracker dan menambahkan import yang diperlukan serta menambahkan beberapa kode untuk mengembalikan data dalam bentuk XML dan Json 

- Membuat file HTML baru yang bernama create_assignment pada folder study_tracker/templates.

menjadi seperti ini

```
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Tambah Jadwal Baru</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Tambah"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
 
- Membuka urls.py pada folder study_tracker dan mengimport 

```
from django.urls import path
from . import views
from study_tracker.views import create_assignment
from study_tracker.views import show_xml, show_json
from study_tracker.views import show_xml_by_id, show_json_by_id

setelah itu menambahkan path yang diperlukan

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('create', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), 
]
```








