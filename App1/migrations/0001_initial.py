# Generated by Django 4.1.3 on 2022-11-22 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armazones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=30)),
                ('tamagno', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Cristales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=30)),
                ('graduacion', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Lentes_Sol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('color_armazon', models.CharField(max_length=30)),
                ('color_lente', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=30)),
                ('tamagno', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
    ]
