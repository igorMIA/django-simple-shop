# Generated by Django 2.1 on 2018-09-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180905_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='is_recommend',
            field=models.BooleanField(default=False),
        ),
    ]
