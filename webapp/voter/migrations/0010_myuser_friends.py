# Generated by Django 3.1.2 on 2020-10-07 14:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0009_auto_20201006_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
