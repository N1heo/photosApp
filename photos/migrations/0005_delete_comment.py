# Generated by Django 4.2.4 on 2024-05-09 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]