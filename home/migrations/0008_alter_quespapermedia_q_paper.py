# Generated by Django 3.2.3 on 2021-05-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210522_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quespapermedia',
            name='q_paper',
            field=models.FileField(upload_to='q_paper'),
        ),
    ]
