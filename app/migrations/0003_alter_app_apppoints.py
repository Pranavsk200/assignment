# Generated by Django 3.2.8 on 2022-12-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20221213_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='appPoints',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]