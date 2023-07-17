# Generated by Django 4.2.3 on 2023-07-17 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0003_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='tunr.artist'),
        ),
    ]
