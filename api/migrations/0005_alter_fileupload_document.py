# Generated by Django 3.2.3 on 2021-05-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210527_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='document',
            field=models.FileField(upload_to='userUploaded/'),
        ),
    ]
