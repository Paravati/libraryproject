# Generated by Django 3.1 on 2021-07-21 21:20

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('photo', models.ImageField(default='foto.png', upload_to='photos')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=20)),
                ('cover', models.ImageField(default='download.png', upload_to='book_cover')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.author')),
                ('genre', models.ManyToManyField(to='library.Genre')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]