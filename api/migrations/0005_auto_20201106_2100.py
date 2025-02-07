# Generated by Django 3.0.5 on 2020-11-06 18:00

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201027_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='confirmation_code',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='token',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(
                choices=[
                    ('user',
                     'User'),
                    ('moderator',
                     'Moderator'),
                    ('admin',
                     'Admin')],
                default='user',
                max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(
                error_messages={
                    'unique': 'A user with that username already exists.'},
                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                max_length=150,
                unique=True,
                validators=[
                    django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name='username'),
        ),
    ]
