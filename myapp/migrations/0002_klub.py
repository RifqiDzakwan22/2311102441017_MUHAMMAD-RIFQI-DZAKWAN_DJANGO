# Generated by Django 5.1.6 on 2025-04-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('negara', models.CharField(max_length=100)),
                ('tahunberdiri', models.IntegerField()),
            ],
        ),
    ]
