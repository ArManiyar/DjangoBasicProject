# Generated by Django 4.1 on 2022-08-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0010_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
