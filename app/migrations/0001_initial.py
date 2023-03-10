# Generated by Django 3.2.8 on 2022-12-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appName', models.CharField(max_length=60)),
                ('appLinks', models.CharField(max_length=60)),
                ('appCategory', models.CharField(max_length=60)),
                ('appSubCategory', models.CharField(max_length=60)),
                ('appImage', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
