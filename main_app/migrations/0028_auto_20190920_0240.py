# Generated by Django 2.2.5 on 2019-09-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0027_auto_20190920_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(default='No Summary Was Found'),
        ),
    ]
