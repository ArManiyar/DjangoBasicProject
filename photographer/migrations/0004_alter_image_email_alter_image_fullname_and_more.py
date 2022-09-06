# Generated by Django 4.1 on 2022-08-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0003_alter_contacts_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='email',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='image',
            name='fullname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]