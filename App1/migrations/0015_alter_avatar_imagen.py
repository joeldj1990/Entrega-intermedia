# Generated by Django 4.1.3 on 2022-11-26 04:37

import App1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0014_alter_avatar_imagen_alter_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='avatares/default.jpg', null=True, upload_to=App1.models.user_path),
        ),
    ]