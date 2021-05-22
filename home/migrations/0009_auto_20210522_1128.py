# Generated by Django 3.2.3 on 2021-05-22 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_quespapermedia_q_paper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quespaper',
            old_name='fl_name',
            new_name='fl_id',
        ),
        migrations.AddField(
            model_name='quespapermedia',
            name='fl_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
