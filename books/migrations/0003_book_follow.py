# Generated by Django 4.2.3 on 2023-07-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='follow',
            field=models.BooleanField(default=False),
        ),
    ]