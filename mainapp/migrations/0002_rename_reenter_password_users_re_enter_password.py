# Generated by Django 3.2.3 on 2021-07-08 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='reenter_password',
            new_name='re_enter_password',
        ),
    ]
