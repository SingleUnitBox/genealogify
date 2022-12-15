# Generated by Django 4.1.4 on 2022-12-15 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('place_of_birth', models.CharField(max_length=200)),
                ('place_of_death', models.CharField(max_length=200)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('date_of_death', models.CharField(max_length=50)),
                ('date_of_marriage', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=1000)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('children', models.ManyToManyField(blank=True, to='base.person')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('siblings', models.ManyToManyField(blank=True, to='base.person')),
                ('spouses', models.ManyToManyField(blank=True, to='base.person')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
