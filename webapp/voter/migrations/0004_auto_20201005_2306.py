# Generated by Django 3.1.2 on 2020-10-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0003_game_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='shortcut',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
