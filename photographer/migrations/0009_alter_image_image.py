# Generated by Django 4.1 on 2022-08-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0008_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
    ]
