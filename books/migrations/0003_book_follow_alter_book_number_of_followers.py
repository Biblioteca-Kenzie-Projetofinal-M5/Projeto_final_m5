# Generated by Django 4.2.3 on 2023-07-08 19:52

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
        migrations.AlterField(
            model_name='book',
            name='number_of_followers',
            field=models.IntegerField(default=0),
        ),
    ]