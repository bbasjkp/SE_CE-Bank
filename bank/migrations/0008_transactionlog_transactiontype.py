# Generated by Django 2.1.3 on 2018-11-28 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20181128_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionlog',
            name='transactiontype',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
    ]
