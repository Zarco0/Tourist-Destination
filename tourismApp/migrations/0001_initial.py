# Generated by Django 5.1.4 on 2024-12-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=255)),
                ('weather', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('google_map_link', models.URLField()),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='destination_images/')),
                ('image2', models.ImageField(blank=True, help_text='Optional second image', null=True, upload_to='destination_images/')),
                ('image3', models.ImageField(blank=True, help_text='Optional third image', null=True, upload_to='destination_images/')),
            ],
        ),
    ]
