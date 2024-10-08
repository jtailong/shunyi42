# Generated by Django 5.1 on 2024-09-08 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': 'ShuJi Guanli'},
        ),
        migrations.CreateModel(
            name='PepoleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('gender', models.SmallIntegerField(choices=[('1', 'male'), (2, 'female')], default=1)),
                ('description', models.CharField(max_length=500, null=True)),
                ('is_delecte', models.BooleanField(default=False)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo')),
            ],
            options={
                'db_table': 'pepoleinfo',
            },
        ),
    ]
