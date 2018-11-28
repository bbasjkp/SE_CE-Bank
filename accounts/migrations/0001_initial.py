# Generated by Django 2.1.3 on 2018-11-08 20:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_number', models.CharField(default='', max_length=30)),
                ('bank_name', models.CharField(default='', max_length=30)),
                ('bank_surname', models.CharField(default='', max_length=30)),
                ('id_person', models.CharField(default='', max_length=30)),
                ('bank_pin', models.CharField(default='', max_length=4)),
                ('bank_balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
