# Generated by Django 2.1.1 on 2019-04-02 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0004_gamesecret_playersecret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesecret',
            name='game',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='battleships.Game'),
        ),
        migrations.AlterField(
            model_name='playersecret',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='battleships.Player'),
        ),
    ]
