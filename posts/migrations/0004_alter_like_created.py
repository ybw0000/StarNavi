# Generated by Django 3.2.6 on 2021-08-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210808_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]