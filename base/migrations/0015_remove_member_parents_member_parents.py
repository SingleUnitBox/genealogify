# Generated by Django 4.1.4 on 2022-12-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_member_parents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='parents',
        ),
        migrations.AddField(
            model_name='member',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='children', to='base.member'),
        ),
    ]
