# Generated by Django 4.0.6 on 2022-07-20 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_tassurotlar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel',
            old_name='qoliq_mal',
            new_name='toliq_mal',
        ),
    ]