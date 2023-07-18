# Generated by Django 4.2.3 on 2023-07-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0004_alter_song_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default='no album', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='preview_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default='no title', max_length=100),
        ),
    ]