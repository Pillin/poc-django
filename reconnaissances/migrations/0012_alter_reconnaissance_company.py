# Generated by Django 4.0.3 on 2022-04-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('reconnaissances', '0011_alter_reconnaissance_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reconnaissance',
            name='company',
            field=models.ManyToManyField(blank=True, null=True, related_name='company', to='companies.company'),
        ),
    ]
