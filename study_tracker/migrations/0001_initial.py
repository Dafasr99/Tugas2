# Generated by Django 4.1.7 on 2023-02-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Tugas Harian', 'Tugas Harian'), ('Tugas Akhir', 'Tugas Akhir'), ('Ujian', 'Ujian')], max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('progress', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]