# Generated by Django 4.1.3 on 2022-11-25 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default="media 'avatares/default.jpg'", null=True, upload_to='avatares'),
        ),
    ]