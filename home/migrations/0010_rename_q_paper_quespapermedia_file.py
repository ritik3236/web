# Generated by Django 3.2.3 on 2021-05-22 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210522_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quespapermedia',
            old_name='q_paper',
            new_name='file',
        ),
    ]
