# Generated by Django 2.2.5 on 2019-09-16 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20190916_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]