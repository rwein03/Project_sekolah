# Generated by Django 4.0.3 on 2022-05-01 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('mac_addr', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('ip_addr', models.CharField(blank=True, max_length=50, null=True)),
                ('isBlocked', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userWifi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='request_action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(blank=True, max_length=50, null=True)),
                ('action', models.CharField(choices=[('wifi', 'WIFI'), ('shutdown', 'SHUTDOWN'), ('restart', 'RESTART')], max_length=50)),
                ('isStatus', models.BooleanField(blank=True, default=False)),
                ('macaddr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_web.computer')),
            ],
        ),
    ]
