# Generated by Django 4.0.3 on 2022-05-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_web', '0003_alter_request_action_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='isAlive',
            field=models.BooleanField(default=False),
        ),
    ]
