# Generated by Django 4.2.3 on 2023-07-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='number_of_followers',
        ),
    ]