# Generated by Django 4.0.3 on 2022-04-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
        ('reconnaissances', '0003_alter_reconnaissance_survey_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reconnaissance',
            name='speaker',
            field=models.ManyToManyField(to='speakers.speaker'),
        ),
    ]