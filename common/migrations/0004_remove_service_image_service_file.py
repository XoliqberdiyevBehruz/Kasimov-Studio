# Generated by Django 4.2 on 2025-07-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_aboutus_image_alter_gallery_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='file',
            field=models.FileField(null=True, upload_to='kasimov/service/image/'),
        ),
    ]
