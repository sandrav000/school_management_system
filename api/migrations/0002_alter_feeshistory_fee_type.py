# Generated by Django 5.1.4 on 2024-12-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeshistory',
            name='fee_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
