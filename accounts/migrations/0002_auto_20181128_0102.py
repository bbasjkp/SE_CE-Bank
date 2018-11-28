# Generated by Django 2.1.3 on 2018-11-27 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='bank_balance',
            new_name='balance',
        ),
        migrations.RenameField(
            model_name='bankaccount',
            old_name='bank_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='bankaccount',
            old_name='bank_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='bankaccount',
            old_name='id_person',
            new_name='personal_id',
        ),
        migrations.RenameField(
            model_name='bankaccount',
            old_name='bank_pin',
            new_name='pin',
        ),
        migrations.RenameField(
            model_name='bankaccount',
            old_name='bank_surname',
            new_name='surname',
        ),
    ]
