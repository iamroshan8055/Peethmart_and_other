# Generated by Django 3.1.7 on 2021-03-14 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='Email_ID',
            new_name='Email_ID_C',
        ),
        migrations.RenameField(
            model_name='child',
            old_name='First_Name',
            new_name='First_Nam_C',
        ),
        migrations.RenameField(
            model_name='child',
            old_name='Last_Name',
            new_name='Last_Name_C',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='Email_ID',
            new_name='Email_ID_P',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='First_Name',
            new_name='First_Name_P',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='Last_Name',
            new_name='Last_Name_P',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='Phone_No',
            new_name='Phone_No_P',
        ),
    ]
