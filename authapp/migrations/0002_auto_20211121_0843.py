# Generated by Django 3.2.9 on 2021-11-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'authapp'},
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
    ]
