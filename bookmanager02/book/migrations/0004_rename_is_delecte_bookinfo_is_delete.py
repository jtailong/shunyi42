# Generated by Django 5.1 on 2024-09-08 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_pepoleinfo_peopleinfo_alter_peopleinfo_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='is_delecte',
            new_name='is_delete',
        ),
    ]
