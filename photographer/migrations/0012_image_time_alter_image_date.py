# Generated by Django 4.1 on 2022-08-31 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0011_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
