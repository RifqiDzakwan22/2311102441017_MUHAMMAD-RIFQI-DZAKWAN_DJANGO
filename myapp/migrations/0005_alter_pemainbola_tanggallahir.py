# Generated by Django 5.1.6 on 2025-04-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_pemainbola_tanggallahir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemainbola',
            name='tanggalLahir',
            field=models.DateField(blank=True, null=True),
        ),
    ]
