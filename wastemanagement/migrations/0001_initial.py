# Generated by Django 3.1 on 2021-03-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wastemanagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('img1', models.ImageField(upload_to='')),
                ('img2', models.ImageField(upload_to='')),
                ('img3', models.ImageField(upload_to='')),
                ('img4', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
