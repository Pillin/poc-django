# Generated by Django 4.0.3 on 2022-04-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reconnaissances', '0007_alter_reconnaissance_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reconnaissance',
            name='speakers_raw',
            field=models.CharField(blank=True, default='', max_length=400, verbose_name='Speakers'),
        ),
    ]
