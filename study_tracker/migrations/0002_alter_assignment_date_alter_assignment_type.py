# Generated by Django 4.1.7 on 2023-03-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='type',
            field=models.CharField(choices=[('Tugas Harian', 'Tugas Harian'), ('Tugas Kelompok', 'Tugas Kelompok'), ('Tugas Mandiri', 'Tugas Mandiri'), ('Tugas Praktikum', 'Tugas Praktikum'), ('Tugas Akhir', 'Tugas Akhir'), ('Ujian', 'Ujian')], max_length=20),
        ),
    ]
