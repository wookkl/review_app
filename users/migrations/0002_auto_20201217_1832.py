# Generated by Django 2.2.5 on 2020-12-17 09:32

import core.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.managers.CustomUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('EM', 'Email'), ('GH', 'Github'), ('KK', 'Kakao')], default='EM', max_length=2),
        ),
    ]