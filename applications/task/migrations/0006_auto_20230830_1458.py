# Generated by Django 2.2.6 on 2023-08-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20230711_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='artist_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='song_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
