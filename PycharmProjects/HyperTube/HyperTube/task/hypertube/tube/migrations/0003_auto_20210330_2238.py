# Generated by Django 2.2 on 2021-03-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_auto_20210328_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='C:\\Users\\piotr\\PycharmProjects\\HyperTube\\HyperTube\\task'),
        ),
    ]
