# Generated by Django 2.2.12 on 2020-05-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_trash_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regist',
            name='occupation_value',
            field=models.FloatField(),
        ),
    ]
