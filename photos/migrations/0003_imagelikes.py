# Generated by Django 4.2.4 on 2023-08-08 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0002_alter_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='photos.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
