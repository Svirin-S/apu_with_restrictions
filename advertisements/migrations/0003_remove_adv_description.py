# Generated by Django 4.1.5 on 2023-01-11 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_adv_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adv',
            name='description',
        ),
    ]