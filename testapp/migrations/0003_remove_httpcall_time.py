# Generated by Django 3.2.9 on 2021-12-14 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20211214_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='httpcall',
            name='time',
        ),
    ]
