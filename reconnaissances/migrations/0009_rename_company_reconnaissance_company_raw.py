# Generated by Django 4.0.3 on 2022-04-05 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reconnaissances', '0008_alter_reconnaissance_speakers_raw'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reconnaissance',
            old_name='company',
            new_name='company_raw',
        ),
    ]