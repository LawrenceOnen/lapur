# Generated by Django 2.2.5 on 2019-10-07 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0007_farmuser_via_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldworker',
            name='address',
        ),
    ]
