# Generated by Django 4.1.5 on 2023-01-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_remove_adv_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='adv',
            name='descriptions',
            field=models.CharField(default=None, max_length=50),
        ),
    ]